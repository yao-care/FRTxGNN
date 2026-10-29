---
layout: default
title: Efavirenz
parent: Prédiction du modèle uniquement (L5)
nav_order: 270
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-29
monitor_inn: "efavirenz"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Efavirenz : nouvelle indication prédite, Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome) (niveau de preuve L5). Indication d'origine : Non renseignée dans les d…"
---

# Efavirenz
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Efavirenz: Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Résumé en Une Phrase

Efavirenz est un inhibiteur non nucléosidique de la transcriptase inverse, initialement utilisé pour le traitement de l'infection par le VIH et du SIDA.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'immunodéficience acquise féline**, mais aucun essai clinique n'est enregistré et une seule publication préclinique (étude biochimique et structurale in vitro) soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome) |
| Score de Prédiction TxGNN | 0.9980 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 13) |
| Nombre d'AMM | 13 (valides : 10) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'efavirenz fait partie de la classe des inhibiteurs non nucléosidiques de la transcriptase inverse (INNTI), actifs contre la transcriptase inverse du VIH-1. Son efficacité dans l'infection par le VIH est établie.

Le virus de l'immunodéficience féline (FIV) est un lentivirus apparenté au VIH, ce qui explique le score élevé du modèle. Toutefois, sa transcriptase inverse diffère structurellement de celle du VIH-1. Les INNTI sont généralement peu actifs contre les transcriptases inverses de lentivirus autres que le VIH-1, et l'efavirenz ne devrait donc pas être un inhibiteur puissant du FIV. La seule étude disponible (2023) compare des INNTI (névirapine, efavirenz, rilpivirine) sur les plans biochimique et structural contre le FIV et le VIH : il s'agit d'une preuve préclinique indirecte.

Cette indication est en outre vétérinaire, ce qui limite sa pertinence pour le repositionnement chez l'humain.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Étude biochimique/structurale in vitro | Journal of Veterinary Science | Comparaison de la névirapine, de l'efavirenz et de la rilpivirine contre les transcriptases inverses du FIV et du VIH, afin d'évaluer le potentiel des INNTI contre le FIV. Aucun traitement efficace n'existe actuellement pour les chats infectés. |

### Note sur la deuxième prédiction (infection par le virus de l'immunodéficience simienne)

Une deuxième prédiction (score identique, 0,9980) concerne l'infection par le virus de l'immunodéficience simienne, avec 14 publications, essentiellement des études sur le macaque. Ces travaux utilisent le virus chimérique RT-SHIV, qui porte la transcriptase inverse du VIH-1, car le SIV sauvage est naturellement résistant aux INNTI. Il s'agit donc de preuves animales relevant de l'indication VIH d'origine, et non d'une indication nouvelle indépendante. Cette prédiction relève aussi du niveau L4 et de la décision Hold.

### Note sur la troisième prédiction

Un trouble neurodéveloppemental (ataxie, absence de parole, diminution de la substance blanche corticale) est prédit avec un score de 0,9977, sans essai clinique ni littérature (niveau L5, Hold). Aucun lien mécanistique n'est établi dans les données compilées. Les effets indésirables neuropsychiatriques connus de l'efavirenz constituent une préoccupation supplémentaire en population pédiatrique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68039999 | EFAVIRENZ VIATRIS 600 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |
| 65716353 | EFAVIRENZ ARROW 600 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |
| 62728717 | EFAVIRENZ SANDOZ 600 mg, comprimé pelliculé sécable | Comprimé pelliculé sécable | Non renseignée (AMM active) |
| 62130958 | EFAVIRENZ TEVA 600 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |
| 61004700 | EFAVIRENZ/EMTRICITABINE/TENOFOVIR DISOPROXIL KRKA 600 mg/200 mg/245 mg | Comprimé pelliculé | Non renseignée (AMM active) |


## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique, maladie hépatique, stéatose hépatique et stéatohépatite non alcoolique, hépatites virales B et C chroniques, épilepsie, troubles anxieux, troubles névrotiques, trouble dysthymique, trouble délirant, schizophrénie paranoïde, maladie rénale, syndrome de Fanconi, acidose lactique, hypertriglycéridémie, obésité, hypophosphatémie, ostéomalacie, rachitisme, maladie de la vésicule biliaire.
- **Interactions médicamenteuses** : 330 interactions recensées. Parmi les exemples : dolasétron (majeure) ; acarbose, famotidine, rabéprazole, hydrocortisone, pioglitazone, lopéramide, bupropion, aprépitant, dexaméthasone, clarithromycine, saxagliptine, dronabinol, minocycline (modérées).

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à une étude préclinique in vitro pour une indication vétérinaire, sans essai clinique. Le score TxGNN élevé reflète probablement la proximité avec le mécanisme anti-VIH plutôt qu'une efficacité réelle contre le FIV, et le médicament ne dispose plus d'AMM valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA) et analyse du lien mécanistique avec le FIV
- Mises en garde et contre-indications officielles issues de la notice (ANSM)
- Études in vivo chez le chat et évaluation de la pertinence vétérinaire par rapport à l'objectif de repositionnement
- Clarification du statut réglementaire (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

