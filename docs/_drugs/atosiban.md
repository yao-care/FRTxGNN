---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban : De la Prévention de l'Accouchement Prématuré au Glaucome Héréditaire Primaire

## Résumé en Une Phrase

Atosiban est un antagoniste compétitif des récepteurs de l'ocytocine (OTR) et de la vasopressine V1A/V2, utilisé en milieu hospitalier comme tocolytique pour retarder l'accouchement prématuré.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Glaucome Héréditaire Primaire (Primary Hereditary Glaucoma)**,
avec **0 essai clinique** et **0 publication** soutenant directement cette direction — le niveau de preuve est actuellement L5 (prédiction algorithmique uniquement).

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Tocolyse — prévention de l'accouchement prématuré |
| Nouvelle Indication Prédite | Glaucome Héréditaire Primaire |
| Score de Prédiction TxGNN | 99,92% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action d'atosiban ne sont pas disponibles dans le système actuel. Sur la base des informations publiées, atosiban fait partie de la classe des antagonistes des récepteurs à l'ocytocine (OTR) et à la vasopressine V1A/V2. Son efficacité comme tocolytique repose sur l'inhibition des contractions utérines : en bloquant les récepteurs OTR/AVPR1A du myomètre, il réduit la fréquence et l'intensité des contractions, permettant de retarder l'accouchement prématuré.

La connexion hypothétique avec le glaucome héréditaire primaire repose sur l'observation que des récepteurs OTR sont exprimés dans le corps ciliaire de l'œil et que le système ocytocinergique pourrait moduler la pression intraoculaire (PIO). En théorie, un modulateur de ce récepteur pourrait influencer la dynamique de sécrétion de l'humeur aqueuse. Le glaucome héréditaire primaire, caractérisé par une élévation chronique de la PIO d'origine génétique, pourrait donc représenter une cible biologique adjacente dans le graphe de connaissances.

Cependant, cette hypothèse présente d'importantes limites mécanistiques : le score TxGNN très élevé (99,92%) résulte vraisemblablement de la proximité topologique dans le graphe de connaissances biologiques plutôt que d'une corrélation mécanistique directe. Aucune donnée clinique, aucune étude préclinique ni aucune hypothèse validée ne soutient actuellement l'utilisation d'atosiban dans le glaucome. Par ailleurs, il n'existe aucune démonstration que l'antagonisme OTR, par opposition à son agonisme, exercerait un effet bénéfique sur la PIO.

> ⚠️ **Signal d'alerte mécanistique (indication vasculaire, rang 6)** : 17 publications identifiées pour l'indication « vascular disease » documentent presque exclusivement les effets *protecteurs* de **l'ocytocine** sur le système cardiovasculaire (voies RISK/SAFE, cardioprotection ischémie-reperfusion). Atosiban, en tant qu'*antagoniste*, agirait en sens contraire — atténuant cette protection plutôt qu'en la reproduisant. Ce signal de direction mécanistique négative constitue un facteur de risque transversal à considérer pour l'ensemble des repositionnements vasculaires de ce médicament.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé au glaucome héréditaire primaire n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée au glaucome héréditaire primaire n'est disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN pour le glaucome héréditaire primaire atteint un score algorithmique très élevé (99,92%), mais repose exclusivement sur la modélisation par graphe de connaissances (niveau L5), sans aucune donnée clinique ou préclinique à l'appui. Le lien mécanistique entre l'antagonisme OTR/AVPR1A et la pathologie glaucomateuse reste hautement spéculatif, et le signal de direction mécanistique négative identifié pour les indications vasculaires renforce la nécessité d'une validation expérimentale approfondie avant toute progression.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études in vitro sur l'effet d'atosiban sur la sécrétion d'humeur aqueuse dans des modèles de corps ciliaire humain
- Confirmation de l'expression fonctionnelle des récepteurs OTR dans le tissu trabéculaire et le corps ciliaire humains
- Mécanisme d'action (MOA) complet — actuellement absent des données disponibles (DG002)
- Informations de sécurité via la notice officielle — contre-indications et mises en garde actuellement indisponibles (DG001)
- Vérification du statut AMM en France auprès de l'ANSM (atosiban est commercialisé sous le nom Tractocile® dans plusieurs États membres de l'UE — une évaluation de l'extension géographique est requise)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

