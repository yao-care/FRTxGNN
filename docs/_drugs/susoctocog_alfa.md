---
layout: default
title: Susoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog Alfa : De l'Hémophilie A Acquise au Trouble Primaire de la Libération Plaquettaire

## Résumé en Une Phrase

Susoctocog alfa (Obizur®) est un facteur VIII recombinant d'origine porcine, historiquement utilisé pour traiter les épisodes hémorragiques de l'**hémophilie A acquise** (indication approuvée à l'international, non commercialisée en France). Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble Primaire de la Libération Plaquettaire**, mais cette direction n'est actuellement soutenue par **aucun essai clinique** ni **aucune publication** — il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie A acquise (épisodes hémorragiques) |
| Nouvelle Indication Prédite | Trouble Primaire de la Libération Plaquettaire |
| Score de Prédiction TxGNN | 99.94% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues issues des preuves collectées, susoctocog alfa est un facteur VIII recombinant délété du domaine B, d'origine porcine, dont l'efficacité dans le traitement des saignements liés à l'hémophilie A acquise est bien établie (voir preuves de littérature ci-dessous, associées à la 4ᵉ indication prédite de ce dossier).

Le Trouble Primaire de la Libération Plaquettaire, en revanche, est un défaut du relargage des granules plaquettaires : le saignement provient d'une dysfonction plaquettaire, et non d'un déficit en facteur VIII. Le rationnel mécanistique fourni dans ce dossier indique explicitement l'absence de lien direct : le score élevé de TxGNN semble refléter une proximité sémantique entre « maladies hémorragiques » dans le graphe de connaissances, plutôt qu'un mécanisme pharmacologique partagé. Une supplémentation en FVIII ne peut pas corriger un défaut de libération plaquettaire.

Cette prédiction doit donc être interprétée avec prudence : elle illustre un cas où le score TxGNN est élevé sans support mécanistique ni preuve clinique correspondante.

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
Aucune preuve clinique ou littéraire ne soutient cette indication (niveau L5), et le rationnel mécanistique fourni indique lui-même une absence de plausibilité pharmacologique — le signal TxGNN paraît être un artefact du graphe de connaissances plutôt qu'une piste de repositionnement crédible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (MOA) détaillées depuis DrugBank (actuellement en écart, DG002)
- Notice/mises en garde TFDA/ANSM (écart bloquant, DG001) avant toute évaluation de sécurité S1
- Étude préclinique ou mécanistique établissant un lien plausible entre le FVIII et la libération plaquettaire, avant d'envisager une progression au-delà de S0

**Remarque :** ce dossier de preuves contient 10 indications prédites pour ce médicament. Contrairement à celle présentée ici, la 4ᵉ indication du classement (« hemophilia » / hémophilie A acquise) dispose d'un niveau de preuve nettement supérieur (L2, stade S3, décision « Proceed with Guardrails », avec un essai clinique en cours et 20 publications) et correspond en fait à l'indication déjà approuvée du produit à l'international. Un rapport dédié à cette indication serait plus pertinent pour une décision de repositionnement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

