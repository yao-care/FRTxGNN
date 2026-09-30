---
layout: default
title: Vonicog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
---

# Vonicog Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Vonicog alfa : De la maladie de von Willebrand au trouble de la libération plaquettaire primaire

## Résumé en Une Phrase

Vonicog alfa est un facteur de von Willebrand recombinant (rVWF), commercialisé en France sous le nom Veyvondi. D'après les essais et publications fournis, il traite à l'origine la maladie de von Willebrand. Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la libération plaquettaire primaire**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction, et le lien mécanistique est jugé faible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de von Willebrand (déduite des essais et publications ; le texte d'indication de l'AMM n'est pas renseigné dans les données fournies) |
| Nouvelle Indication Prédite | Trouble de la libération plaquettaire primaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, vonicog alfa remplace le facteur de von Willebrand (VWF), qui soutient l'adhésion des plaquettes aux lésions vasculaires. Son efficacité dans la maladie de von Willebrand est documentée par plusieurs études de phase 3.

Le lien avec la nouvelle indication est toutefois **fragile**. Les troubles de la libération plaquettaire résultent d'un défaut intrinsèque de sécrétion des granules plaquettaires. Un apport de VWF exogène ne devrait pas corriger ce défaut. Le score TxGNN très élevé reflète donc probablement une proximité dans le graphe de connaissances (troubles hémorragiques et plaquettaires) plutôt qu'un véritable lien thérapeutique.

Cette prédiction doit donc être considérée comme une simple hypothèse issue du modèle, sans support mécanistique ni clinique à ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65346733 | VEYVONDI 650 UI | Poudre et solvant pour solution injectable | Non renseignée dans les données fournies |
| 69749137 | VEYVONDI 1 300 UI | Poudre et solvant pour solution injectable | Non renseignée dans les données fournies |

Les deux AMM sont détenues par Baxalta Innovations (Autriche).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai ni publication ne concerne le trouble de la libération plaquettaire primaire, et le mécanisme du médicament ne corrige pas le défaut intrinsèque des plaquettes.
- Parmi les autres pistes prédites, seule l'hémophilie (rang 4) dispose d'essais de phase 3. Ceux-ci semblent porter sur la maladie de von Willebrand, l'indication approuvée, et non sur l'hémophilie. Cette piste reste une simple question de recherche (niveau L4).

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM, dont l'absence bloque le passage au criblage de sécurité S1.
- Les données détaillées sur le mécanisme d'action (MOA), à obtenir via DrugBank.
- Le texte d'indication de l'AMM, pour confirmer l'indication originale.
- Une revue de la littérature ciblée sur les troubles plaquettaires de sécrétion, pour rechercher tout signal clinique ou préclinique.
- La vérification, dans les registres, de la pathologie réellement étudiée dans les essais listés pour l'hémophilie, dont les titres sont tronqués.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

