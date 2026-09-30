---
layout: default
title: Lipegfilgrastim
parent: Prédiction du modèle uniquement (L5)
nav_order: 173
evidence_level: L5
indication_count: 5
---

# Lipegfilgrastim
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

# Lipegfilgrastim : Du G-CSF pégylé (stimulation des neutrophiles) au Trouble primaire de la libération plaquettaire

## Résumé en Une Phrase

Lipegfilgrastim est un analogue pégylé du G-CSF, qui stimule la prolifération et la différenciation de la lignée des neutrophiles. Il est commercialisé en France sous le nom LONQUEX.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble primaire de la libération plaquettaire**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM fournies |
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, le lipegfilgrastim est un analogue pégylé du G-CSF qui agit sur la lignée myéloïde (neutrophiles). Rien dans le dossier ne permet de recouper cette description avec une source de référence.

**Cette prédiction est faible sur le plan biologique.** Les troubles de la libération plaquettaire sont des défauts qualitatifs de la fonction des plaquettes. La signalisation du G-CSF n'a aucun mécanisme établi pour les corriger. Le score élevé (99,93 %) reflète très probablement une proximité dans le graphe de connaissances entre nœuds de maladies hématologiques, plutôt qu'une justification biologique. Aucune similarité avec l'indication d'origine n'a pu être évaluée.

Les autres prédictions du modèle vont dans le même sens : Glanzmann (thrombasthénie), pseudo-maladie de von Willebrand, rétinopathie diabétique et rétinopathie diabétique non proliférante sévère. Les trois premières sont des défauts de fonction plaquettaire sans pont mécanistique identifié. Pour la rétinopathie diabétique, l'hypothèse est indirecte : la mobilisation de progéniteurs par le G-CSF pourrait influencer la réparation microvasculaire, mais aussi favoriser une néovascularisation pathologique. Le sens de l'effet est donc incertain.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66910592 | LONQUEX 6 mg/0,6 mL, solution injectable | Solution injectable | Non renseignée |
| 64198267 | LONQUEX 6 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée |

Titulaire : TEVA (Pays-Bas). Voie : injectable uniquement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est élevé, mais il n'existe aucun essai, aucune publication ni mécanisme plausible reliant le G-CSF pégylé aux troubles de la fonction plaquettaire (niveau L5).
- Les données de sécurité et le mécanisme d'action d'origine manquent, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) : lacune bloquante pour le criblage de sécurité.
- Obtenir le mécanisme d'action détaillé via DrugBank (DB13200).
- Pour la rétinopathie diabétique (pistes classées « Research Question ») : validation préclinique, avec évaluation du risque de néovascularisation oculaire avant toute considération clinique.
- Pour les trois troubles plaquettaires : rechercher activement toute littérature ou tout essai avant de reconsidérer la piste. En l'absence de preuves, la piste ne doit pas être poursuivie.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

