---
layout: default
title: Rifaximin
parent: Prédiction du modèle uniquement (L5)
nav_order: 667
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Rifaximin : nouvelle indication prédite, Candidose buccale (niveau de preuve L5). Indication d'origine : Encéphalopathie hépatique…"
monitor_inn: "rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
---

# Rifaximin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Rifaximine : De l'Encéphalopathie Hépatique à la Candidose Buccale
{: .text-alpha }

## Résumé en Une Phrase

La rifaximine est un antibiotique oral peu absorbé, initialement utilisé pour le traitement de l'encéphalopathie hépatique et du coma hépatique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **candidose buccale**, mais **aucun essai clinique** et **une seule publication** sont associés à cette prédiction, et cette publication évoque plutôt un signal de risque (infections à *Candida* résistantes) qu'un bénéfice thérapeutique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Encéphalopathie hépatique, coma hépatique (texte d'indication de l'AMM non disponible) |
| Nouvelle Indication Prédite | Candidose buccale |
| Score de Prédiction TxGNN | 0,9975 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Rifaximin (traduction non officielle) : « La rifaximine est un médicament antibactérien. […] La rifaximine est un dérivé semi-synthétique de la rifampicine et agit en se liant à la sous-unité bêta de l'ARN polymérase ADN-dépendante bactérienne, bloquant l'une des étapes de la transcription. Il en résulte une inhibition de la synthèse des protéines bactériennes et, par conséquent, une inhibition de la croissance des bactéries. » Texte original en anglais : "Rifaximin is an antibacterial drug. […] Rifaximin is a semi-synthetic derivative of rifampin and acts by binding to the beta-subunit of bacterial DNA-dependent RNA polymerase blocking one of the steps in transcription. This results in inhibition of bacterial protein synthesis and consequently inhibits the growth of bacteria." ([DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b), version du 2025-08-27 ; consulté le 2026-11-19). Sur la base des informations connues, la rifaximine est un antibactérien oral faiblement absorbé, dont l'action se concentre dans l'intestin. Son efficacité dans l'encéphalopathie hépatique repose sur la réduction de la flore bactérienne intestinale.

**La prédiction ne repose sur aucun lien mécanistique solide.** La rifaximine n'a pas d'activité antifongique connue. Le score élevé du modèle semble refléter des associations au sein du réseau de connaissances plutôt qu'un bénéfice clinique démontré. La seule publication rattachée suggère même l'inverse : l'usage de la rifaximine a été associé à des infections à *Candida* résistantes à la micafungine chez des receveurs de greffe allogénique de cellules souches hématopoïétiques, ce qui évoque une perturbation du microbiote intestinal favorisant *Candida*.

### Autres prédictions examinées

Les autres prédictions du modèle ne sont pas mieux étayées :

| Maladie prédite | Score TxGNN | Niveau de preuve | Remarque |
|------|------|------|------|
| Fistule commissurale des lèvres | 0,9964 | L5 | Aucune étude ; pas de lien mécanistique identifiable |
| Ostéoradionécrose de la mandibule | 0,9964 | L5 | Aucune étude ; l'absorption systémique minime rend l'atteinte de l'os irradié improbable |
| Leucoedème buccal | 0,9964 | L5 | Aucune étude ; variante bénigne de la muqueuse, sans besoin thérapeutique |
| Syndrome de la bouche brûlante | 0,9964 | L5 | Aucune étude ; mécanismes plutôt neuropathiques et hormonaux |
| Candidose (générale) | 0,9915 | L5 | Deux études observationnelles indirectes, suggérant un risque et non un bénéfice |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohorte | Annals of Hematology | Chez des receveurs de greffe allogénique de cellules souches hématopoïétiques, l'usage de la rifaximine en prophylaxie a été associé à des infections à *Candida* résistantes à la micafungine : signal de risque, non de bénéfice |

Pour la candidose en général, une étude cas-témoins supplémentaire ([32360775](https://pubmed.ncbi.nlm.nih.gov/32360775/), 2021, *Clinical Microbiology and Infection*) a identifié les facteurs de risque de candidémie chez des patients hospitalisés atteints de cirrhose, population qui reçoit couramment de la rifaximine. Elle est indirecte et ne démontre aucun bénéfice thérapeutique.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63467355 | TIXTAR 550 mg, comprimé pelliculé | Comprimé pelliculé | ALFASIGMA FRANCE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : colite à *Clostridium difficile* et entérocolite nécrosante périnatale.
- **Interactions médicamenteuses** : 69 interactions recensées, dont une de niveau majeur et la plupart de niveau modéré.
  - **Majeure** : vaccin vivant contre le choléra (*Vibrio cholerae* CVD 103-HgR).
  - **Modérées (exemples)** : warfarine, ciclosporine, tolvaptan, alpélisib, apalutamide, darolutamide, cabozantinib, brigatinib, encorafénib, élagolix, élexacaftor, éliglustat, énasidénib, daclatasvir, lédipasvir, acide picosulfurique, acide bempédoïque, istradéfylline, capmatinib.
- **Signal spécifique à cette prédiction** : une association entre l'usage de la rifaximine et des infections à *Candida* résistantes a été rapportée chez des patients greffés.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (0,9975), mais il n'est soutenu par aucun essai clinique, et la seule publication directement liée évoque un risque d'infections à *Candida* plutôt qu'un bénéfice. Le niveau de preuve est L4 et le mécanisme antifongique est absent. Les autres indications prédites relèvent du niveau L5 (prédiction du modèle uniquement).
- Les données de sécurité de la notice sont manquantes, ce qui bloque le passage à l'étape de criblage de sécurité.

<!-- review:begin fr-lic-20261106-rifaximin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'unique AMM française est annulée, et les données de sécurité de la notice sont manquantes, ce qui bloque le passage à l'étape de criblage de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-rifaximin-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), donnée bloquante.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Produire des données précliniques ou cliniques démontrant une éventuelle activité contre la candidose, et évaluer le signal de risque fongique associé à la rifaximine.
- Clarifier la pertinence de la prédiction par rapport à l'indication d'origine (similarité à documenter) et la compatibilité des voies d'administration (voie orale, action intestinale, face à une atteinte buccale).

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « 'unique AMM française est annulée, et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

