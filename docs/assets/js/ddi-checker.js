/**
 * FRTxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author FRTxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'Majeure' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'Modérée' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'Mineure' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Warfarine + Ibuprofène : risque hémorragique accru',
      detail: 'Les AINS inhibent la fonction plaquettaire et peuvent potentialiser l’effet anticoagulant de la warfarine, ce qui augmente nettement le risque d’hémorragie digestive.',
      recommendation: 'Utilisez plutôt du paracétamol ou associez un IPP pour la protection gastrique.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Warfarine + Aspirine : risque hémorragique accru',
      detail: 'Les deux agissent sur l’hémostase ; leur association augmente fortement le risque hémorragique.',
      recommendation: 'Si l’association est nécessaire, utilisez l’aspirine à faible dose et surveillez étroitement l’INR.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Warfarine + Naproxène : risque hémorragique accru',
      detail: 'L’association du naproxène à la warfarine augmente le risque d’hémorragie digestive et d’autres saignements.',
      recommendation: 'Utilisez plutôt du paracétamol contre la douleur.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformine + produits de contraste iodés : risque d’acidose lactique',
      detail: 'Les produits de contraste peuvent provoquer une insuffisance rénale aiguë, entraînant une accumulation de metformine et une acidose lactique.',
      recommendation: 'Arrêtez la metformine 48 heures avant l’examen et ne la reprenez qu’après avoir confirmé une fonction rénale normale.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Colchicine + Clarithromycine : risque de toxicité',
      detail: 'La clarithromycine est un inhibiteur puissant du CYP3A4 et augmente fortement les concentrations sanguines de colchicine.',
      recommendation: 'Évitez l’association ou réduisez fortement la dose de colchicine.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Colchicine + inhibiteurs de la protéase du VIH : risque de toxicité grave',
      detail: 'Les inhibiteurs de la protéase du VIH augmentent nettement les concentrations de colchicine et peuvent entraîner une toxicité mortelle.',
      recommendation: 'Contre-indiqué chez les patients atteints d’insuffisance rénale ou hépatique.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Simvastatine + Amiodarone : risque de myopathie',
      detail: 'L’amiodarone augmente les concentrations de simvastatine, ce qui accroît le risque de rhabdomyolyse.',
      recommendation: 'Ne dépassez pas 20 mg/jour de simvastatine ou passez à une autre statine.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'ISRS + Tramadol : risque de syndrome sérotoninergique',
      detail: 'Les deux augmentent l’activité sérotoninergique ; leur association peut provoquer un syndrome sérotoninergique potentiellement mortel.',
      recommendation: 'Surveillez étroitement les symptômes (hyperthermie, myoclonies, altération de l’état mental) et envisagez un autre antalgique.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'ISRS + Linézolide : risque de syndrome sérotoninergique',
      detail: 'Le linézolide est un inhibiteur de la MAO ; l’associer à un ISRS est très dangereux.',
      recommendation: 'Évitez l’association. Si le linézolide est nécessaire, arrêtez l’ISRS et respectez une période de sevrage adaptée.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodarone + Moxifloxacine : risque d’allongement du QT',
      detail: 'Les deux peuvent allonger l’intervalle QT ; leur association augmente le risque de torsades de pointes.',
      recommendation: 'Évitez l’association ou surveillez étroitement l’ECG.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digoxine + Amiodarone : risque de toxicité de la digoxine',
      detail: 'L’amiodarone augmente les concentrations sanguines de digoxine d’environ 70%.',
      recommendation: 'À l’instauration de l’amiodarone, réduisez de moitié la dose de digoxine et surveillez les concentrations.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Clopidogrel + IPP : effet antiagrégant diminué',
      detail: 'L’oméprazole inhibe le CYP2C19 et réduit la transformation du clopidogrel en son métabolite actif.',
      recommendation: 'Envisagez plutôt le pantoprazole ou un anti-H2.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Lithium + AINS : risque de toxicité du lithium',
      detail: 'Les AINS réduisent l’élimination rénale du lithium, ce qui augmente ses concentrations sanguines.',
      recommendation: 'Évitez l’association ou surveillez étroitement la lithémie.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'Suppléments de potassium + diurétiques épargneurs de potassium : risque d’hyperkaliémie',
      detail: 'Les deux augmentent la kaliémie ; leur association peut provoquer une hyperkaliémie potentiellement mortelle.',
      recommendation: 'Surveillez régulièrement la kaliémie et évitez toute supplémentation potassique concomitante.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Méthotrexate + Cotrimoxazole : risque d’aplasie médullaire',
      detail: 'Les deux inhibent le métabolisme des folates ; leur association augmente le risque d’aplasie médullaire et de mucite.',
      recommendation: 'Évitez l’association ou assurez une supplémentation suffisante en folates et surveillez étroitement la numération sanguine.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'Règles d’interaction intégrées de FRTxGNN (15 règles sélectionnées ; pas une consultation complète de DDInter)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">Aucune alerte d’interaction médicamenteuse</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>Recommandation :</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">Source : ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nRecommandation : ${alert.recommendation}`,
      source: {
        label: 'FRTxGNN DDI Checker',
        url: 'https://frtxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.TwTxGNN = global.TwTxGNN || {};
  global.TwTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
