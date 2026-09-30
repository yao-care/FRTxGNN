---
layout: default
title: Famciclovir
parent: Preuves modérées (L3-L4)
nav_order: 125
evidence_level: L4
indication_count: 9
---

# Famciclovir
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **9** 
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

# Famciclovir : Vers la Névralgie Post-Infectieuse

## Résumé en Une Phrase

Famciclovir est un antiviral, prodrogue du penciclovir, qui agit sur l'ADN polymérase des herpèsvirus. Le texte de l'indication autorisée en France n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **névralgie post-infectieuse** (en pratique, la névralgie post-zostérienne), avec **2 essais cliniques** liés à la maladie, dont aucun ne teste le famciclovir, et **aucune publication** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Névralgie post-infectieuse |
| Score de Prédiction TxGNN | 99,75 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank. Sur la base des informations connues, le famciclovir est converti en penciclovir, qui inhibe l'ADN polymérase du virus varicelle-zona (VZV) après phosphorylation par la thymidine kinase virale.

La névralgie post-infectieuse est la complication douloureuse la plus fréquente du zona. Un traitement antiviral précoce pendant la phase aiguë du zona pourrait réduire la gravité et la durée de cette phase, ce qui constitue une voie indirecte plausible pour diminuer le risque de névralgie ultérieure.

Cette hypothèse reste indirecte. Les deux essais associés portent sur d'autres interventions (oxycodone, blocs nerveux) et ne fournissent aucune preuve directe pour le famciclovir dans cette indication.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Non applicable | Inconnu | 140 | Oxycodone précoce en phase aiguë du zona pour prévenir la névralgie post-zostérienne. Le famciclovir n'est pas testé. |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | Non applicable | Recrutement non commencé | 120 | Bloc nerveux multimodal et radiofréquence pulsée pour la douleur du zona aigu. Aucun bras famciclovir. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 69092403 | ORAVIR 125 mg, comprimé pelliculé | Comprimé pelliculé |
| 62801318 | ORAVIR 500 mg, comprimé pelliculé | Comprimé pelliculé |

Les deux AMM sont détenues par PHOENIX LABS (Irlande).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose sur un score de modèle élevé et sur un lien mécanistique indirect. Aucun essai ni publication ne teste le famciclovir dans la névralgie post-infectieuse, et les données de sécurité de la notice ANSM sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Un essai comparatif évaluant directement le famciclovir sur la prévention de la névralgie post-zostérienne
- La notice ANSM (mises en garde, contre-indications) et le texte de l'indication autorisée
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Un point d'attention : dans le même Evidence Pack, la varicelle et le zona (rang 7) sont soutenus par un essai de phase 3 terminé comparant famciclovir et aciclovir dans le zona (NCT01327144), ainsi qu'un essai pédiatrique de phase 3 sur la pharmacocinétique et la sécurité (NCT00098046). Cette piste, au niveau L1, est recommandée en « Proceed with Guardrails » ; il faudrait confirmer s'il s'agit de la varicelle ou du zona et la base de dosage pédiatrique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

