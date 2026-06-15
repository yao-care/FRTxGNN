---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Caplacizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Caplacizumab : Du Purpura Thrombotique Thrombocytopénique Acquis (aTTP) à son Introduction en France

---

## Résumé en Une Phrase

Caplacizumab est un nanoanticorps humanisé bivalent ciblant le domaine A1 du facteur von Willebrand (vWF), approuvé par la FDA (2019) et l'EMA pour le traitement du purpura thrombotique thrombocytopénique acquis à médiation immunitaire (aTTP) — une microangiopathie thrombotique rare et potentiellement mortelle — actuellement non commercialisé en France.
Le modèle TxGNN prédit avec un score de **99,9965%** son efficacité dans le **Purpura Thrombotique Thrombocytopénique (TTP)**,
soutenu par **14 essais cliniques** (dont 3 essais de Phase 3 complétés) et **20 publications** incluant des RCT dans le *New England Journal of Medicine* et les directives cliniques ISTH 2020 et 2025.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | aTTP (approuvé FDA 2019 / EMA — non commercialisé en France) |
| Nouvelle Indication Prédite | Purpura Thrombotique Thrombocytopénique (TTP) |
| Score de Prédiction TxGNN | 99,9965% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données formelles sur le mécanisme d'action (MOA) ne sont pas disponibles dans le présent dossier. Sur la base des informations issues des rationales de repositionnement, caplacizumab est un nanoanticorps bivalent humanisé (fragment de domaine variable seul, format Nanobody®) qui cible spécifiquement le **domaine A1 du facteur von Willebrand (vWF)**. En bloquant directement l'interaction entre les multimères de vWF et la glycoprotéine plaquettaire **GPIbα**, il interrompt l'adhésion des plaquettes aux parois vasculaires lésées et la formation de microthrombus, sans affecter l'hémostase primaire dans des conditions physiologiques normales.

La physiopathologie de l'aTTP repose sur une déficience sévère en **ADAMTS13** — la protéase qui clive normalement les ultra-larges multimères de vWF. En l'absence d'ADAMTS13 (le plus souvent par auto-anticorps inhibiteurs), ces multimères s'accumulent dans la circulation, se lient massivement aux plaquettes via GPIbα, et génèrent des microthrombus plaquettaires diffus entraînant thrombocytopénie, anémie hémolytique microangiopathique et ischémie multi-organes. Caplacizumab cible précisément ce maillon terminal de la cascade thrombotique, permettant une normalisation rapide du nombre de plaquettes indépendamment de la restauration de l'activité ADAMTS13 par l'immunosuppression.

