---
layout: default
title: Bictegravir
parent: Preuves modérées (L3-L4)
nav_order: 107
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Bictegravir : nouvelle indication prédite, Infection par le virus de l'immunodéficience simienne (SIV) (niveau de preuve L4). Indication d'origine : Infection par le VIH, SIDA"
monitor_inn: "bictegravir"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Bictegravir
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

## Bictégravir : Du VIH/SIDA à l'Infection par le Virus de l'Immunodéficience Simienne
{: .text-alpha }

## Résumé en Une Phrase

Le bictégravir est un inhibiteur de l'intégrase du VIH-1 (INSTI), initialement utilisé pour le traitement de l'infection par le VIH et du SIDA, au sein de l'association Biktarvy.
Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection par le virus de l'immunodéficience simienne (SIV)**, mais **aucun essai clinique** n'existe et seules **3 publications** précliniques ou structurales soutiennent cette piste.
Il s'agit d'un modèle d'étude translationnel pour la recherche sur le VIH, et non d'une véritable nouvelle indication humaine.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Infection par le virus de l'immunodéficience simienne (SIV) |
| Score de Prédiction TxGNN | 99,82 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le bictégravir est un inhibiteur de transfert de brin de l'intégrase du VIH-1 (INSTI) de seconde génération, doté d'une barrière génétique élevée à la résistance. Son efficacité dans l'infection par le VIH a été établie.

L'intégrase du SIV est structurellement très proche de celle du VIH-1, de sorte qu'une liaison de l'INSTI et une activité antivirale sont plausibles sur le plan mécanistique. Une étude *in vitro* rapporte une activité antivirale du bictégravir et du cabotégravir contre des variants du SIVmac239 résistants aux INSTI. Des travaux structuraux sur les intasomes VIH/SIV expliquent la liaison des INSTI et les mécanismes d'échappement viral.

Il faut toutefois relativiser : le SIV est une maladie animale (primates non humains), sans pertinence clinique humaine directe. Le score TxGNN élevé reflète probablement la grande proximité entre le SIV et le VIH dans le graphe de connaissances plutôt qu'un signal de repositionnement réellement nouveau.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Étude *in vitro* | Antimicrobial Agents and Chemotherapy | Activité antivirale du bictégravir et du cabotégravir contre le SIVmac239 et le VIH-1 résistants aux INSTI ; barrière génétique à la résistance plus élevée que le raltégravir et l'elvitégravir |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Revue (biologie structurale) | The FEBS Journal | Structures des intasomes VIH/SIV éclairant la liaison des INSTI et les mécanismes d'échappement viral |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Étude préclinique sur modèle animal | Frontiers in Immunology | Modèle de souris humanisée à double usage pour tester des stratégies antivirales contre le SIV et le VIH |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62844771 | BIKTARVY 50 mg/200 mg/25 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 60246298 | BIKTARVY 30 mg/120 mg/15 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 81 interactions sont recensées. Parmi les principales :
  - **Majeures** : antiacides et sels polyvalents (hydroxyde d'aluminium, attapulgite, kaolin, magaldrate, carbonate/chlorure/citrate de magnésium), sels de calcium (acétate, carbonate, citrate, glubionate, gluconate, lactate, phosphate) et fer. Ces cations polyvalents peuvent réduire l'absorption des INSTI.
  - **Modérées** : aprépitant, clarithromycine, dexaméthasone, éliglustat, phénylbutyrate de glycérol.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à des études *in vitro*, structurales et sur modèle animal, sans aucun essai clinique. Le SIV étant une maladie animale, cette piste a surtout une valeur de modèle de recherche et non de nouvelle indication humaine. Par ailleurs, les deux AMM françaises sont annulées.
- Les deux autres prédictions (sida félin, score identique de 99,82 %, et un trouble neurodéveloppemental rare, score de 99,76 %) ne s'appuient sur aucune preuve ni lien mécanistique plausible, et sont probablement des artefacts du graphe de connaissances.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (mises en garde et contre-indications), actuellement manquante et bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action
- Clarifier le statut réglementaire en France (AMM annulées) et le texte d'indication associé
- Définir si l'objectif est un usage comme modèle de recherche translationnelle (SIV/VIH) plutôt qu'une indication clinique
- Étudier, si pertinent, des données *in vivo* chez le primate non humain
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

