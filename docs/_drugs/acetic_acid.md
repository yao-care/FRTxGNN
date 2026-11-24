---
layout: default
title: Acetic Acid
parent: Prédiction du modèle uniquement (L5)
nav_order: 20
evidence_level: L5
indication_count: 9
monitor_inn: "acetic acid"
predicted_indications: ["post-bacterial disorder", "postinfectious vasculitis", "post-infectious syndrome", "Chagas cardiomyopathy", "infective urethral stricture", "infection-related hemolytic uremic syndrome", "drug-induced osteoporosis", "pityriasis simplex", "tinea corporis"]
last_modified_at: 2026-11-24
description: "Acetic Acid : nouvelle indication prédite, Trouble post-bactérien (post-bacterial disorder) (niveau de preuve L5). En France, AMM dans la BDPM : 3 (valides : 2)"
---

# Acetic Acid
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

## Acide acétique : antiseptique et acidifiant à usage topique → trouble post-bactérien (post-bacterial disorder)
{: .text-alpha }

## Résumé en Une Phrase

L'acide acétique est un antiseptique et acidifiant à usage topique, dont l'activité antibactérienne est connue.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble post-bactérien (post-bacterial disorder)**,
mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble post-bactérien (post-bacterial disorder) |
| Score de Prédiction TxGNN | 0,9998 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 3) |
| Nombre d'AMM | 3 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Acetic Acid (traduction non officielle) : « L'acide acétique est antibactérien et antifongique ; le propylène glycol est hydrophile et confère une faible tension superficielle ; le chlorure de benzéthonium est un agent tensioactif qui favorise le contact de la solution avec les tissus. » Texte original en anglais : "Acetic acid is antibacterial and antifungal; propylene glycol is hydrophilic and provides a low surface tension; benzethonium chloride is a surface active agent that promotes contact of the solution with tissues." ([DailyMed: acetic acid prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c1c28375-9b03-4590-9d39-ab28403da93d), version du 2026-03-18 ; consulté le 2026-11-19). Sur la base des informations connues, l'acide acétique est un antiseptique et acidifiant topique doté d'une activité antibactérienne.

Un lien plausible avec les troubles post-bactériens (séquelles d'une infection bactérienne) n'est étayé par aucune donnée récupérée. Il s'agit d'une prédiction purement computationnelle, malgré un score très élevé. La similarité avec l'indication d'origine reste à évaluer.

À ce stade, cette piste doit être considérée comme une hypothèse à documenter, et non comme une base de recommandation.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

L'acide acétique est commercialisé en France. Les deux autorisations valides (tableau ci-dessus) sont des produits homéopathiques à une seule substance ; une troisième AMM, DIABENE (67698943), est abrogée.

<!-- review:begin fr-lic-20261124-acetic_acid-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les deux autorisations enregistrées sont des produits homéopathiques à une seule substance. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-acetic_acid-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 68976484 | ACETICUM ACIDUM LEHNING, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH | Comprimé et solution(s) et granules et poudre et pommade | LEHNING | Active |
| 69773711 | ACETICUM ACIDUM BOIRON, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH | Comprimé et solution(s) et granules et poudre et pommade | BOIRON | Active |
| 67698943 | DIABENE, solution buvable en gouttes | Solution buvable en gouttes | LEHNING | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications relevées dans les données de relations médicament-maladie** (hors texte de notice) : porphyrie héréditaire, maladie du métabolisme des porphyrines, porphyrie, infection herpétique (herpès simplex), zona du ganglion géniculé.
- **Interactions médicamenteuses** : aucune interaction retrouvée.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN est très élevé (0,9998), mais il repose uniquement sur le calcul. Aucun essai clinique ni aucune publication ne concerne le trouble post-bactérien, et aucun mécanisme plausible n'est documenté. Le niveau de preuve est donc L5.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA)
- Mises en garde et contre-indications issues de la notice ANSM
- Une définition clinique précise du « trouble post-bactérien » et un lien mécanistique documenté avec l'acide acétique
- Études précliniques ou cliniques portant directement sur cette indication
- Évaluation de la compatibilité des voies d'administration

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: acetic acid prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c1c28375-9b03-4590-9d39-ab28403da93d) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

