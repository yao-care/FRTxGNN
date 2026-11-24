---
layout: default
title: Docusate
parent: Prédiction du modèle uniquement (L5)
nav_order: 252
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Docusate"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia"]
description: "Docusate : nouvelle indication prédite, Syndrome de Plummer-Vinson (Plummer-Vinson syndrome) (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Docusate
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

## Docusate: Syndrome de Plummer-Vinson (Plummer-Vinson syndrome)
{: .text-alpha }

## Résumé en Une Phrase

Docusate est un tensioactif laxatif émollient des selles, dont les indications d'origine répertoriées concernent la constipation et plusieurs formes d'anémie (carence en fer, carence en folates, anémie hypochrome, microcytaire).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Plummer-Vinson**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome de Plummer-Vinson (Plummer-Vinson syndrome) |
| Score de Prédiction TxGNN | 0.9918 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Docusate est (traduction non officielle) : « Laxatif surfactant ». Texte original en anglais : "Surfactant laxative" ([ChEMBL CHEMBL1477036 (docusate): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1477036), CC BY-SA 3.0 ; consulté le 2026-11-19). Sur la base des informations connues, le docusate est un tensioactif émollient des selles ; son usage dans la constipation est établi.

Le syndrome de Plummer-Vinson associe dysphagie, membranes œsophagiennes et anémie ferriprive. Le score provient du modèle TxGNN (deep learning) et peut refléter des similitudes apprises par le modèle entre maladies voisines, et non une preuve biologique.

Le docusate n'a aucun effet connu sur l'absorption du fer, les membranes œsophagiennes ou la dysphagie. Le traitement de ce syndrome repose sur la supplémentation en fer et, si nécessaire, la dilatation endoscopique des membranes. La plausibilité mécanistique est donc faible : la prédiction est à considérer comme un artefact probable du modèle.

Une seconde prédiction du modèle, l'anémie mégaloblastique constitutionnelle indépendante de la vitamine B12 et des folates (score de 0,9915), présente la même limite : aucune preuve clinique ni mécanisme connu dans l'hématopoïèse ou la synthèse de l'ADN.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69281980 | NORGALAX, gel rectal en récipient unidose | Gel | ESSENTIAL PHARMA (M) (MALTE) | Active |
| 68486676 | JAMYLENE 50 mg, comprimé enrobé | Comprimé enrobé | COOPER (ABRÉGÉ DE COOPERATION PHARMACEUTIQUE FRANCAISE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : ulcère gastroduodénal, carence en potassium, drépanocytose, persistance héréditaire de l'hémoglobine fœtale, hyperoxalurie primaire, hémochromatose héréditaire, hémosidérose, trouble du métabolisme du fer, maladie de Wilson, rectocolite ulcéro-hémorragique, maladie inflammatoire chronique de l'intestin, anémie hémolytique, appendicite, gastrite atrophique chronique, neuropathie optique héréditaire de Leber, gastroentérite.
- **Interactions médicamenteuses** (4 identifiées) :
  - Lactulose : modérée
  - Mineral oil (huile minérale) : modérée
  - Phénolphtaléine : modérée
  - Linaclotide : mineure

Les mises en garde et contre-indications de la notice officielle n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et le lien mécanistique est improbable.

<!-- review:begin fr-lic-20261106-docusate-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et le lien mécanistique est improbable. De plus, la seule AMM française est annulée, ce qui limite toute voie de développement pratique. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-docusate-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de sécurité de la notice (mises en garde et contre-indications), indispensables avant tout examen de sécurité
- Les données détaillées sur le mécanisme d'action
- Toute preuve clinique ou publiée reliant le docusate au syndrome de Plummer-Vinson
- Une évaluation de la compatibilité des voies d'administration et de la similarité avec l'indication d'origine, non réalisées à ce stade

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « De plus, la seule AMM française est annulée, ce qui limite toute voie de développement pratique » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé (révisé le 2026-11-20 ; version antérieure conservée dans le journal) | [ChEMBL CHEMBL1477036 (docusate): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1477036) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

