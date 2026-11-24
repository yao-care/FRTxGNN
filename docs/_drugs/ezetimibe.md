---
layout: default
title: Ezetimibe
parent: Prédiction du modèle uniquement (L5)
nav_order: 314
evidence_level: L5
indication_count: 1
monitor_inn: "ezetimibe"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Ezetimibe : nouvelle indication prédite, Déficit en protéine de transfert des esters de cholestérol (niveau de preuve L5). Indication d'origine : Hyperlipidémie"
---

# Ezetimibe
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

## Ézétimibe : De l'hyperlipidémie au déficit en protéine de transfert des esters de cholestérol
{: .text-alpha }

## Résumé en Une Phrase

L'ézétimibe est un médicament hypocholestérolémiant, enregistré dans le graphe de connaissances pour l'hyperlipidémie, l'hypercholestérolémie familiale homozygote et la sitostérolémie.
Le modèle TxGNN prédit qu'il pourrait être utile dans le **déficit en protéine de transfert des esters de cholestérol (CETP)**,
mais **aucun essai clinique** et **aucune publication** ne l'étudie directement : cette prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperlipidémie (relation enregistrée dans le graphe de connaissances ; les textes d'indication des AMM ne sont pas renseignés dans les données compilées) |
| Nouvelle Indication Prédite | Déficit en protéine de transfert des esters de cholestérol |
| Score de Prédiction TxGNN | 0,9909 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ezetimibe (traduction non officielle) : « L'ézétimibe réduit le cholestérol sanguin en inhibant l'absorption du cholestérol par l'intestin grêle. Il a été démontré que la cible moléculaire de l'ézétimibe est le transporteur de stérols Niemann-Pick C1-Like 1 (NPC1L1), qui intervient dans l'absorption intestinale du cholestérol et des phytostérols. » Texte original en anglais : "Ezetimibe reduces blood cholesterol by inhibiting the absorption of cholesterol by the small intestine. The molecular target of ezetimibe has been shown to be the sterol transporter, Niemann-Pick C1-Like 1 (NPC1L1), which is involved in the intestinal uptake of cholesterol and phytosterols." ([DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9), version du 2026-10-08 ; consulté le 2026-11-19). D'après les connaissances générales en pharmacologie, l'ézétimibe inhibe l'absorption intestinale du cholestérol via la protéine NPC1L1 et abaisse ainsi le LDL-cholestérol.

Le déficit en CETP se caractérise par un HDL-cholestérol élevé et un transfert réduit des esters de cholestérol des HDL vers les lipoprotéines contenant l'apoB. Les deux situations touchent le métabolisme des lipoprotéines, ce qui explique probablement le score élevé du modèle.

Cependant, le déficit en CETP est généralement un phénotype bénin, voire potentiellement protecteur, qui ne nécessite pas de traitement hypocholestérolémiant. Aucun lien mécanistique ou clinique direct entre l'inhibition de NPC1L1 et ce déficit n'a été démontré. La prédiction est vraisemblablement un artefact de proximité dans le réseau de connaissances.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Les deux publications recensées ne portent pas directement sur l'ézétimibe dans le déficit en CETP : l'une est une revue générale sur les cibles hypolipémiantes, l'autre une étude animale (modèle de hamster) sur un anticorps anti-PCSK9.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Revue | European Heart Journal | Panorama des cibles hypolipémiantes (LDL-C, triglycérides, apoB, Lp(a)) et de leurs implications translationnelles ; pas d'étude directe sur le déficit en CETP |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Étude animale | International Journal of Molecular Sciences | Hamster Ldlr+/- comme modèle pour évaluer un anticorps anti-PCSK9 dans l'hyperlipidémie et l'athérosclérose ; sans lien direct avec l'ézétimibe |

## Informations de Marché en France

L'ézétimibe est commercialisé en France. Les données compilées recensent des AMM pour la plupart valides (69062997 est archivée), et la liste peut être partielle. Les textes d'indication approuvée ne sont pas renseignés. Plusieurs produits listés sont des associations (par exemple avec la rosuvastatine) ; leurs AMM ne décrivent pas l'usage de l'ézétimibe seul.

<!-- review:begin fr-lic-20261112-ezetimibe-1 -->

