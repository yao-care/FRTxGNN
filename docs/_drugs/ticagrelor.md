---
layout: default
title: Ticagrelor
parent: Prédiction du modèle uniquement (L5)
nav_order: 760
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "ticagrelor"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
description: "Ticagrelor : nouvelle indication prédite, Artériosclérose intracrânienne (intracranial arteriosclerosis) (niveau de preuve L5). En France, AMM dans la BDPM : 12 (valides : 12)"
---

# Ticagrelor
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

## Ticagrelor: Artériosclérose intracrânienne (intracranial arteriosclerosis)
{: .text-alpha }

## Résumé en Une Phrase

Le ticagrélor est un antiagrégant plaquettaire initialement utilisé pour le traitement du syndrome coronarien aigu et des maladies artérielles périphériques.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**artériosclérose intracrânienne**,
avec **2 essais cliniques** (dont un essai de Phase 3 toujours en cours) et **2 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Artériosclérose intracrânienne (intracranial arteriosclerosis) |
| Score de Prédiction TxGNN | 0.9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 12 sur 12) |
| Nombre d'AMM | 12 (valides : 12) |
| Décision Recommandée | Proceed with Guardrails |

> Remarque : le niveau L2 est celui attribué dans les données compilées pour ce rapport. Il reste fragile : l'essai de Phase 3 (CAPTIVA) est en cours, sans résultats, et le ticagrélor n'y est pas le seul bras expérimental.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ticagrelor (traduction non officielle) : « Le ticagrélor et son principal métabolite interagissent de manière réversible avec le récepteur P2Y 12 de l'ADP plaquettaire pour empêcher la transduction du signal et l'activation plaquettaire. Le ticagrélor et son métabolite actif sont approximativement équipotents. » Texte original en anglais : "Ticagrelor and its major metabolite reversibly interact with the platelet P2Y 12 ADP-receptor to prevent signal transduction and platelet activation. Ticagrelor and its active metabolite are approximately equipotent." ([DailyMed: Brilinta (ticagrelor) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7b3f443-e83d-4bf2-0e96-023448fed9a8), version du 2026-05-07 ; consulté le 2026-11-19). Sur la base des informations connues, le ticagrélor est un antagoniste réversible du récepteur plaquettaire P2Y12, qui réduit l'agrégation plaquettaire. Son efficacité dans le syndrome coronarien aigu est établie, et il pourrait mécanistiquement être applicable à d'autres maladies athérothrombotiques.

L'artériosclérose intracrânienne partage avec les maladies coronariennes et périphériques un processus athérothrombotique : rupture ou érosion de plaque, activation plaquettaire, puis thrombose. Un antiagrégant puissant comme le ticagrélor est donc une hypothèse pertinente, d'autant que le traitement standard actuel (clopidogrel + aspirine) laisse persister un risque élevé de récidive d'AVC jusqu'à 12 mois.

Des données indirectes vont dans le même sens : l'essai CHANCE-2 (PMID 34708996) montre un bénéfice du ticagrélor par rapport au clopidogrel chez les porteurs d'allèles CYP2C19 à perte de fonction après AVC ou AIT. Ces données ne sont toutefois pas spécifiques à la maladie intracrânienne.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) (CAPTIVA) | Phase 3 | Actif, ne recrute plus | 1683 | Rivaroxaban, ticagrélor ou les deux comparés au clopidogrel pour réduire à 1 an les AVC ischémiques, hémorragies intracérébrales ou décès vasculaires ; pas de résultats publiés |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | Non applicable | En recrutement | 100 | Étude pilote : sélection d'un inhibiteur de P2Y12 guidée par le génotype vs clopidogrel dans la maladie athéroscléreuse intracrânienne symptomatique |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohorte | J Neurointerv Surg | Ticagrélor 60 mg deux fois par jour + aspirine 81 mg comparé au schéma aspirine-clopidogrel lors d'un stenting intracrânien |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Article de conception d'essai | Int J Stroke | Conception et avancement précoce de l'essai CAPTIVA, qui cherche à déterminer si d'autres associations antithrombotiques sont supérieures à clopidogrel + aspirine dans la sténose intracrânienne symptomatique |

## Informations de Marché en France

Le médicament est commercialisé : voir l'Aperçu rapide pour le nombre et le statut des AMM. Le texte des indications approuvées n'est pas renseigné.

