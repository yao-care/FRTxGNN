---
layout: default
title: Theophylline
parent: Prédiction du modèle uniquement (L5)
nav_order: 751
evidence_level: L5
indication_count: 6
monitor_inn: "theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-11-20
description: "Theophylline : nouvelle indication prédite, Maladie thrombotique (niveau de preuve L5). Indication d'origine : Asthme"
---

# Theophylline
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Théophylline : De l'asthme à la maladie thrombotique
{: .text-alpha }

## Résumé en Une Phrase

La théophylline est un bronchodilatateur dont l'usage d'origine concerne l'asthme et d'autres maladies respiratoires (bronchite, emphysème). Le modèle TxGNN la prédit comme potentiellement efficace pour la **maladie thrombotique**. Aucun essai clinique ni aucune publication ne teste la théophylline dans cette indication : la prédiction reste donc purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Asthme (relation enregistrée dans le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné dans les données compilées) |
| Nouvelle Indication Prédite | Maladie thrombotique |
| Score de Prédiction TxGNN | 0,9962 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 6) |
| Nombre d'AMM | 6 (valides : 6) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Theophylline (traduction non officielle) : « La théophylline exerce deux actions distinctes dans les voies aériennes des patients présentant une obstruction réversible : une relaxation des muscles lisses (c.-à-d. une bronchodilatation) et une suppression de la réponse des voies aériennes aux stimuli (c.-à-d. des effets prophylactiques non bronchodilatateurs). » Texte original en anglais : "Theophylline has two distinct actions in the airways of patients with reversible obstruction: smooth muscle relaxation (i.e., bronchodilation) and suppression of the response of the airways to stimuli (i.e., non-bronchodilator prophylactic effects)." ([DailyMed: Theo-24 (theophylline anhydrous) prescribing information, ENDO USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7a108fa0-c230-475f-be93-6f864b98a410), version du 2024-07-08 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, la théophylline est un inhibiteur non sélectif des phosphodiestérases (PDE) et un antagoniste des récepteurs de l'adénosine. Ces propriétés expliquent son effet bronchodilatateur dans l'asthme et les maladies respiratoires apparentées.

Le lien avec la thrombose est théoriquement plausible mais non démontré. L'inhibition des PDE pourrait augmenter l'AMPc plaquettaire et réduire l'agrégation plaquettaire. Cependant, l'asthme et la thrombose sont des maladies très différentes, et la prédiction ne s'appuie pas sur une parenté clinique entre les deux indications.

La littérature récupérée ne teste pas la théophylline contre la thrombose. Elle porte sur la pharmacocinétique de la ticlopidine, des dosages de biomarqueurs plaquettaires, le traitement des échantillons sanguins, un capteur de détection de la théophylline, etc. Le score élevé de 0,9962 est donc une prédiction informatique sans soutien clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune de ces publications n'étudie directement la théophylline comme traitement de la maladie thrombotique. Elles sont listées à titre de contexte.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revue | Clinical Pharmacokinetics | Pharmacocinétique de la ticlopidine, antiplaquettaire ; ne concerne pas la théophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revue | CRC Critical Reviews in Biochemistry | Rôle des prostaglandines (thromboxane A2, prostacycline) dans l'agrégation plaquettaire et l'athérosclérose |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Étude de laboratoire | General Pharmacology | Effet de la milrinone et de l'adénosine sur l'agrégation plaquettaire et l'AMPc ; la théophylline n'est pas l'objet de l'étude |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Transversale / laboratoire | Rheumatology | Activation des plaquettes et des neutrophiles dans la maladie de Behçet |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Observationnelle | Inflammatory Bowel Diseases | Agrégats plaquettes-leucocytes dans les maladies inflammatoires de l'intestin |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Méthodologie | British Journal of Haematology | Dosage du facteur plaquettaire 4 ; la théophylline n'y est qu'un additif de l'anticoagulant du prélèvement |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Méthode analytique | Analytica Chimica Acta | Capteur électrochimique de détection de la théophylline ; non clinique |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Non classé | Minerva Cardioangiologica | Dérivé nicotinate de théophylline dans l'artériopathie périphérique oblitérante chronique (résumé non disponible) ; ce n'est pas la théophylline elle-même |

## Informations de Marché en France

Les six AMM sont valides, correspondent à des spécialités à base de théophylline seule et sont détenues par SERP. Les textes d'indication autorisée ne sont pas renseignés dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 65265758 | DILATRANE 300 mg | Gélule à libération prolongée |
| 68957644 | DILATRANE 50 mg | Gélule à libération prolongée |
| 64447761 | DILATRANE 100 mg | Gélule à libération prolongée |
| 63514285 | TEDRALAN 200 mg | Gélule à libération prolongée |
| 61848891 | DILATRANE 1 POUR CENT | Sirop |
| 62481804 | DILATRANE 200 mg | Gélule à libération prolongée |

## Considérations de Sécurité

- **Contre-indications (relations du graphe de connaissances, non issues de la notice)** : hypertension, insuffisance hépatique et maladies hépatiques, épilepsie, troubles anxieux et psychotiques, porphyries, maladie rénale, ulcère gastroduodénal, glaucome à angle ouvert, hypothyroïdie, diabète et acidocétose diabétique, hyperplasie bénigne de la prostate, thrombopénie, neutropénie et agranulocytose, entre autres. Ces éléments doivent être confirmés avec la notice officielle.
- **Interactions médicamenteuses** : 371 interactions recensées. La plus notable est l'interaction **majeure** avec le bupropion. Parmi les interactions modérées figurent la cimétidine, la clarithromycine, l'oméprazole, la famotidine, la ranitidine, les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), les tétracyclines (doxycycline, minocycline, tétracycline) et le charbon actif. Les éphédrines présentent une interaction mineure.
- **Index thérapeutique étroit** : la théophylline nécessite une surveillance de sa concentration. Ce point est particulièrement important dans une indication antithrombotique, où des associations avec des anticoagulants ou antiplaquettaires seraient probables.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni aucune publication ne porte directement sur la théophylline dans la maladie thrombotique (niveau de preuve L5). Le score TxGNN élevé n'est qu'une prédiction informatique, et le profil de sécurité (index thérapeutique étroit, nombreuses interactions) est défavorable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des études précliniques ou ex vivo montrant un effet de la théophylline sur l'agrégation plaquettaire et la thrombose.
- Les données de mécanisme d'action détaillées et l'analyse du lien mécanistique avec la thrombose.
- Les informations de la notice (mises en garde, contre-indications) pour l'évaluation de sécurité.
- Une évaluation des interactions avec les anticoagulants et antiplaquettaires.
- À titre de comparaison, une autre indication prédite, la maladie de la cavité nasale (rhinite allergique), dispose d'une étude clinique humaine indirecte (PMID 9648963). Elle pourrait constituer une piste de recherche plus avancée.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Theo-24 (theophylline anhydrous) prescribing information, ENDO USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7a108fa0-c230-475f-be93-6f864b98a410) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

