---
layout: default
title: Abacavir
parent: Preuves modérées (L3-L4)
nav_order: 11
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Abacavir : nouvelle indication prédite, Infection par le virus de l'immunodéficience simienne (niveau de preuve L4). Indication d'origine : Infection par le VIH, SIDA"
monitor_inn: "ABACAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Abacavir
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

# Abacavir : Du VIH/SIDA à l'Infection par le Virus de l'Immunodéficience Simienne

## Résumé en Une Phrase

Abacavir est un inhibiteur nucléosidique de la transcriptase inverse, initialement utilisé pour le traitement de l'infection par le VIH et du SIDA.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le virus de l'immunodéficience simienne (SIV)**, mais **aucun essai clinique** et seulement **1 publication** (étude in vitro) soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Infection par le virus de l'immunodéficience simienne |
| Score de Prédiction TxGNN | 99,79 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 9 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, l'abacavir est un inhibiteur nucléosidique de la transcriptase inverse (INTI) : il est converti dans la cellule en carbovir triphosphate, qui interrompt l'élongation de l'ADN viral.

Le SIV est un lentivirus étroitement apparenté au VIH et utilise une transcriptase inverse homologue. La plausibilité mécanistique est donc élevée. Toutefois, il s'agit essentiellement d'une extension de l'indication antirétrovirale d'origine à un lentivirus non humain, et non d'une véritable nouvelle opportunité thérapeutique.

Le score élevé du modèle (99,79 %) reflète vraisemblablement la proximité avec le VIH. La pertinence clinique pour un repositionnement chez l'humain est minimale, car l'infection par le SIV n'est pas une maladie humaine.

### Autres prédictions du modèle

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|------|
| 2 | Syndrome d'immunodéficience acquise féline (FIV) | 99,79 % | L4 | Indication vétérinaire ; une seule étude in vitro en association (zidovudine + lamivudine + abacavir), qui ne permet pas d'isoler la contribution de l'abacavir |
| 3 | Trouble neurodéveloppemental avec démarche ataxique, absence de langage et diminution de la substance blanche corticale | 99,78 % | L5 | Aucun lien mécanistique établi ; possible artefact du graphe de connaissances ; hypothèses spéculatives |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Étude de sensibilité in vitro | Antiviral Therapy | Évaluation de l'activité antivirale de 16 médicaments approuvés et d'un médicament expérimental (AMD3100) contre des souches de VIH-2, de SIV et de SHIV ; soutien préclinique indirect uniquement |

## Informations de Marché en France

Toutes les AMM listées ci-dessous sont annulées ; le texte d'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 63797011 | ABACAVIR SANDOZ 300 mg | Comprimé pelliculé sécable | Annulée |
| 62070450 | ZIAGEN 20 mg/ml | Solution buvable | Annulée |
| 62401060 | ABACAVIR VIATRIS 300 mg | Comprimé pelliculé sécable | Annulée |
| 68556562 | ZIAGEN 300 mg | Comprimé pelliculé sécable | Annulée |
| 69855489 | KIVEXA 600 mg/300 mg | Comprimé pelliculé | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : insuffisance hépatique, maladie hépatique, stéatose hépatique et stéatohépatite non alcoolique, maladie rénale, pancréatite, maladie de la vésicule biliaire, myopathie et maladies musculaires (y compris myosite et dermatomyosite), paralysie périodique familiale, neutropénie, agranulocytose, anémie (dont macrocytaire), hypertriglycéridémie, obésité, acidose lactique.
- **Hypersensibilité** : l'abacavir est connu pour le risque de réaction d'hypersensibilité associé à l'allèle HLA-B*57:01.
- **Interactions médicamenteuses** : 93 interactions recensées. Les plus notables, de niveau modéré, concernent la naltrexone et l'orlistat. Les autres interactions listées (par exemple metformine, morphine, prednisone, oméprazole, vancomycine) ont un niveau de gravité non déterminé.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle et sur une étude in vitro unique ; il n'existe aucun essai clinique, et l'indication visée (SIV) est une infection animale, sans intérêt thérapeutique humain direct. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (ANSM), actuellement manquantes et bloquantes pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Préciser si l'objectif est de valider le SIV/FIV comme modèle préclinique ou de rechercher une véritable indication humaine nouvelle
- Pour la prédiction de trouble neurodéveloppemental rare : établir au préalable un lien mécanistique crédible avant toute étude, en tenant compte de la toxicité connue (hypersensibilité HLA-B*57:01) et du nombre élevé d'interactions
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

