---
layout: default
title: Talc
parent: Preuves modérées (L3-L4)
nav_order: 300
evidence_level: L4
indication_count: 10
---

# Talc
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Talc : D'une indication d'origine non documentée à la maladie thrombotique

## Résumé en une phrase

Le talc est présent en France dans une pâte pour application locale (ALOPLASTINE), mais son indication d'origine n'est pas renseignée dans les données disponibles.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **maladie thrombotique**, avec **0 essai clinique** et **11 publications** qui décrivent surtout le talc comme une cause de lésions vasculaires.
Cette prédiction doit être lue comme un **signal de sécurité** et non comme une piste thérapeutique.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Nouvelle indication prédite | Maladie thrombotique (thrombotic disease) |
| Score de prédiction TxGNN | 99,85 % |
| Niveau de preuve | L4 |
| Statut de marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision recommandée | Hold |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le talc est connu comme agent sclérosant, utilisé notamment pour la pleurodèse. Aucune action antithrombotique n'est décrite, et l'indication d'origine du produit français n'est pas renseignée.

**La prédiction ne repose donc sur aucun mécanisme thérapeutique plausible.** La littérature retrouvée décrit le talc comme une cause de lésions vasculaires. Chez les usagers de drogues par voie intraveineuse, l'injection de talc ou d'excipients provoque une hypertension pulmonaire angiothrombotique, des microemboles rétiniens et cérébraux et une granulomatose.

Le score TxGNN très élevé (99,85 %, rang 1610) reflète probablement une association du talc avec la thrombose dans le graphe de connaissances, en tant qu'effet indésirable, et non un effet thérapeutique. Le produit français est aussi une pâte à usage local. Cette voie paraît peu compatible avec une maladie thrombotique systémique (évaluation rédactionnelle, la compatibilité de voie n'étant pas encore analysée dans les données).

---

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la littérature

Aucun essai contrôlé randomisé ni revue systématique n'a été retrouvé. Toutes les publications sont des rapports ou séries de cas, des revues narratives ou une étude de cohorte, et elles décrivent un préjudice lié au talc.

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [7756380](https://pubmed.ncbi.nlm.nih.gov/7756380/) | 1995 | Revue | Current Opinion in Oncology | Complications intrathoraciques des cancers ; le syndrome cave supérieur par thrombose augmente avec les dispositifs d'accès veineux |
| [4854601](https://pubmed.ncbi.nlm.nih.gov/4854601/) | 1974 | Série de cas | J Can Assoc Radiol | Granulomatose au talc et hypertension pulmonaire angiothrombotique chez des toxicomanes |
| [7387487](https://pubmed.ncbi.nlm.nih.gov/7387487/) | 1980 | Rapport de cas | Arch Neurol | Syndrome bulbaire médian avec infarctus ischémiques et granulomatose systémique au talc après injection intraveineuse |
| [4692998](https://pubmed.ncbi.nlm.nih.gov/4692998/) | 1973 | Rapport de cas | Am J Med Sci | Microembolisation rétinienne et cérébrale de talc chez un toxicomane |
| [6893924](https://pubmed.ncbi.nlm.nih.gov/6893924/) | 1981 | Série de cas | Arch Pathol Lab Med | Embolie pulmonaire et granulomatose à la cellulose microcristalline après injection de comprimés ; la lésion vasculaire principale est la thrombose |
| [1784766](https://pubmed.ncbi.nlm.nih.gov/1784766/) | 1991 | Rapport de cas (2 cas) | Rev Clin Esp | Granulomatose pulmonaire angiothrombotique chez des toxicomanes ; le talc utilisé comme excipient provoque des phénomènes thrombotiques |
| [8537192](https://pubmed.ncbi.nlm.nih.gov/8537192/) | 1995 | Cohorte | Int Ophthalmol | Zone avasculaire fovéale élargie dans l'occlusion veineuse rétinienne, comme dans la rétinopathie au talc |
| [23700302](https://pubmed.ncbi.nlm.nih.gov/23700302/) | 2013 | Rapport de cas | Dtsch Med Wochenschr | Insuffisance cardiaque droite aiguë après injection intraveineuse d'héroïne et de flunitrazépam broyé |
| [35648447](https://pubmed.ncbi.nlm.nih.gov/35648447/) | 2022 | Rapport de cas | Tex Heart Inst J | Syndrome de Trousseau (thrombose associée à un cancer occulte du côlon), sans lien avec le talc |
| [41646593](https://pubmed.ncbi.nlm.nih.gov/41646593/) | 2026 | Rapport de cas | Cureus | Pneumothorax récidivant après pneumonectomie sous ECMO, peu pertinent pour la thrombose |

---

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique |
|---------|------|------|
| 62744504 | ALOPLASTINE, pâte pour application locale (Laboratoires Macors) | Pâte pour application |

---

## Considérations de sécurité

Veuillez consulter la notice pour les informations de sécurité.

Un signal ressort néanmoins de la littérature analysée : l'administration intraveineuse de talc ou d'excipients contenant du talc est associée à des événements thrombotiques et emboliques (poumon, rétine, cerveau). Aucune interaction médicamenteuse n'a été retrouvée dans les données disponibles.

---

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique n'existe et aucun mécanisme thérapeutique n'est étayé. La littérature indique plutôt que le talc peut provoquer des lésions thrombotiques, et le score TxGNN élevé semble être un artefact du graphe de connaissances.
- Les neuf autres indications prédites (exostose, polyarthrite rhumatoïde, bronchite, déficit en cofacteur II de l'héparine, etc.) sont également en Hold, au niveau de preuve L4 ou L5.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) afin de pouvoir engager le criblage de sécurité
- Obtenir le mécanisme d'action détaillé via DrugBank
- Confirmer l'indication d'origine de l'AMM 62744504
- Ne relancer l'évaluation que si de nouvelles preuves cliniques ou mécanistiques apparaissent. Sinon, traiter la prédiction comme un signal de sécurité à documenter.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

