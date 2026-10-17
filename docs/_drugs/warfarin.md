---
layout: default
title: Warfarin
parent: Preuves modérées (L3-L4)
nav_order: 824
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Warfarin : nouvelle indication prédite, Déficit en cofacteur II de l'héparine (niveau de preuve L4). Indication d'origine : Embolie pulmonaire, maladie thrombotique, embolie intracrânienne"
monitor_inn: "warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
---

# Warfarin
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

# Warfarine : De l'embolie pulmonaire au déficit en cofacteur II de l'héparine

## Résumé en Une Phrase

La warfarine est un anticoagulant antivitamine K, initialement utilisé pour traiter et prévenir la maladie thrombo-embolique (embolie pulmonaire, maladie thrombotique, embolie intracrânienne).
Le modèle TxGNN prédit qu'elle pourrait être utile pour le **déficit en cofacteur II de l'héparine**, mais cette prédiction ne repose que sur **3 publications (rapports de cas)** et **aucun essai clinique**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Embolie pulmonaire, maladie thrombotique, embolie intracrânienne (le texte d'indication des AMM françaises n'est pas renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Déficit en cofacteur II de l'héparine |
| Score de Prédiction TxGNN | 99,87 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la warfarine est un antagoniste de la vitamine K : elle réduit la synthèse des facteurs de coagulation vitamine K-dépendants (II, VII, IX, X). Son efficacité dans la maladie thrombo-embolique veineuse est établie.

Le déficit en cofacteur II de l'héparine est une thrombophilie héréditaire qui altère l'inhibition de la thrombine. Comme l'indication originale (thrombose, embolie), il s'agit d'un état à risque thrombotique : une anticoagulation prolongée est donc mécanistiquement plausible comme prévention des récidives.

Il faut toutefois rester prudent : les preuves se limitent à trois rapports de cas ou de famille (1990-2001), sans données comparatives. Il s'agit davantage d'un usage déjà existant en pratique pour la thrombose que d'un véritable repositionnement.

Autres prédictions du modèle, à titre indicatif :
- **Excès de facteur V avec thrombose spontanée** (99,84 %) et **déficit en antithrombine de type 2** (99,84 %) : plausibles mécanistiquement, mais soutenus par très peu de données (aucune publication, ou un seul rapport de cas).
- **Thrombophilie** (99,75 %) : seule prédiction avec un essai de phase 3, mais il évalue une stratégie de durée guidée par les D-dimères, pas la warfarine spécifiquement.
- **Polyarthrite rhumatoïde, maladie fibrokystique du sein, dysplasie mammaire bénigne** : aucun lien mécanistique plausible. Les essais liés à la polyarthrite sont des études d'interaction où la warfarine sert de substrat sonde ; ces scores élevés sont probablement des artefacts du graphe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour le déficit en cofacteur II de l'héparine.

À titre de contexte, pour la prédiction « thrombophilie » (rang 4) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Phase 3 | Inconnu | 300 | Stratégie guidée par les D-dimères pour adapter la durée de l'anticoagulation orale après une thrombose veineuse profonde non provoquée ; non spécifique à la thrombophilie |

## Preuves de la Littérature

Pour le déficit en cofacteur II de l'héparine :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Rapport de cas | Kyobu Geka | Thrombose du ventricule droit chez une adolescente de 14 ans avec déficit familial en cofacteur II de l'héparine, initialement prise pour un myxome |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Rapport de cas | Nihon Kyobu Shikkan Gakkai Zasshi | Déficit congénital en antithrombine avec infarctus pulmonaire ; warfarine pendant 7 ans, puis relais par l'héparine |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Rapport de cas (famille) | Journal of UOEH | Famille avec thromboses multiples ; warfarine instaurée chez un enfant qui a présenté une récidive à 7 ans |

Pour le contexte de la thrombophilie, une revue récente à citer : [39233011](https://pubmed.ncbi.nlm.nih.gov/39233011/) (2024, J Thromb Haemost) sur l'usage des anticoagulants oraux directs dans la prévention secondaire des thromboses en cas de thrombophilie sévère, qui souligne que ces derniers sont devenus le traitement de première intention, avec peu de données dans ce sous-groupe.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63245753 | COUMADINE 5 mg, comprimé sécable (TEOFARMA) | Comprimé sécable | Non renseignée (AMM annulée) |
| 64631925 | COUMADINE 2 mg, comprimé sécable (TEOFARMA) | Comprimé sécable | Non renseignée (AMM annulée) |
| 68364117 | COUMADINE 5 mg, comprimé sécable (DIFARMED, Espagne) | Comprimé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, insuffisance ou maladie hépatique, maladie de la vésicule biliaire, insuffisance cardiaque congestive, hypothyroïdie/myxœdème, syndrome néphrotique, troubles psychotiques et mentaux, maladies du tissu conjonctif, maladies osseuses et cartilagineuses, abus de substances, troubles de la coagulation, hyperlipidémie, anémie, insuffisance rénale, cholestase, diarrhée chronique.
- **Interactions médicamenteuses** : 865 interactions recensées. Parmi les principales :
  - **Majeures** : acide acétylsalicylique, métronidazole.
  - **Modérées** : ranitidine, rabéprazole, doxycycline, hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone, metformine, amoxicilline, bupropion, aprépitant, mésalazine, balsalazide, acide chénodésoxycholique.
  - **Mineures** : acarbose, albiglutide, acide ascorbique.
- Les mises en garde et contre-indications de la notice ANSM n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations. Le risque hémorragique, inhérent à tout anticoagulant, impose une surveillance de l'INR.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves pour le déficit en cofacteur II de l'héparine se limitent à trois rapports de cas anciens (niveau L4), sans essai clinique. Toutes les AMM françaises de la warfarine (Coumadine) sont annulées, et les données de sécurité de la notice font défaut.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), préalable bloquant au criblage de sécurité.
- Obtenir les données sur le mécanisme d'action via DrugBank.
- Rechercher des études observationnelles ou des registres comparant la warfarine aux alternatives (héparines de bas poids moléculaire, anticoagulants oraux directs) dans les thrombophilies héréditaires.
- Pour la thrombophilie, confirmer la pertinence de l'essai NCT00895505 pour une population spécifique et clarifier son statut.
- Clarifier le statut réglementaire actuel de la warfarine en France (autres spécialités éventuellement commercialisées).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

