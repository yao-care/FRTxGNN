---
layout: default
title: Sulbactam
parent: Prédiction du modèle uniquement (L5)
nav_order: 718
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "sulbactam"
predicted_indications: ["bacterial arthritis"]
description: "Sulbactam : nouvelle indication prédite, Arthrite bactérienne (bacterial arthritis) (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 1)"
---

# Sulbactam
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

## Sulbactam: Arthrite bactérienne (bacterial arthritis)
{: .text-alpha }

## Résumé en Une Phrase

Le sulbactam est un inhibiteur de bêta-lactamases, initialement utilisé dans le traitement d'infections bactériennes (infections à *Staphylococcus aureus* et à *Escherichia coli*, cholangites).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**arthrite bactérienne**, mais aucun essai clinique n'est enregistré ; seules **20 publications** ont été identifiées, dont une minorité seulement porte directement sur le sulbactam (études anciennes, petites séries ou cas cliniques).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Arthrite bactérienne (bacterial arthritis) |
| Score de Prédiction TxGNN | 0.9979 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 2) |
| Nombre d'AMM | 2 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour ampicillin and sulbactam (association contenant Sulbactam) (traduction non officielle) : « Des études biochimiques réalisées sur des systèmes bactériens acellulaires ont montré qu’un large éventail de bêta-lactamases présentes chez des micro-organismes résistants aux pénicillines et aux céphalosporines est inhibé de manière irréversible par le sulbactam. Bien que le sulbactam seul ne possède que peu d’activité antibactérienne utile, sauf contre les Neisseriaceae, des études sur organismes entiers ont montré que le sulbactam restaure l’activité de l’ampicilline contre les souches productrices de bêta-lactamases. » Texte original en anglais : "A wide range of beta-lactamases found in microorganisms resistant to penicillins and cephalosporins have been shown in biochemical studies with cell free bacterial systems to be irreversibly inhibited by sulbactam. Although sulbactam alone possesses little useful antibacterial activity except against the Neisseriaceae, whole organism studies have shown that sulbactam restores ampicillin activity against beta-lactamase producing strains." ([DailyMed: ampicillin and sulbactam prescribing information, Avenacy, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4446d4c8-056d-4bc3-8f58-21255b063398), version du 2026-11-12 ; consulté le 2026-11-19). Sur la base des connaissances pharmacologiques générales, le sulbactam est un inhibiteur irréversible des bêta-lactamases, doté d'une activité intrinsèque contre *Acinetobacter* spp. Associé à l'ampicilline, il élargit le spectre à des germes producteurs de bêta-lactamases : *S. aureus*, *E. coli* et des anaérobies.

Ces germes figurent parmi les agents fréquents des arthrites septiques et des infections ostéo-articulaires. La nouvelle indication est donc cohérente avec les indications antibactériennes d'origine (infections à *S. aureus* et à *E. coli*). Le score élevé de TxGNN reflète probablement cette proximité avec des indications infectieuses existantes, plutôt qu'une découverte réellement nouvelle.

Cette lecture mécanistique est déduite de la pharmacologie connue et non d'un enregistrement de mécanisme fourni dans les données ; elle doit être confirmée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Parmi les publications identifiées, seules les plus pertinentes pour le sulbactam dans les infections ostéo-articulaires sont listées. Le type d'étude indiqué est celui attribué lors du tri automatique ; il n'a pas été vérifié sur les textes complets.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [3026009](https://pubmed.ncbi.nlm.nih.gov/3026009/) | 1986 | Étude comparative ouverte randomisée | Rev Infect Dis | Sulbactam/ampicilline vs céfotaxime pendant 2 semaines dans des infections osseuses, articulaires et des tissus mous (13 vs 9 patients) ; guérison ou amélioration chez tous les 13 patients du groupe sulbactam/ampicilline |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | Étude clinique | Rev Infect Dis | 9 enfants atteints d'ostéomyélite et/ou d'arthrite septique traités séquentiellement par sulbactam/ampicilline IV puis sultamicilline orale ; germes identifiés sensibles dans 6 cas |
| [3252119](https://pubmed.ncbi.nlm.nih.gov/3252119/) | 1988 | Essai clinique non comparatif | Mikrobiyol Bul | 84 patients avec infections variées traités par ampicilline/sulbactam, dont 5 arthrites septiques et ostéomyélites |
| [9263167](https://pubmed.ncbi.nlm.nih.gov/9263167/) | 1997 | Cas clinique | J Rheumatol | Arthrite à *Pasteurella multocida* après morsure de chat, associée à une goutte aiguë ; résolution de l'infection sous ampicilline/sulbactam |
| [1745624](https://pubmed.ncbi.nlm.nih.gov/1745624/) | 1991 | Étude in vitro et revue | Pharmacotherapy | Comparaison de l'activité in vitro ampicilline-sulbactam et ticarcilline-acide clavulanique, et revue de l'efficacité clinique |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revue | Int J Antimicrob Agents | Usage hors AMM versus recommandations formelles des antibiotiques dans les infections à bactéries multirésistantes |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohorte rétrospective | Clin Lab | Répartition des pathogènes et résistances dans les infections ostéo-articulaires chez l'enfant de moins de 4 ans |

Les autres publications identifiées (cas cliniques d'arthrites à germes rares, étude sur cellules canines, données vétérinaires, utilisation d'antibiotiques dans la COVID-19) ne concernent pas directement le sulbactam dans cette indication et ne sont pas retenues.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69057530 | UNACIM INJECTABLE 0,5 g/1 g, poudre pour usage parentéral | Poudre pour usage parentéral | PFIZER HOLDING FRANCE | Active |
| 64892672 | UNACIM INJECTABLE 1 g, poudre et solution pour usage parentéral | Poudre et solution pour usage parentéral | PFIZER HOLDING FRANCE | Archivée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Maladies en contre-indication selon le graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, mononucléose infectieuse, syndrome d'infection chronique par le virus d'Epstein-Barr.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées. Les mises en garde et contre-indications issues de la notice n'étant pas disponibles, veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique n'est enregistré et les données publiées sont anciennes, de petite taille et portent sur l'association ampicilline/sulbactam, et non sur le sulbactam seul. Les données de sécurité issues de la notice ainsi que le mécanisme d'action sont manquants, ce qui bloque l'évaluation de sécurité.

<!-- review:begin fr-lic-20261106-sulbactam-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le produit n'est plus commercialisé en France (AMM annulées), et les données de sécurité issues de la notice ainsi que le mécanisme d'action sont manquants, ce qui bloque l'évaluation de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-sulbactam-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM
- Compléter les données sur le mécanisme d'action (DrugBank)
- Examiner en texte intégral les études ostéo-articulaires pour confirmer leur design et leurs résultats
- Vérifier si des associations avec le sulbactam (par ex. ampicilline/sulbactam) restent disponibles en France pour cette indication
- Évaluer la place du sulbactam par rapport aux recommandations actuelles sur l'arthrite septique

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « e produit n'est plus commercialisé en France (AMM annulées), et l » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: ampicillin and sulbactam prescribing information, Avenacy, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4446d4c8-056d-4bc3-8f58-21255b063398) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

