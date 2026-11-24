---
layout: default
title: Droperidol
parent: Prédiction du modèle uniquement (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "droperidol"
predicted_indications: ["Tourette syndrome", "trichotillomania", "manic bipolar affective disorder", "attention deficit hyperactivity disorder, inattentive type", "nephrogenic syndrome of inappropriate antidiuresis", "attention deficit-hyperactivity disorder", "headache disorder", "common cold", "hypertrichosis (disease)", "specific developmental disorder"]
description: "Droperidol : nouvelle indication prédite, Syndrome de Gilles de la Tourette (Tourette syndrome) (niveau de preuve L5). En France, AMM dans la BDPM : 12 (valides : 9)"
---

# Droperidol
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

## Droperidol: Syndrome de Gilles de la Tourette (Tourette syndrome)
{: .text-alpha }

## Résumé en Une Phrase

Le dropéridol est un neuroleptique de la famille des butyrophénones, administré par voie injectable. Les données compilées pour ce rapport ne précisent pas son indication originale en France.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Gilles de la Tourette**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction (preuve de niveau L5).
Parmi les autres prédictions, la **céphalée/migraine** (1 essai terminé prématurément, 19 publications) et le **trouble bipolaire de type maniaque** (11 publications) sont les mieux documentées.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome de Gilles de la Tourette (Tourette syndrome) |
| Score de Prédiction TxGNN | 0.9989 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 9 sur 12) |
| Nombre d'AMM | 12 (valides : 9) |
| Décision Recommandée | Hold |

