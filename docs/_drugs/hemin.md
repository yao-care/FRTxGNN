---
layout: default
title: Hemin
parent: Prédiction du modèle uniquement (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "hemin"
predicted_indications: ["thrombocytopenic purpura", "hemophilia", "C1 inhibitor deficiency", "acquired coagulation factor deficiency", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "inherited thrombophilia", "symptomatic form of hemophilia in female carriers", "hereditary von Willebrand disease", "congenital factor XI deficiency"]
description: "Hemin : nouvelle indication prédite, Purpura thrombopénique (thrombocytopenic purpura) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Hemin
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

## Hemin: Purpura thrombopénique (thrombocytopenic purpura)
{: .text-alpha }

## Résumé en Une Phrase

L'hémine est un médicament initialement utilisé pour le traitement de la porphyrie aiguë intermittente.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **purpura thrombopénique**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Purpura thrombopénique (thrombocytopenic purpura) |
| Score de Prédiction TxGNN | 0.9979 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Hemin (traduction non officielle) : « L'hème agit en limitant la synthèse hépatique et/ou médullaire de porphyrine. Cette action est probablement due à l'inhibition de la δ-aminolévulinique acide synthétase, l'enzyme qui limite la vitesse de la voie de biosynthèse des porphyrines/de l'hème. » Texte original en anglais : "Heme acts to limit the hepatic and/or marrow synthesis of porphyrin. This action is likely due to the inhibition of δ-aminolevulinic acid synthetase, the enzyme which limits the rate of the porphyrin/heme biosynthetic pathway." ([DailyMed: Panhematin (hemin) prescribing information, Recordati Rare Diseases, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9984267a-4d57-4444-9bb5-16bca7dea691), version du 2026-02-26 ; consulté le 2026-11-19). Sur la base des informations connues, l'hémine induit l'hème oxygénase-1 et freine la biosynthèse de l'hème (enzyme ALA synthase) dans la porphyrie. C'est ce qui explique son efficacité dans la porphyrie aiguë intermittente.

Aucun lien mécanistique avec le purpura thrombopénique (immunologique ou thrombotique) n'est établi dans les données compilées pour ce rapport. Le score élevé du modèle reflète probablement une proximité dans le réseau de connaissances, et non une raison pharmacologique démontrée.

L'hémine est par ailleurs connue pour des effets pro-coagulants et des effets possibles sur les plaquettes. Dans ce contexte, un bénéfice thérapeutique est mécanistiquement douteux et un risque pour la sécurité est plausible.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le purpura thrombopénique.

À titre d'information, la deuxième indication prédite (hémophilie) a ramené trois publications, mais elles concernent le givosiran ou la porphyrie hépatique aiguë, et non l'hémine dans l'hémophilie. Elles n'apportent donc aucune preuve en faveur d'une indication hors porphyrie.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 65109937 | NORMOSANG 25 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | RECORDATI RARE DISEASES | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 74 interactions ont été identifiées. Parmi celles listées :
  - **Majeures** : éthinylestradiol, estradiol, estrogènes conjugués, butalbital, amobarbital, phénobarbital.
  - **Modérées** : acide acétylsalicylique, abciximab, alteplase, anagrélide, dipyridamole, apixaban, bétrixaban, acalabrutinib, avapritinib, antithrombine III (humaine et alfa), trastuzumab emtansine, ibritumomab tiuxétan, tositumomab (I-131).
- Beaucoup de ces associations concernent l'hémostase (anticoagulants, antiagrégants, thrombolytiques). Elles sont particulièrement pertinentes pour une indication touchant les plaquettes ou la coagulation.
- Des effets pro-coagulants et une thrombophlébite ont été rapportés avec l'hémine. Un risque est plausible chez les patients présentant un trouble de la coagulation ou une thrombopénie.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique ni publication pertinente, et aucun mécanisme plausible. Les effets connus de l'hémine sur la coagulation suggèrent plutôt un risque qu'un bénéfice.
- Les données de sécurité issues de la notice sont manquantes, ce qui bloque l'évaluation de sécurité.

<!-- review:begin fr-lic-20261106-hemin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'AMM française est annulée et les données de sécurité issues de la notice sont manquantes, ce qui bloque l'évaluation de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-hemin-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Mener une revue de la littérature ciblée sur l'hémine et le purpura thrombopénique, ainsi que sur ses effets hématologiques.
- Évaluer la compatibilité de la voie d'administration (perfusion) avec l'indication visée.
- Réaliser des études précliniques sur les effets de l'hémine sur les plaquettes avant toute étude clinique.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « 'AMM française est annulée et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Panhematin (hemin) prescribing information, Recordati Rare Diseases, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9984267a-4d57-4444-9bb5-16bca7dea691) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

