---
layout: default
title: Topotecan
parent: Prédiction du modèle uniquement (L5)
nav_order: 774
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "topotecan"
predicted_indications: ["female breast carcinoma", "adult germ cell tumor"]
description: "Topotecan : nouvelle indication prédite, Carcinome du sein féminin (female breast carcinoma) (niveau de preuve L5). En France, AMM dans la BDPM : 5 (valides : 5)"
---

# Topotecan
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Topotecan: Carcinome du sein féminin (female breast carcinoma)
{: .text-alpha }

## Résumé en Une Phrase

Le topotécan est un inhibiteur de la topoisomérase I, initialement utilisé pour le traitement du cancer de l'ovaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome du sein féminin**, mais les preuves restent limitées : **3 essais cliniques** (tous de phase précoce, deux terminés prématurément et un en cours de recrutement) et **20 publications** (principalement des revues et des études précliniques) soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Carcinome du sein féminin (female breast carcinoma) |
| Score de Prédiction TxGNN | 0.9992 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 5 sur 5) |
| Nombre d'AMM | 5 (valides : 5) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Topotecan (traduction non officielle) : « La topoisomérase I soulage la contrainte de torsion de l'ADN en induisant des cassures simple brin réversibles. Le topotécan se lie au complexe topoisomérase I-ADN et empêche la religation de ces cassures simple brin. On pense que la cytotoxicité du topotécan est due aux lésions double brin de l'ADN produites au cours de la synthèse de l'ADN, lorsque les enzymes de réplication interagissent avec le complexe ternaire formé par le topotécan, la topoisomérase I et l'ADN. » Texte original en anglais : "Topoisomerase I relieves torsional strain in DNA by inducing reversible single-strand breaks. Topotecan binds to the topoisomerase I-DNA complex and prevents re-ligation of these single-strand breaks. The cytotoxicity of topotecan is thought to be due to double-strand DNA damage produced during DNA synthesis, when replication enzymes interact with the ternary complex formed by topotecan, topoisomerase I, and DNA." ([DailyMed: Hycamtin (topotecan) prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b23b46f5-c276-47f5-8bbd-940680b3f579), version du 2023-09-18 ; consulté le 2026-11-19). D'après les connaissances établies, le topotécan est un inhibiteur de la topoisomérase I : il provoque des lésions de l'ADN et une mort cellulaire dépendante de la réplication dans les cellules tumorales à division rapide. Son efficacité dans le cancer de l'ovaire est reconnue, et il pourrait mécanistiquement être applicable à d'autres tumeurs solides.

Une étude préclinique de 2023 (PMID 37987734) suggère que l'inhibition de Top1 entraîne une accumulation anormale de boucles R et une létalité synthétique dans les cancers dépendants de MYC, ce qui concernerait certains sous-types de cancer du sein, comme les formes triple négatives. Par ailleurs, l'efflux par BCRP/ABCG2 est un mécanisme reconnu de transport et de résistance au topotécan dans le cancer du sein (PMID 25236865).

