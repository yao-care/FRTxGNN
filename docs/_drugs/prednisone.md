---
layout: default
title: Prednisone
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Prednisone
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

# Prednisone : D'un Corticostéroïde Systémique à l'Alopécie Areata

## Résumé en Une Phrase

La prednisone est un corticostéroïde systémique de référence, utilisé depuis des décennies comme anti-inflammatoire et immunosuppresseur dans de nombreuses maladies auto-immunes et inflammatoires (l'indication d'origine précise n'est pas documentée dans ce jeu de données). Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**Alopécie Areata**, avec **1 essai clinique directement pertinent** et **20 publications** soutenant cette direction — étant précisé que la majorité des 33 essais renvoyés par la recherche automatisée concernent en réalité le lupus érythémateux disséminé et d'autres pathologies où la prednisone n'est qu'un traitement de fond, et non l'objet testé.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans ce jeu de données (Prednisone est un corticostéroïde systémique à usage anti-inflammatoire/immunosuppresseur large — cf. Lacune de Données DG002) |
| Nouvelle Indication Prédite | Alopécie Areata |
| Score de Prédiction TxGNN | 99.99 % (rang du modèle : 263) |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé (données de ce jeu) |
| Nombre d'AMM | 0 |
| Decision Recommandée | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce jeu de données (Lacune DG002, sévérité *High*). Sur la base des informations pharmacologiques connues, la prednisone est un glucocorticoïde de synthèse qui agit par liaison au récepteur des glucocorticoïdes, inhibant la transcription de gènes pro-inflammatoires (NF-κB, cytokines telles que l'IL-1, l'IL-6, le TNF-α) et modulant la réponse immunitaire à médiation cellulaire (lymphocytes T). Son effet anti-inflammatoire et immunosuppresseur large est établi de longue date en rhumatologie, en dermatologie et en hématologie.

L'alopécie areata est une maladie auto-immune dans laquelle des lymphocytes T ciblent le follicule pileux, provoquant une perte de cheveux en plaques pouvant évoluer vers une forme totale (totalis) ou universelle (universalis). L'infiltrat lymphocytaire péri- et intra-folliculaire caractéristique de cette maladie repose sur des mécanismes inflammatoires directement comparables à ceux que la prednisone cible dans d'autres pathologies auto-immunes, ce qui rend la prédiction du modèle TxGNN mécanistiquement cohérente.

En pratique clinique, la corticothérapie systémique — dont la prednisone — est utilisée depuis les années 1950 dans les formes sévères d'alopécie areata, le plus souvent en association avec le méthotrexate ou, plus récemment, le baricitinib, pour les formes totales/universelles résistantes. Cet usage historique, documenté dans la littérature depuis plus de 60 ans, renforce la plausibilité biologique de la prédiction, même s'il ne s'agit pas actuellement d'une indication approuvée au sens réglementaire, et même si l'effet observé est souvent attribué à l'association thérapeutique plutôt qu'à la prednisone seule.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Terminé | 90 | Essai randomisé en double aveugle comparant méthotrexate seul, méthotrexate + prednisone à faible dose (traitement secondaire), et placebo, dans la pelade (alopécie areata) sévère |

**Remarque sur la qualité des données :** la recherche automatisée « prednisone + alopecia areata » a renvoyé 33 essais cliniques, mais seul l'essai ci-dessus porte réellement sur l'alopécie areata. Les 32 autres essais (ex. NCT03021499, NCT01283139, NCT03616964, NCT01254513, NCT01055496, NCT01972217, etc.) concernent principalement le lupus érythémateux disséminé, le cancer de la prostate ou le lymphome, où la prednisone/corticothérapie n'est qu'un comparateur ou un traitement de fond mentionné dans le protocole. Ils ont été exclus du tableau car non pertinents pour cette indication.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | ECR | JAMA Dermatology | Essai randomisé en double aveugle en 2 étapes : méthotrexate seul vs méthotrexate + prednisone à faible dose chez des patients avec AA totalis/universalis, formes sévères où le méthotrexate seul est peu efficace |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Série de cas | Clinical and Experimental Dermatology | 8 cas d'AA très sévère (SALT ≥ 95) traités par baricitinib + faibles doses de corticostéroïdes ; amélioration majeure alors que le baricitinib ou le méthotrexate seuls restaient peu efficaces dans ces formes |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Étude rétrospective | Dermatology (Basel) | Efficacité et sécurité du méthotrexate combiné à des corticostéroïdes à dose faible à modérée dans l'AA sévère, où la rémission spontanée est peu probable |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Étude clinique | Annales de Dermatologie et de Vénéréologie | Évaluation de l'efficacité et de la sécurité de la prednisone orale administrée en pulse mensuel unique dans la prise en charge de l'AA |
| [41958306](https://pubmed.ncbi.nlm.nih.gov/41958306/) | 2026 | Série de cas | JEADV | Série de cas rétrospective sur l'association baricitinib + prednisone à faible dose dans l'AA très sévère (résumé détaillé non indexé) |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Étude de suivi | Archives of Dermatology | 18 patients traités par prednisone en jours alternés pour l'AA, réévalués ~15 mois après l'arrêt : réponse initiale mais bénéfice à long terme limité, effets secondaires stéroïdiens fréquents (acné, obésité, opacités du cristallin, HTA légère) |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | Étude clinique/immunopathologique | Journal of the American Academy of Dermatology | Évaluation clinique et immunopathologique de la ciclosporine systémique associée à la prednisone à faible dose dans l'AA chronique sévère (résumé non indexé) |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Étude clinique | Archives of Dermatology | Étude des paramètres immunologiques et de la réponse au traitement par prednisone dans l'alopécie areata (résumé non indexé) |
| [911178](https://pubmed.ncbi.nlm.nih.gov/911178/) | 1977 | Rapport clinique | Archives of Dermatology | Rapport/commentaire clinique sur le traitement par prednisone de l'alopécie areata (résumé non indexé) |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Rapport historique | Medical Times | Traitement de l'alopécie areata, partialis et totalis par la cortisone, l'hydrocortisone et leurs analogues (prednisone, prednisolone) (résumé non indexé) |

---

## Informations de Marché en France

D'après ce jeu de données, la prednisone n'est actuellement associée à **aucune AMM enregistrée en France** (statut de marché : « non commercialisé », 0 licence). Aucune information de produit commercial (nom, forme pharmaceutique, indication approuvée) n'est donc disponible.

*Point d'attention méthodologique : la prednisone est une molécule générique largement utilisée en pratique clinique courante ; l'absence totale d'AMM dans ce pipeline suggère probablement une lacune de collecte de données côté ANSM plutôt qu'une réalité réglementaire, et devrait être vérifiée manuellement avant toute conclusion.*

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune donnée de mise en garde, de contre-indication ou d'interaction médicamenteuse n'a pu être extraite pour cette évaluation. Il s'agit d'une **lacune bloquante** (DG001 : « TFDA 仿單警語/禁忌 », sévérité *Blocking*) qui empêche à ce stade toute évaluation de sécurité préliminaire (étape S1).

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Une lacune de données **bloquante** (DG001) empêche toute évaluation de sécurité préliminaire (mises en garde et contre-indications absentes), ce qui interdit de faire progresser ce candidat au-delà de la revue documentaire à ce stade.
- Le niveau de preuve d'efficacité (L2 : un essai de Phase 3 complété + littérature historique et rétrospective abondante) est encourageant mais repose presque exclusivement sur des **associations** (prednisone + méthotrexate ou + baricitinib), rendant difficile d'isoler la contribution propre de la prednisone.
- L'absence apparente d'AMM en France (0 licence) prive ce dossier de base réglementaire immédiate, bien que ce point nécessite une vérification manuelle indépendante.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données d'étiquetage TFDA/ANSM (mises en garde, contre-indications) — remédiation DG001
- Obtenir les données structurées de mécanisme d'action depuis DrugBank — remédiation DG002
- Clarifier l'indication d'origine réellement approuvée pour la prednisone en France/UE
- Réaliser une analyse de contribution du composant pour distinguer l'effet de la prednisone seule de celui des associations (méthotrexate, baricitinib) dans l'AA
- Vérifier manuellement auprès de l'ANSM le statut réel de commercialisation en France, la valeur « 0 AMM » semblant incohérente avec l'usage clinique bien établi de cette molécule
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