<!-- review:begin fr-lic-20261124-ticagrelor-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « 11 AMM valides sur 11. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-ticagrelor-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 61128160 | TICAGRELOR ZYDUS 90 mg, comprimé pelliculé | Comprimé pelliculé | ZYDUS FRANCE | Active |
| 64794751 | TICAGRELOR VIATRIS 90 mg, comprimé pelliculé | Comprimé pelliculé | VIATRIS SANTE | Active |
| 65532093 | TICAGRELOR BIOGARAN 90 mg, comprimé pelliculé | Comprimé pelliculé | BIOGARAN | Active |
| 61645948 | TICAGRELOR EVOLUGEN 90 mg, comprimé pelliculé | Comprimé pelliculé | EVOLUPHARM | Active |
| 62051838 | TICAGRELOR KRKA 90 mg, comprimé pelliculé | Comprimé pelliculé | KRKA (SLOVENIE) | Active |
| 64746646 | BRILIQUE 90 mg, comprimé orodispersible | Comprimé orodispersible | ASTRAZENECA AB | Active |
| 60044649 | TICAGRELOR EG 90 mg, comprimé pelliculé | Comprimé pelliculé | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 69133266 | TICAGRELOR SANDOZ 90 mg, comprimé pelliculé | Comprimé pelliculé | SANDOZ | Active |
| 65416772 | TICAGRELOR ZENTIVA 90 mg, comprimé pelliculé | Comprimé pelliculé | ZENTIVA FRANCE | Active |
| 61661991 | TICAGRELOR TEVA 90 mg, comprimé pelliculé | Comprimé pelliculé | TEVA (PAYS-BAS) | Active |
| 61958462 | BRILIQUE 90 mg, comprimé pelliculé | Comprimé pelliculé | ASTRAZENECA AB | Active |
| 67382735 | TICAGRELOR ARROW 90 mg, comprimé pelliculé | Comprimé pelliculé | ARROW GENERIQUES | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie hépatique, maladie de la vésicule biliaire, hémorragie intracrânienne. Ce dernier point est particulièrement important pour une indication cérébrovasculaire, où le risque hémorragique est un critère de jugement de CAPTIVA.
- **Interactions médicamenteuses** : 423 interactions recensées. Parmi les principales :
  - **Majeure** : clarithromycine.
  - **Modérées** : acide acétylsalicylique, morphine (retard d'action du ticagrélor oral), aprépitant, dexaméthasone, budésonide, simvastatine, miconazole, saxagliptine, cisapride, clotrimazole, rolapitant, élisglustat, nitisinone.
  - **Mineures** : naloxégol, prucalopride.

Pour les mises en garde détaillées, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- L'hypothèse mécanistique est cohérente et un essai de Phase 3 de grande taille est en cours, mais sans résultats ; le ticagrélor n'est pas l'unique agent testé et les données directes restent limitées.
- Le statut réglementaire français et le risque hémorragique, notamment intracrânien, imposent la prudence.

<!-- review:begin fr-lic-20261106-ticagrelor-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le statut réglementaire français (toutes AMM annulées) et le risque hémorragique, notamment intracrânien, imposent la prudence. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ticagrelor-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats de CAPTIVA (fin prévue en janvier 2027), en particulier le bras ticagrélor.
- Données détaillées sur le mécanisme d'action.
- Informations de sécurité issues de la notice (mises en garde et contre-indications) et clarification du statut des AMM en France.
- Critères de sélection des patients (statut CYP2C19, risque hémorragique) et plan de surveillance des saignements.

**Note sur les autres prédictions :** l'« maladie ischémique » (rang 4, L1) correspond essentiellement à l'usage cardiovasculaire déjà établi du ticagrélor et ne constitue pas un véritable repositionnement. Les autres indications prédites (artériosclérose de Mönckeberg, priapisme, syndrome de May-Thurner, livedo reticularis, occlusion vasculaire mésentérique, ectasie vasculaire, angiodysplasie, thromboembolie veineuse) ne disposent pas de preuves suffisantes (L4-L5) et sont à mettre en attente. L'angiodysplasie, source de saignements digestifs, est en outre en contradiction avec le profil de sécurité d'un antiagrégant.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (toutes AMM annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Brilinta (ticagrelor) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7b3f443-e83d-4bf2-0e96-023448fed9a8) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

