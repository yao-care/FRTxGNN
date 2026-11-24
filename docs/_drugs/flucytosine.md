---
layout: default
title: Flucytosine
parent: Prédiction du modèle uniquement (L5)
nav_order: 332
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Flucytosine : nouvelle indication prédite, Maladie osseuse de Paget (bone Paget disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "FLUCYTOSINE"
predicted_indications: ["bone Paget disease"]
drugbank_id: DB01099
---

# Flucytosine
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

## Flucytosine : De l'antifongique à la Maladie osseuse de Paget (bone Paget disease)
{: .text-alpha }

## Résumé en Une Phrase

La flucytosine est un antimycosique de la famille des pyrimidines fluorées, commercialisée en France sous le nom d'Ancotil.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie osseuse de Paget**,
mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction, qui repose uniquement sur le score du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Maladie osseuse de Paget (bone Paget disease) |
| Score de Prédiction TxGNN | 0,9904 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Clinical Pharmacology » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Flucytosine (traduction non officielle) : « La flucytosine est captée par les organismes fongiques par l'intermédiaire de l'enzyme cytosine perméase. À l'intérieur de la cellule fongique, la flucytosine est rapidement convertie en fluorouracile par l'enzyme cytosine désaminase. Le fluorouracile exerce son activité antifongique par sa conversion ultérieure en plusieurs métabolites actifs, qui inhibent la synthèse protéique en étant incorporés de façon erronée dans l'ARN fongique ou interfèrent avec la biosynthèse de l'ADN fongique par l'inhibition de l'enzyme thymidylate synthétase. » Texte original en anglais : "Flucytosine is taken up by fungal organisms via the enzyme cytosine permease. Inside the fungal cell, flucytosine is rapidly converted to fluorouracil by the enzyme cytosine deaminase. Fluorouracil exerts its antifungal activity through the subsequent conversion into several active metabolites, which inhibit protein synthesis by being falsely incorporated into fungal RNA or interfere with the biosynthesis of fungal DNA through the inhibition of the enzyme thymidylate synthetase." ([DailyMed: Ancobon (flucytosine) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aea0df00-a88c-4a16-abcf-750f3ff2004e), version du 2022-02-02 ; consulté le 2026-11-19). Sur la base des connaissances générales, la flucytosine est un antimycosique qui est converti par la cytosine désaminase des champignons en 5-fluorouracile, lequel perturbe la synthèse de l'ARN et de l'ADN fongiques.

La maladie osseuse de Paget est un trouble du remodelage osseux lié à une dérégulation de l'activité des ostéoclastes (souvent associée à des variants de SQSTM1). Les cellules humaines étant largement dépourvues de cytosine désaminase, **aucun lien mécanistique évident** n'apparaît entre le mode d'action de la flucytosine et cette maladie.

Le score élevé du modèle TxGNN (deep learning), 0,9904, correspond à un lien purement computationnel. Il peut refléter des similarités apprises par le modèle entre maladies proches, et non une preuve biologique. Cette prédiction doit donc être considérée avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67250203 | ANCOTIL 1 POUR CENT, solution pour perfusion | Solution pour perfusion | VIATRIS MEDICAL | Active |
| 68758674 | ANCOTIL 500 mg, comprimé | Comprimé | VIATRIS MEDICAL | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe PrimeKG, et non texte de la notice) : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, pyo-uretère, déficit en potassium, thrombopénie, leucopénie, agranulocytose, neutropénie (y compris formes congénitales et idiopathiques de l'adulte), syndrome de Kostmann, hématopoïèse cyclique, anémie aplasique (acquise et autres formes).
- **Interactions médicamenteuses** : 85 interactions recensées. Principales :
  - **Majeure** : déférasirox n'est pas concerné ; la déféripone présente une interaction de niveau **majeur**.
  - **Modérée** : amphotéricine B (formes conventionnelle, lipidique, liposomale et sulfate de cholestéryle), mésalazine, balsalazide, olsalazine, sulfasalazine, vancomycine, kanamycine, néomycine, streptomycine, polymyxine B, bacitracine, déférasirox, pentamidine, ibuprofène, iobenguane (I-131), chlorure de strontium Sr-89.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible.

<!-- review:begin fr-lic-20261106-flucytosine-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible. De plus, les AMM françaises sont toutes annulées et le profil hématologique, rénal et hépatique du médicament appelle à la prudence. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 2 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-flucytosine-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) et hypothèse biologique reliant la flucytosine à la maladie de Paget
- Notice officielle de l'ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Études précliniques ou revue de la littérature apportant un premier signal d'efficacité
- Clarification de l'indication d'origine et de la situation réglementaire actuelle
- Évaluation de la compatibilité des voies d'administration pour la nouvelle indication

<!-- review:begin fr-lic-20261106-flucytosine-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification de l'indication d'origine et de la situation réglementaire actuelle (AMM annulées) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 2 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-flucytosine-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « De plus, les AMM françaises sont toutes annulées et le profil hématologique, rénal et hépatique du médicament appelle à la prudence » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Ancobon (flucytosine) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aea0df00-a88c-4a16-abcf-750f3ff2004e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