> **Note :** la prédiction classée n°1 par TxGNN n'est pas la mieux soutenue par les données. Les prédictions n°7 (céphalée) et n°3 (manie) sont étayées par la littérature ; elles sont présentées dans la section « Autres prédictions notables ».

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Droperidol est (traduction non officielle) : « Antagoniste des récepteurs de la sérotonine 2a (5-HT2a) ; antagoniste des récepteurs dopaminergiques de type D2 ». Texte original en anglais : "Serotonin 2a (5-HT2a) receptor antagonist; D2-like dopamine receptor antagonist" ([ChEMBL CHEMBL1108 (droperidol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1108), CC BY-SA 3.0 ; consulté le 2026-11-19). Sur la base des connaissances pharmacologiques générales, le dropéridol est une butyrophénone dotée d'un puissant effet antagoniste des récepteurs dopaminergiques D2.

Le syndrome de Gilles de la Tourette est traité par d'autres antagonistes D2 (halopéridol, pimozide). La prédiction est donc plausible sur le plan mécanistique. En revanche, aucun essai ni publication ne l'étaye pour le dropéridol. De plus, le risque d'allongement de l'intervalle QT constitue une préoccupation majeure pour un traitement chronique.

### Autres prédictions notables

| Maladie prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|
| Céphalée | 0,9947 | L3 | L'antagonisme D2 et l'effet antiémétique sont utiles dans la migraine aiguë. Soutien surtout par des revues, des recommandations et des études observationnelles. |
| Trouble bipolaire maniaque | 0,9982 | L5 | Preuves principalement pour l'agitation et la psychose aiguës, pas pour la manie en tant que telle. |
| Trichotillomanie | 0,9989 | L5 | Rationnel dopaminergique limité, aucune donnée clinique. |
| TDAH (y compris type inattentif) | 0,9954 à 0,9968 | L5 | Lien spéculatif, antagonisme opposé à l'approche par stimulants. |
| Syndrome néphrogénique d'antidiurèse inappropriée | 0,9963 | L5 | Aucun lien plausible : le score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises entre maladies proches, pas une preuve biologique. |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour le syndrome de Gilles de la Tourette.

À titre indicatif, un essai existe pour la céphalée (prédiction n°7) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01406860](https://clinicaltrials.gov/study/NCT01406860) | Non applicable | Terminé prématurément | 19 | Dropéridol versus métoclopramide + diphénhydramine dans les céphalées primaires aux urgences. Effectif trop faible pour conclure sur l'efficacité. |

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour le syndrome de Gilles de la Tourette.

À titre indicatif, voici les publications les plus pertinentes pour les deux prédictions documentées.

**Céphalée / migraine**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12552051](https://pubmed.ncbi.nlm.nih.gov/12552051/) | 2003 | ECR | Neurology | Traitement de la migraine aiguë par dropéridol, essai randomisé en double aveugle contre placebo |
| [11781912](https://pubmed.ncbi.nlm.nih.gov/11781912/) | 2002 | ECR | Am J Emerg Med | Efficacité du dropéridol intramusculaire dans la migraine aiguë |
| [25416184](https://pubmed.ncbi.nlm.nih.gov/25416184/) | 2015 | Revue | Ann Pharmacother | Sécurité et efficacité du dropéridol dans la migraine aiguë |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Revue | Headache | Évaluation des preuves de l'American Headache Society sur les traitements de la migraine aiguë |
| [9237411](https://pubmed.ncbi.nlm.nih.gov/9237411/) | 1997 | Cohorte | Headache | Étude pilote de dropéridol IV chez 35 patients en état de mal migraineux ou migraine réfractaire |
| [32839811](https://pubmed.ncbi.nlm.nih.gov/32839811/) | 2020 | Revue | Am J Health Syst Pharm | Réintégration du dropéridol aux urgences : sécurité, indications, posologie |

**Trouble bipolaire maniaque / agitation**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27976370](https://pubmed.ncbi.nlm.nih.gov/27976370/) | 2016 | Revue Cochrane | Cochrane Database Syst Rev | Dropéridol pour l'agitation ou l'agressivité liées à la psychose |
| [15495037](https://pubmed.ncbi.nlm.nih.gov/15495037/) | 2004 | Revue Cochrane | Cochrane Database Syst Rev | Dropéridol dans la psychose aiguë |
| [9789713](https://pubmed.ncbi.nlm.nih.gov/9789713/) | 1998 | Séries de cas / revue | Clin Neuropharmacol | Trois cas de manie mixte réfractaire améliorés par le dropéridol oral |
| [321727](https://pubmed.ncbi.nlm.nih.gov/321727/) | 1977 | Essai en double aveugle contre placebo | J Nerv Ment Dis | Moins de recours à l'halopéridol de renfort dans le groupe dropéridol chez 41 patients agités |
| [10460140](https://pubmed.ncbi.nlm.nih.gov/10460140/) | 1999 | Rapport de cas | Ann Emerg Med | Détresse respiratoire après dropéridol pour une agitation (signal de sécurité) |

---

## Informations de Marché en France

Le texte des indications approuvées n'est pas renseigné.

<!-- review:begin fr-lic-20261106-droperidol-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 10 AMM identifiées sont toutes annulées. Le texte des indications approuvées n'est pas renseigné. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 10 AMM pour ce médicament, dont 9 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-droperidol-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 68810459 | DROPERIDOL AGUETTANT 5 mg/2 ml, solution injectable (I.M.) | Solution injectable | AGUETTANT | Active |
| 67888889 | DROPERIDOL AGUETTANT 1,25 mg/ml, solution injectable (I.V.) | Solution injectable | AGUETTANT | Active |
| 69560873 | DROPERIDOL KALCEKS 1,25 mg/mL, solution injectable | Solution injectable | AS KALCEKS (LETTONIE) | Active |
| 63578074 | DROPERIDOL AGUETTANT 2,5 mg/1 ml, solution injectable (I.V.) | Solution injectable | AGUETTANT | Active |
| 64057843 | DROPERIDOL HIKMA 2,5 mg/mL, solution injectable | Solution injectable | HIKMA FARMACEUTICA (PORTUGAL) | Active |
| 67226227 | DROPERIDOL KALCEKS 2,5 mg/mL, solution injectable | Solution injectable | AS KALCEKS (LETTONIE) | Active |
| 67738409 | DROPERIDOL PANPHARMA 0,5 mg/ml, solution injectable | Solution injectable | PANPHARMA | Active |
| 67527433 | DROPERIDOL PANPHARMA 2,5 mg/ml, solution injectable | Solution injectable | PANPHARMA | Active |
| 61646847 | DROLEPTAN 1,25 mg/2,5 ml, solution injectable | Solution injectable | SUBSTIPHARM | Active |
| 66682612 | DROPERIDOL PANPHARMA 5 mg/2 ml, solution injectable (IM) | Solution injectable | PANPHARMA | Archivée |
| 60828455 | DROPERIDOL ARROW 2,5 mg/1 ml, solution injectable (IV) | Solution injectable | EUGIA PHARMA (MALTA) (MALTE) | Abrogée |
| 61756877 | DROPERIDOL ARROW 5 mg/2 ml, solution injectable (IM) | Solution injectable | EUGIA PHARMA (MALTA) (MALTE) | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de la notice) :
  - Cardiovasculaires : syndrome du QT long (familial ou non), torsades de pointes, hypertension, hypotension orthostatique, syndrome de tachycardie orthostatique posturale, atrophie multisystématisée.
  - Neurologiques : maladies des noyaux gris centraux, dystonie focale de la main, blépharospasme.
  - Respiratoires : BPCO, insuffisance respiratoire.
  - Psychiatriques : troubles anxieux, troubles névrotiques, dysthymie, abus ou dépendance à des substances.
  - Autres : insuffisance rénale, maladie hépatique, maladie de la vésicule biliaire, maladie inflammatoire de l'intestin, déficit en potassium, hyperplasie bénigne de la prostate, phéochromocytome.
- **Interactions médicamenteuses** : 194 interactions recensées. Parmi les exemples de niveau **majeur** : hydrocortisone, amphotéricine B (et ses formes lipidiques), morphine, naloxone, clarithromycine, dolasétron, acide picosulfurique, polyéthylène glycol avec électrolytes. Parmi les exemples de niveau **modéré** : famotidine, épinéphrine, lopéramide, lorcasérine, bisacodyl, dronabinol, huile de ricin.
- **Signal de sécurité de la littérature** : détresse respiratoire rapportée après dropéridol pour agitation (PMID 10460140). Le risque d'allongement du QT, mis en avant dans l'analyse mécanistique, est une préoccupation majeure pour un usage chronique.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le syndrome de Gilles de la Tourette, la prédiction repose uniquement sur le modèle TxGNN (apprentissage profond) (L5), sans essai ni publication, et le risque d'allongement du QT est un frein majeur pour un usage chronique. Le médicament est commercialisé en France : 9 AMM valides sur 10.
- Si une piste doit être explorée, la **céphalée/migraine aiguë aux urgences** (L3, plusieurs ECR et revues publiés) est la plus solide. Elle relève d'une question de recherche plutôt que d'une décision d'engagement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le texte de la notice (mises en garde, contre-indications) auprès de l'ANSM, un blocage pour tout examen de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Clarifier l'indication originale et les raisons de l'annulation des AMM.
- Pour la migraine : analyse critique des ECR publiés (PMID 12552051 et 11781912) et évaluation du rapport bénéfice/risque cardiaque (QT) à faible dose.
- Pour le syndrome de Gilles de la Tourette : revue ciblée de la littérature, puis évaluation de la sécurité cardiaque en usage répété avant tout essai.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 10 AMM identifiées sont toutes annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé (révisé le 2026-11-20 ; version antérieure conservée dans le journal) | [ChEMBL CHEMBL1108 (droperidol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1108) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

