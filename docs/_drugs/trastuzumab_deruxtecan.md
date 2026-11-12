---
layout: default
title: Trastuzumab Deruxtecan
parent: Prédiction du modèle uniquement (L5)
nav_order: 780
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Trastuzumab Deruxtecan : nouvelle indication prédite, Ostéoporose médicamenteuse (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "trastuzumab deruxtecan"
predicted_indications: ["drug-induced osteoporosis"]
---

# Trastuzumab Deruxtecan
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

## Trastuzumab déruxtécan : De l'indication originale non renseignée à l'ostéoporose médicamenteuse
{: .text-alpha }

## Résumé en Une Phrase

Trastuzumab déruxtécan (ENHERTU) est un conjugué anticorps-médicament ciblant HER2, utilisé dans les cancers exprimant HER2. L'indication originale n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**ostéoporose médicamenteuse**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Ostéoporose médicamenteuse |
| Score de Prédiction TxGNN | 0,9931 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le trastuzumab déruxtécan est un anticorps-médicament conjugué dirigé contre HER2, portant une charge utile inhibitrice de la topoisomérase I (déruxtécan, dérivé de l'exatécan). Son usage concerne les cancers exprimant HER2.

**Cette prédiction n'est pas étayée sur le plan biologique.** Les voies du métabolisme osseux (RANK/RANKL, Wnt/sclérostine, régulation des ostéoblastes et ostéoclastes) ne sont pas des cibles connues de ce médicament. Le score très élevé (0,9931) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

De plus, la charge utile cytotoxique et les toxicités connues du médicament (pneumopathie interstitielle, myélosuppression, nausées/vomissements) rendent un effet protecteur osseux peu plausible. Les traitements oncologiques associés (suppression ovarienne, corticoïdes) pourraient au contraire favoriser la perte osseuse. La similarité avec l'indication originale n'a pas pu être évaluée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63648081 | ENHERTU 100 mg, poudre pour solution à diluer pour perfusion (statut : active) | Poudre pour solution à diluer pour perfusion | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Conjugué anticorps-médicament (thérapie ciblée) avec charge utile cytotoxique inhibitrice de la topoisomérase I |
| Risque de Myélosuppression | Moyen à élevé (myélosuppression rapportée parmi les toxicités connues du médicament) |
| Classification d'Émétogénicité | Moyenne (nausées/vomissements parmi les toxicités connues) |
| Éléments de Surveillance | NFS, fonction hépatique et rénale, surveillance respiratoire (pneumopathie interstitielle) |
| Protection de Manipulation | Suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

Veuillez consulter la notice pour les mises en garde et contre-indications.

**Interactions médicamenteuses :** 42 interactions ont été recensées, dont les principales d'après les données compilées :

- **Majeures** : défériprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pégol, cladribine, léflunomide, natalizumab
- **Modérées** : palifermine, chlorure de strontium Sr-89, roflumilast, chloramphénicol, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, diméthyl fumarate, niraparib

Beaucoup concernent des immunosuppresseurs ou des agents myélosuppresseurs, avec un risque additif d'immunosuppression et de toxicité hématologique.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique crédible n'existe entre ce médicament cytotoxique et l'ostéoporose.

<!-- review:begin fr-lic-20261106-trastuzumab_deruxtecan-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique crédible n'existe entre ce médicament cytotoxique et l'ostéoporose. L'AMM française est de plus annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-trastuzumab_deruxtecan-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications), bloquant pour l'étape de sécurité
- Obtenir les données sur le mécanisme d'action et l'indication originale
- Clarifier le statut réglementaire en France
- Démontrer un lien biologique plausible avec le métabolisme osseux, par des études précliniques
- Réexaminer la pertinence de cette prédiction, dont le score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises entre maladies apparentées, non une preuve biologique

<!-- review:begin fr-lic-20261106-trastuzumab_deruxtecan-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier le statut réglementaire en France (AMM annulée) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-trastuzumab_deruxtecan-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « L'AMM française est de plus annulée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulée) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

