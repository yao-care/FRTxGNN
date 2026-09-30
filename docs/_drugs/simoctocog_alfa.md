---
layout: default
title: Simoctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog alfa : De l'Hémophilie A (présumée) à la Pseudo-maladie de von Willebrand

## Résumé en Une Phrase

Simoctocog alfa est un facteur VIII de coagulation humain recombinant, commercialisé en France sous le nom NUWIQ. Son indication d'origine n'est pas renseignée dans les données réglementaires disponibles, mais il est présumé destiné au traitement de l'hémophilie A.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pseudo-maladie de von Willebrand**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie A (présumée ; texte d'indication non renseigné dans les AMM) |
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand (pseudo-von Willebrand disease) |
| Score de Prédiction TxGNN | 99,997 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 8 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, simoctocog alfa est un facteur VIII recombinant humain qui remplace le FVIII manquant dans l'hémophilie A. Ce mécanisme est bien établi pour cette maladie, mais son application à la nouvelle indication reste hypothétique.

La pseudo-maladie de von Willebrand (forme de type plaquettaire) est due à un gain de fonction de la GPIb-alpha, qui augmente la fixation des plaquettes au facteur de von Willebrand (VWF). Un apport de FVIII ne corrige pas ce défaut du récepteur plaquettaire. De plus, le produit ne contient pas de VWF, ce qui affaiblit encore le lien mécanistique.

Le score TxGNN très élevé provient d'une prédiction fondée sur le graphe de connaissances, sans donnée clinique ou bibliographique à l'appui. Il ne doit pas être interprété comme un signal d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Le texte de l'indication approuvée n'est pas renseigné pour ces AMM. Sur 8 AMM au total, 5 sont détaillées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 66102792 | NUWIQ 1000 UI | Poudre et solvant pour solution injectable | Octapharma (Suède) |
| 69144152 | NUWIQ 4000 UI | Poudre et solvant pour solution injectable | Octapharma (Suède) |
| 63023286 | NUWIQ 250 UI | Poudre et solvant pour solution injectable | Octapharma (Suède) |
| 63383804 | NUWIQ 1500 UI | Poudre et solvant pour solution injectable | Octapharma (Suède) |
| 67351693 | NUWIQ 500 UI | Poudre et solvant pour solution injectable | Octapharma (Suède) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les bases interrogées. Une prédiction concerne toutefois un risque théorique : dans le purpura thrombotique thrombocytopénique (rang 10), un apport de FVIII pourrait ajouter un risque prothrombotique. Ce n'est pas un signal de bénéfice, et cette prédiction ne doit pas être retenue.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai, aucune publication, et un lien mécanistique faible, car le défaut porte sur la fonction plaquettaire et non sur le FVIII.
- Les 10 candidats prédits sont tous au niveau L5 avec la recommandation Hold. Le plus plausible est l'**hémophilie A avec anomalie vasculaire** (rang 9), proche de l'indication native ; il mérite une revue manuelle, mais aucune preuve spécifique n'est fournie pour cette entité. Les autres candidats sont plaquettaires ou immunologiques, sans rationnel mécanistique net.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications). Cette lacune bloque le passage à l'évaluation de sécurité.
- Obtenir le texte de l'indication approuvée pour les AMM NUWIQ.
- Obtenir les données de mécanisme d'action via DrugBank.
- Effectuer une recherche bibliographique et d'essais ciblée sur la pseudo-maladie de von Willebrand et sur l'hémophilie A avec anomalie vasculaire.
- Faire une revue d'expert de la candidature au rang 9 avant toute décision de poursuite.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