> **Correction de vérification (2026-11-12)**: Texte initial : « recensent au moins 20 AMM, toutes valides, » D'après la BDPM (données du 2026-11-09), parmi les 20 AMM compilées pour ce rapport, 19 sont actives et 1 est archivée (69062997). Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261112-ezetimibe-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60887592 | EZETIMIBE ALMUS 10 mg, comprimé | Comprimé | ALMUS FRANCE | Active |
| 69510055 | EZETIMIBE EG 10 mg, comprimé | Comprimé | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 65825737 | EZETIMIBE CRISTERS PHARMA 10 mg, comprimé | Comprimé | SUN PHARMA FRANCE | Active |
| 66718898 | EZETIMIBE SANDOZ 10 mg, comprimé | Comprimé | SANDOZ | Active |
| 68139818 | EZETIMIBE EVOLUGEN 10 mg, comprimé | Comprimé | EVOLUPHARM | Active |
| 60977940 | EZETIMIBE ZENTIVA 10 mg, comprimé | Comprimé | ZENTIVA FRANCE | Active |
| 68607455 | EZETIMIBE KRKA 10 mg, comprimé | Comprimé | KRKA (SLOVENIE) | Active |
| 67451779 | EZETIMIBE VIATRIS 10 mg, comprimé | Comprimé | VIATRIS SANTE | Active |
| 63964962 | EZETIMIBE ACCORD 10 mg, comprimé | Comprimé | ACCORD HEALTHCARE FRANCE | Active |
| 60981789 | EZETROL 10 mg, comprimé | Comprimé | ORGANON FRANCE | Active |
| 66999267 | EZETIMIBE TEVA 10 mg, comprimé | Comprimé | TEVA SANTE | Active |
| 69068516 | EZETIMIBE BIOGARAN 10 mg, comprimé | Comprimé | BIOGARAN | Active |
| 65639202 | EZETIMIBE ARROW 10 mg, comprimé | Comprimé | ARROW GENERIQUES | Active |
| 64894794 | EZETIMIBE ZYDUS 10 mg, comprimé | Comprimé | ZYDUS FRANCE | Active |
| 63934271 | TWICOR 20 mg/10 mg, comprimé pelliculé | Comprimé pelliculé | DIFARMED (ESPAGNE) | Active |
| 64518219 | TWICOR 10 mg/10 mg, comprimé pelliculé | Comprimé pelliculé | VIATRIS MEDICAL | Active |
| 69491256 | LIPOROSA 20 mg/10 mg, gélule | Gélule | DIFARMED (ESPAGNE) | Active |
| 63501238 | JUNALIZA 20 mg/10 mg, gélule | Gélule | EGIS PHARMACEUTICALS (HONGRIE) | Active |
| 65237214 | LIPOROSA 10 mg/10 mg, gélule | Gélule | CRISTERS | Active |
| 69062997 | EZETIMIBE CRISTERS 10 mg, comprimé | Comprimé | CRISTERS | Archivée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications relevées dans le graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : pancréatite, maladie du foie, maladie de la vésicule biliaire, myopathie, maladie musculaire, maladie du muscle squelettique, paralysie périodique familiale, abus/dépendance à une substance, rhabdomyolyse, fasciite nodulaire.
- **Interactions médicamenteuses** : 171 interactions recensées. Parmi les principales, de niveau modéré : acide chénodésoxycholique, éluxadoline, rosuvastatine, simvastatine. D'autres interactions (calcitriol, pantoprazole, metformine, oméprazole, morphine, vancomycine, etc.) ont un niveau de gravité non précisé.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication étudiant directement le déficit en CETP. Cette maladie est le plus souvent bénigne et ne justifie pas de traitement hypocholestérolémiant. Le lien est probablement un artefact du réseau.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action détaillé de l'ézétimibe
- Éléments de preuve directs (études mécanistiques ou cliniques) sur l'ézétimibe dans le déficit en CETP
- Démonstration d'un bénéfice clinique d'un traitement hypolipémiant dans cette maladie
- Mises en garde et contre-indications issues de la notice officielle de l'ANSM

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-12 | AMM compilées : 19 valides et 1 archivée, pas toutes valides | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: ezetimibe prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c37c695b-fb40-423c-9b73-d1aa58a34db9) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

