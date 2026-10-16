---
layout: default
title: Droperidol
parent: Prédiction du modèle uniquement (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Droperidol : nouvelle indication prédite, Syndrome de Gilles de la Tourette (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
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

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Dropéridol : De l'Indication Originale Non Renseignée au Syndrome de Gilles de la Tourette

## Résumé en Une Phrase

Le dropéridol est un neuroleptique de la famille des butyrophénones, administré par voie injectable. Les données compilées pour ce rapport ne précisent pas son indication originale en France.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Gilles de la Tourette**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction (preuve de niveau L5).
Parmi les autres prédictions, la **céphalée/migraine** (1 essai terminé prématurément, 19 publications) et le **trouble bipolaire de type maniaque** (11 publications) sont les mieux documentées.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Syndrome de Gilles de la Tourette |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 10 (toutes annulées) |
| Décision Recommandée | Hold |

> **Note :** la prédiction classée n°1 par TxGNN n'est pas la mieux soutenue par les données. Les prédictions n°7 (céphalée) et n°3 (manie) sont étayées par la littérature ; elles sont présentées dans la section « Autres prédictions notables ».

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, le dropéridol est une butyrophénone dotée d'un puissant effet antagoniste des récepteurs dopaminergiques D2.

Le syndrome de Gilles de la Tourette est traité par d'autres antagonistes D2 (halopéridol, pimozide). La prédiction est donc plausible sur le plan mécanistique. En revanche, aucun essai ni publication ne l'étaye pour le dropéridol. De plus, le risque d'allongement de l'intervalle QT constitue une préoccupation majeure pour un traitement chronique.

### Autres prédictions notables

| Maladie prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|
| Céphalée | 99,47 % | L3 | L'antagonisme D2 et l'effet antiémétique sont utiles dans la migraine aiguë. Soutien surtout par des revues, des recommandations et des études observationnelles. |
| Trouble bipolaire maniaque | 99,82 % | L3 | Preuves principalement pour l'agitation et la psychose aiguës, pas pour la manie en tant que telle. |
| Trichotillomanie | 99,89 % | L5 | Rationnel dopaminergique limité, aucune donnée clinique. |
| TDAH (y compris type inattentif) | 99,54 % à 99,68 % | L5 | Lien spéculatif, antagonisme opposé à l'approche par stimulants. |
| Syndrome néphrogénique d'antidiurèse inappropriée | 99,63 % | L5 | Aucun lien plausible, probablement un artefact du graphe. |
| Rhume, hypertrichose, trouble spécifique du développement | 99,39 % à 99,46 % | L5 | Aucun mécanisme crédible ni donnée clinique. |

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

Les 10 AMM identifiées sont toutes annulées. Le texte des indications approuvées n'est pas renseigné. Les 5 premières sont listées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68810459 | DROPERIDOL AGUETTANT 5 mg/2 ml (I.M.) | Solution injectable | Non renseignée |
| 67888889 | DROPERIDOL AGUETTANT 1,25 mg/ml (I.V.) | Solution injectable | Non renseignée |
| 69560873 | DROPERIDOL KALCEKS 1,25 mg/mL | Solution injectable | Non renseignée |
| 66682612 | DROPERIDOL PANPHARMA 5 mg/2 ml (IM) | Solution injectable | Non renseignée |
| 63578074 | DROPERIDOL AGUETTANT 2,5 mg/1 ml (I.V.) | Solution injectable | Non renseignée |

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
- Pour le syndrome de Gilles de la Tourette, la prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et le risque d'allongement du QT est un frein majeur pour un usage chronique. Toutes les AMM françaises sont aujourd'hui annulées.
- Si une piste doit être explorée, la **céphalée/migraine aiguë aux urgences** (L3, plusieurs ECR et revues publiés) est la plus solide. Elle relève d'une question de recherche plutôt que d'une décision d'engagement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le texte de la notice (mises en garde, contre-indications) auprès de l'ANSM, un blocage pour tout examen de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Clarifier l'indication originale et les raisons de l'annulation des AMM.
- Pour la migraine : analyse critique des ECR publiés (PMID 12552051 et 11781912) et évaluation du rapport bénéfice/risque cardiaque (QT) à faible dose.
- Pour le syndrome de Gilles de la Tourette : revue ciblée de la littérature, puis évaluation de la sécurité cardiaque en usage répété avant tout essai.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

