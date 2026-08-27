---
layout: default
title: Siltuximab
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 8
---

# Siltuximab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Siltuximab : De la Maladie de Castleman Multicentrique Idiopathique au Mastocytome Extracutané

## Résumé en Une Phrase

Siltuximab est un anticorps monoclonal anti-IL-6, dont l'indication de référence est la maladie de Castleman multicentrique idiopathique (iMCD).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **mastocytome extracutané**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction — la prédiction repose uniquement sur le modèle (L5).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Castleman multicentrique idiopathique (iMCD)* |
| Nouvelle Indication Prédite | Mastocytome extracutané |
| Score de Prédiction TxGNN | 99.64% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

*\* Le champ structuré `taiwan_regulatory.licenses` est vide (médicament non commercialisé en France). Cette indication est reconstituée à partir du contexte fourni dans le dossier de preuves (rationale mécanistique associée à ce médicament), et non d'une AMM française.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de siltuximab ne sont pas disponibles dans ce dossier. Sur la base des informations connues, siltuximab est un anticorps monoclonal chimérique dirigé contre l'interleukine-6 (IL-6), dont l'efficacité dans la maladie de Castleman multicentrique idiopathique repose sur le blocage de la voie inflammatoire IL-6, mécanistiquement impliquée dans la prolifération lymphocytaire de cette pathologie.

Le lien avec le mastocytome extracutané est faible : dans les maladies prolifératives des mastocytes, l'IL-6 peut être un marqueur inflammatoire corrélé à la sévérité, mais le mécanisme moteur principal est la mutation du gène KIT, indépendante de l'axe IL-6. Aucun essai clinique ni aucune publication ne relie actuellement siltuximab à cette indication — la prédiction TxGNN (rang 3001, score 99.64%) n'est donc soutenue par aucune preuve réelle à ce stade.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve est L5 (prédiction du modèle seule, aucune étude réelle) et le lien mécanistique proposé (IL-6 comme marqueur de sévérité, non comme moteur pathogénique du mastocytome extracutané, dont la mutation KIT est le principal driver) reste peu convaincant. Aucun essai clinique ni publication ne permet à ce stade de dépasser le stade de simple hypothèse computationnelle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications du RCP/TFDA (data gap bloquant — nécessaire avant toute évaluation de sécurité S1)
- Données sur le mécanisme d'action (MOA) via DrugBank
- Études précliniques explorant un rôle éventuel de l'IL-6 dans le mastocytome extracutané
- Confirmation de l'indication d'origine et du statut réglementaire (les champs structurés `taiwan_regulatory` et `original_indications` sont actuellement vides)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

