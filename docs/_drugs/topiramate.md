---
layout: default
title: Topiramate
parent: Prédiction du modèle uniquement (L5)
nav_order: 773
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "TOPIRAMATE"
predicted_indications: ["trigeminal nerve neoplasm"]
description: "Topiramate : nouvelle indication prédite, Néoplasme du nerf trijumeau (trigeminal nerve neoplasm) (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Topiramate
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

## Topiramate: Néoplasme du nerf trijumeau (trigeminal nerve neoplasm)
{: .text-alpha }

## Résumé en Une Phrase

Le topiramate est un médicament antiépileptique à large spectre, initialement utilisé pour traiter l'épilepsie généralisée tonico-clonique, l'épilepsie partielle et le syndrome de Lennox-Gastaut.
Le modèle TxGNN (apprentissage profond) prédit en tête de classement le **néoplasme du nerf trijumeau** (score très élevé). Ce score provient du modèle et peut refléter des similarités apprises entre maladies voisines, et non une preuve biologique ; il n'existe **aucun essai clinique** ni **aucune publication** à l'appui pour cette indication.
Les autres prédictions du classement sont surtout des **épilepsies réflexes** (épilepsie visuelle, audiogène, de lecture, etc.), proches de l'indication d'origine, avec des preuves indirectes ou précliniques.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Néoplasme du nerf trijumeau (trigeminal nerve neoplasm) |
| Score de Prédiction TxGNN | 0.9970 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 17) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Topiramate (traduction non officielle) : « Les mécanismes précis par lesquels le topiramate exerce ses effets anticonvulsivants et préventifs de la migraine sont inconnus ; cependant, des études précliniques ont révélé quatre propriétés susceptibles de contribuer à l'efficacité du topiramate dans l'épilepsie et le traitement préventif de la migraine. » Texte original en anglais : "The precise mechanisms by which topiramate exerts its anticonvulsant and preventive migraine effects are unknown; however, preclinical studies have revealed four properties that may contribute to topiramate's efficacy for epilepsy and the preventive treatment of migraine." ([DailyMed: Trokendi Xr (topiramate) prescribing information, Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2dc7957e-a3e5-46bb-aa66-f3250f872f5e), version du 2026-10-05 ; consulté le 2026-11-19). D'après les connaissances générales, le topiramate est un antiépileptique à large spectre dont les actions décrites comprennent le blocage des canaux sodiques, le renforcement de la transmission GABA-A, l'antagonisme des récepteurs AMPA/kaïnate et une inhibition faible de l'anhydrase carbonique.

Pour la prédiction principale (néoplasme du nerf trijumeau), **aucun fondement mécanistique établi** n'existe : le topiramate n'a pas d'activité antitumorale reconnue. Le score élevé (0,9970) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises entre maladies voisines, et non une preuve biologique. Tout lien éventuel resterait spéculatif et relèverait plutôt du contrôle symptomatique (douleur neuropathique ou crises associées à la tumeur) que d'un effet sur la tumeur elle-même.

Les autres prédictions (épilepsie visuelle, épilepsie de la lecture, crises audiogènes, etc.) sont mécanistiquement plus plausibles, car ce sont des épilepsies réflexes relevant du spectre des épilepsies déjà traitées. Elles chevauchent toutefois les indications existantes et ne représentent pas un véritable signal de repositionnement.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la prédiction principale (néoplasme du nerf trijumeau).

