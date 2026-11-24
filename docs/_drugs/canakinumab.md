---
layout: default
title: Canakinumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 133
evidence_level: L5
indication_count: 9
monitor_inn: "CANAKINUMAB"
predicted_indications: ["hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "periodic fever-infantile enterocolitis-autoinflammatory syndrome", "extracutaneous mastocytoma", "Blau syndrome", "monosomy X", "liver angiosarcoma"]
last_modified_at: 2026-11-24
description: "Canakinumab : nouvelle indication prédite, Infarctus hépatique (hepatic infarction) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Canakinumab
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

## Canakinumab : inhibiteur de l'interleukine-1β → infarctus hépatique (hepatic infarction)
{: .text-alpha }

## Résumé en une phrase

Le canakinumab est un anticorps monoclonal dirigé contre l'interleukine-1β (IL-1β), un médiateur central de l'inflammation.
Le modèle TxGNN prédit qu'il pourrait être utile pour l'**infarctus hépatique (hepatic infarction)**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données locales |
| Nouvelle indication prédite | Infarctus hépatique (hepatic infarction) |
| Score de prédiction TxGNN | 0,9986 |
| Niveau de preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Canakinumab (traduction non officielle) : « Le canakinumab est un anticorps monoclonal humain anti-IL-1β humaine d'isotype IgG1/κ. Le canakinumab se lie à l'IL-1β humaine et neutralise son activité en bloquant son interaction avec les récepteurs de l'IL-1, mais il ne se lie pas à l'IL-1α ni à l'antagoniste du récepteur de l'IL-1 (IL-1ra). » Texte original en anglais : "Canakinumab is a human monoclonal anti-human IL-1β antibody of the IgG1/κ isotype. Canakinumab binds to human IL-1β and neutralizes its activity by blocking its interaction with IL-1 receptors, but it does not bind IL-1α or IL-1 receptor antagonist (IL-1ra)." ([DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e), version du 2026-06-08 ; consulté le 2026-11-19). D'après les informations connues, le canakinumab neutralise l'IL-1β, une cytokine pro-inflammatoire.

Une hypothèse purement spéculative serait que l'inflammation dépendante de l'IL-1β après une lésion ischémique contribue aux dégâts tissulaires hépatiques, et que son blocage pourrait en limiter l'ampleur. Aucune donnée fournie ne confirme ce lien.

La prédiction repose donc uniquement sur le score du modèle. Elle doit être considérée comme une piste de recherche à valider, et non comme un résultat étayé par des preuves cliniques ou mécanistiques.

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée disponible actuellement.

## Informations de marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69541570 | ILARIS 150 mg/ml, solution injectable | Solution injectable | NOVARTIS EUROPHARM (IRLANDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de sécurité

**Interactions médicamenteuses** (100 interactions recensées ; principales listées) :
- **Modérées** : corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisolone, prednisone), simvastatine, apixaban, rivaroxaban, warfarine, dicoumarol, ibritumomab tiuxétan, tositumomab, iobenguane (I-131).
- **Mineures** : sels de zinc (acétate, gluconate, sulfate).

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
La prédiction pour l'infarctus hépatique n'est soutenue par aucun essai ni aucune publication (niveau L5), et aucun mécanisme documenté ne la corrobore.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) du canakinumab
- Mises en garde et contre-indications issues de la notice ANSM
- Données précliniques ou observationnelles reliant l'IL-1β à l'infarctus hépatique
- Revue de la littérature ciblée sur l'ischémie hépatique et l'inhibition de l'IL-1

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

