---
layout: default
title: Clonidine
parent: Preuves modérées (L3-L4)
nav_order: 188
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Clonidine : nouvelle indication prédite, Syndrome de Gilles de la Tourette (niveau de preuve L3). Indication d'origine : Hypertension artérielle"
monitor_inn: "CLONIDINE"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "Tourette syndrome", "obesity disorder", "hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "migraine disorder", "manic bipolar affective disorder"]
---

# Clonidine
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **10** 
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

# Clonidine : De l'hypertension au syndrome de Gilles de la Tourette

## Résumé en Une Phrase

La clonidine est un agoniste alpha-2 adrénergique à action centrale, initialement utilisé dans le traitement de l'hypertension artérielle, du glaucome à angle ouvert et du trouble déficit de l'attention avec hyperactivité (TDAH).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de Gilles de la Tourette**, avec **2 essais cliniques** (de phase 4, de petite taille) et **19 publications** soutenant actuellement cette direction.
Cette indication correspond toutefois davantage à un usage déjà établi dans les recommandations qu'à un repositionnement réellement nouveau.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (selon les indications du graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome de Gilles de la Tourette |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Proceed with Guardrails |

> Remarque : les prédictions classées aux rangs 1 à 4 (syndrome facio-digito-génital, trouble spécifique du développement, fibrome chondromyxoïde, trichotillomanie) ont des scores TxGNN plus élevés mais des preuves nulles ou très faibles (L4-L5). Le syndrome de Gilles de la Tourette, bien que classé 5e par score, est la prédiction la mieux étayée par les données ; il a donc été retenu comme indication principale de ce rapport.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques générales, la clonidine est un agoniste des récepteurs alpha-2 adrénergiques : elle réduit l'activité noradrénergique centrale et la décharge sympathique, ce qui explique son effet antihypertenseur.

Ce même mécanisme est pertinent dans les tics : la réduction de la transmission noradrénergique module les circuits cortico-striato-thalamo-corticaux impliqués dans le syndrome de Gilles de la Tourette. L'usage de la clonidine dans le TDAH (indication originale du graphe de connaissances) est également pertinent, car le TDAH est la comorbidité la plus fréquente du syndrome de Gilles de la Tourette. La clonidine figure comme option dans les lignes directrices européennes de 2022 pour les tics, en particulier en présence d'un TDAH associé.

Les effets observés restent modestes selon les méta-analyses. Cette indication est d'ailleurs plutôt un usage déjà établi qu'un repositionnement inédit.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | Inconnu | 32 | Effet de la clonidine administrée la nuit (amélioration du sommeil) sur l'agressivité diurne d'enfants atteints du syndrome de Gilles de la Tourette avec TDAH associé |
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Phase 4 | Terminé | 12 | Comparaison du lévétiracétam et de la clonidine sur les tics de l'enfant (essai croisé en double aveugle) ; effectif très faible |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Méta-analyse en réseau | Lancet Child Adolesc Health | Comparaison de l'efficacité, de la tolérance et de l'acceptabilité des traitements pharmacologiques chez l'enfant et le jeune adulte |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Recommandations | Eur Child Adolesc Psychiatry | Recommandations européennes (partie III) sur le traitement pharmacologique des tics |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Étude clinique | Psychiatry Investigation | Efficacité et sécurité du patch de clonidine dans le syndrome de Gilles de la Tourette avec TDAH |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Revue systématique | Neurology | Traitement des tics dans le syndrome de Gilles de la Tourette et les tics chroniques |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Revue systématique | J Psychopharmacol | Qualité des preuves des traitements pharmacologiques chez l'enfant et l'adulte |
| [27132945](https://pubmed.ncbi.nlm.nih.gov/27132945/) | 2016 | Revue systématique | J Child Psychol Psychiatry | Traitements du syndrome chez l'enfant et le jeune |
| [23473832](https://pubmed.ncbi.nlm.nih.gov/23473832/) | 2013 | Revue | Eur J Paediatr Neurol | Options pharmacologiques en cas de TDAH associé |
| [89558](https://pubmed.ncbi.nlm.nih.gov/89558/) | 1979 | Rapport clinique précoce | Lancet | De faibles doses de clonidine améliorent l'état de certains enfants non répondeurs à l'halopéridol |
| [6109915](https://pubmed.ncbi.nlm.nih.gov/6109915/) | 1981 | Étude clinique | Lancet | Clonidine dans le syndrome de Gilles de la Tourette |
| [1414629](https://pubmed.ncbi.nlm.nih.gov/1414629/) | 1992 | Étude clinique | Adv Neurol | Clonidine et clonazépam dans le syndrome de Gilles de la Tourette |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64256681 | CATAPRESSAN 0,15 mg/ml | Solution injectable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, ne provenant pas de la notice) : hypotension, infarctus du myocarde et ischémie myocardique, arrêt cardiaque soudain, maladies de la conduction cardiaque, insuffisance hépatique, pancréatite, diabète de type 1 et 2 (dont acidocétose diabétique), lupus érythémateux systémique, troubles anxieux et névrotiques, trouble dysthymique, insuffisance respiratoire, anurie, goutte, troubles de la coagulation, troubles du métabolisme calcique et phosphoré, carence en potassium, hémoglobinopathies, dermatite.
- **Interactions médicamenteuses** : 100 interactions recensées, toutes de niveau modéré parmi les 20 présentées. Principales classes concernées : corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), antidiabétiques (insulines, sulfamides hypoglycémiants, inhibiteurs du SGLT2 tels que canagliflozine, dapagliflozine, empagliflozine), ainsi que bupropion, morphine et dronabinol.
- **Effets indésirables attendus dans les populations pédiatriques et psychiatriques** (d'après les données de la littérature compilées) : sédation, hypotension, bradycardie.

Veuillez consulter la notice pour les mises en garde officielles, car les données issues de la notice de l'ANSM ne sont pas disponibles.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Les lignes directrices européennes et une méta-analyse en réseau soutiennent l'usage de la clonidine dans les tics, notamment avec TDAH associé, mais les deux essais de phase 4 sont petits et aucun essai de phase 3 n'est fourni ; le niveau de preuve est donc plafonné à L3.
- Le statut réglementaire français est défavorable : la seule AMM, celle d'une forme injectable, est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications officielles), actuellement manquante et bloquante pour l'évaluation de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Confirmer la disponibilité d'une formulation adaptée en France (voie orale ou transdermique), la seule AMM recensée étant une solution injectable annulée.
- Disposer d'au moins un essai randomisé de phase 3 de bonne qualité ou d'une méta-analyse centrée sur la clonidine.
- Établir un plan de surveillance (tension artérielle, fréquence cardiaque, sédation) et vérifier l'absence des contre-indications cardiovasculaires et métaboliques listées.

**Autres pistes prédites (à titre indicatif) :** l'obésité, la migraine et le trouble bipolaire maniaque (niveau L3, statut « question de recherche ») nécessitent des essais complémentaires ; le syndrome facio-digito-génital, le trouble spécifique du développement, le fibrome chondromyxoïde, la trichotillomanie, l'hypervitaminose et le syndrome de microdélétion 16p11.2 restent en « Hold » faute de preuves ou de lien mécanistique identifié.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

