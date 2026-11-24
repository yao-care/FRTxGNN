---
layout: default
title: Tolvaptan
parent: Prédiction du modèle uniquement (L5)
nav_order: 772
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "TOLVAPTAN"
predicted_indications: ["renal-hepatic-pancreatic dysplasia", "karyomegalic interstitial nephritis", "thoracic malformation", "Joubert syndrome with renal defect", "adult familial nephronophthisis-spastic quadriparesia syndrome", "Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
description: "Tolvaptan : nouvelle indication prédite, Renal-hepatic-pancreatic dysplasia (niveau de preuve L5). En France, AMM dans la BDPM : 17 (valides : 17)"
---

# Tolvaptan
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Tolvaptan: Renal-hepatic-pancreatic dysplasia
{: .text-alpha }

## Résumé en Une Phrase

Tolvaptan est un antagoniste sélectif des récepteurs V2 de la vasopressine, initialement utilisé dans le syndrome de sécrétion inappropriée d'ADH, le syndrome néphrogénique d'antidiurèse inappropriée et la polykystose rénale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **polykystose rénale de type 3 avec ou sans polykystose hépatique**,
avec **0 essai clinique** enregistré et **20 publications** associées (dont 2 essais randomisés de référence dans la polykystose rénale autosomique dominante).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Renal-hepatic-pancreatic dysplasia |
| Score de Prédiction TxGNN | 0.9998 |
| Niveau de Preuve | L5 (selon l'évaluation du dossier ; les ECR proviennent de la PKD autosomique dominante en général, non spécifiquement du type 3) |
| Statut de Marché en France | Commercialisé (autorisations valides : 17 sur 17) |
| Nombre d'AMM | 17 (valides : 17) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Tolvaptan (traduction non officielle) : « Le tolvaptan est un antagoniste sélectif des récepteurs V 2 de la vasopressine dont l'affinité pour le récepteur V 2 est 1,8 fois celle de l'arginine vasopressine (AVP) native. L'affinité du tolvaptan pour le récepteur V 2 est 29 fois celle pour le récepteur V 1a. » Texte original en anglais : "Tolvaptan is a selective vasopressin V 2 -receptor antagonist with an affinity for the V 2 -receptor that is 1.8 times that of native arginine vasopressin (AVP). Tolvaptan affinity for the V 2 -receptor is 29 times that for the V 1a -receptor." ([DailyMed: Jynarque (tolvaptan) prescribing information, Otsuka America Pharmaceutical, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3febc0a1-9e5a-4ce0-843d-210f21d862c4), version du 2026-09-30 ; consulté le 2026-11-19). Sur la base des informations connues, tolvaptan est un antagoniste sélectif du récepteur V2 de la vasopressine. Dans la polykystose rénale, l'augmentation de la signalisation par l'AMPc favorise la croissance des kystes et la sécrétion de liquide ; le blocage des récepteurs V2 réduit l'AMPc rénal et ralentit l'expansion des kystes.

La polykystose de type 3 (liée à GANAB) partage ce mécanisme de kystogenèse avec la polykystose autosomique dominante (ADPKD), pour laquelle tolvaptan est déjà un traitement établi. Il s'agit donc, en pratique, d'une indication proche de l'indication d'origine plutôt que d'un véritable repositionnement.

Réserve importante : les essais pivots (TEMPO 3:4, REPRISE) ont été menés dans l'ADPKD au sens large, et non spécifiquement chez des patients porteurs de mutations de GANAB.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

<!-- review:begin fr-lic-20261106-tolvaptan-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « (5 AMM présentées sur 17 au total, toutes annulées.) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-tolvaptan-1 -->

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | ECR | N Engl J Med | Tolvaptan dans l'ADPKD : les antagonistes V2 inhibent la croissance des kystes et ralentissent le déclin de la fonction rénale (essai TEMPO 3:4) |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | ECR | N Engl J Med | Tolvaptan dans l'ADPKD de stade avancé ; élévations des aminotransférases et de la bilirubine rapportées dans l'essai précédent |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Revue systématique / méta-analyse | Cochrane Database Syst Rev | Interventions pour prévenir la progression de l'ADPKD, dont les agents modifiant la maladie |
| [41771281](https://pubmed.ncbi.nlm.nih.gov/41771281/) | 2026 | Revue | Lancet | Base de preuves solide pour tolvaptan comme traitement modificateur de la maladie chez les patients à haut risque d'insuffisance rénale |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Revue | JAMA | Revue générale de l'ADPKD, première maladie rénale héréditaire |
| [40844441](https://pubmed.ncbi.nlm.nih.gov/40844441/) | 2025 | Revue | Am J Kidney Dis | Programme de formation 2025 : traitement modificateur recommandé selon le risque de progression |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Revue | Clin Liver Dis | Polykystose rénale/hépatique ; tolvaptan peut ralentir la détérioration de la fonction rénale et la croissance des kystes |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Revue | Curr Opin Nephrol Hypertens | Thérapies émergentes au-delà de tolvaptan, seul traitement approuvé par la FDA ciblant la progression |
| [32392574](https://pubmed.ncbi.nlm.nih.gov/32392574/) | 2021 | Revue | Pediatr Res | Utilisation de tolvaptan chez les adolescents et jeunes adultes à progression rapide |
| [33376103](https://pubmed.ncbi.nlm.nih.gov/33376103/) | 2020 | Commentaire | Clin J Am Soc Nephrol | Sécurité à long terme de tolvaptan dans l'ADPKD |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60108831 | TOLVAPTAN SANDOZ 15 mg, comprimé + TOLVAPTAN SANDOZ 45 mg, comprimé | Comprimé et comprimé | SANDOZ | Active |
| 64599993 | TOLVAPTAN TEVA 30 mg, comprimé + TOLVAPTAN TEVA 60 mg, comprimé | Comprimé et comprimé | TEVA (PAYS-BAS) | Active |
| 66056341 | JINARC 30 mg, comprimé | Comprimé | OTSUKA PHARMACEUTICAL NETHERLANDS (PAYS BAS) | Active |
| 68174566 | JINARC 30 mg, comprimé + JINARC 60 mg, comprimé | Comprimé et comprimé | OTSUKA PHARMACEUTICAL NETHERLANDS (PAYS BAS) | Active |
| 68053529 | TOLVAPTAN SANDOZ 30 mg, comprimé + TOLVAPTAN SANDOZ 90 mg, comprimé | Comprimé et comprimé | SANDOZ | Active |
| 63026453 | JINARC 30 mg, comprimé + JINARC 90 mg, comprimé | Comprimé et comprimé | OTSUKA PHARMACEUTICAL NETHERLANDS (PAYS BAS) | Active |
| 66055638 | TOLVAPTAN BIOGARAN 30 mg, comprimé + TOLVAPTAN BIOGARAN 60 mg, comprimé | Comprimé et comprimé | BIOGARAN | Active |
| 67126700 | TOLVAPTAN TEVA 15 mg, comprimé + TOLVAPTAN TEVA 45 mg, comprimé | Comprimé et comprimé | TEVA (PAYS-BAS) | Active |
| 61666369 | JINARC 15 mg, comprimé | Comprimé | OTSUKA PHARMACEUTICAL NETHERLANDS (PAYS BAS) | Active |
| 62302589 | TOLVAPTAN SANDOZ 30 mg, comprimé + TOLVAPTAN SANDOZ 60 mg, comprimé | Comprimé et comprimé | SANDOZ | Active |
| 64887903 | TOLVAPTAN ZENTIVA 15 mg, comprimé + TOLVAPTAN ZENTIVA 45 mg, comprimé | Comprimé et comprimé | ZENTIVA FRANCE | Active |
| 69512405 | TOLVAPTAN BIOGARAN 15 mg, comprimé + TOLVAPTAN BIOGARAN 45 mg, comprimé | Comprimé et comprimé | BIOGARAN | Active |
| 63235257 | TOLVAPTAN TEVA 30 mg, comprimé + TOLVAPTAN TEVA 90 mg, comprimé | Comprimé et comprimé | TEVA (PAYS-BAS) | Active |
| 65920174 | TOLVAPTAN ZENTIVA 30 mg, comprimé + TOLVAPTAN ZENTIVA 90 mg, comprimé | Comprimé et comprimé | ZENTIVA FRANCE | Active |
| 69411993 | TOLVAPTAN ZENTIVA 30 mg, comprimé + TOLVAPTAN ZENTIVA 60 mg, comprimé | Comprimé et comprimé | ZENTIVA FRANCE | Active |
| 64598514 | JINARC 15 mg, comprimé + JINARC 45 mg, comprimé | Comprimé et comprimé | OTSUKA PHARMACEUTICAL NETHERLANDS (PAYS BAS) | Active |
| 60544558 | TOLVAPTAN BIOGARAN 30 mg, comprimé + TOLVAPTAN BIOGARAN 90 mg, comprimé | Comprimé et comprimé | BIOGARAN | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (non issues de la notice) : insuffisance hépatique, cirrhose du foie, abus/dépendance à des substances, ulcère gastroduodénal actif, maladie démyélinisante.
- **Hépatotoxicité** : des élévations des aminotransférases et de la bilirubine ont été rapportées dans les essais ; un programme de surveillance hépatique de type REMS est nécessaire.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Majeure : clarithromycine.
  - Modérées : aprépitant, dexaméthasone, empagliflozine, éliglustat, lopéramide, miconazole, naltrexone, rifaximine, rolapitant, ainsi que plusieurs sels de potassium (citrate, bicarbonate, chlorure, gluconate).
  - Mineures : fidaxomicine, naloxégol, prucalopride.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Tolvaptan est déjà un traitement établi de l'ADPKD, avec deux ECR de phase 3 (TEMPO 3:4 et REPRISE) et une revue systématique, ce qui soutient fortement la plausibilité mécanistique pour la polykystose de type 3. Les preuves ne portent toutefois pas spécifiquement sur les mutations de GANAB, et le risque hépatique impose un encadrement strict.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice ANSM (lacune bloquante pour la phase de sélection de sécurité).
- Les données détaillées sur le mécanisme d'action (DrugBank).
- Des données cliniques spécifiques à la polykystose de type 3 (GANAB).
- Un plan de surveillance hépatique (bilan hépatique régulier).

**Autres indications prédites (non recommandées à ce stade) :** dysplasie rénale-hépatique-pancréatique, néphrite interstitielle caryomégalique, malformation thoracique, syndrome de Joubert avec atteinte rénale (question de recherche, niveau L4), syndrome néphronophtise-quadriparésie spastique de l'adulte, hypertrichose et autres syndromes malformatifs : preuves absentes ou très indirectes (niveaux L4-L5), décision **Hold**.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (5 AMM présentées sur 17 au total, toutes annulées.) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Jynarque (tolvaptan) prescribing information, Otsuka America Pharmaceutical, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3febc0a1-9e5a-4ce0-843d-210f21d862c4) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

