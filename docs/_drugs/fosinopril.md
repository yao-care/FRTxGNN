---
layout: default
title: Fosinopril
parent: Prédiction du modèle uniquement (L5)
nav_order: 349
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Fosinopril : nouvelle indication prédite, Maladie rénale hypertensive maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle"
monitor_inn: "fosinopril"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Fosinopril
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Fosinopril : De l'Hypertension à l'Hypertension Rénale Maligne

## Résumé en Une Phrase

Le fosinopril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC), initialement utilisé pour traiter l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie rénale hypertensive maligne**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne |
| Score de Prédiction TxGNN | 99,87 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 10 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le fosinopril fait partie de la classe des IEC. Son efficacité dans l'hypertension est établie, et le système rénine-angiotensine est un acteur central de l'hypertension maligne et de l'atteinte rénale associée (lésions vasculaires, néphrosclérose).

Le lien biologique est plausible et très proche de l'indication d'origine. Toutefois, la maladie rénale hypertensive maligne recoupe largement l'hypertension déjà traitée : il s'agit probablement d'un sous-type de l'usage existant plutôt que d'une véritable opportunité de repositionnement.

Les autres prédictions du modèle sont plus fragiles :
- **Hypertension rénovasculaire maligne** (99,87 %) : plausible sur le plan mécanistique, mais à manier avec prudence en cas de sténose bilatérale des artères rénales, où les IEC peuvent provoquer une insuffisance rénale aiguë.
- **Hypertension pulmonaire** (formes multifactorielle et liée à une maladie pulmonaire/hypoxie, 99,87 %) : rationnel hypothétique seulement, les IEC n'étant pas un traitement établi de cette maladie.
- **Syndrome de Braddock** (99,81 %) : aucun lien mécanistique identifiable.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature soutenant l'indication principale (maladie rénale hypertensive maligne) n'est disponible actuellement.

À titre indicatif, deux publications ont été retrouvées pour une indication prédite secondaire (hypertension pulmonaire liée à une maladie pulmonaire/hypoxie). Aucune ne soutient l'efficacité :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) | 1998 | Rapport de cas (événement indésirable) | Rev Mal Respir | Pneumonie éosinophilique hypoxique chez deux patients traités par énalapril et fosinopril : signal de sécurité, non thérapeutique |
| [31105790](https://pubmed.ncbi.nlm.nih.gov/31105790/) | 2019 | Préclinique (analyse bioinformatique) | Exp Ther Med | Gènes candidats dans des cellules mésangiales de souris (néphropathie diabétique) : sans rapport direct avec l'hypertension pulmonaire |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60095526 | Fosinopril Zentiva 10 mg | Comprimé sécable | Non renseignée (AMM annulée) |
| 62518708 | Fosinopril Biogaran 10 mg | Comprimé sécable | Non renseignée (AMM annulée) |
| 61520873 | Fosinopril Arrow Lab 10 mg | Comprimé sécable | Non renseignée (AMM annulée) |
| 61248124 | Fosinopril Biogaran 20 mg | Comprimé | Non renseignée (AMM annulée) |
| 60736761 | Fosinopril Arrow Lab 20 mg | Comprimé | Non renseignée (AMM annulée) |

Au total, 10 AMM figurent dans la base, toutes annulées (dont 3 associations avec l'hydrochlorothiazide 20 mg/12,5 mg).

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : angiœdème (acquis, héréditaire, induit par les bloqueurs du système rénine-angiotensine), insuffisance rénale, maladie hépatique et encéphalopathie hépatique, pancréatite, maladie de la vésicule biliaire, sténose aortique, hypotension, lupus érythémateux systémique et maladies du tissu conjonctif, diabète et acidocétose diabétique, déficit en potassium, neutropénie et agranulocytose, hyperparathyroïdie, maladies osseuses.
- **Interactions médicamenteuses** : 183 interactions recensées. Les plus notables sont de niveau **majeur** avec le bicarbonate de potassium et le citrate de potassium (risque d'hyperkaliémie). Des interactions de niveau modéré concernent notamment les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), l'aspirine, la metformine, les inhibiteurs de SGLT2 (canagliflozine, dapagliflozine, empagliflozine), les gliptines (alogliptine, saxagliptine), le chlorpropamide, le bupropion, la morphine et le dronabinol.
- **Signal pulmonaire** : un rapport de cas décrit une pneumonie éosinophilique hypoxique sous IEC, dont le fosinopril.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être consultées ; veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication pour l'indication proposée, et elle recoupe largement l'hypertension déjà couverte. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une recherche ciblée d'essais cliniques et de littérature sur l'atteinte rénale de l'hypertension maligne
- Une clarification : cette indication est-elle un véritable repositionnement ou un sous-type de l'hypertension déjà traitée ?
- Une évaluation de la faisabilité réglementaire, compte tenu de l'annulation de toutes les AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

