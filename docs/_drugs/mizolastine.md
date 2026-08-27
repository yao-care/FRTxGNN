---
layout: default
title: Mizolastine
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Mizolastine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mizolastine : De l'Antihistaminique H1 (Indication d'Origine Non Documentée) à la Porphyrie Aiguë Intermittente

## Résumé en Une Phrase

Mizolastine est un antihistaminique H1 de deuxième génération ; aucune indication d'origine ni AMM ne sont enregistrées dans les données actuelles, le médicament n'étant pas commercialisé en France.
Le modèle TxGNN prédit une association avec la **Porphyrie Aiguë Intermittente**,
mais cette direction n'est actuellement soutenue par **aucun essai clinique** ni **aucune publication** — il s'agit d'une prédiction de niveau L5 reposant uniquement sur le graphe de connaissances.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans les données actuelles (aucune indication approuvée enregistrée) |
| Nouvelle Indication Prédite | Porphyrie Aiguë Intermittente |
| Score de Prédiction TxGNN | 99.76% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action de la mizolastine ne sont pas disponibles dans ce dossier. Sur la base des informations disponibles dans les éléments de preuve, la mizolastine appartient à la classe des antihistaminiques H1 de deuxième génération ; aucune indication d'origine approuvée n'est en revanche enregistrée, le médicament n'étant pas commercialisé en France (0 AMM).

La justification mécanistique fournie pour cette prédiction indique explicitement l'**absence de lien connu** entre l'antagonisme du récepteur H1 et la voie métabolique de la porphyrine (ALA synthase / biosynthèse de l'hème). Le score TxGNN élevé (99,76%) semble donc refléter une proximité structurelle dans le graphe de connaissances plutôt qu'un mécanisme pharmacologique établi.

Un point doit même être noté dans le sens inverse : certains médicaments métabolisés par le CYP450 sont connus pour pouvoir déclencher des crises aiguës chez les patients porteurs de porphyrie — ce qui constitue une préoccupation potentielle de sécurité plutôt qu'un argument en faveur de cette indication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Aucune AMM enregistrée en France. Selon les données actuelles, la mizolastine n'est pas commercialisée sur le marché français (statut : non commercialisé, 0 AMM).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L5 (aucun essai clinique, aucune publication), et le lien mécanistique entre l'antagonisme H1 et la porphyrie aiguë intermittente n'est pas établi. Par ailleurs, les données de sécurité essentielles (notice, contre-indications) sont manquantes — un écart bloquant qui empêche toute évaluation de sécurité préliminaire (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (avertissements, contre-indications) — écart bloquant (DG001)
- Données détaillées sur le mécanisme d'action (MOA) via DrugBank — écart élevé (DG002)
- Données précliniques sur une éventuelle interaction entre les antihistaminiques H1 et le métabolisme de l'hème/porphyrine
- Confirmation du statut réglementaire et de commercialisation du médicament en France
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

