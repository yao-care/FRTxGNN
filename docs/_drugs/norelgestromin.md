---
layout: default
title: Norelgestromin
parent: Prédiction du modèle uniquement (L5)
nav_order: 544
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Norelgestromin : nouvelle indication prédite, Aménorrhée (niveau de preuve L5). Indication d'origine : Non renseignée dans l'AMM"
monitor_inn: "norelgestromin"
predicted_indications: ["amenorrhea (disease)"]
---

# Norelgestromin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Norelgestromine : D'une indication d'origine non renseignée à l'aménorrhée
{: .text-alpha }

## Résumé en Une Phrase

La norelgestromine est le principal métabolite actif du norgestimate, un progestatif commercialisé en France sous forme de dispositif transdermique (EVRA), associé à l'éthinylestradiol. Le texte de son indication d'origine n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**aménorrhée**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM |
| Nouvelle Indication Prédite | Aménorrhée |
| Score de Prédiction TxGNN | 0,9951 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la norelgestromine est un progestatif, agoniste du récepteur de la progestérone, et le métabolite actif principal du norgestimate.

Les progestatifs sont utilisés pour provoquer un saignement de privation dans l'aménorrhée secondaire. L'effet progestatif sur l'endomètre constitue donc un lien mécanistique plausible avec cette indication.

Cette plausibilité reste théorique. Le score de 0,9951 est une prédiction purement computationnelle. De plus, la forme commercialisée est un patch transdermique associant l'éthinylestradiol, à visée contraceptive, qui modifie lui-même le profil des saignements menstruels. Un usage réel dans l'aménorrhée serait donc difficile à interpréter.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 69729088 | EVRA 203 microgrammes/24 heures + 33,9 microgrammes/24 heures, dispositif transdermique (GEDEON RICHTER) | Dispositif transdermique | Non renseignée | Active |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une interaction de niveau **majeur** est signalée avec le **sugammadex**.
- **Contre-indications potentielles (graphe de connaissances, hors texte de la notice)** : les relations du graphe de connaissances associent le médicament aux affections suivantes, à vérifier auprès de la notice :
  - Cardiovasculaires et métaboliques : hypertension, thrombophlébite, maladie coronarienne, hyperlipidémie (dont familiale), hypertriglycéridémie, diabète, acidocétose diabétique, hyperglycémie.
  - Hépatiques et rénales : maladie hépatique, maladie de la vésicule biliaire, maladie rénale, pyo-uretère.
  - Neurologiques et psychiatriques : épilepsie, migraine, trouble anxieux, trouble névrotique, trouble dysthymique.
  - Autres : porphyries, lupus érythémateux systémique (dont forme pédiatrique), asthme (intrinsèque et allergique), carcinome du sein chez la femme.

Les mises en garde et contre-indications issues de la notice ANSM ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication.
- L'AMM française est annulée, et la seule forme connue est un patch contraceptif combiné, ce qui limite toute voie de développement.
- Les données de sécurité de la notice, nécessaires au criblage de sécurité, sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications).
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Préciser l'indication d'origine de l'AMM.
- Rechercher des études cliniques ou observationnelles sur les progestatifs dans l'aménorrhée.
- Évaluer la compatibilité de la voie d'administration et la pertinence d'une formulation sans œstrogène.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

