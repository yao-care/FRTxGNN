---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol : De la Douleur à la Dysplasie Acromésomélique de Type Hunter-Thompson

## Résumé en Une Phrase

Le tramadol est un analgésique opioïde (agoniste des récepteurs mu combiné à une action IRSN) utilisé pour les douleurs modérées à sévères. Le modèle TxGNN prédit un lien avec la **dysplasie acromésomélique de type Hunter-Thompson**, une maladie osseuse génétique rare, mais cette prédiction n'est actuellement soutenue par **aucun essai clinique ni aucune publication**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Douleurs modérées à sévères (analgésique opioïde) — non documentée par une AMM dans les données fournies |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson |
| Score de Prédiction TxGNN | 99.99 % (rang 215) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données structurées sur le mécanisme d'action (MOA) ne sont pas disponibles dans la fiche DrugBank (data gap DG002, sévérité High). Sur la base des informations descriptives disponibles dans l'analyse de repositionnement, le tramadol est un agoniste des récepteurs opioïdes mu associé à une inhibition de la recapture de la sérotonine et de la noradrénaline (SNRI) — un mécanisme strictement analgésique.

La dysplasie acromésomélique de type Hunter-Thompson est une maladie génétique rare causée par des mutations du gène CDMP1/GDF5, affectant le développement du cartilage et de la plaque de croissance osseuse. Il s'agit d'une pathologie structurelle du développement, sans rapport physiopathologique connu avec la douleur ou avec les récepteurs opioïdes/monoaminergiques ciblés par le tramadol.

L'analyse de repositionnement associée à cette prédiction conclut elle-même que ce score élevé provient très probablement d'un artefact du graphe de connaissances (proximité des nœuds « douleur » ou « maladie osseuse » dans l'espace d'embedding TxGNN), et non d'une correspondance mécanistique réelle. Aucune donnée clinique, préclinique ou de la littérature ne vient appuyer cette hypothèse à ce jour.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Niveau de preuve L5 : la prédiction repose uniquement sur le score du modèle TxGNN, sans aucun essai clinique, aucune littérature, ni justification mécanistique solide ; l'analyse de repositionnement qualifie elle-même ce lien de probable faux positif lié à la topologie du graphe de connaissances.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résoudre le data gap bloquant DG001 : obtenir le RCP/notice TFDA du tramadol (téléchargement PDF + extraction) pour permettre l'évaluation de sécurité S1
- Résoudre le data gap DG002 : interroger l'API DrugBank pour documenter le MOA structuré du tramadol
- Ne pas poursuivre cette indication en l'état ; si une piste de repositionnement doit être approfondie pour le tramadol, le candidat classé #7 (arthrite juvénile idiopathique — niveau de preuve L4, 2 publications, stade S1 « Research Question ») est nettement mieux étayé et mérite une évaluation dédiée séparée
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