Ces éléments restent mécanistiques ou de phase précoce. Aucune donnée de phase 3 ou randomisée ne démontre un bénéfice dans le cancer du sein, et une étude de phase 2 sur la perfusion continue de topotécan (PMID 9413954) n'a pas montré d'augmentation de l'efficacité.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminé (arrêt anticipé) | Non renseignée | Topotécan à dose intensive, ifosfamide/mesna et étoposide (TIME) suivis d'une autogreffe de cellules souches dans le cancer du sein métastatique ; bras unique, preuve faible |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminé (arrêt anticipé) | 221 | Sécurité du sélinexor associé à plusieurs chimiothérapies ou immunothérapies standard, dont le topotécan ; informations limitées sur le topotécan dans le cancer du sein |
| [NCT06840886](https://clinicaltrials.gov/study/NCT06840886) | Phase 1 | En recrutement | 426 | Étude de première administration chez l'homme du PHST001 dans les tumeurs solides avancées ; aucune donnée d'efficacité pour le moment, rôle du topotécan non clairement établi |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Essai de phase 2 | Br J Cancer | Topotécan en perfusion continue dans le cancer du sein avancé et le CBNPC : pas de preuve d'une efficacité accrue |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Étude pilote | Onkologie | Topotécan comme chimiothérapie primaire des métastases cérébrales du cancer du sein |
| [9425961](https://pubmed.ncbi.nlm.nih.gov/9425961/) | 1997 | Revue | Semin Oncol | Rôle potentiel du topotécan dans le cancer du sein avancé |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Préclinique | Cancer Res | L'inhibition de Top1 induit une létalité synthétique dans les cancers dépendants de MYC |
| [25236865](https://pubmed.ncbi.nlm.nih.gov/25236865/) | 2015 | Revue | AAPS J | Rôle de BCRP/ABCG2 dans le transport et la résistance au topotécan |
| [10930538](https://pubmed.ncbi.nlm.nih.gov/10930538/) | 2000 | Préclinique | Biochem Pharmacol | Expression de BCRP dans des cellules de cancer du sein résistantes au topotécan |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Préclinique | Anticancer Res | Efficacité comparée de xénogreffes de carcinomes du côlon, du poumon et du sein traitées par doxorubicine, cisplatine, irinotécan ou topotécan |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | Préclinique | J Surg Res | Effet de la quercétine sur la cytotoxicité du topotécan dans des cellules de cancer du sein |
| [39657238](https://pubmed.ncbi.nlm.nih.gov/39657238/) | 2024 | Préclinique | ACS Appl Mater Interfaces | Nanoparticules biomimétiques médicament-gène contenant du topotécan pour le cancer du sein métastatique |
| [39013199](https://pubmed.ncbi.nlm.nih.gov/39013199/) | 2024 | Consensus d'experts | Rev Colomb Obstet Ginecol | Prise en charge du cancer épithélial de l'ovaire avancé ou métastatique (indication d'origine) |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63901015 | HYCAMTIN 1 mg, gélule | Gélule | SANDOZ PHARMACEUTICALS (SLOVENIE) | Active |
| 61126871 | HYCAMTIN 4 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | SANDOZ PHARMACEUTICALS (SLOVENIE) | Active |
| 63093822 | HYCAMTIN 0,25 mg, gélule | Gélule | SANDOZ PHARMACEUTICALS (SLOVENIE) | Active |
| 65275325 | TOPOTECAN HOSPIRA 4 mg/4ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 65945665 | TOPOTECANE ACCORD 1 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | ACCORD HEALTHCARE FRANCE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (inhibiteur de la topoisomérase I, dérivé de la camptothécine) |
| Risque de Myélosuppression | Élevé : la myélosuppression est la toxicité principale du topotécan. Les contre-indications du graphe de connaissances incluent la thrombopénie, la neutropénie, l'agranulocytose et l'anémie |
| Classification d'Émétogénicité | Moyenne (selon la classe du médicament) |
| Éléments de Surveillance | NFS avec formule (neutrophiles, plaquettes, hémoglobine), fonction rénale, fonction hépatique, surveillance des symptômes respiratoires et de la diarrhée |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications ou maladies à risque (issues du graphe de connaissances, et non du texte de la notice)** : thrombopénie, neutropénie, agranulocytose, anémie (y compris macrocytaire), pneumopathie interstitielle, fibrose pulmonaire (y compris post-inflammatoire), maladie diarrhéique, insuffisance rénale.
- **Interactions médicamenteuses** : 296 interactions recensées. Parmi celles listées, les interactions de niveau **majeur** concernent le défériprone et le samarium (153Sm) lexidronam. Des interactions de niveau **modéré** concernent notamment l'éliglustat, le rolapitant, l'iobenguane (I-131), la palifermine, le chlorure de strontium Sr-89 et l'ibritumomab tiuxétan. Les interactions avec la lévofloxacine et la caféine sont de niveau mineur.

Les mises en garde et contre-indications issues de la notice officielle ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve pour le cancer du sein est L3 : les essais sont de phase précoce, terminés prématurément ou sans résultats d'efficacité, et aucune donnée randomisée ne confirme un bénéfice. La seule étude de phase 2 de perfusion continue n'a pas montré d'efficacité accrue.
- Le médicament dispose d'AMM valides en France (statut des AMM : voir l'Aperçu rapide) (médicament commercialisé), mais les informations de sécurité issues de la notice sont manquantes, ce qui empêche de passer l'étape de criblage de sécurité.

<!-- review:begin fr-lic-20261124-topotecan-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 4 AMM françaises sont valides » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-topotecan-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications) ; cette lacune est bloquante.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Clarifier la situation réglementaire et la disponibilité réelle d'une formulation en France.
- Obtenir des données cliniques plus solides dans le cancer du sein, par exemple des essais de phase 2 ciblant les sous-types dépendants de MYC ou triple négatifs.
- Définir un plan de surveillance hématologique et de sécurité, compte tenu du risque élevé de myélosuppression.

<!-- review:begin fr-lic-20261106-topotecan-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier la situation réglementaire (AMM annulées) et la disponibilité réelle d'une formulation en France. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-topotecan-1 -->

**Autres indications prédites (pour information) :** la tumeur germinale de l'adulte (score 0,9957, niveau L2, preuves surtout indirectes issues d'études pédiatriques).

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Hycamtin (topotecan) prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b23b46f5-c276-47f5-8bbd-940680b3f579) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

