---
layout: default
title: Nefopam
parent: Prédiction du modèle uniquement (L5)
nav_order: 529
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nefopam : nouvelle indication prédite, 99,98 % (niveau de preuve L5). Indication d'origine : Cataracte avec craniosténose"
monitor_inn: "nefopam"
predicted_indications: ["craniostenosis cataract", "immature cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic cataract", "lumbar spinal stenosis"]
---

# Nefopam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Néfopam : D'une indication d'origine non documentée à la cataracte avec craniosténose

## Résumé en Une Phrase

Le néfopam est un analgésique d'action centrale non opioïde, commercialisé en France sous la forme injectable (ACUPAN 20 mg/2 mL). L'indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cataracte avec craniosténose** (syndrome rare), avec un score très élevé mais **aucun essai clinique et aucune publication** à l'appui de cette prédiction précise.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Cataracte avec craniosténose |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement AMM abrogée (aucune AMM valide) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier source. D'après les connaissances générales, le néfopam est un analgésique d'action centrale qui inhibe la recapture de la sérotonine, de la noradrénaline et de la dopamine, et module les canaux sodiques et calciques voltage-dépendants.

Il n'existe **aucun lien mécanistique connu** entre ce profil pharmacologique et la cataracte avec craniosténose, un syndrome rare associant une atteinte du cristallin et une fusion prématurée des sutures crâniennes. Le score élevé semble refléter la proximité des nœuds « cataracte » dans le graphe de connaissances plutôt qu'une justification biologique.

La prédiction doit donc être considérée comme une **hypothèse purement algorithmique**. Huit autres formes de cataracte (immature, mature, sénile, nucléaire, corticale, diabétique, etc.) reçoivent des scores similaires, sans plus de preuves.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|---------|------|------|------|------|
| 62580656 | ACUPAN 20 mg/2 mL, solution injectable | Solution injectable | BIOCODEX | Abrogée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées, et aucune contre-indication issue du graphe de connaissances n'est répertoriée.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5). Il n'y a ni essai clinique, ni publication, ni mécanisme plausible reliant le néfopam à cette maladie rare.
- L'unique AMM française est abrogée, et les informations de sécurité issues de la notice sont indisponibles.

**Piste alternative à noter :** parmi les prédictions moins bien classées, la **sténose lombaire** (score 99,97 %) est la seule qui dispose de publications (4 références, niveau L3). Il s'agit d'études sur le néfopam périopératoire : douleur postopératoire, dysesthésies et épargne des opioïdes en chirurgie du rachis. Elles concernent le contrôle des symptômes et non la modification de la maladie. Une étude randomisée en double aveugle de 2023 (73 patients) pourrait justifier un niveau L2 si son design est confirmé. Un cas de **crises convulsives / état de mal épileptique** attribué au néfopam impose une évaluation attentive de la sécurité. Cette piste, davantage plausible sur le plan pharmacologique, mérite d'être évaluée séparément.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (ANSM) pour les mises en garde et contre-indications, et clarifier le statut réglementaire de l'AMM abrogée.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank) pour analyser un éventuel lien mécanistique.
- Pour la cataracte avec craniosténose : une justification biologique préclinique avant tout investissement clinique.
- Pour la sténose lombaire : confirmer le design des études (essai randomisé ou non), puis réaliser une revue de sécurité centrée sur le risque convulsif.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

