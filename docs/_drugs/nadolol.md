---
layout: default
title: Nadolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 521
evidence_level: L5
indication_count: 5
---

# Nadolol
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

# Nadolol : De l'Hypertension à l'Hypertension Rénovasculaire Maligne

## Résumé en Une Phrase

Le nadolol est un bêta-bloquant non sélectif, initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**,
mais **aucun essai clinique** et **aucune publication** spécifique ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (le texte d'indication de l'AMM française n'est pas renseigné ; l'indication provient du graphe de connaissances) |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99,59 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le nadolol est un bêta-bloquant non sélectif dont l'efficacité dans l'hypertension est établie. Le blocage bêta-adrénergique réduit la libération de rénine par les cellules juxtaglomérulaires.

Cet effet est plausiblement pertinent dans l'hypertension rénovasculaire, où l'activation du système rénine-angiotensine entretient l'élévation de la pression artérielle. Le score très élevé du modèle reflète probablement surtout la proximité sémantique avec l'indication déjà connue (hypertension), plutôt qu'une preuve réelle.

Il faut aussi noter que la forme maligne (accélérée) est une urgence, généralement prise en charge par des médicaments intraveineux et la revascularisation. Un bêta-bloquant oral comme le nadolol ne serait donc pas un traitement de première intention.

**Autres prédictions du modèle (toutes de niveau L5, sans essai clinique) :**
- Néphropathie hypertensive maligne (score 99,59 %) : l'effet antihypertenseur pourrait théoriquement limiter l'atteinte rénale, mais le nadolol est éliminé par voie rénale et nécessiterait un ajustement posologique.
- Hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie, et hypertension pulmonaire d'origine multifactorielle (score 99,53 %) : les bêta-bloquants sont en général évités dans ces situations (baisse du débit cardiaque, risque de bronchospasme). Les 12 publications retrouvées pour la première sont précliniques ou périphériques ; aucune n'étudie le nadolol dans cette indication.
- Syndrome de Braddock (score 99,43 %) : aucun lien mécanistique évident ; à ne pas exploiter sans validation indépendante.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature directement associée à l'hypertension rénovasculaire maligne n'est disponible actuellement. Pour l'hypertension pulmonaire (prédiction de rang 3), les publications retrouvées sont indirectes ; les plus pertinentes sont listées ci-dessous.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6488695](https://pubmed.ncbi.nlm.nih.gov/6488695/) | 1984 | Étude animale | Clin Physiol Biochem | Le propranolol (et, de façon similaire, le nadolol) diminue la pression artérielle pulmonaire chez le chien conscient |
| [25350545](https://pubmed.ncbi.nlm.nih.gov/25350545/) | 2014 | Étude animale | PLoS One | Rôle du récepteur β2-adrénergique dans l'atténuation de la vasoconstriction pulmonaire hypoxique chez le rat |
| [2566504](https://pubmed.ncbi.nlm.nih.gov/2566504/) | 1989 | Préclinique | Eur J Pharmacol | Propriétés annexes des bêta-bloquants dans la protection du cœur de cobaye contre l'anoxie |
| [24795691](https://pubmed.ncbi.nlm.nih.gov/24795691/) | 2014 | Préclinique | Front Neurol | Les bêta1-bloquants réduisent la libération de noradrénaline chez le rat |
| [39252618](https://pubmed.ncbi.nlm.nih.gov/39252618/) | 2025 | Étude animale | CNS Neurol Disord Drug Targets | Le nadolol atténue la ferroptose dans un modèle d'AVC ischémique chez le rat (hors sujet) |
| [8729060](https://pubmed.ncbi.nlm.nih.gov/8729060/) | 1996 | Préclinique | J Mol Cell Cardiol | Raccourcissement du potentiel d'action en hypoxie, avec nadolol dans le protocole expérimental |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62092895 | CORGARD 80 mg, comprimé sécable (CHEPLAPHARM FRANCE) | Comprimé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de notice) : atteintes cardiorespiratoires (bloc atrioventriculaire, emphysème pulmonaire, maladie bronchique), myasthénie grave et maladies de la jonction neuromusculaire, diabète et acidocétose diabétique, maladies rénales et anurie, maladies hépatiques (dont encéphalopathie et coma hépatiques), pancréatite, maladie de la vésicule biliaire, lupus érythémateux systémique, goutte et hyperuricémie, troubles du métabolisme du calcium et du phosphore (hypercalcémie, hyperparathyroïdie, néphrocalcinose), carence en potassium, ainsi que troubles anxieux et dysthymiques.
- **Interactions médicamenteuses** : 100 interactions recensées. La principale de niveau majeur est l'**épinéphrine**. Parmi les interactions modérées figurent les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), les anticholinergiques (atropine, hyoscyamine, méthscopolamine), le bupropion, la morphine, la cimétidine, les sels de calcium, le canagliflozine, la dapagliflozine et le chlorpropamide. Interactions mineures : acide acétylsalicylique, clarithromycine, oxyde de magnésium.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Toutes les prédictions reposent uniquement sur le modèle (niveau L5), sans essai clinique ni publication clinique. Les scores élevés reflètent surtout la proximité avec l'indication hypertension. Les prédictions d'hypertension pulmonaire soulèvent en outre une préoccupation de sécurité, et la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études cliniques ou observationnelles du nadolol dans l'hypertension rénovasculaire ou la néphropathie hypertensive
- Évaluation de la compatibilité des voies d'administration et de la faisabilité en urgence hypertensive
- Évaluation de la sécurité en insuffisance rénale (élimination rénale) et en maladie respiratoire
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

