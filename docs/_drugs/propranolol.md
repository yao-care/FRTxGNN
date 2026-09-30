---
layout: default
title: Propranolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 252
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Propranolol : D'un Bêtabloquant Commercialisé à la Myopathie Distale de type Tateyama

## Résumé en Une Phrase

Le propranolol est un bêtabloquant commercialisé en France. Les données d'AMM fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **myopathie distale de type Tateyama** (maladie musculaire rare), mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : c'est une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Myopathie distale de type Tateyama |
| Score de Prédiction TxGNN | 99,40 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le propranolol fait partie de la classe des bêtabloquants non sélectifs (blocage des récepteurs bêta-adrénergiques, qui réduit la fréquence cardiaque et la contractilité).

Aucun lien mécanistique entre le blocage bêta-adrénergique et cette myopathie distale rare n'est étayé par les données fournies. Le score élevé (99,40 %, rang 4269) provient uniquement du graphe de connaissances de TxGNN. Il ne constitue pas une preuve d'efficacité.

Cette prédiction doit donc être considérée comme une piste exploratoire et non comme une hypothèse thérapeutique argumentée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 65667550 | PROPRANOLOL TEVA L P 80 mg, gélule à libération prolongée | Gélule à libération prolongée | TEVA SANTE |
| 66415335 | PROPRANOLOL EG 40 mg, comprimé | Comprimé | EG LABO - LABORATOIRES EUROGENERICS |
| 63077978 | PROPRANOLOL TEVA L P 160 mg, gélule à libération prolongée | Gélule à libération prolongée | TEVA SANTE |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5, stade S0) : aucun essai, aucune publication et aucun mécanisme plausible ne la soutiennent. Les données de sécurité de la notice sont également absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), ce qui est bloquant
- Obtenir les données de mécanisme d'action (par exemple via l'API DrugBank)
- Renseigner l'indication d'origine à partir des textes d'AMM, actuellement vides
- Rechercher toute donnée préclinique ou clinique reliant le propranolol à cette myopathie ; à défaut, ne pas poursuivre cette piste

**Autres pistes prédites pour ce médicament, à évaluer séparément :**
- **Cardiomyopathie** (score 99,12 %, niveau L3) : 3 essais de phase 3 ou 4 et 20 publications, surtout de petites études hémodynamiques, des cas cliniques et des revues. Aucun essai ne teste l'efficacité du propranolol dans cette indication, et des données par sous-type (CMH, CMD, IC à fraction d'éjection préservée, amylose) sont nécessaires.
- **Cardiomyopathie cirrhotique** (score 99,12 %, niveau L3) : 5 publications aux résultats contrastés. Un rapport de 2024 suggère une correction de l'allongement du QT, tandis que d'autres décrivent une altération de la fonction circulatoire et rénale sous bêtabloquants non sélectifs dans la maladie avancée. Le bénéfice dépend donc du stade.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

