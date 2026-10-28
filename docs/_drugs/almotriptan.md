---
layout: default
title: Almotriptan
parent: Prédiction du modèle uniquement (L5)
nav_order: 44
evidence_level: L5
indication_count: 2
monitor_inn: "almotriptan"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis"]
last_modified_at: 2026-10-28
description: "Almotriptan : nouvelle indication prédite, Atrophodermie vermiculée (niveau de preuve L5). Indication d'origine : Migraine"
---

# Almotriptan
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Almotriptan : De la migraine à l'atrophodermie vermiculée
{: .text-alpha }

## Résumé en Une Phrase

L'almotriptan est un médicament de la classe des triptans, utilisé à l'origine pour le traitement de la migraine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**atrophodermie vermiculée** (atrophoderma vermiculata), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Migraine (relation enregistrée dans le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné dans les données compilées pour ce rapport) |
| Nouvelle Indication Prédite | Atrophodermie vermiculée |
| Score de Prédiction TxGNN | 0,9977 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 5 sur 5) |
| Nombre d'AMM | 5 (valides : 5) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales sur sa classe, l'almotriptan est un agoniste sélectif des récepteurs sérotoninergiques 5-HT1B/1D, qui agit dans la migraine par vasoconstriction crânienne et inhibition de la libération de neuropeptides.

L'atrophodermie vermiculée est une affection rare des joues, classée parmi les kératoses pilaires atrophiantes. Sa physiopathologie repose sur la kératinisation folliculaire, l'inflammation et la cicatrisation atrophique, sans lien évident avec la signalisation sérotoninergique 1B/1D.

**Aucun lien mécanistique n'est établi** dans les données disponibles. Le score élevé de TxGNN (0,9977) provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Une seconde prédiction, l'*ulérythème ophryogène* (score 0,9964), appartient au même groupe des kératoses pilaires atrophiantes. Ce score provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

L'almotriptan est commercialisé en France sous forme de spécialités à base d'un seul principe actif (5 AMM valides, toutes génériques). Le texte d'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 65724460 | ALMOTRIPTAN EG 12,5 mg | Comprimé pelliculé | EG LABO - Laboratoires Eurogenerics |
| 65959736 | ALMOTRIPTAN ZENTIVA 12,5 mg | Comprimé pelliculé | Zentiva France |
| 65840148 | ALMOTRIPTAN SANDOZ 12,5 mg | Comprimé pelliculé | Sandoz |
| 64165648 | ALMOTRIPTAN ARROW 12,5 mg | Comprimé pelliculé | Arrow Génériques |
| 68877714 | ALMOTRIPTAN TEVA 12,5 mg | Comprimé pelliculé | Teva Santé |

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour ces informations.

- **Contre-indications enregistrées dans le graphe de connaissances** (relations du graphe, et non texte de la notice) : hypertension, maladie coronarienne, infarctus du myocarde, angor de Prinzmetal, ischémie myocardique, accident vasculaire cérébral et ischémie cérébrale, accident ischémique transitoire, insuffisance vertébro-basilaire, maladie artérielle périphérique, maladie de Raynaud, migraine hémiplégique familiale ou sporadique, syndrome sérotoninergique, maladie hépatique, diabète et acidocétose diabétique, obésité, maladie de la vésicule biliaire, hémoglobinopathie, arrêt cardiaque soudain, troubles de la conduction cardiaque.
- **Interactions médicamenteuses** (56 interactions recensées ; principales) :
  - Majeures : dexfenfluramine, fenfluramine, lorcasérine, sibutramine, dolasétron, granisétron, ondansétron, palonosétron.
  - Modérées : aprépitant, clarithromycine, morphine (y compris liposomale).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L5 : aucun essai ni aucune publication n'étudie l'almotriptan dans l'atrophodermie vermiculée, et aucun lien mécanistique plausible n'est identifié.
- Les données de sécurité de la notice sont manquantes, ce qui bloque un examen de sécurité complet.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (téléchargement et analyse de la notice).
- Les données détaillées sur le mécanisme d'action (DrugBank).
- Une justification biologique reliant la signalisation 5-HT1B/1D à la physiopathologie de l'atrophodermie vermiculée, ou des données précliniques / cas cliniques.
- Une évaluation de la compatibilité de la voie d'administration (comprimés oraux uniquement disponibles ; atteinte cutanée localisée).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

