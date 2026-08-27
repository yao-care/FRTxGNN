---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol : De l'Asthme/BPCO à la Conjonctivite Papillaire

## Résumé en Une Phrase

Le salbutamol est un agoniste β2-adrénergique à courte durée d'action (SABA), utilisé de façon établie comme bronchodilatateur dans la prise en charge de l'asthme et de la bronchopneumopathie chronique obstructive (BPCO).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Conjonctivite Papillaire**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction — il s'agit d'un signal de prédiction pur, non validé.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Asthme / BPCO (bronchospasme réversible) |
| Nouvelle Indication Prédite | Conjonctivite papillaire |
| Score de Prédiction TxGNN | 99.996% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) du salbutamol ne sont pas disponibles dans ce dossier. Sur la base des informations recueillies à travers l'ensemble du pack de preuves, le salbutamol appartient à la classe des agonistes β2-adrénergiques à courte durée d'action (SABA), dont l'efficacité dans le traitement du bronchospasme réversible associé à l'asthme et à la BPCO est bien établie et largement documentée par de multiples essais cliniques de phase 3 identifiés dans ce même dossier (voir les indications « bronchite » et « maladie pulmonaire obstructive »).

Pour l'indication prédite ici — la conjonctivite papillaire — le lien mécanistique est jugé faible. La conjonctivite papillaire est principalement une réaction mécanique ou de contact (par exemple liée au port de lentilles de contact), dont la physiopathologie ne recoupe pas directement l'action bronchodilatatrice du salbutamol sur le muscle lisse des voies respiratoires. Aucun essai clinique ni aucune publication n'a été identifié pour appuyer cette hypothèse ; il s'agit exclusivement d'un signal généré par le modèle TxGNN, sans validation expérimentale ou clinique à ce stade.

Il est à noter que d'autres indications prédites dans ce même dossier (bronchite, maladie pulmonaire obstructive) bénéficient d'un niveau de preuve L1 avec de nombreux essais de phase 3, mais celles-ci correspondent en réalité au périmètre d'usage déjà établi du salbutamol plutôt qu'à un véritable repositionnement — contrairement à la conjonctivite papillaire, qui représenterait une indication réellement nouvelle si elle venait à être confirmée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucune preuve clinique ou de littérature n'existe actuellement pour la conjonctivite papillaire ; il s'agit d'un score de prédiction TxGNN isolé (niveau de preuve L5), avec un lien mécanistique jugé faible. De plus, les données réglementaires de base (mises en garde/contre-indications TFDA) sont manquantes de façon bloquante, empêchant toute évaluation de sécurité préliminaire (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice TFDA (mises en garde, contre-indications) — actuellement un blocage identifié (sévérité *Blocking*) empêchant l'évaluation de sécurité S1
- Données détaillées sur le mécanisme d'action (MOA) via l'API DrugBank — gap de sévérité *High*
- Études précliniques ou de mécanisme établissant un lien biologique plausible entre l'action β2-adrénergique et la physiopathologie de la conjonctivite papillaire
- Si de nouvelles données cliniques ou de littérature émergent, réévaluer le niveau de preuve et la décision

*Note : ce dossier contient également des indications prédites avec un niveau de preuve nettement supérieur (L1, « Proceed with Guardrails ») — bronchite et maladie pulmonaire obstructive — mais celles-ci correspondent à l'usage déjà établi du salbutamol plutôt qu'à un nouveau repositionnement, et ne remplacent pas l'évaluation ci-dessus centrée sur la conjonctivite papillaire.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

