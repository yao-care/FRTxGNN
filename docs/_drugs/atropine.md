---
layout: default
title: Atropine
parent: Preuves modérées (L3-L4)
nav_order: 81
evidence_level: L4
indication_count: 2
last_modified_at: 2026-11-12
description: "Atropine : nouvelle indication prédite, Migraine (migraine disorder) (niveau de preuve L4). Indication d'origine : Non renseignée dans les AMM disponibles"
monitor_inn: "ATROPINE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Atropine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **2** 
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

## Atropine : Du Domaine Anticholinergique (indication d'origine non précisée) à la Migraine
{: .text-alpha }

## Résumé en Une Phrase

L'atropine est un antagoniste muscarinique non sélectif ; les données compilées pour ce rapport ne précisent pas son indication d'origine dans les AMM françaises.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **migraine** (*migraine disorder*), avec **0 essai clinique** et **11 publications** (surtout précliniques, revues et cas cliniques) sans aucune étude directe chez des patients migraineux.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM disponibles |
| Nouvelle Indication Prédite | Migraine (*migraine disorder*) |
| Score de Prédiction TxGNN | 0,9956 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 7) |
| Nombre d'AMM | 7 (valides : 7) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques générales, l'atropine est un antagoniste non sélectif des récepteurs muscariniques de l'acétylcholine. Son indication d'origine n'est pas documentée ici, car les AMM ne contiennent aucun texte d'indication.

La littérature préclinique relie la signalisation cholinergique à la physiopathologie de la migraine :
- une modulation cholinergique via les mastocytes méningés dans l'inflammation neurogène (modèle de rat) ;
- la stimulation du ganglion sphénopalatin parasympathique, qui provoque une extravasation de protéines plasmatiques dans la dure-mère (rat) ;
- une implication cholinergique centrale dans l'antinociception.

Le blocage muscarinique pourrait donc, en théorie, réduire l'inflammation neurogène d'origine parasympathique. Toutefois, aucune étude ne teste directement l'atropine chez des patients migraineux. Le score élevé de TxGNN (0,9956) reste une prédiction computationnelle.

**Point de vigilance :** pour la sous-forme « migraine avec aura du tronc cérébral » (score 0,9942, niveau L5, Hold), une seule étude sur le néocortex de souris montre que l'activation cholinergique inhibe la dépression corticale envahissante. Un antagoniste muscarinique comme l'atropine pourrait donc ne pas aider, voire s'opposer à ce mécanisme protecteur.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Revue | J Appl Toxicol | Pharmacologie de l'anisodamine, dérivé naturel de l'atropine, moins puissant et moins toxique ; aucune donnée d'efficacité dans la migraine |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Préclinique/Revue | Eur J Neurosci | Rôle de la modulation cholinergique via les mastocytes méningés dans l'inflammation neurogène de la migraine (modèle de rat) |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Observation clinique | Cephalalgia | Chez 4 patients atteints d'hémicrânie paroxystique chronique, l'atropine systémique a réduit nettement la sudation, le larmoiement et la sécrétion nasale liés aux crises |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Préclinique (animal) | Exp Neurol | La stimulation du ganglion sphénopalatin parasympathique induit une extravasation plasmatique dans la dure-mère du rat |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Préclinique (animal) | J Pharmacol Exp Ther | Le système cholinergique central participe à l'antinociception induite par le sumatriptan |
| [40590589](https://pubmed.ncbi.nlm.nih.gov/40590589/) | 2024 | Cas clinique | Pain Med Case Rep | Syndrome de la tête tombante après traitement par toxine botulique chez un patient avec migraines chroniques et sclérose en plaques |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Préclinique (in vitro) | Br J Pharmacol | L'ergotamine et la dihydroergotamine sont de puissants agonistes des récepteurs 5-HT1C (plexus choroïde de porcelet) |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Préclinique (in vitro) | Br J Pharmacol | Inhibition de la relaxation induite par la nicotine dans l'artère basilaire de cobaye par certains analgésiques |

Les publications restantes (cas de glaucome et de myopie liés au topiramate, cas de myocarde sidéré) sont d'une pertinence très limitée et ne sont pas détaillées.

<!-- review:begin fr-lic-20261106-atropine-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Deux AMM supplémentaires, également annulées, existent (Atropine Alcon 0,5 % et 0,3 %, collyres). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 7 AMM pour ce médicament, dont 7 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-atropine-1 -->

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63667263 | Atropine (sulfate) Lavoisier 0,25 mg/1 ml | Solution injectable | Non renseignée (AMM active) |
| 61397901 | Atropine (sulfate) Lavoisier 0,50 mg/ml | Solution injectable | Non renseignée (AMM active) |
| 66063364 | Atropine (sulfate) Aguettant 1 mg/mL | Solution injectable | Non renseignée (AMM active) |
| 69984085 | Atropine Alcon 1 pour cent | Collyre | Non renseignée (AMM active) |
| 61883472 | Atropine (sulfate) Lavoisier 1 mg/ml | Solution injectable | Non renseignée (AMM active) |

---

## Considérations de Sécurité

**Interactions médicamenteuses** (100 interactions recensées ; principales ci-dessous) :
- **Modérées** : toxine botulique de type A, fentanyl, chlorphéniramine, acébutolol, dihydrocodéine, codéine, tramadol, acétylcholine, aclidinium, acrivastine, éthanol, alfentanil, galantamine, phényltoloxamine, amantadine, amitriptyline, hyoscyamine, lopéramide.
- **Mineures** : paracétamol, hydrochlorothiazide.

Ces interactions reflètent surtout des effets anticholinergiques additifs et une dépression du système nerveux central. Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur un score computationnel et des données précliniques indirectes, sans essai clinique ni étude chez les patients migraineux.
- Les informations de sécurité officielles sont absentes.
- Pour la migraine avec aura du tronc cérébral, le mécanisme suggère même un possible effet défavorable.

<!-- review:begin fr-lic-20261106-atropine-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les AMM françaises sont toutes annulées et les informations de sécurité officielles sont absentes. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 7 AMM pour ce médicament, dont 7 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-atropine-2 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (bloquant pour le criblage de sécurité).
- Les données détaillées sur le mécanisme d'action (via DrugBank).
- Les indications d'origine de l'atropine.
- Des études précliniques ou cliniques précoces testant directement l'atropine dans la migraine, avec évaluation de la faisabilité de la voie d'administration.
- Une analyse du rapport bénéfice/risque, notamment des effets anticholinergiques systémiques.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Deux AMM supplémentaires, également annulées, existent (Atropine Alcon 0,5 % et 0,3 %, collyres) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « es AMM françaises sont toutes annulées et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

