---
layout: default
title: Talc
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
---

# Talc
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

# TALC : D'une Indication Originale Non Documentée à la Maladie Thrombotique

## Résumé en Une Phrase

TALC (DrugBank DB09511) ne dispose d'aucune indication d'origine ni de statut réglementaire documenté dans les sources actuelles (non commercialisé en France, 0 AMM). Le modèle TxGNN prédit une efficacité potentielle pour la **Maladie Thrombotique**, avec **0 essai clinique** et **11 publications** actuellement associées — mais ces publications décrivent en réalité des complications thrombotiques *causées* par le talc, et non un effet thérapeutique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans les sources disponibles |
| Nouvelle Indication Prédite | Maladie Thrombotique (thrombotic disease) |
| Score de Prédiction TxGNN | 99.85 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, TALC (silicate de magnésium hydraté) n'a pas d'indication thérapeutique documentée dans les sources consultées, et aucune licence n'est enregistrée sur le marché français.

L'ensemble des publications identifiées pour l'indication « maladie thrombotique » décrit en réalité la formation de granulomes vasculaires et de thromboses **induites** par des microparticules de talc, lorsqu'il est introduit par voie intraveineuse (contaminant de comprimés broyés lors d'injections illicites) ou par inhalation. Il ne s'agit pas d'un effet antithrombotique thérapeutique, mais d'un mécanisme de toxicité vasculaire bien établi.

Le score élevé attribué par TxGNN (99.85 %) reflète très probablement une confusion du graphe de connaissances entre corrélation pathologique (« talc → thrombose ») et relation thérapeutique (« talc traite la thrombose ») — c'est-à-dire une inversion du sens causal réel. Cette même problématique se retrouve dans les 9 autres indications prédites pour ce candidat (arthrite rhumatoïde, bronchite, maladie veineuse, etc.), toutes classées « Hold » avec un niveau de preuve L4-L5, la littérature disponible étant presque exclusivement toxicologique ou occupationnelle plutôt que thérapeutique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [7756380](https://pubmed.ncbi.nlm.nih.gov/7756380/) | 1995 | Revue | Current Opinion in Oncology | Revue des complications intrathoraciques malignes, dont la thrombose de la veine cave supérieure liée aux cathéters |
| [7387487](https://pubmed.ncbi.nlm.nih.gov/7387487/) | 1980 | Rapport de cas | Archives of Neurology | Syndrome médullaire médian chez une toxicomane suite à une granulomatose systémique au talc et infarctus ischémiques après injection IV |
| [4854601](https://pubmed.ncbi.nlm.nih.gov/4854601/) | 1974 | Série de cas | J Can Assoc Radiol | Granulomatose au talc et hypertension pulmonaire angiothrombotique chez des toxicomanes |
| [8537192](https://pubmed.ncbi.nlm.nih.gov/8537192/) | 1995 | Série de cas | International Ophthalmology | Élargissement de la zone avasculaire fovéale dans l'occlusion veineuse rétinienne, incluant la rétinopathie au talc |
| [4692998](https://pubmed.ncbi.nlm.nih.gov/4692998/) | 1973 | Rapport de cas | Am J Med Sci | Microembolisation rétinienne et cérébrale de talc chez un toxicomane |
| [35648447](https://pubmed.ncbi.nlm.nih.gov/35648447/) | 2022 | Rapport de cas | Texas Heart Institute Journal | Syndrome de Trousseau (thrombose) associé à un cancer du côlon occulte, un syndrome de Lynch et une hypertension pulmonaire thromboembolique chronique |
| [8010794](https://pubmed.ncbi.nlm.nih.gov/8010794/) | 1994 | Série de cas | The Annals of Thoracic Surgery | Chirurgie thoracique vidéo-assistée pour le traitement du chylothorax compliqué |
| [23700302](https://pubmed.ncbi.nlm.nih.gov/23700302/) | 2013 | Rapport de cas | Dtsch Med Wochenschr | Insuffisance cardiaque droite aiguë après injection IV d'héroïne mêlée à du flunitrazépam broyé (excipients dont le talc) |
| [6893924](https://pubmed.ncbi.nlm.nih.gov/6893924/) | 1981 | Rapport de cas | Arch Pathol Lab Med | Granulomatose pulmonaire par embolie de cellulose microcristalline suite à des injections IV illicites de pentazocine ; le talc y induit une thrombose vasculaire |
| [1784766](https://pubmed.ncbi.nlm.nih.gov/1784766/) | 1991 | Non classé | Revista Clínica Española | Granulomatose pulmonaire angiothrombotique chez des toxicomanes IV : le talc provoque des phénomènes thrombotiques avec formation de granulomes à corps étranger |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune indication d'origine, MOA ou donnée de marché n'est documentée pour TALC, et l'absence de notice/mise en garde TFDA (gap bloquant DG001) empêche toute évaluation de sécurité de niveau S1.
- Pour l'indication la mieux dotée en littérature (maladie thrombotique, score 99.85 %), les 11 publications disponibles décrivent des complications **causées** par le talc et non un effet thérapeutique — signal probable d'inversion causale dans le graphe de connaissances TxGNN. Les 9 autres indications prédites présentent le même profil (preuve L4-L5, toxicologie occupationnelle ou cas cliniques isolés) et sont toutes classées Hold.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir le RCP/notice TFDA pour lever le blocage DG001 (mises en garde, contre-indications)
- Clarifier le mécanisme d'action officiel via l'API DrugBank (DG002)
- Réévaluer les arêtes du graphe TxGNN à l'origine de ces prédictions pour corriger une possible inversion toxicité/traitement
- Si l'usage clinique reconnu du talc (agent sclérosant de pleurodèse) doit être exploré, requalifier la piste de recherche vers une indication cohérente avec les données réellement disponibles, hors du cadre actuel « maladie thrombotique »
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

