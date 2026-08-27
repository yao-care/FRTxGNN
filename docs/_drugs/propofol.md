---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Propofol : De l'Anesthésie Générale à la Migraine

## Résumé en Une Phrase

Propofol est un agent anesthésique/sédatif intraveineux, historiquement utilisé pour l'induction et l'entretien de l'anesthésie générale ainsi que pour la sédation procédurale.
Le modèle TxGNN prédit qu'il pourrait être efficace, à dose infra-anesthésique, pour le traitement de la **Migraine (crise aiguë)**,
avec **5 essais cliniques** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Anesthésie générale / Sédation intraveineuse |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99.69 % (rang TxGNN #2716) |
| Niveau de Preuve | L2 |
| Statut de Marché (Taïwan) | ✗ Non commercialisé |
| Nombre d'AMM (Taïwan) | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le champ officiel de mécanisme d'action (DrugBank) est actuellement une lacune de données (Data Gap High — DG002). Cependant, la littérature associée à cette prédiction documente elle-même un mécanisme plausible : le propofol est un modulateur allostérique positif du récepteur GABA-A, à l'origine de ses effets sédatifs, anxiolytiques et antiémétiques. Une étude de mécanisme (PMID 22390898) montre qu'à dose sub-anesthésique, le propofol supprime la **dépression corticale envahissante** (cortical spreading depression, CSD), phénomène considéré comme le corrélat neuronal de l'aura migraineuse et un déclencheur possible de la douleur migraineuse.

Le lien entre l'indication d'origine (anesthésie/sédation) et la nouvelle indication (migraine) repose donc sur un changement de posologie plutôt que sur un changement de cible pharmacologique : aux doses utilisées en anesthésie, le propofol induit une perte de conscience ; à doses beaucoup plus faibles (« low-dose » ou « sub-hypnotic »), il conserverait un effet inhibiteur sur la CSD et sur la transmission nociceptive centrale sans sédation profonde, ce qui a conduit des équipes d'urgence à l'utiliser en perfusion lente pour interrompre des crises de migraine réfractaires.

Cette hypothèse est soutenue par plus de 20 ans de littérature clinique (premiers rapports de cas dès 2000) et par au moins un essai contrôlé randomisé de Phase 2/3 chez l'enfant. Les limites principales restent la petite taille des échantillons, la prédominance de données pédiatriques/urgences, et l'absence de données de sécurité structurées (cf. section Sécurité) qui imposeraient une utilisation encadrée (surveillance respiratoire et hémodynamique).

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Terminé (Completed) | 74 | Essai le plus solide : traitement abortif par propofol faible dose vs traitement standard de la migraine pédiatrique en urgence. |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | N/A | Terminé (Completed) | 40 | Perfusion de propofol à faible dose comme agent abortif de la migraine chez l'enfant ; évaluation de l'efficacité et des limites de dose sûres. |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | N/A | Arrêté (Terminated) | 12 | Propofol à faible dose pour migraine sévère réfractaire aux urgences ; essai arrêté prématurément, échantillon très limité. |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | N/A | Statut inconnu (Unknown) | 130 | Comparaison sévoflurane vs propofol sur la survenue de céphalées postopératoires — pertinence indirecte (contexte chirurgical, pas traitement de crise migraineuse). |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | N/A | Terminé (Completed) | 315 | Électroacupuncture périopératoire en chirurgie cardiaque — pertinence faible, probablement un signal de bruit dans le graphe de connaissances plutôt qu'une preuve directe. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Recommandation (Guideline) | Headache | Mise à jour 2025 des recommandations de l'American Headache Society sur les traitements parentéraux de la migraine aux urgences. |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Revue Systématique | Acad Emerg Med | Revue systématique sur la sécurité et l'efficacité du propofol pour la migraine aiguë aux urgences. |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | ECR | J Emerg Med | ECR prospectif : propofol à faible dose pour la migraine pédiatrique, profil d'effets secondaires favorable. |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | ECR | Arch Acad Emerg Med | ECR en double aveugle : propofol + granisétron vs propofol + métoclopramide dans la migraine aiguë. |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | ECR pilote | Emerg Med Australas | Essai pilote randomisé : propofol IV à dose de sédation procédurale vs traitement standard pour la migraine aux urgences. |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | ECR | Arch Acad Emerg Med | ECR : efficacité de la combinaison sumatriptan/propofol vs sumatriptan/placebo dans la migraine aiguë. |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Revue Systématique / Méta-analyse en réseau | Headache | Comparaison de l'efficacité des agents parentéraux (dont propofol) pour réduire les rechutes après une crise sévère. |
| [26790849](https://pubmed.ncbi.nlm.nih.gov/26790849/) | 2016 | Revue Systématique | Headache | Revue systématique qualitative des traitements abortifs de la migraine pédiatrique aux urgences. |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Revue Systématique / Recommandation | Cephalalgia | Recommandations de la Société Canadienne de Céphalée sur le traitement de la douleur migraineuse en contexte d'urgence. |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Revue | Curr Pain Headache Rep | Revue du traitement intraveineux de la migraine chez l'enfant et l'adolescent, incluant le propofol. |

---

## Informations de Marché (Taïwan)

Aucune Autorisation de Mise sur le Marché (AMM) n'est enregistrée pour le propofol dans le pack de données (statut : **Non commercialisé**, 0 licence recensée). Aucun tableau de spécialités n'est donc disponible à ce stade.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*(Les rubriques mises en garde, contre-indications et interactions médicamenteuses ne contiennent actuellement aucune donnée exploitable — cf. lacune bloquante DG001 ci-dessous.)*

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le niveau de preuve L2 repose sur un essai contrôlé randomisé de Phase 2/3 complet (NCT01604785, n=74) et plusieurs autres ECR de plus petite taille, appuyés par une revue systématique et une recommandation de société savante récente (2026). Le mécanisme (inhibition de la CSD) est biologiquement plausible et cohérent avec l'usage clinique rapporté depuis 2000. Toutefois, la population étudiée est majoritairement pédiatrique/urgence, les échantillons restent petits, et **aucune donnée de sécurité structurée n'est disponible** — un point classé comme lacune bloquante (DG001) empêchant à ce stade l'entrée en évaluation de sécurité initiale (S1). La recommandation « Proceed with Guardrails » doit donc être comprise comme conditionnelle à la levée de cette lacune avant toute utilisation clinique encadrée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtention de la notice / des mises en garde officielles (TFDA ou équivalent) — lacune bloquante (DG001)
- Données structurées de mécanisme d'action (DrugBank) — lacune importante (DG002)
- Données d'interactions médicamenteuses (DDI), actuellement introuvables
- Protocole de surveillance dédié aux effets liés à la sédation (dépression respiratoire, hypotension) lors d'un usage à dose infra-anesthésique
- Données complémentaires chez l'adulte (les ECR disponibles sont majoritairement pédiatriques) pour élargir la population cible
- Clarification de la voie d'accès réglementaire, le produit n'étant actuellement pas commercialisé à Taïwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

