---
layout: default
title: Pyrazinamide
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide : De la Tuberculose à l'Otite Moyenne Infectieuse

## Résumé en Une Phrase

Le pyrazinamide est un antituberculeux de première ligne, historiquement utilisé en association (avec rifampicine, isoniazide et éthambutol) dans le traitement de la tuberculose.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Otite Moyenne Infectieuse**, avec un score de prédiction de **99,96 %**.
Cependant, **aucun essai clinique** et **aucune publication** ne soutiennent actuellement spécifiquement cette direction : il s'agit d'une extrapolation purement statistique du modèle, sans preuve mécanistique vérifiable à ce stade.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tuberculose (traitement antituberculeux de première ligne — aucune AMM française disponible pour confirmer le libellé officiel) |
| Nouvelle Indication Prédite | Otite Moyenne Infectieuse (infectious otitis media) |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles (donnée manquante classée « High » dans le pack de preuves, à combler via l'API DrugBank). Sur la base des informations connues, le pyrazinamide est un promédicament converti par la pyrazinamidase bactérienne en acide pyrazinoïque, actif principalement en milieu acide contre *Mycobacterium tuberculosis* en phase semi-dormante intracellulaire ; son efficacité dans la tuberculose est bien établie depuis des décennies d'usage clinique.

Pour l'indication prédite en tête de liste — l'otite moyenne infectieuse au sens large —, aucun lien mécanistique n'a pu être établi : la justification associée indique explicitement qu'il s'agit d'une extrapolation par similarité d'embedding, sans essai ni publication à l'appui. Le pyrazinamide n'a pas d'activité antibactérienne connue contre les pathogènes usuels de l'otite moyenne (pneumocoque, *Haemophilus influenzae*).

Il est toutefois utile de noter que, parmi les autres indications prédites par le même modèle (non détaillées ci-dessous), plusieurs variantes d'otite moyenne — otite moyenne chronique, otite moyenne suppurée, maladie de l'oreille moyenne — sont associées à de la littérature réelle, mais celle-ci décrit systématiquement des cas d'**otite moyenne tuberculeuse** (une manifestation rare de tuberculose extra-pulmonaire), traitée par le protocole antituberculeux standard incluant le pyrazinamide — et non une action antibactérienne directe du pyrazinamide sur l'otite moyenne commune. Cette nuance est importante : la piste la plus crédible n'est pas celle du rang 1 présentée ici, mais celle, plus restreinte, de l'otite moyenne d'origine tuberculeuse.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Aucune AMM enregistrée en France — le pyrazinamide n'est pas commercialisé sous licence répertoriée dans le registre consulté (statut : non commercialisé, 0 AMM).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucun essai clinique ni aucune publication ne soutient l'indication « otite moyenne infectieuse » spécifiquement ; le score TxGNN élevé reflète une proximité d'embedding sans mécanisme vérifiable. De plus, l'absence de données sur les mises en garde/contre-indications TFDA (écart bloquant) empêche toute évaluation de sécurité S1.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir le libellé officiel (mises en garde, contre-indications) via l'AMM/notice réglementaire — écart bloquant actuel
- Documenter le mécanisme d'action complet via l'API DrugBank
- Réorienter, le cas échéant, l'hypothèse de recherche vers l'**otite moyenne tuberculeuse** (sous-catégorie disposant d'un corpus de cas cliniques réels), plutôt que l'otite moyenne infectieuse générique
- Rechercher une éventuelle activité antibactérienne directe du pyrazinamide contre les pathogènes usuels de l'otite moyenne avant toute étude préclinique
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

