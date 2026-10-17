---
layout: default
title: Ganirelix
parent: Prédiction du modèle uniquement (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ganirelix : nouvelle indication prédite, Hypertrichose (niveau de preuve L5). Indication d'origine : Prévention de l'ovulation prématurée lors de la stimulation ovarienne…"
monitor_inn: "ganirelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial male-limited precocious puberty", "persistent fetal circulation syndrome", "aromatase excess syndrome", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Ganirelix
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Ganirelix : De la prévention de l'ovulation prématurée à l'hypertrichose

## Résumé en Une Phrase

Le ganirelix est un antagoniste du récepteur de la GnRH, utilisé dans la stimulation ovarienne lors des traitements de fertilité pour prévenir l'ovulation prématurée.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**hypertrichose**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Prévention de l'ovulation prématurée lors de la stimulation ovarienne (source : base pharmacologique ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypertrichose |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le ganirelix est un antagoniste peptidique du récepteur GnRH1 (gène GNRHR). Il freine la sécrétion de LH et de FSH, donc la production des stéroïdes sexuels gonadiques.

Le lien avec l'hypertrichose reste **spéculatif**. Une baisse des androgènes pourrait aider dans l'hirsutisme, mais l'hypertrichose vraie est en général indépendante des androgènes et non pilotée par l'axe hypophyso-gonadique. Le score très élevé de TxGNN reflète vraisemblablement une proximité dans le graphe de connaissances (nœuds de phénotypes pileux) plutôt qu'une connexion biologique démontrée.

Les autres prédictions du top 10 sont aussi sans soutien clinique (toutes en L5). Trois méritent d'être notées comme questions de recherche, car mécanistiquement plus cohérentes :
- **Puberté précoce centrale** (score 99,75 %) : la modulation du récepteur GnRH est le principe thérapeutique établi, mais la formulation à courte durée d'action n'est pas adaptée à une suppression chronique.
- **Puberté précoce familiale limitée au sexe masculin** (99,85 %) : la maladie est périphérique (mutation activatrice du récepteur LH), le ganirelix n'agirait que sur une éventuelle composante centrale secondaire.
- **Syndrome d'excès d'aromatase** (99,80 %) : suppression hormonale adjuvante plausible, mais les inhibiteurs de l'aromatase sont l'approche directe.

Les autres prédictions (syndrome d'Ambras, malformation de Dandy-Walker, anomalies de la tige pilaire, trichomégalie familiale, circulation fœtale persistante, etc.) n'ont pas de plausibilité mécanistique identifiée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61125958 | GANIRELIX EG 0,25 mg/0,5 mL, solution injectable en seringue préremplie (annulée) | Solution injectable | Non renseignée |
| 62225235 | ORGALUTRAN 0,25 mg/0,5 mL, solution injectable (annulée) | Solution injectable | Non renseignée |
| 61462270 | FYREMADEL 0,25 mg/0,5 mL, solution injectable en seringue pré-remplie (annulée) | Solution injectable | Non renseignée |
| 62428488 | GANIRELIX THERAMEX 0,25 mg/0,5 mL, solution injectable en seringue pré-remplie (annulée) | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 6 interactions de niveau modéré sont recensées (source : DDInter) avec d'autres médicaments agissant sur l'axe gonadotrope : gonadoréline, gonadotrophine chorionique humaine, ménotropines, triptoréline, follitropine et urofollitropine.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'hypertrichose repose uniquement sur une prédiction du modèle (L5), sans essai, sans publication, et avec un lien mécanistique jugé spéculatif. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Obtenir les données détaillées sur le mécanisme d'action
- Mener une revue de littérature ciblée et rechercher des essais, en priorité pour la puberté précoce centrale, qui est l'hypothèse la plus cohérente
- Évaluer la compatibilité des voies d'administration et la pertinence d'une formulation à action prolongée pour une utilisation chronique
- Clarifier la situation réglementaire, puisque aucune AMM n'est actuellement valide en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

