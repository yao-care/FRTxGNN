---
layout: default
title: Talc
parent: Prédiction du modèle uniquement (L5)
nav_order: 730
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Talc : nouvelle indication prédite, Maladie thrombotique (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "TALC"
predicted_indications: ["thrombotic disease", "exostosis", "rheumatoid arthritis", "bronchitis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "vein disease", "fibromyalgia", "myositis fibrosa"]
drugbank_id: DB09511
---

# Talc
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

## Talc : D'une Pâte à Usage Local à la Maladie Thrombotique (prédiction à très faible plausibilité)
{: .text-alpha }

## Résumé en Une Phrase

Le talc (TALC) figurait dans une pâte pour application locale (ALOPLASTINE), dont l'AMM est aujourd'hui annulée ; aucune indication originale n'est renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **maladie thrombotique**, mais aucun essai clinique n'est recensé et la littérature (**11 publications**, essentiellement des cas cliniques) décrit le talc comme une **cause** de thrombose, et non comme un traitement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Maladie thrombotique |
| Score de Prédiction TxGNN | 0,9985 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé (autorisations annulées : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 0) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Talc (traduction non officielle) : « On pense que le talc instillé dans la cavité pleurale entraîne une réaction inflammatoire. Cette réaction favorise l’adhérence de la plèvre viscérale et de la plèvre pariétale afin d’empêcher la réaccumulation d’air ou de liquide pleural. » Texte original en anglais : "Talc instilled into the pleural cavity is thought to result in an inflammatory reaction. This reaction promotes adherence of the visceral and parietal pleura to prevent reaccumulation of pleural air or fluid." ([DailyMed: Steritalc 2G (talc) prescribing information, Novatech SA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c94e51d9-beef-4b06-e053-2a95a90a754a), version du 2025-06-25 ; consulté le 2026-11-19). Le talc (silicate de magnésium) est connu comme excipient et comme agent à usage local ; son indication d'origine n'est pas documentée dans les données d'AMM disponibles.

En réalité, la prédiction paraît **peu plausible** sur le plan mécanistique. Les publications retrouvées décrivent le talc injecté par voie intraveineuse (chez des usagers de drogues) comme responsable d'embolie pulmonaire, de granulomatose, d'hypertension pulmonaire angiothrombotique et de micro-embolies rétiniennes et cérébrales. Le score élevé (0,9985) reflète vraisemblablement une association dans le réseau de connaissances avec la pathologie thrombotique, et non un effet thérapeutique.

Les autres indications prédites (exostose, polyarthrite rhumatoïde, bronchite, déficit en cofacteur II de l'héparine, excès de facteur V, déficit en antithrombine de type 2, maladie veineuse, fibromyalgie, myosite fibreuse) ne reposent pas non plus sur des preuves thérapeutiques : aucune littérature, ou seulement des cas et associations fortuites, et des données plutôt orientées vers un risque (par exemple bronchite professionnelle chez les travailleurs exposés au talc).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Les publications ci-dessous sont des cas cliniques, séries de cas ou revues ; aucune ne démontre un bénéfice thérapeutique du talc.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [7756380](https://pubmed.ncbi.nlm.nih.gov/7756380/) | 1995 | Revue | Current Opinion in Oncology | Complications thoraciques du cancer ; syndrome cave supérieur par thrombose lié aux dispositifs d'accès veineux |
| [7387487](https://pubmed.ncbi.nlm.nih.gov/7387487/) | 1980 | Cas clinique | Archives of Neurology | Infarctus bulbaires et granulomatose au talc chez une usagère de drogues par voie intraveineuse |
| [6893924](https://pubmed.ncbi.nlm.nih.gov/6893924/) | 1981 | Cas clinique | Arch Pathol Lab Med | Granulomatose pulmonaire par injection de cellulose ; la thrombose est la lésion vasculaire principale |
| [4854601](https://pubmed.ncbi.nlm.nih.gov/4854601/) | 1974 | Série de cas | J Can Assoc Radiol | Granulomatose au talc et hypertension pulmonaire angiothrombotique chez des toxicomanes |
| [4692998](https://pubmed.ncbi.nlm.nih.gov/4692998/) | 1973 | Cas clinique | Am J Med Sci | Micro-embolisation rétinienne et cérébrale de talc chez un usager de drogues |
| [1784766](https://pubmed.ncbi.nlm.nih.gov/1784766/) | 1991 | Non classé | Rev Clin Esp | Granulomatose pulmonaire angiothrombotique chez des toxicomanes intraveineux (talc en cause) |
| [23700302](https://pubmed.ncbi.nlm.nih.gov/23700302/) | 2013 | Cas clinique | Dtsch Med Wochenschr | Insuffisance cardiaque droite aiguë après injection intraveineuse d'héroïne et de flunitrazépam broyé |
| [8537192](https://pubmed.ncbi.nlm.nih.gov/8537192/) | 1995 | Cohorte | Int Ophthalmol | Zone avasculaire fovéale élargie dans l'occlusion veineuse rétinienne ; rétinopathie au talc citée |
| [35648447](https://pubmed.ncbi.nlm.nih.gov/35648447/) | 2022 | Cas clinique | Tex Heart Inst J | Syndrome de Trousseau chez une patiente avec cancer du côlon occulte (sans lien direct avec le talc) |
| [8010794](https://pubmed.ncbi.nlm.nih.gov/8010794/) | 1994 | Série de cas | Ann Thorac Surg | Chirurgie thoracoscopique du chylothorax |
| [41646593](https://pubmed.ncbi.nlm.nih.gov/41646593/) | 2026 | Cas clinique | Cureus | Pneumothorax récidivant après pneumonectomie, prise en charge sous ECMO |

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 62744504 | ALOPLASTINE, pâte pour application locale | Pâte pour application | LABORATOIRES MACORS | Archivée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Points relevés dans la littérature compilée : le talc est associé à des événements thrombo-emboliques et granulomateux après injection intraveineuse, à une morbidité respiratoire (bronchite, sténose des voies aériennes, pneumoconiose) en cas d'inhalation, et à des granulomes après application sur une plaie chirurgicale. Aucune interaction médicamenteuse n'a été retrouvée.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score du modèle est élevé, mais aucune étude clinique n'existe et la littérature indique que le talc provoque la thrombose plutôt qu'il ne la traite. Le niveau de preuve est L4, et aucune AMM n'est actuellement valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications), actuellement manquante et bloquante pour l'évaluation de sécurité
- Obtenir les données sur le mécanisme d'action (via DrugBank)
- Disposer d'une étude préclinique ou clinique démontrant un effet antithrombotique du talc, ce qui paraît improbable au vu des données actuelles
- Reconsidérer l'intérêt du dossier ; la recherche devrait plutôt porter sur le profil de risque du talc

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Steritalc 2G (talc) prescribing information, Novatech SA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c94e51d9-beef-4b06-e053-2a95a90a754a) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

