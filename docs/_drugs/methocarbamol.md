---
layout: default
title: Methocarbamol
parent: Prédiction du modèle uniquement (L5)
nav_order: 486
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methocarbamol : nouvelle indication prédite, Syndrome de la queue de cheval (niveau de preuve L5). Indication d'origine : Non précisée dans les données d'AMM compilées (texte d'indication vid…"
monitor_inn: "methocarbamol"
predicted_indications: ["cauda equina syndrome", "irritable bowel syndrome", "panuveitis (disease)", "anaphylaxis", "iris disease", "uveitis", "ventricular tachycardia", "food-dependent exercise-induced anaphylaxis", "conjunctivitis", "obsolete bundle branch block"]
---

# Methocarbamol
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

## Méthocarbamol : D'un myorelaxant central au syndrome de la queue de cheval
{: .text-alpha }

## Résumé en Une Phrase

Le méthocarbamol est un myorelaxant à action centrale, utilisé classiquement pour soulager les spasmes musculaires douloureux. Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la queue de cheval**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM compilées (texte d'indication vide) |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval |
| Score de Prédiction TxGNN | 0,9998 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le méthocarbamol est un myorelaxant à action centrale dont le mécanisme exact reste mal défini ; on lui attribue une action par dépression du système nerveux central.

Le lien avec le syndrome de la queue de cheval est très spéculatif. Il s'agit d'une urgence neurologique compressive qui nécessite une décompression chirurgicale. Au mieux, la myorelaxation pourrait soulager de façon symptomatique les spasmes dorsaux associés, sans agir sur la cause de la maladie. Le score élevé du modèle ne repose sur aucune donnée clinique.

Les autres prédictions du modèle (syndrome de l'intestin irritable, panuvéite, anaphylaxie, uvéite, etc.) sont également sans soutien clinique. Pour l'anaphylaxie, les deux publications retrouvées ne soutiennent pas un usage thérapeutique : elles traitent de la prise en charge générale des piqûres d'arthropodes et du profil d'effets indésirables des myorelaxants centraux.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le syndrome de la queue de cheval.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60665015 | METHOCARBAMOL ARROW 500 mg, comprimé pelliculé (statut : active) | Comprimé pelliculé | Non précisée |
| 67212035 | LUMIRELAX 500 mg, comprimé (statut : active) | Comprimé | Non précisée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe PrimeKG, et non texte de la notice) : épilepsie, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, thrombocytopénie, purpura thrombopénique, ulcère gastroduodénal (y compris actif), gastrite, goutte, abus/dépendance aux substances, hémophilie, anémie (y compris macrocytaire), déficit congénital en prothrombine, maladie hémorragique par carence en vitamine K, maladie de von Willebrand, polype nasal, syndrome de Reye, maladie d'Alzheimer, maladie de Pick, dégénérescence cérébelleuse.
- **Interactions médicamenteuses** : 126 interactions recensées. Les principales, de niveau majeur, concernent la morphine (y compris sa forme liposomale). Des interactions de niveau modéré sont signalées avec le dronabinol, la nabilone, le métoclopramide, l'opium et la sibutramine ; ces associations relèvent d'une addition d'effets sédatifs centraux.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, avec un mécanisme plausible très faible. Par ailleurs, le médicament est commercialisé en France, avec 2 AMM valides sur 2, et la notice de sécurité est manquante, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice officielle (ANSM) : mises en garde et contre-indications
- Données détaillées sur le mécanisme d'action (par ex. via DrugBank)
- Revue de la littérature ciblée sur le méthocarbamol et les atteintes radiculaires ou spasmes associés à la queue de cheval
- Clarification de l'indication d'origine et de la situation réglementaire (AMM annulées)
- Si une piste est retenue, étude préclinique ou pilote avant tout essai clinique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

