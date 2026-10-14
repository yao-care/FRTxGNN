---
layout: default
title: Denosumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 224
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Denosumab : De l'ostéoporose à la rétinopathie diabétique sévère non proliférante

## Résumé en Une Phrase

Denosumab est un anticorps monoclonal initialement utilisé pour le traitement de l'ostéoporose (y compris l'ostéoporose post-ménopausique et l'ostéoporose d'origine médicamenteuse).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **rétinopathie diabétique non proliférante sévère**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Ostéoporose (ostéoporose post-ménopausique, ostéoporose médicamenteuse) d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 13 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des connaissances générales, denosumab est un inhibiteur de RANKL (ligand du récepteur activateur du facteur nucléaire kappa-B), qui freine la résorption osseuse en bloquant la voie RANKL/RANK/OPG. C'est ce mécanisme qui sous-tend son usage dans l'ostéoporose.

La relation avec la rétinopathie diabétique est hypothétique. La voie RANKL/RANK/OPG a été associée à l'inflammation et à la calcification vasculaire, ce qui pourrait se rattacher à la pathologie inflammatoire et microvasculaire de la rétinopathie diabétique. On ignore toutefois si un blocage de RANKL, par voie systémique ou intravitréenne, agit sur la maladie microvasculaire rétinienne : ce raisonnement repose sur des connaissances générales et non sur les données compilées pour ce rapport.

La seconde prédiction, la **rétinopathie diabétique** (score de 99,23 %), est une catégorie parente de la première. Les deux prédictions ne constituent donc pas des preuves indépendantes, et un score élevé ne doit pas être interprété comme un soutien clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 13 AMM recensées sont toutes annulées ; aucune n'est valide actuellement. Le texte de l'indication approuvée n'est pas renseigné. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69058988 | JUBEREQ 120 mg, solution injectable | Solution injectable | Non renseignée |
| 63575523 | OSENVELT 120 mg, solution injectable | Solution injectable | Non renseignée |
| 62960231 | OSVYRTI 60 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée |
| 69747403 | JUBBONTI 60 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée |
| 65243459 | XGEVA 120 mg, solution injectable | Solution injectable | Non renseignée |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 193 interactions sont recensées. Les principales, de niveau modéré (source : DDInter), concernent :
  - les corticoïdes : hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisolone, prednisone, méthylprednisolone ;
  - les immunosuppresseurs et agents apparentés : tacrolimus, mercaptopurine, dupilumab, lévamisole, triméthrexate ;
  - les radiopharmaceutiques et anticorps apparentés : ibritumomab tiuxétan, iobenguane (I-131), tositumomab (avec ou sans I-131) ;
  - les corticotrophines : corticotropine, tétracosactide.
- **Points d'attention généraux** (connaissances générales, non issus des données compilées) : hypocalcémie et fractures vertébrales multiples de rebond à l'arrêt du traitement systémique, à examiner avant tout repositionnement.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées, qui ne sont pas disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,63 %), mais il n'existe ni essai clinique ni publication à l'appui, et le niveau de preuve est L5. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes, ce qui bloque la suite de l'évaluation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) pour mener le dépistage de sécurité.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Réaliser une revue systématique de la littérature (modèles précliniques rétiniens, données observationnelles chez des patients diabétiques traités par denosumab).
- Clarifier la voie d'administration envisagée (systémique ou intravitréenne) et sa compatibilité avec les formes disponibles.
- Vérifier la situation réglementaire en France, puisqu'aucune AMM n'est valide.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