À titre de contexte, pour les prédictions suivantes du classement, la littérature récupérée est surtout générale (revues sur les antiépileptiques) ou préclinique. Exemples les plus pertinents, rattachés aux crises audiogènes (rang 4) et aux crises de pensée (rang 8) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24570033](https://pubmed.ncbi.nlm.nih.gov/24570033/) | 2014 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Topiramate en traitement additif de l'épilepsie partielle pharmacorésistante |
| [31642054](https://pubmed.ncbi.nlm.nih.gov/31642054/) | 2019 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Topiramate en traitement additif de l'épilepsie focale pharmacorésistante |
| [10666508](https://pubmed.ncbi.nlm.nih.gov/10666508/) | 2000 | Préclinique (animal) | Eur J Pharmacol | Le topiramate antagonise les crises audiogènes chez la souris DBA/2 et potentialise d'autres anticonvulsivants |
| [12581224](https://pubmed.ncbi.nlm.nih.gov/12581224/) | 2003 | Préclinique (animal) | Epilepsia | Effets du topiramate dans deux modèles génétiques d'épilepsie généralisée (GAERS, rat audiogène Wistar AS) |
| [39854828](https://pubmed.ncbi.nlm.nih.gov/39854828/) | 2025 | Revue | Epilepsy Behav | Revue des antiépileptiques dans le syndrome de Lennox-Gastaut, dont le topiramate |

Ces publications soutiennent l'efficacité générale du topiramate dans l'épilepsie, mais n'évaluent pas directement les épilepsies réflexes rares, ni a fortiori le néoplasme du nerf trijumeau.

---

## Informations de Marché en France

Le texte d'indication approuvée n'est pas renseigné. Principales AMM (5 sur 21) :

<!-- review:begin fr-lic-20261106-topiramate-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 17 AMM recensées sont toutes annulées ; le texte d'indication approuvée n'est pas renseigné. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 17 AMM pour ce médicament, dont 17 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-topiramate-1 -->

<!-- review:begin fr-lic-20261124-topiramate-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Principales AMM (5 sur 17) : » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-topiramate-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 68906660 | TOPIRAMATE VIATRIS 200 mg, comprimé pelliculé | Comprimé pelliculé | VIATRIS SANTE | Active |
| 64696702 | TOPIRAMATE ARROW LAB 100 mg, comprimé pelliculé | Comprimé pelliculé | ARROW GENERIQUES | Active |
| 61913385 | EPITOMAX 100 mg, comprimé pelliculé | Comprimé pelliculé | JANSSEN CILAG | Active |
| 64137353 | TOPIRAMATE VIATRIS 50 mg, comprimé pelliculé | Comprimé pelliculé | VIATRIS SANTE | Active |
| 68987922 | EPITOMAX 25 mg, gélule | Gélule | JANSSEN CILAG | Active |
| 63478939 | TOPIRAMATE BGR 50 mg, comprimé pelliculé | Comprimé pelliculé | BIOGARAN | Active |
| 64866909 | TOPIRAMATE BGR 200 mg, comprimé pelliculé | Comprimé pelliculé | BIOGARAN | Active |
| 65109823 | EPITOMAX 200 mg, comprimé pelliculé | Comprimé pelliculé | JANSSEN CILAG | Active |
| 65691302 | TOPIRAMATE ARROW LAB 200 mg, comprimé pelliculé | Comprimé pelliculé | ARROW GENERIQUES | Active |
| 69104026 | EPITOMAX 15 mg, gélule | Gélule | JANSSEN CILAG | Active |
| 62430966 | TOPIRAMATE ARROW LAB 50 mg, comprimé pelliculé | Comprimé pelliculé | ARROW GENERIQUES | Active |
| 69946106 | EPITOMAX 50 mg, comprimé pelliculé | Comprimé pelliculé | JANSSEN CILAG | Active |
| 64738083 | TOPIRAMATE SANDOZ 50 mg, comprimé pelliculé | Comprimé pelliculé | SANDOZ | Active |
| 61572507 | TOPIRAMATE BGR 100 mg, comprimé pelliculé | Comprimé pelliculé | BIOGARAN | Active |
| 68353836 | TOPIRAMATE SANDOZ 100 mg, comprimé pelliculé | Comprimé pelliculé | SANDOZ | Active |
| 69710351 | EPITOMAX 50 mg, gélule | Gélule | JANSSEN CILAG | Active |
| 66961409 | TOPIRAMATE VIATRIS 100 mg, comprimé pelliculé | Comprimé pelliculé | VIATRIS SANTE | Active |
| 61184700 | TOPIRAMATE ACCORD 25 mg, comprimé pelliculé | Comprimé pelliculé | ACCORD HEALTHCARE FRANCE | Abrogée |
| 66096713 | TOPIRAMATE ACCORD 50 mg, comprimé pelliculé | Comprimé pelliculé | ACCORD HEALTHCARE FRANCE | Abrogée |
| 67018272 | TOPIRAMATE ACCORD 200 mg, comprimé pelliculé | Comprimé pelliculé | ACCORD HEALTHCARE FRANCE | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : trouble anxieux, trouble névrotique, trouble dysthymique, maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, maladie diarrhéique, hypertension oculaire, néphrolithiase (dont la susceptibilité liée à SLC26A1), néphropathie uratique aiguë, acidose (dont acidose métabolique), trouble amnésique, amnésie rétrograde.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Majeures : metformine, hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, mépenzolate, méthscopolamine, propanthéline, trospium (notamment les anticholinergiques).
  - Modérées : pioglitazone, morphine, dronabinol, phentermine, métoclopramide, acide phénylbutyrique, nabilone, glibenclamide, phénylbutyrate de glycérol.
- La littérature récupérée signale par ailleurs des effets indésirables psychiatriques et des complications en cas d'utilisation pendant la grossesse.

Les mises en garde officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de securité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (néoplasme du nerf trijumeau) repose uniquement sur un score du modèle TxGNN (apprentissage profond), pouvant refléter des similarités apprises entre maladies voisines et non une preuve biologique, sans essai, sans publication ni logique mécanistique antitumorale ; le niveau de preuve est L5.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Pour le néoplasme du nerf trijumeau : définir une hypothèse biologique précise (effet antitumoral ou simple contrôle symptomatique) et rechercher des données précliniques ou cliniques.
- Les épilepsies réflexes (épilepsie visuelle, audiogène, de lecture, crises de pensée) pourraient être étudiées comme questions de recherche, mais elles recoupent les indications existantes ; clarifier le statut réglementaire du topiramate en France.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « es 17 AMM recensées sont toutes annulées ; l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Trokendi Xr (topiramate) prescribing information, Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2dc7957e-a3e5-46bb-aa66-f3250f872f5e) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

