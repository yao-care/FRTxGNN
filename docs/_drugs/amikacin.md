---
layout: default
title: Amikacin
parent: Prédiction du modèle uniquement (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
monitor_inn: "amikacin"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "meningococcemia"]
last_modified_at: 2026-11-24
description: "Amikacin : nouvelle indication prédite, Fièvre paratyphoïde (paratyphoid fever) (niveau de preuve L5). En France, AMM dans la BDPM : 7 (valides : 7)"
---

# Amikacin
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

## Amikacine : aminoside antibactérien → fièvre paratyphoïde (paratyphoid fever)
{: .text-alpha }

## Resume en Une Phrase

L'amikacine est un antibiotique de la famille des aminosides, actif sur les bactéries à Gram négatif.
Le modèle TxGNN prédit qu'elle pourrait être utile pour la **fièvre paratyphoïde (paratyphoid fever)**,
mais les données compilées ne contiennent **aucun essai clinique** et **8 publications**, toutes indirectes (surveillance, antibiogrammes, cas isolés).

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Predite | Fièvre paratyphoïde (paratyphoid fever) |
| Score de Prediction TxGNN | 0,9982 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 7) |
| Nombre d'AMM | 7 (valides : 7) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Amikacin (traduction non officielle) : « L'amikacine, un aminoside, se lie au ribosome procaryote, inhibant la synthèse protéique chez les bactéries sensibles. Elle est bactéricide in vitro vis-à-vis des bactéries à Gram positif et à Gram négatif. » Texte original en anglais : "Amikacin, an aminoglycoside, binds to the prokaryotic ribosome, inhibiting protein synthesis in susceptible bacteria. It is bactericidal in vitro against Gram-positive and Gram-negative bacteria." ([DailyMed: amikacin sulfate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f260ff2a-76a0-4672-9516-91c344b67890), version du 2026-07-27 ; consulté le 2026-11-19). D'après les connaissances générales, l'amikacine est un aminoside actif in vitro sur les entérobactéries à Gram négatif, dont Salmonella.

Le lien mécanistique reste toutefois fragile. Salmonella Paratyphi est un pathogène à localisation intracellulaire, or les aminosides pénètrent mal dans les cellules. Ils ne sont pas recommandés comme traitement cliniquement efficace de la fièvre entérique. Le lien est donc plausible in vitro seulement.

Le score élevé du modèle traduit une proximité avec d'autres infections bactériennes à Gram négatif, mais il ne remplace pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune des publications ci-dessous n'étudie directement l'efficacité de l'amikacine dans la fièvre paratyphoïde. Elles portent sur l'épidémiologie, la sensibilité aux antibiotiques ou des cas isolés. Le niveau de preuve est donc plafonné à L5.

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Cohorte prospective | J Indian Med Assoc | 145 cas d'hémoculture positive chez l'enfant ; profil clinique et sensibilité de S. typhi et S. paratyphi |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Rapport de cas | Pediatr Hematol Oncol | Cholécystite alithiasique à S. paratyphi B chez un enfant leucémique, traitée avec céfépime, amikacine et G-CSF |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Observation clinique | Mikrobiyol Bul | 48 patients avec infection à paratyphi B résistante aux traitements classiques ; antibiogrammes et résultats |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Observationnel (antibiogramme) | Med J Armed Forces India | Sensibilité in vitro de S. typhi et S. paratyphi A, avec réapparition de la sensibilité au chloramphénicol |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | Surveillance | Indian J Pathol Microbiol | Souches de S. typhi multirésistantes restant sensibles aux aminosides et à la ciprofloxacine |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Étude d'isolement microbiologique | Pak J Biol Sci | Isolement de S. paratyphi chez des patients atteints de fièvre entérique à Quetta |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Épidémiologie | New Microbiol | Fréquence de S. typhi et S. paratyphi en Jordanie, 1988-2000 |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Surveillance (antibiogramme) | JNMA | Isolats d'hémocultures et profils de sensibilité dans un hôpital universitaire |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 63408093 | AMIKACINE PANPHARMA 250 mg/mL | Solution injectable | Non renseignée |
| 68502148 | AMIKACINE VIATRIS 500 mg | Poudre pour solution injectable | Non renseignée |
| 65156805 | ARIKAYCE LIPOSOMAL 590 mg | Dispersion pour inhalation par nébuliseur | Non renseignée |
| 62000612 | AMIKACINE VIATRIS 50 mg/1 mL | Solution injectable | Non renseignée |
| 62516778 | AMIKACINE VIATRIS 1 g | Poudre pour solution injectable en flacon | Non renseignée |

## Considerations de Securite

- **Interactions médicamenteuses** : 212 interactions ont été recensées. Les plus sévères (niveau majeur) concernent le **sulfate de magnésium** et le **mannitol**. Des interactions de niveau modéré concernent notamment l'amphotéricine B (toutes formes), la kanamycine, la néomycine, l'acide acétylsalicylique, la mésalazine, l'exénatide et plusieurs inhibiteurs de la pompe à protons (oméprazole, ésoméprazole, lansoprazole, pantoprazole, rabéprazole).

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Aucun essai clinique n'existe et la littérature disponible est indirecte (antibiogrammes, épidémiologie, cas isolés). Le mécanisme est limité par la faible pénétration intracellulaire des aminosides, et les traitements établis (fluoroquinolones, azithromycine, céphalosporines de 3e génération) sont préférés.

**Pour avancer, les elements suivants sont necessaires :**
- Des données cliniques comparatives directes sur l'amikacine dans la fièvre paratyphoïde
- Les données sur le mécanisme d'action et le texte officiel de la notice (mises en garde, contre-indications)
- Une évaluation du profil de sécurité (toxicité rénale et auditive) dans cette population
- Une évaluation de la pertinence face aux traitements de référence

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: amikacin sulfate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f260ff2a-76a0-4672-9516-91c344b67890) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

