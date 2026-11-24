---
layout: default
title: Metronidazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
description: "Metronidazole : nouvelle indication prédite, Pneumocystose (pneumocystosis) (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Metronidazole
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

## Metronidazole: Pneumocystose (pneumocystosis)
{: .text-alpha }

## Résumé en Une Phrase

Le métronidazole est un antibiotique et antiprotozoaire de la famille des nitro-imidazolés, utilisé à l'origine contre les infections à bactéries anaérobies, la giardiase, la vaginose bactérienne et la rosacée (forme topique).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **pneumocystose**, mais **aucun essai clinique** n'est enregistré et la littérature disponible (**10 publications**) est essentiellement composée de revues générales et de cas isolés qui ne démontrent pas d'efficacité du métronidazole dans cette maladie.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Predite | Pneumocystose (pneumocystosis) |
| Score de Prediction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Metronidazole (traduction non officielle) : « Le métronidazole, un nitroimidazolé, exerce des effets antibactériens en milieu anaérobie contre la plupart des anaérobies stricts. Une fois que le métronidazole a pénétré dans l'organisme par diffusion passive et a été activé dans le cytoplasme des bactéries anaérobies sensibles, il est réduit ; ce processus fait intervenir des donneurs intracellulaires de transport d'électrons tels que la ferrédoxine et le transfert d'un électron au groupement nitro du métronidazole, conduisant à la formation d'un radical libre nitroso de courte durée de vie. » Texte original en anglais : "Metronidazole, a nitroimidazole, exerts antibacterial effects in an anaerobic environment against most obligate anaerobes. Once metronidazole enters the organism by passive diffusion and activated in the cytoplasm of susceptible anaerobic bacteria, it is reduced; this process includes intra-cellular electron transport donors such as ferredoxin and transfer of an electron to the nitro group of the metronidazole leading to formation of a short-lived nitroso free radical." ([DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255), version du 2026-11-02 ; consulté le 2026-11-19). Sur la base des connaissances générales, le métronidazole est un nitro-imidazole actif contre les anaérobies et certains protozoaires (Giardia, Entamoeba, Trichomonas). Son activation dépend de nitroréductases propres aux organismes anaérobies ou microaérophiles.

**Cette prédiction n'apparaît pas plausible sur le plan mécanistique.** *Pneumocystis jirovecii* est un champignon qui ne possède pas cette voie d'activation. Le score élevé du modèle reflète probablement une proximité dans le réseau de connaissances avec des médicaments antiparasitaires et anti-infectieux, et non une relation pharmacologique réelle. Le traitement de référence de la pneumocystose est le triméthoprime-sulfaméthoxazole.

Il faut donc considérer ce résultat comme un artefact probable de la prédiction computationnelle.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Revue | Mayo Clin Proc | Revue générale des antiparasitaires ; pas de données sur le métronidazole dans la pneumocystose |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revue | Am Fam Physician | Le métronidazole est cité pour l'amibiase et la trichomonase ; la pneumocystose relève du triméthoprime-sulfaméthoxazole |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Revue | Clin Pharmacokinet | Justification pharmacocinétique des traitements antiprotozoaires |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revue | Clin Pharm | Traitement des complications infectieuses du SIDA |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Revue | Top Antivir Med | Infections opportunistes liées au VIH, vue d'ensemble |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Rapport de cas | Am Rev Respir Dis | Pneumocystose et infection à CMV chez un adulte ayant reçu du métronidazole pour une diarrhée, sans bénéfice sur la pneumocystose |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Rapport de cas | Kansenshogaku Zasshi | Amibiase traitée par métronidazole chez des patients atteints du SIDA, pneumocystose survenue ensuite |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Revue | Rev Infect Dis | Critique des essais de prophylaxie antimicrobienne |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Rapport de cas | J Formos Med Assoc | Perforation colique avec amibiase et CMV chez un patient atteint du SIDA |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Rapport de cas | J Med Case Rep | Abcès cérébelleux à *Streptococcus intermedius* révélant une sarcoïdose |

Ces publications mentionnent le métronidazole dans d'autres contextes ; aucune ne montre un effet sur la pneumocystose.

---

## Informations de Marche en France

