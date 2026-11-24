---
layout: default
title: Pembrolizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 584
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Pembrolizumab : nouvelle indication prédite, Fibromatose gingivale (niveau de preuve L5). Indication d'origine : Cancer du poumon non à petites cellules, cancer du poumon…"
monitor_inn: "PEMBROLIZUMAB"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "fibroma of lung", "lung benign neoplasm", "ovarioleukodystrophy", "lung germ cell tumor", "pulmonary sulcus neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Pembrolizumab
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

## Pembrolizumab : Du Cancer du Poumon Non à Petites Cellules à la Fibromatose Gingivale
{: .text-alpha }

## Résumé en Une Phrase

Pembrolizumab est un anticorps monoclonal anti-PD-1, initialement utilisé pour le traitement du cancer du poumon non à petites cellules et du mélanome métastatique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale** (score élevé), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du poumon non à petites cellules, cancer du poumon, mélanome métastatique (le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 0,9940 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Pembrolizumab (traduction non officielle) : « La liaison des ligands de PD-1, PD-L1 et PD-L2, au récepteur PD-1 présent sur les lymphocytes T inhibe la prolifération des lymphocytes T et la production de cytokines. Une surexpression des ligands de PD-1 se produit dans certaines tumeurs et la signalisation par cette voie peut contribuer à l'inhibition de l'immunosurveillance active des tumeurs par les lymphocytes T. […] Le pembrolizumab est un anticorps monoclonal qui se lie au récepteur PD-1 et bloque son interaction avec PD-L1 et PD-L2, levant ainsi l'inhibition de la réponse immunitaire médiée par la voie PD-1, y compris la réponse immunitaire antitumorale. » Texte original en anglais : "Binding of the PD-1 ligands, PD-L1 and PD-L2, to the PD-1 receptor found on T cells, inhibits T cell proliferation and cytokine production. Upregulation of PD-1 ligands occurs in some tumors and signaling through this pathway can contribute to inhibition of active T-cell immune surveillance of tumors. […] Pembrolizumab is a monoclonal antibody that binds to the PD-1 receptor and blocks its interaction with PD-L1 and PD-L2, releasing PD-1 pathway-mediated inhibition of the immune response, including the anti-tumor immune response." ([DailyMed: Keytruda (pembrolizumab) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9333c79b-d487-4538-a9f0-71b91a02b287), version du 2026-10-16 ; consulté le 2026-11-19). Les informations pharmacologiques connues indiquent que pembrolizumab est un anticorps dirigé contre le récepteur PD-1 (CD279, gène *PDCD1*). Il lève le frein immunitaire exercé sur les lymphocytes T et renforce ainsi la réponse antitumorale. Son efficacité est établie dans le cancer du poumon et le mélanome.

**Cette prédiction n'est pas étayée mécanistiquement.** La fibromatose gingivale est une affection fibrotique bénigne, héréditaire ou médicamenteuse. Aucun lien n'est établi avec l'axe PD-1/PD-L1, et aucun essai ni aucune publication ne soutient un rôle du blocage de PD-1 dans cette maladie. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Activer le système immunitaire dans une pathologie bénigne exposerait en outre à des effets indésirables immunologiques sans bénéfice démontré.

À titre de comparaison, parmi les autres prédictions de haut rang, seules les tumeurs pulmonaires malignes (carcinome du hile pulmonaire, tumeur de Pancoast) sont biologiquement plausibles. Elles relèvent toutefois de l'indication déjà approuvée et ne constituent pas un véritable repositionnement.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour la fibromatose gingivale.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la fibromatose gingivale.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 62689214 | KEYTRUDA 25 mg/mL, solution à diluer pour perfusion | Solution à diluer pour perfusion | MERCK SHARP & DOHME (PAYS-BAS) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps anti-PD-1), non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible en monothérapie ; peut augmenter en association à une chimiothérapie |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice (surveillance usuelle des effets immunologiques : fonctions hépatique, thyroïdienne et surrénalienne, NFS) |
| Protection de Manipulation | Veuillez consulter la notice |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** (13 interactions recensées) :
  - **Majeures** : lénalidomide, pomalidomide, thalidomide.
  - **Modérées** : corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisolone, prednisone, méthylprednisolone, déflazacort).
- **Profil de toxicité immunologique** : la littérature rapportée pour d'autres indications décrit des effets indésirables d'origine immunitaire (endocrinopathies, myocardite, myosite, atteintes neurologiques, hyperprogression). Ce risque est particulièrement préoccupant dans une maladie bénigne.

Les mises en garde et contre-indications de la notice n'étant pas disponibles, veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai, aucune publication, aucun lien mécanistique pour la fibromatose gingivale, maladie bénigne pour laquelle le risque immunologique dépasse tout bénéfice spéculatif.

<!-- review:begin fr-lic-20261106-pembrolizumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le modèle (L5) : aucun essai, aucune publication, aucun lien mécanistique pour la fibromatose gingivale, maladie bénigne pour laquelle le risque immunologique dépasse tout bénéfice spéculatif. / Le produit n'a plus d'AMM valide en France (une seule AMM, annulée). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-pembrolizumab-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action détaillé (DrugBank) et analyse d'un éventuel lien PD-1/fibrose gingivale
- Données de la notice ANSM (mises en garde et contre-indications), actuellement bloquantes pour le criblage de sécurité
- Données précliniques démontrant une pertinence biologique avant toute étude clinique
- Clarification du statut réglementaire en France

<!-- review:begin fr-lic-20261106-pembrolizumab-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification du statut réglementaire en France (AMM annulée) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-pembrolizumab-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Le produit n'a plus d'AMM valide en France (une seule AMM, annulée) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulée) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Keytruda (pembrolizumab) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9333c79b-d487-4538-a9f0-71b91a02b287) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

