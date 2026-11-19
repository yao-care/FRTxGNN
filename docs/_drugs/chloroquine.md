---
layout: default
title: Chloroquine
parent: Prédiction du modèle uniquement (L5)
nav_order: 163
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-29
description: "Chloroquine : nouvelle indication prédite, Arthrite juvénile idiopathique polyarticulaire à facteur rhumatoïde positif (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, lupus érythéma…"
monitor_inn: "chloroquine"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis"]
---

# Chloroquine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Chloroquine : Du Paludisme et de la Polyarthrite Rhumatoïde à l'Arthrite Juvénile Idiopathique Polyarticulaire à Facteur Rhumatoïde Positif
{: .text-alpha }

## Résumé en Une Phrase

La chloroquine est un antipaludique, également utilisé dans la polyarthrite rhumatoïde et le lupus érythémateux.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**arthrite juvénile idiopathique polyarticulaire à facteur rhumatoïde positif**,
mais **aucun essai clinique** n'est enregistré et une seule publication (une cohorte portant sur un autre médicament, le léflunomide) est associée à cette prédiction : il s'agit donc d'une hypothèse reposant essentiellement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, lupus érythémateux systémique, paludisme (à *P. vivax*, *P. falciparum*, *P. ovale*, *P. malariae*), lupus discoïde et cutané chronique |
| Nouvelle Indication Prédite | Arthrite juvénile idiopathique polyarticulaire à facteur rhumatoïde positif |
| Score de Prédiction TxGNN | 0,9941 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé (aucune autorisation enregistrée) |
| Nombre d'AMM | 0 (valides : 0) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Chloroquine (traduction non officielle) : « La chloroquine, une 4-aminoquinoléine, est un agent antiprotozoaire. Le mécanisme précis par lequel la chloroquine exerce son activité n'est pas connu. La chloroquine pourrait exercer son effet contre les espèces de Plasmodium en se concentrant dans les vésicules acides du parasite et en inhibant la polymérisation de l'hème. » Texte original en anglais : "Chloroquine, a 4-aminoquinoline, is an anti-protozoal agent. The precise mechanism by which chloroquine exhibits activity is not known. Chloroquine, may exert its effect against Plasmodium species by concentrating in the acid vesicles of the parasite and by inhibiting polymerization of heme." ([DailyMed: chloroquine phosphate prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=06c69e2b-211b-4746-9f3a-f86d36520570), version du 2026-10-21 ; consulté le 2026-11-19). Sur la base des informations connues, la chloroquine appartient à la classe des antipaludiques de la famille des 4-aminoquinoléines. Son efficacité dans la polyarthrite rhumatoïde et le lupus est établie, et elle pourrait mécanistiquement être applicable à la nouvelle indication.

Ses effets immunomodulateurs (inhibition de la fonction lysosomale, réduction de la présentation antigénique, diminution de la signalisation des cytokines pro-inflammatoires) constituent un lien plausible avec l'arthrite juvénile idiopathique polyarticulaire à facteur rhumatoïde positif, qui ressemble à la polyarthrite rhumatoïde de l'adulte.

Cependant, ce score élevé reste une prédiction du modèle : aucune donnée clinique spécifique à la chloroquine n'a été fournie pour cette indication.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohorte | The Journal of Rheumatology | Description de l'expérience clinique prospective à long terme du léflunomide dans l'arthrite juvénile idiopathique (ne concerne pas la chloroquine) |

---

## Informations de Marché en France

Aucune AMM n'est enregistrée en France pour ce médicament (non commercialisé).

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : épilepsie, porphyries, maladie hépatique, maladie de la vésicule biliaire, maladies oculaires (dont rétinopathie, rétinite, scotome, troubles de la vision, cécité), troubles de l'audition, psoriasis, neutropénie, agranulocytose, leucopénie, anémie, déficit en G6PD, glycogénose, cystinurie, galactosémie, abus de substances/dépendance.
- **Interactions médicamenteuses** : 467 interactions recensées. Parmi les principales, des interactions **majeures** avec l'agalsidase bêta, le bupropion, le cisapride, la clarithromycine, le dolasétron et le granisétron ; des interactions **modérées** avec notamment la famotidine, le lopéramide, l'aprépitant, le métronidazole, la cimétidine, les antiacides (hydroxyde d'aluminium, carbonate de calcium), les sulfamides hypoglycémiants (glimépiride, glipizide, glibenclamide) et l'insuline humaine.

Les mises en garde et contre-indications figurant dans la notice n'ont pas pu être consultées ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique, et la seule publication associée concerne un autre médicament. Le médicament n'est pas commercialisé dans ce pays (non commercialisé) et les données de sécurité issues de la notice sont manquantes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice de l'ANSM (mises en garde, contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Rechercher des données cliniques spécifiques à la chloroquine dans l'arthrite juvénile idiopathique, notamment pédiatriques
- Évaluer la place de la chloroquine face aux traitements actuels (DMARD, biothérapies)
- Réaliser une revue de sécurité ciblée : toxicité rétinienne, effets cardiaques (QT/conduction, un cas de bloc auriculo-ventriculaire de 3e degré rapporté), et gestion des 467 interactions médicamenteuses

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: chloroquine phosphate prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=06c69e2b-211b-4746-9f3a-f86d36520570) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

