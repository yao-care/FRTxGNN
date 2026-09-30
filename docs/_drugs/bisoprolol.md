---
layout: default
title: Bisoprolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 59
evidence_level: L5
indication_count: 5
---

# Bisoprolol
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

# Bisoprolol : Du Bêtabloquant Antihypertenseur à l'Hypertension Rénovasculaire Maligne

## Résumé en Une Phrase

Bisoprolol est un bêtabloquant bêta-1 sélectif, connu pour son effet antihypertenseur.
Le modèle TxGNN prédit qu'il pourrait être utile dans l'**hypertension rénovasculaire maligne**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM fournies |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99.94% |
| Niveau de Preuve | L5 (aucune étude réelle ; le pack d'évidence indique L4 sur la base d'un raisonnement pharmacologique indirect) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 12 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le bisoprolol est un bêtabloquant bêta-1 sélectif dont l'effet antihypertenseur est établi. Mécanistiquement, il pourrait être applicable à l'hypertension rénovasculaire.

Le lien proposé est indirect. Le blocage bêta réduit la libération de rénine, or l'activation du système rénine-angiotensine est centrale dans l'hypertension rénovasculaire. Il s'agit d'un raisonnement pharmacologique général, et non d'une preuve propre à cette maladie.

Il faut aussi rester prudent. L'hypertension maligne est une urgence hypertensive, habituellement prise en charge par voie parentérale. L'adéquation d'un bêtabloquant oral n'est donc pas établie. La similarité avec l'indication d'origine et la compatibilité des voies d'administration restent à évaluer.

Le modèle prédit aussi l'*atteinte rénale hypertensive maligne* avec un score identique (99.94%). Cela suggère que les deux entrées partagent un même voisinage dans le graphe et ne constituent pas deux signaux indépendants.

Trois autres prédictions sont classées Hold (niveau L5, sans essai clinique) :
- hypertension pulmonaire d'origine multifactorielle peu claire ;
- hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie ;
- syndrome de Braddock.

La littérature récupérée pour l'hypertension pulmonaire liée à l'hypoxie porte sur la biologie de l'hypoxie en général (cerveau, cancer, sclérose en plaques, altitude) et ne mentionne jamais le bisoprolol. Ce comptage est un artefact de recherche, et non un signal.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69455705 | BISOPROLOL BGR 7,5 mg (BIOGARAN) | Comprimé pelliculé sécable | Non renseignée dans la source |
| 65591063 | BISOPROLOL KRKA 5 mg (KRKA) | Comprimé pelliculé sécable | Non renseignée dans la source |
| 62969789 | BISOPROLOL TEVA 5 mg (TEVA SANTE) | Comprimé pelliculé | Non renseignée dans la source |
| 63162282 | CARDENSIEL 1,25 mg (MERCK SANTE) | Comprimé pelliculé | Non renseignée dans la source |
| 60524826 | BISOPROLOL TEVA 10 mg (TEVA SANTE) | Comprimé pelliculé | Non renseignée dans la source |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni publication ne soutient la paire médicament-maladie. Le seul appui est un score TxGNN élevé et un raisonnement pharmacologique indirect.
- Les données de sécurité et de mécanisme d'action sont absentes, et l'adéquation d'une forme orale à une urgence hypertensive n'est pas démontrée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (bloquant pour le criblage de sécurité).
- Obtenir les données de mécanisme d'action depuis DrugBank.
- Lancer une recherche bibliographique ciblée « bisoprolol » + hypertension rénovasculaire / néphropathie hypertensive maligne.
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication d'origine.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

