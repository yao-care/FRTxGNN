---
layout: default
title: Cefoxitin
parent: Prédiction du modèle uniquement (L5)
nav_order: 147
evidence_level: L5
indication_count: 8
monitor_inn: "cefoxitin"
predicted_indications: ["infectious otitis media", "chronic otitis media", "suppurative otitis media", "middle ear disease", "Ureaplasma urethritis", "toxocariasis", "otosalpingitis", "non-suppurative otitis media"]
last_modified_at: 2026-11-03
description: "Cefoxitin : nouvelle indication prédite, Otite moyenne infectieuse (infectious otitis media) (niveau de preuve L5). En France, AMM dans la BDPM : 4 (valides : 4)"
---

# Cefoxitin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Céfoxitine : céphamycine de deuxième génération (inhibiteur de la synthèse de la paroi bactérienne) → otite moyenne infectieuse (infectious otitis media)
{: .text-alpha }

## Résumé en Une Phrase

La céfoxitine est une céphamycine de deuxième génération, antibiotique injectable à large spectre.
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**otite moyenne infectieuse (infectious otitis media)**.
Aucun essai clinique n'est enregistré pour cette indication, et une seule publication est liée : une revue générale sur le SARM, qui ne teste pas la céfoxitine comme traitement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Otite moyenne infectieuse (infectious otitis media) |
| Score de Prédiction TxGNN | 0,9930 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Cefoxitin (traduction non officielle) : « La céfoxitine est un médicament antibactérien. […] La céfoxitine est un agent bactéricide qui agit par inhibition de la synthèse de la paroi cellulaire bactérienne. La céfoxitine est active en présence de certaines bêta-lactamases, à la fois pénicillinases et céphalosporinases, des bactéries à Gram négatif et à Gram positif. » Texte original en anglais : "Cefoxitin is an antibacterial drug. […] Cefoxitin is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Cefoxitin has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: Cefoxitin And Dextrose (cefoxitin sodium) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6c7e9485-1ede-411c-8c46-911439332864), version du 2019-07-29 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, la céfoxitine inhibe la synthèse de la paroi bactérienne et résiste à de nombreuses bêtalactamases. Son spectre couvre notamment *S. aureus*, *E. coli* et des anaérobies, germes pouvant être retrouvés dans les otites moyennes.

Cependant, le lien reste purement théorique. La seule publication associée est une revue sur le SARM (*Staphylococcus aureus* résistant à la méticilline) mentionnant l'otite moyenne parmi les infections qu'il provoque. Elle n'évalue pas la céfoxitine en traitement : la céfoxitine y est surtout connue comme marqueur de laboratoire pour détecter le SARM. Le score élevé du modèle est une simple prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Revue | Infection and Drug Resistance | Revue sur l'épidémiologie, la virulence et la résistance du SARM, citant l'otite moyenne parmi ses infections ; aucune évaluation clinique de la céfoxitine |

Cette publication ne porte pas directement sur l'efficacité de la céfoxitine dans l'otite moyenne : c'est pourquoi le niveau de preuve est plafonné à L5.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60329598 | CEFOXITINE SUBSTIPHARM 1 g | Poudre pour solution injectable | Non renseignée |
| 69084488 | CEFOXITINE PANPHARMA 1 g (IV) | Poudre pour solution injectable | Non renseignée |
| 60580134 | CEFOXITINE SUBSTIPHARM 2 g | Poudre pour solution injectable | Non renseignée |
| 67355243 | CEFOXITINE PANPHARMA 2 g (IV) | Poudre pour solution injectable | Non renseignée |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 35 interactions recensées. Parmi celles de niveau modéré : kanamycine, néomycine, streptomycine (aminosides), acide picosulfurique et dicoumarol. Une interaction mineure est signalée avec l'héparine. Plusieurs autres (vancomycine, métronidazole, clarithromycine, oméprazole, etc.) ont un niveau non précisé.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucun essai clinique ni étude directe ne soutient la céfoxitine dans l'otite moyenne infectieuse ; la prédiction repose uniquement sur le modèle (L5). Par ailleurs, des pathogènes fréquents des otites chroniques, comme *Pseudomonas*, sont naturellement résistants à la céfoxitine.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études cliniques ou observationnelles évaluant la céfoxitine dans l'otite moyenne
- Données de sensibilité des germes d'otite à la céfoxitine
- Mises en garde et contre-indications issues de la notice (ANSM)
- Données détaillées sur le mécanisme d'action

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Cefoxitin And Dextrose (cefoxitin sodium) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6c7e9485-1ede-411c-8c46-911439332864) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

