---
layout: default
title: Cefazolin
parent: Prédiction du modèle uniquement (L5)
nav_order: 146
evidence_level: L5
indication_count: 8
monitor_inn: "cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
last_modified_at: 2026-11-24
description: "Cefazolin : nouvelle indication prédite, Otite moyenne infectieuse (infectious otitis media) (niveau de preuve L5). En France, AMM dans la BDPM : 10 (valides : 10)"
---

# Cefazolin
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

## Céfazoline : antibiotique céphalosporine de première génération → Otite moyenne infectieuse (infectious otitis media)
{: .text-alpha }

## Résumé en Une Phrase

La céfazoline est une céphalosporine de première génération, antibiotique qui bloque la synthèse de la paroi des bactéries.
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**otite moyenne infectieuse (infectious otitis media)**,
mais aucun essai clinique n'est enregistré et les **2 publications** retrouvées sont indirectes (un rapport de cas pédiatrique d'association d'antibiotiques et une revue hors sujet).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Otite moyenne infectieuse (infectious otitis media) |
| Score de Prédiction TxGNN | 0,9944 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 10) |
| Nombre d'AMM | 10 (valides : 10) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Cefazolin (traduction non officielle) : « La céfazoline est un médicament antibactérien. […] La céfazoline est un agent bactéricide qui agit par inhibition de la synthèse de la paroi cellulaire bactérienne. » Texte original en anglais : "Cefazolin is an antibacterial drug. […] Cefazolin is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis." ([DailyMed: Cefazolin (cefazolin sodium) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d91a8d13-99a0-4d87-88dc-71cbd37922b4), version du 2026-08-31 ; consulté le 2026-11-19). D'après les connaissances générales, la céfazoline inhibe la synthèse de la paroi bactérienne et agit sur les bactéries à Gram positif, notamment les streptocoques et les staphylocoques sensibles à la méticilline. Ces germes peuvent être impliqués dans l'otite moyenne, ce qui rend le lien biologiquement plausible.

Des limites importantes existent : la céfazoline s'administre uniquement par voie injectable et son activité est limitée contre *Haemophilus influenzae* et *Moraxella catarrhalis*, deux agents majeurs de l'otite moyenne. Le score élevé du modèle reflète une proximité statistique avec d'autres maladies infectieuses traitées par ce médicament, et non une démonstration clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Rapport de cas | Annals of Otology, Rhinology, and Laryngology | Syndrome de Gradenigo pédiatrique (complication d'otite moyenne aiguë) traité empiriquement par l'association ceftazidime-céfazoline ; la contribution propre de la céfazoline ne peut pas être isolée |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revue | Clinical Pharmacy | Prise en charge du syndrome de Stevens-Johnson ; l'otite moyenne n'apparaît qu'en contexte, article hors sujet |

Aucune de ces publications n'étudie directement la céfazoline comme traitement de l'otite moyenne infectieuse : le niveau de preuve reste donc L5.

## Informations de Marché en France

La céfazoline est commercialisée en France. Les données compilées pour ce rapport recensent 10 autorisations de mise sur le marché pour des produits à base de céfazoline seule, sous forme de poudre pour solution injectable ou pour perfusion (voies IM/IV).

<!-- review:begin fr-lic-20261124-cefazolin-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « recensent 8 autorisations de mise sur le marché » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-cefazolin-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67948546 | CEFAZOLINE VIATRIS 2 g, poudre pour solution injectable (IM-IV) | Poudre pour solution injectable | VIATRIS SANTE | Active |
| 67504598 | CEFAZOLINE QILU 1 g, poudre pour solution injectable/pour perfusion | Poudre pour solution injectable ou pour perfusion | QILU PHARMA SPAIN (ESPAGNE) | Active |
| 61876894 | CEFAZOLINE PANPHARMA 1 g, poudre pour solution injectable/pour perfusion | Poudre pour solution injectable ou pour perfusion | PANPHARMA | Active |
| 69312237 | CEFAZOLINE QILU 2 g, poudre pour solution injectable/pour perfusion | Poudre pour solution injectable ou pour perfusion | QILU PHARMA SPAIN (ESPAGNE) | Active |
| 60461151 | CEFAZOLINE PANPHARMA 2 g, poudre pour solution injectable/pour perfusion | Poudre pour solution injectable ou pour perfusion | PANPHARMA | Active |
| 61242331 | CEFAZOLINE VIATRIS 1 g, poudre pour solution injectable (IM-IV) | Poudre pour solution injectable | VIATRIS SANTE | Active |
| 69258056 | CEFAZOLINE PANPHARMA 1 g/5 ml, poudre et solution pour usage parentéral (IV) | Poudre et solution pour usage parentéral | PANPHARMA | Active |
| 67089141 | CEFAZOLINE PANPHARMA 2 g/10 ml, poudre et solution pour usage parentéral (IV) | Poudre et solution pour usage parentéral | PANPHARMA | Active |
| 60859237 | CEFAZOLINE BASI 1 g, poudre pour solution injectable/pour perfusion | Poudre pour solution injectable ou pour perfusion | BASI | Active |
| 63051517 | CEFAZOLINE BASI 2 g, poudre pour solution injectable/pour perfusion | Poudre pour solution injectable ou pour perfusion | BASI | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions médicamenteuses** : 112 interactions sont répertoriées. Les interactions de niveau modéré concernent les aminosides (kanamycine, néomycine, streptomycine) et l'acide picosulfurique. D'autres interactions, de niveau non précisé, concernent par exemple l'amphotéricine B, l'acide acétylsalicylique, l'amoxicilline, la metformine et l'oméprazole.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucun essai clinique n'est enregistré et aucune publication n'étudie directement la céfazoline dans l'otite moyenne infectieuse. Le seul élément récent est un rapport de cas où la céfazoline est associée à un autre antibiotique. La voie injectable seule et le spectre limité sur les germes principaux de l'otite moyenne affaiblissent encore l'intérêt.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données sur le mécanisme d'action et le spectre d'activité face aux germes de l'otite moyenne
- Des études cliniques comparatives ciblant l'otite moyenne infectieuse
- Les mises en garde et contre-indications issues de la notice officielle
- Une évaluation de la pertinence de la voie injectable pour cette indication

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Cefazolin (cefazolin sodium) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d91a8d13-99a0-4d87-88dc-71cbd37922b4) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

