---
layout: default
title: Rocuronium
parent: Prédiction du modèle uniquement (L5)
nav_order: 677
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Rocuronium : nouvelle indication prédite, Migraine (migraine disorder) (niveau de preuve L5). Indication d'origine : Non disponible dans les données compilées"
monitor_inn: "ROCURONIUM"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "sciatic neuropathy", "headache disorder"]
---

# Rocuronium
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

## Rocuronium : Du Bloc Neuromusculaire à la Migraine (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

Les données compilées pour ce rapport ne précisent pas l'indication d'origine du rocuronium. Il s'agit d'un myorelaxant non dépolarisant, utilisé en anesthésie.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **migraine** (*migraine disorder*), mais cette prédiction repose uniquement sur le modèle : **1 essai clinique** (pharmacocinétique pédiatrique, non pertinent pour l'efficacité) et **aucune publication** ne la soutiennent.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans les données compilées |
| Nouvelle Indication Prédite | Migraine (*migraine disorder*) |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base compilée. D'après les connaissances pharmacologiques générales, le rocuronium est un myorelaxant non dépolarisant : il agit comme antagoniste compétitif des récepteurs nicotiniques de l'acétylcholine à la jonction neuromusculaire.

Aucun mécanisme établi ne relie cette action à la physiopathologie de la migraine (CGRP, activation trigémino-vasculaire, dépression corticale envahissante). Le score élevé du modèle est très probablement un artefact du graphe de connaissances. La toxine botulique, qui réduit aussi la transmission neuromusculaire et s'utilise dans la migraine chronique, agit par un autre mécanisme (inhibition de la libération présynaptique, modulation des nocicepteurs périphériques) : l'analogie est donc faible.

Les autres prédictions du modèle (migraine avec aura du tronc cérébral, syndrome de la queue de cheval, susceptibilité génétique à la migraine, atrophodermie vermiculée, uléryhtème ophryogène, vessie neurogène « obsolète », syndrome de l'intestin irritable, neuropathie sciatique, céphalées) ne disposent d'aucune justification mécanistique ni d'aucune preuve clinique solide. La plupart découlent de la proximité de nœuds dans le graphe.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Terminé | 3520 | Étude de pharmacocinétique de médicaments peu étudiés chez l'enfant, administrés selon les soins courants. Non conçue pour évaluer l'efficacité dans la migraine ; lien jugé incidentel (pertinence : C). |

## Preuves de la Littérature

Aucune littérature associée à la migraine n'est disponible actuellement.

Pour la prédiction « céphalées » (rang 10), deux publications indirectes existent, sans valeur démonstrative d'efficacité :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23812022](https://pubmed.ncbi.nlm.nih.gov/23812022/) | 2014 | Étude clinique | J ECT | Comparaison succinylcholine vs rocuronium-sugammadex sur les myalgies et céphalées après électroconvulsivothérapie : la céphalée y est un effet périprocédural, pas une cible thérapeutique. |
| [24196089](https://pubmed.ncbi.nlm.nih.gov/24196089/) | 2013 | Cas clinique | Pediatr Emerg Care | Intubation en séquence rapide chez un enfant à risque d'aspiration avec pression intracrânienne élevée ; sans rapport avec un effet antimigraineux. |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 73 interactions recensées. Parmi celles listées :
  - **Majeures** : paromomycine, kanamycine, néomycine (potentialisation du bloc neuromusculaire par les aminosides).
  - **Modérées** : doxycycline, tétracycline, minocycline, vancomycine, sulfate et chlorure de magnésium, mannitol, métoclopramide, amphotéricine B (y compris complexe lipidique), néomycine topique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, prednisone).
  - **Mineure** : ranitidine.

Veuillez consulter la notice pour les mises en garde et contre-indications, non disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai pertinent, aucune publication, aucun mécanisme plausible. Le médicament n'est pas commercialisé en France (0 AMM). Un myorelaxant systémique entraînant une paralysie respiratoire est difficilement envisageable pour une pathologie chronique comme la migraine.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications), qui bloque actuellement le criblage de sécurité.
- Obtenir les données sur le mécanisme d'action et l'indication d'origine.
- Démontrer un mécanisme plausible reliant le bloc nicotinique à la migraine, puis des études précliniques.
- Évaluer la compatibilité des voies d'administration (analyse non encore réalisée).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

