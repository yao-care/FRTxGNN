---
layout: default
title: Loxapine
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Loxapine
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

# Loxapine : Rapport d'Évaluation de Repositionnement — Données Insuffisantes

## Résumé en Une Phrase

La Loxapine est un antipsychotique de la classe des dibenzoxazépines, utilisé en psychiatrie pour le traitement de la schizophrénie et des états d'agitation aiguë. Le présent dossier ne contient **aucune indication prédite par TxGNN** et aucune donnée réglementaire française, ce qui rend impossible l'analyse de repositionnement complète à ce stade. Une collecte de données complémentaires est indispensable avant toute évaluation.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Schizophrénie / Agitation aiguë (connaissance générale ; non renseignée dans le dossier) |
| Nouvelle Indication Prédite | Aucune — `predicted_indications` vide |
| Score de Prédiction TxGNN | Non disponible |
| Niveau de Preuve | L5 — Aucune étude réelle disponible |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Cette section ne peut pas être complétée dans l'état actuel du dossier.

Le modèle TxGNN n'a retourné **aucune indication prédite** (`predicted_indications: []`), ce qui signifie soit que la requête n'a pas abouti, soit que le médicament n'a pas atteint le seuil de score minimal. De plus, les données sur le mécanisme d'action (MOA) sont absentes du dossier (`[Data Gap]`).

Sur la base des connaissances pharmaceutiques générales : la Loxapine est un antagoniste des récepteurs dopaminergiques D2 et sérotoninergiques 5-HT2A. Elle appartient à la famille des antipsychotiques typiques/atypiques de première génération, avec une affinité particulière pour les récepteurs histaminergiques H1. Ces propriétés de liaison multi-récepteurs font de la Loxapine un candidat potentiellement intéressant pour des analyses de repositionnement, mais aucune donnée computationnelle n'est disponible dans ce dossier pour étayer une direction précise.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement — données `predicted_indications` absentes du dossier.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement — données `predicted_indications` absentes du dossier.

---

## Informations de Marché en France

La Loxapine ne dispose d'**aucune AMM** enregistrée dans le système réglementaire interrogé (0 licence, statut : non commercialisé). Aucun tableau ne peut être produit.

> **Note :** La Loxapine est commercialisée dans d'autres pays (États-Unis, Canada, Royaume-Uni) sous les noms Loxitane® et Adasuve® (forme inhalée). L'absence de données ANSM dans ce dossier peut refléter une lacune de collecte plutôt qu'une absence réelle d'autorisation historique.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> Les données de sécurité (mises en garde, contre-indications, interactions médicamenteuses) sont toutes absentes du dossier actuel (`[Data Gap]`). La fiche TFDA a bien été interrogée (statut : `success`) mais aucun contenu exploitable n'a été retourné. Une extraction manuelle de la notice est nécessaire.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le dossier Evidence Pack est structurellement incomplet : aucune indication prédite par TxGNN, aucune donnée réglementaire française, et aucune donnée de sécurité exploitable. Il est impossible de produire une évaluation de repositionnement fiable dans ces conditions.

**Pour avancer, les éléments suivants sont nécessaires :**

1. **Relancer le pipeline TxGNN** pour DB00408 (Loxapine) et vérifier pourquoi `predicted_indications` est vide — vérifier le seuil de score, la présence du nœud dans le graphe de connaissances, et les logs de prédiction
2. **Extraire le MOA complet** depuis l'API DrugBank (DB00408) : mécanisme détaillé, cibles pharmacologiques, voies de signalisation
3. **Récupérer la notice ANSM/EMA** : la requête `tfda_package_insert` a retourné `success` mais aucun contenu n'est présent dans `safety` — vérifier le parsing du PDF
4. **Vérifier le statut réglementaire réel** en France via la base de données publique de l'ANSM (la Loxapine a pu bénéficier d'une AMM historique ou d'une importation sous ATU/AAP)
5. **Relancer l'analyse DDI** une fois le MOA disponible, afin d'évaluer les interactions médicamenteuses pertinentes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