Le médicament est commercialisé en France, avec 20 AMM valides ; le texte d'indication approuvée n'est pas renseigné dans les données compilées.

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67119549 | ROZEX 0,75 %, émulsion pour application cutanée | Émulsion pour application | GALDERMA INTERNATIONAL | Active |
| 60647323 | ROZEX 0,75 %, gel | Gel | GALDERMA INTERNATIONAL | Active |
| 66962240 | METRONIDAZOLE SUBSTIPHARM 250 mg, comprimé pelliculé | Comprimé pelliculé | SUBSTIPHARM | Active |
| 63815096 | ROZAGEL, gel pour application locale | Gel | LABORATOIRES BAILLEUL (LUXEMBOURG) | Active |
| 66095383 | METRONIDAZOLE B BRAUN 0,5 %, solution pour perfusion | Solution pour perfusion | B BRAUN MEDICAL | Active |
| 61659061 | FLAGYL 500 mg, comprimé pelliculé | Comprimé pelliculé | LABORATOIRES FIDIA | Active |
| 68602579 | METRONIDAZOLE BIOGARAN 500 mg, comprimé pelliculé | Comprimé pelliculé | BIOGARAN | Active |
| 60480276 | METRONIDAZOLE BIOGARAN 250 mg, comprimé pelliculé | Comprimé pelliculé | BIOGARAN | Active |
| 67914540 | METRONIDAZOLE ARROW 250 mg, comprimé pelliculé | Comprimé pelliculé | ARROW GENERIQUES | Active |
| 67763113 | ROZEX 0,75 %, crème | Crème | GALDERMA INTERNATIONAL | Active |
| 60416081 | METRONIDAZOLE ARROW 500 mg, comprimé pelliculé sécable | Comprimé pelliculé | ARROW GENERIQUES | Active |
| 62806411 | ROZACREME 0,75 %, crème | Crème | LABORATOIRES BAILLEUL (LUXEMBOURG) | Active |
| 67207102 | METRONIDAZOLE NORIDEM 500 mg/100 mL, solution pour perfusion | Solution pour perfusion | NORIDEM | Active |
| 68818192 | FLAGYL 250 mg, comprimé pelliculé | Comprimé pelliculé | LABORATOIRES FIDIA | Active |
| 65020253 | FLAGYL 125 mg/5 ml, suspension buvable | Suspension buvable | LABORATOIRES FIDIA | Active |
| 65687841 | METRONIDAZOLE BAXTER 0,5 POUR CENT, solution injectable en poche | Solution injectable | BAXTER | Active |
| 68364551 | METRONIDAZOLE SUBSTIPHARM 500 mg, comprimé pelliculé | Comprimé pelliculé | SUBSTIPHARM | Active |
| 62708127 | FLAGYL 500 mg, ovule | Ovule | LABORATOIRES FIDIA | Active |
| 62319930 | SPIRAMYCINE METRONIDAZOLE ZENTIVA 1,5 MUI/250 mg, comprimé pelliculé | Comprimé pelliculé | ZENTIVA FRANCE | Active |
| 64161144 | SPIRAMYCINE/METRONIDAZOLE VIATRIS 750.000 UI/125 mg, comprimé pelliculé | Comprimé pelliculé | VIATRIS SANTE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

Au total, 20 AMM sont recensées (comprimés, gels, crèmes, ovules, suspension buvable, solutions injectables et associations avec la spiramycine).

<!-- review:begin fr-lic-20261106-metronidazole-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Au total, 20 AMM sont recensées (comprimés, gels, crèmes, ovules, suspension buvable, solutions injectables et associations avec la spiramycine), toutes annulées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-metronidazole-1 -->

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique et maladies hépatiques, épilepsie, maladies rénales, maladies hématologiques (neutropénie, agranulocytose, leucopénie), troubles de la coagulation, neuropathie périphérique et maladies du système nerveux, maladies cérébrales, névrite optique et atteintes des voies visuelles, insuffisance cardiaque congestive, diabète et acidocétose diabétique, goutte, maladies de la vésicule biliaire, dermatite, méningite non infectieuse, abus de substances.
- **Interactions médicamenteuses** : 620 interactions recensées. Parmi les exemples, une interaction **majeure** avec l'éthanol (effet de type disulfirame) ; des interactions **modérées** avec le paclitaxel, l'adalimumab, le trastuzumab emtansine, l'éthinylestradiol, l'estradiol, le butalbital, l'amiodarone, le célécoxib, l'amobarbital et le lopéramide ; des interactions mineures avec notamment l'abiratérone, le tramadol, la famotidine, le salbutamol et le propofol.

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être récupérées : veuillez consulter la notice.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique, pas de lien mécanistique plausible (*Pneumocystis* est un champignon sans voie d'activation du métronidazole), et une littérature sans démonstration d'effet. Un traitement de référence efficace existe déjà.
- Le médicament est commercialisé en France, avec 20 AMM valides, mais les données de sécurité issues de la notice manquent (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Démontrer une activité in vitro ou précliniques sur *Pneumocystis*, sans quoi l'indication ne devrait pas être poursuivie

**Autres pistes plus plausibles parmi les prédictions du modèle** (niveau L4, à étudier comme questions de recherche) : la polypose en capuchon (*cap polyposis*, hypothèse anti-inflammatoire/dysbiose) et l'ulcération vulvaire (maladie de Crohn vulvaire, amibiase génitale), ainsi que la rectosigmoïdite ulcéreuse et la myiase (rôle d'appoint seulement).

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « toutes annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

