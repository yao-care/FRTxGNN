---
layout: default
title: Prucalopride
parent: Prédiction du modèle uniquement (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride : De la Constipation Chronique à l'Hypoalphalipoprotéinémie

## Résumé en Une Phrase

Prucalopride est un agoniste sélectif du récepteur 5-HT4 (prokinétique), utilisé à l'origine pour traiter la constipation chronique chez l'adulte lorsque les laxatifs sont inefficaces.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypoalphalipoprotéinémie** (HDL bas).
Cette prédiction repose sur le seul score du modèle : **0 essai clinique** et **0 publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Constipation chronique (source : données de pharmacologie ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypoalphalipoprotéinémie |
| Score de Prédiction TxGNN | 99,82 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les données de pharmacologie, la prucalopride cible le récepteur 5-HT4 (gène HTR4). Cet agonisme stimule la motilité gastro-intestinale, ce qui explique son efficacité dans la constipation chronique.

La relation entre l'indication d'origine et la nouvelle indication est très faible. Aucun rôle connu du récepteur 5-HT4 dans le métabolisme des lipoprotéines de haute densité (HDL) n'a été identifié. La prédiction ne repose donc que sur des associations dans le graphe de connaissances du modèle.

Il faut donc interpréter ce score élevé avec prudence. En l'état, il ne s'appuie sur aucun lien mécanistique plausible, aucun essai clinique ni aucune publication. Il constitue une hypothèse de travail, pas une piste thérapeutique étayée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69471136 | RESOLOR 1 mg | Comprimé pelliculé | Non renseignée dans les données |
| 63947653 | RESOLOR 2 mg | Comprimé pelliculé | Non renseignée dans les données |

Les deux présentations sont exploitées par Takeda Pharmaceuticals International (Irlande).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 : score du modèle uniquement, sans essai, sans publication et sans lien mécanistique plausible entre l'agonisme 5-HT4 et le métabolisme des HDL.
- Les données de sécurité de l'ANSM manquent, ce qui empêche de passer à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) et l'indication approuvée de chaque AMM.
- Compléter le mécanisme d'action via DrugBank.
- Établir une hypothèse biologique reliant le récepteur 5-HT4 au métabolisme des HDL, ou prioriser une autre indication candidate.

**Note sur les autres candidats :** parmi les dix indications prédites, seules l'amylose (rang 6) et l'amylose primaire (rang 9) disposent de publications (niveau L4). Il s'agit d'un rapport de cas et d'une étude de cohorte sur les troubles de la motilité, notamment la pseudo-obstruction intestinale chronique. Ces travaux ne montrent pas d'efficacité de la prucalopride. Un rôle purement symptomatique sur la dysmotilité liée à l'amylose reste une simple question de recherche.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

