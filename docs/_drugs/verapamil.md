---
layout: default
title: Verapamil
parent: Prédiction du modèle uniquement (L5)
nav_order: 809
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Verapamil : nouvelle indication prédite, Bloc de branche (terme obsolète) (niveau de preuve L5). Indication d'origine : Hypertension, fibrillation auriculaire, syndrome coronarien aigu…"
monitor_inn: "verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
---

# Verapamil
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

## Vérapamil : Des troubles cardiovasculaires à l'Hypertension rénale maligne (prédiction principale : bloc de branche obsolète)
{: .text-alpha }

> Remarque : la prédiction au rang 1 (« obsolete bundle branch block ») correspond à un terme d'ontologie obsolète et est mécanistiquement douteuse. Le rapport suit néanmoins la prédiction de rang 1 telle que fournie dans les données compilées.

## Résumé en Une Phrase

Le vérapamil est un inhibiteur calcique de type L, initialement utilisé pour l'hypertension, la fibrillation auriculaire, le syndrome coronarien aigu, l'angor de Prinzmetal et la tachycardie ventriculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **bloc de branche (terme obsolète)**, mais **aucun essai clinique et aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction de modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension, fibrillation auriculaire, syndrome coronarien aigu, angor de Prinzmetal, tachycardie ventriculaire (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Bloc de branche (terme obsolète) |
| Score de Prédiction TxGNN | 99,62 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulé (aucune AMM valide) |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, le vérapamil est un inhibiteur calcique qui ralentit la conduction du nœud auriculo-ventriculaire (AV) et réduit la résistance vasculaire. Son efficacité dans les arythmies supraventriculaires et l'hypertension est établie.

Pour le bloc de branche, le lien est faible. Il s'agit d'un trouble de conduction du système de His-Purkinje, pour lequel le blocage du nœud AV n'offre aucun bénéfice thérapeutique clair et pourrait aggraver la conduction. De plus, le terme « obsolete » indique probablement une entrée d'ontologie dépréciée. La prédiction est donc mécanistiquement douteuse.

Parmi les autres prédictions, la plus plausible est l'**hypertension rénale maligne** (rang 2, score 99,27 %) et l'**hypertension rénovasculaire maligne** (rang 3) : elles prolongent l'usage antihypertenseur connu, mais sans preuve directe. Les prédictions suivantes (hypertension pulmonaire, syndrome de Braddock, paralysie périodique) sont spéculatives ; pour l'hypertension pulmonaire, l'effet inotrope négatif du vérapamil constitue en outre une préoccupation de sécurité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'indication de rang 1.

Pour information, les publications retrouvées pour les indications de rang inférieur ne fournissent pas non plus de preuve clinique d'efficacité du vérapamil. Pour l'hypertension rénovasculaire maligne (rang 3), il s'agit d'une revue sur le rapport aldostérone/rénine (2012) et d'un rapport de cas pédiatrique (1999), sans lien avec le vérapamil. Pour l'hypertension pulmonaire hypoxique (rang 4), la littérature est essentiellement hors sujet ou préclinique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69181930 | VERAPAMIL EG L.P. 240 mg | Comprimé pelliculé sécable à libération prolongée | Non renseignée (AMM annulée) |
| 69865024 | ISOPTINE 40 mg | Comprimé enrobé | Non renseignée (AMM annulée) |
| 63803877 | ISOPTINE L.P. 240 mg | Comprimé pelliculé sécable à libération prolongée | Non renseignée (AMM annulée) |
| 60614889 | ISOPTINE 5 mg/2 ml | Solution injectable | Non renseignée (AMM annulée) |
| 66814925 | ISOPTINE 120 mg | Gélule | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance cardiaque, bloc auriculo-ventriculaire, sténose aortique, cardiomyopathie hypertrophique, trouble hypotensif, tachycardie ventriculaire, myasthénie grave, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, angio-œdème (dont héréditaire), neutropénie et agranulocytose, sténose de l'artère rénale, entre autres.
- **Interactions médicamenteuses** : 328 interactions recensées. Parmi celles affichées, la plus sévère est avec le **lopéramide (majeure)**. Les interactions modérées concernent notamment la cimétidine, la clarithromycine, la metformine, le bupropion, l'aprépitant, l'acide acétylsalicylique, les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), la canagliflozine et plusieurs sels de calcium. L'interaction avec la morphine est mineure.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Le mécanisme est douteux (le bloc de branche est un trouble de conduction infranodal, et le terme est obsolète). Le vérapamil n'a par ailleurs plus d'AMM valide en France (5 AMM annulées).

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérifier la validité du terme d'ontologie et envisager de privilégier les prédictions plus plausibles (hypertension maligne avec atteinte rénale)
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Récupérer les mises en garde et contre-indications de la notice (site de l'ANSM), étape bloquante pour le dépistage de sécurité
- Rechercher des études cliniques ou observationnelles spécifiques au vérapamil dans l'indication retenue
- Clarifier le statut réglementaire, toutes les AMM étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

