---
layout: default
title: Nelarabine
parent: Prédiction du modèle uniquement (L5)
nav_order: 530
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Nelarabine : nouvelle indication prédite, Sclérose en plaques récurrente-rémittente (niveau de preuve L5). Indication d'origine : Leucémie aiguë lymphoblastique, leucémie à cellules T…"
monitor_inn: "nelarabine"
predicted_indications: ["relapsing-remitting multiple sclerosis"]
---

# Nelarabine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Nélarabine : De la leucémie aiguë lymphoblastique à la sclérose en plaques récurrente-rémittente

## Résumé en Une Phrase

La nélarabine est un analogue nucléosidique, initialement utilisé pour le traitement de la leucémie aiguë lymphoblastique à cellules T et du lymphome lymphoblastique T.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **sclérose en plaques récurrente-rémittente**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie aiguë lymphoblastique, leucémie à cellules T, lymphome lymphoblastique T (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Sclérose en plaques récurrente-rémittente |
| Score de Prédiction TxGNN | 99,43 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, la nélarabine est une prodrogue de l'ara-G, un analogue de la désoxyguanosine. Elle est convertie en ara-GTP, qui s'incorpore à l'ADN et provoque l'apoptose des lymphoblastes, avec une sélectivité particulière pour les lymphocytes T.

Un lien plausible, mais non vérifié, avec la sclérose en plaques récurrente-rémittente serait la déplétion sélective de lymphocytes pathogènes, comme pour la cladribine, un analogue de purine approuvé dans la SEP. Cette hypothèse n'est étayée par aucune donnée compilée.

Un élément va fortement à l'encontre de cette piste : la nélarabine est connue pour sa neurotoxicité importante (somnolence sévère, neuropathies, démyélinisation, syndromes de type Guillain-Barré). Son usage dans une maladie démyélinisante du système nerveux central est donc très préoccupant. Le score TxGNN (0,994) est une prédiction computationnelle et ne constitue pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66034512 | ATRIANCE 5 mg/ml, solution pour perfusion (SANDOZ PHARMACEUTICALS) | Solution pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (analogue nucléosidique/purique) |
| Risque de Myélosuppression | Élevé à moyen : le graphe de connaissances signale la neutropénie, la thrombocytopénie, l'agranulocytose et l'anémie comme contre-indications associées |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale, bilirubine, surveillance neurologique rigoureuse |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : insuffisance hépatique, épilepsie, thrombocytopénie, neutropénie, agranulocytose, maladies du système nerveux périphérique, neuropathie périphérique, anémie (dont macrocytaire), hyperbilirubinémie (dont héréditaire et syndrome de Gilbert), insuffisance rénale, troubles d'apprentissage, déficience intellectuelle, maladies démyélinisantes, polyradiculoneuropathie démyélinisante inflammatoire.
- **Interactions médicamenteuses** : 194 interactions recensées. Parmi les principales de niveau **majeur** : bupropion, déférisone (déféripone), iopamidol, iohexol, samarium (153Sm) lexidronam. Parmi les niveaux **modérés** : métronidazole, tinidazole, sécnidazole, bénznidazole, rosuvastatine, simvastatine, chloroquine, hydroxychloroquine, disulfirame, palifermine, chlorure de strontium Sr-89, lindane, picosulfate, polyéthylène glycol, sulfate de sodium.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. La neurotoxicité démyélinisante connue de la nélarabine est contraire à l'usage dans la sclérose en plaques, et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM, élément bloquant pour l'évaluation de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Évaluer par des études précliniques la plausibilité d'une déplétion lymphocytaire sélective, et la comparer à la cladribine
- Analyser en profondeur le risque neurotoxique (démyélinisation, neuropathie) au regard d'une maladie démyélinisante
- Vérifier la compatibilité de la voie d'administration et la similarité avec l'indication originale
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