La cohérence entre la prédiction TxGNN et le corpus clinique mondial est remarquable : caplacizumab figure aujourd'hui comme traitement adjuvant de première ligne dans les directives ISTH 2020 et leur mise à jour 2025, en association à l'échange plasmatique thérapeutique et à l'immunosuppression. Son introduction en France représente ainsi moins un repositionnement exploratoire qu'une mise à disposition d'un médicament dont l'efficacité est solidement établie au niveau international.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Phase 2 | Terminé | 75 | **TITAN trial** — Premier RCT randomisé simple aveugle contre placebo en aTTP ; établit la sécurité et l'efficacité initiales de caplacizumab comme traitement adjuvant à l'échange plasmatique |
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Phase 3 | Terminé | 145 | **HERCULES trial** — RCT double aveugle contre placebo ; démontre une restauration plus rapide du nombre de plaquettes et une réduction significative de la microthrombose et des exacerbations |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Phase 3 | Terminé | 51 | Étude ouverte multicentrique mono-bras évaluant l'efficacité et la sécurité de caplacizumab + immunosuppression **sans échange plasmatique de première ligne** chez les adultes atteints d'iTTP |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Phase 2/3 | Terminé | 21 | Étude japonaise multicentrique ouverte ; évalue la prévention des récurrences d'aTTP et la sécurité dans la population est-asiatique |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Phase 3 | Terminé | 104 | **Post-HERCULES** — Suivi prospectif à long terme ; évalue la sécurité et l'efficacité lors de réutilisations répétées de caplacizumab |
| [NCT05876221](https://clinicaltrials.gov/study/NCT05876221) | N/A | Terminé | 223 | Étude observationnelle (n=223) réévaluant la cinétique plaquettaire à l'ère de caplacizumab ; découplage thrombocytes/ADAMTS13 et risques de sur- ou sous-traitement |
| [NCT06291025](https://clinicaltrials.gov/study/NCT06291025) | N/A | En recrutement | 131 | Étude multicentrique de non-infériorité évaluant immunosuppression + caplacizumab + perfusion plasmatique **sans échange plasmatique thérapeutique** dans l'iTTP |
| [NCT06376786](https://clinicaltrials.gov/study/NCT06376786) | N/A | En recrutement | 132 | **Registre iTTP italien** prospectif national multicentrique ; données réelles sur l'histoire naturelle et les résultats cliniques à long terme (suivi 3 ans) |
| [NCT07205861](https://clinicaltrials.gov/study/NCT07205861) | N/A | En recrutement | 1 200 | **TWI-LIGHT** — Grande étude rétrospective française (Cohorte nationale Centre TMA) ; analyse épidémiologique, pronostique et thérapeutique de l'aTTP en France |
| [NCT05262881](https://clinicaltrials.gov/study/NCT05262881) | N/A | Inconnu | 50 | **ROSCAPLI** — Expérience italienne multicentrique rétrospective de caplacizumab en aTTP (données réelles, Q4-2019 – février 2021) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | RCT Phase 3 | *N Engl J Med* | **Publication HERCULES** — Caplacizumab réduit significativement la durée de l'échange plasmatique, le taux d'exacerbations et les événements thromboemboliques majeurs dans l'aTTP |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | RCT Phase 2 | *N Engl J Med* | **Publication TITAN** — Premier RCT démontrant l'efficacité de caplacizumab ; réponse au traitement plus rapide et réduction de 73% des exacerbations vs placebo |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Directive clinique | *J Thromb Haemost* | **Directives ISTH 2020 — Traitement du TTP** ; recommande caplacizumab comme traitement adjuvant de première ligne de l'aTTP |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Directive clinique | *J Thromb Haemost* | **Mise à jour ciblée ISTH 2025** des directives de prise en charge du TTP ; intègre les nouvelles données sur l'iTTP et le TTP congénital |
| [32914582](https://pubmed.ncbi.nlm.nih.gov/32914582/) | 2020 | Directive clinique | *J Thromb Haemost* | **Directives ISTH 2020 — Diagnostic du TTP** ; standardisation des approches diagnostiques incluant ADAMTS13 |
| [36053773](https://pubmed.ncbi.nlm.nih.gov/36053773/) | 2023 | Revue systématique + méta-analyse | *Blood Advances* | Méta-analyse RCT + études observationnelles ; caplacizumab ajouté au standard de soins réduit mortalité, rechutes et durée d'hospitalisation dans l'iTTP |
| [37045600](https://pubmed.ncbi.nlm.nih.gov/37045600/) | 2023 | Revue systématique + méta-analyse | *Expert Rev Hematol* | Évaluation exhaustive de l'efficacité et de la sécurité de caplacizumab dans le TTP ; synthèse des populations à risque et des sous-groupes |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | Cohorte multicentrique | *EClinicalMedicine* | **Capla 1000+** — Première grande cohorte internationale rétrospective (>1 000 patients en vie réelle) ; évalue l'impact de caplacizumab sur la mortalité et le moment optimal d'initiation dans l'iTTP |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Revue | *JAMA* | Revue narrative actualisée sur l'iTTP (incidence, pathophysiologie, traitement) destinée aux cliniciens ; synthèse des meilleures pratiques 2025 |
| [34266669](https://pubmed.ncbi.nlm.nih.gov/34266669/) | 2022 | Recommandations d'experts | *Med Clin* | Recommandations espagnoles pour le diagnostic et le traitement du TTP ; intégration de caplacizumab dans les algorithmes thérapeutiques nationaux |

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes (mises en garde, contre-indications et interactions médicamenteuses).

> **Note :** Les données de sécurité françaises (ANSM) et les interactions médicamenteuses (DDI) ne sont pas disponibles dans le présent dossier. Le risque hémorragique — inhérent au mécanisme anti-vWF — constitue la principale préoccupation clinique documentée dans les essais TITAN et HERCULES et devra être évalué dans le plan de gestion des risques.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Caplacizumab dispose du niveau de preuve le plus élevé (L1) pour le traitement de l'aTTP, avec deux essais de Phase 3 complétés (HERCULES, NCT05468320), une approbation FDA/EMA, et une intégration dans les directives cliniques internationales ISTH comme traitement de première ligne — la prédiction TxGNN est entièrement cohérente avec ce corpus clinique mondial. L'absence d'AMM en France pour une maladie rare à mortalité >90% sans traitement constitue une lacune thérapeutique identifiée qui justifie une démarche d'introduction structurée.

**Pour avancer, les éléments suivants sont nécessaires :**

- **Clarification réglementaire urgente** : vérifier si Cablivi® (nom commercial EMA) bénéficie d'un accès précoce en France (AAP/ATU historique) ou si une procédure d'AMM nationale est en cours auprès de l'ANSM
- **Données de sécurité complètes** : récupérer les avertissements et contre-indications officiels via la notice EMA / ANSM (DG001 — priorité Blocking)
- **Mécanisme d'action détaillé** : requête DrugBank DB06081 pour le MOA complet (DG002 — priorité High)
- **Évaluation des interactions médicamenteuses (DDI)** : particulièrement avec anticoagulants et antiplaquettaires co-prescrits dans la prise en charge de l'aTTP
- **Plan de gestion du risque hémorragique** : protocole de surveillance spécifique compte tenu du mécanisme anti-vWF (antidote, protocole chirurgical d'urgence)
- **Analyse médico-économique** : l'aTTP touche ~4 cas/million/an en France (~270 cas/an) — évaluation coût-efficacité requise pour le remboursement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

