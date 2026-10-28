---
layout: default
title: Irbesartan
parent: Prédiction du modèle uniquement (L5)
nav_order: 412
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Irbesartan : nouvelle indication prédite, Malignant hypertensive renal disease (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Irbesartan
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Irbesartan: Malignant hypertensive renal disease
{: .text-alpha }

## Résumé en Une Phrase

L'irbésartan est un antagoniste des récepteurs de l'angiotensine II (type 1), initialement utilisé pour traiter l'hypertension artérielle et la néphropathie diabétique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette indication précise : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Malignant hypertensive renal disease |
| Score de Prédiction TxGNN | 0.9931 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, l'irbésartan est un antagoniste du récepteur AT1 de l'angiotensine II. Son efficacité dans l'hypertension et la néphropathie diabétique est établie.

L'hypertension rénovasculaire est en grande partie liée à l'activation du système rénine-angiotensine. Le blocage du récepteur AT1 est donc biologiquement plausible. Cependant, les ARA II sont généralement contre-indiqués ou à utiliser avec grande prudence en cas de sténose bilatérale des artères rénales, en raison du risque d'insuffisance rénale aiguë.

**Autres indications prédites (également de niveau L5, sans essai) :**
- Maladie rénale hypertensive maligne (score 0,9931) : très proche des indications existantes ; elle relèverait plutôt d'une extension d'indication que d'un véritable repositionnement.
- Hypertension pulmonaire d'origine multifactorielle incertaine (score 0,9925) : rationnel théorique issu de modèles précliniques, mais les ARA II ne sont pas un traitement établi.
- Hypertension pulmonaire liée à une maladie pulmonaire et/ou à l'hypoxie (score 0,9925) : 11 publications récupérées, uniquement précliniques ou hors sujet (niveau L4, voir ci-dessous).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'indication principale (hypertension rénovasculaire maligne).

À titre indicatif, pour l'indication de rang 4 (hypertension pulmonaire liée à l'hypoxie), les publications pertinentes sont les suivantes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Non classé (modèle animal) | Eur Rev Med Pharmacol Sci | L'irbésartan améliore le stress oxydatif dans l'hypertension pulmonaire d'altitude chez le rat, via la flore intestinale |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Préclinique | Biomed Pharmacother | Amélioration des lésions de l'artère pulmonaire dans un modèle de mal chronique des montagnes, via le métabolisme du cholestérol |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Préclinique | Sleep Breath | Atténuation de l'apoptose cardiaque induite par l'apnée du sommeil |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Préclinique | PLoS One | Protection des cardiomyocytes sous stress hypoxique |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Préclinique | Am J Physiol Heart Circ Physiol | Inhibition de l'angiogenèse coronaire stimulée par l'hypoxie intermittente chez le rat nouveau-né |
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Revue | Inflammopharmacology | Effets pléiotropes des antagonistes AT1 dans l'hypoxie induite par l'ischémie cardiaque |

Ces travaux concernent l'hypoxie cardiaque ou systémique chez l'animal, et non l'hypertension pulmonaire chez le patient. Plusieurs autres publications récupérées sont hors sujet.

## Informations de Marché en France

Principales AMM (5 sur 20) :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67229700 | IRBESARTAN EVOLUGEN 150 mg | comprimé pelliculé | Non disponible (active) |
| 64933635 | APROVEL 75 mg | comprimé pelliculé | Non disponible (active) |
| 66542998 | IFIRMASTA 75 mg | comprimé pelliculé | Non disponible (active) |
| 69985835 | IRBESARTAN CRISTERS 75 mg | comprimé pelliculé | Non disponible (active) |
| 61200414 | IRBESARTAN ARROW 75 mg | comprimé | Non disponible (active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : angio-œdème (dont héréditaire et induit par les bloqueurs du SRAA), pancréatite, lupus érythémateux systémique, myopathie et rhabdomyolyse, diabète et acidocétose diabétique, hypotension, anurie, sténose/obstruction de l'artère rénale, encéphalopathie hépatique, hyperparathyroïdie, hypercalcémie, goutte et hyperuricémie, carence en potassium, ictère néonatal, néphrocalcinose.
- **Interactions médicamenteuses** : 216 interactions recensées. Interactions **majeures** : citrate de potassium et bicarbonate de potassium (risque d'hyperkaliémie). Interactions modérées notamment avec les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), l'acide acétylsalicylique, la morphine, le bupropion, l'aprépitant, les inhibiteurs de SGLT2 (canagliflozine, dapagliflozine, empagliflozine) et des insulines.

La notice (mises en garde et contre-indications officielles) n'a pas pu être analysée ; veuillez la consulter pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. De plus, la contre-indication connue en cas de sténose des artères rénales va directement à l'encontre de l'indication proposée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde et contre-indications), bloquante pour le dépistage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Revue systématique de la littérature clinique sur les ARA II dans l'hypertension rénovasculaire, avec évaluation du risque rénal
- Pour l'hypertension pulmonaire liée à l'hypoxie : validation préclinique spécifique avant toute étude clinique (question de recherche, niveau L4)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

