---
layout: default
title: Benralizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 96
evidence_level: L5
indication_count: 5
monitor_inn: "BENRALIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis"]
last_modified_at: 2026-10-28
description: "Benralizumab : nouvelle indication prédite, Thrombopénie par destruction immunitaire (thrombocytopenia due to immune destruction) (niveau de preuve L5). Indication d'origine : Non renseignée dans les…"
---

# Benralizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Benralizumab : anti-récepteur alpha de l'IL-5 (anticorps monoclonal) → thrombopénie par destruction immunitaire (thrombocytopenia due to immune destruction)
{: .text-alpha }

## Résumé en Une Phrase

Le bénralizumab est un anticorps monoclonal dirigé contre le récepteur alpha de l'interleukine-5, qui élimine les éosinophiles et les basophiles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **thrombopénie par destruction immunitaire (thrombocytopenia due to immune destruction)**,
mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Thrombopénie par destruction immunitaire (thrombocytopenia due to immune destruction) |
| Score de Prédiction TxGNN | 0,9934 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Benralizumab (traduction non officielle) : « Le benralizumab est un anticorps monoclonal humanisé afucosylé (IgG1, kappa) qui se lie directement à la sous-unité alpha du récepteur humain de l'interleukine-5 (IL-5Rα) avec une constante de dissociation de 11 pM. Le récepteur de l'IL-5 est exprimé à la surface des éosinophiles et des basophiles. » Texte original en anglais : "Benralizumab is a humanized afucosylated, monoclonal antibody (IgG1, kappa) that directly binds to the alpha subunit of the human interleukin-5 receptor (IL-5Rα) with a dissociation constant of 11 pM. The IL-5 receptor is expressed on the surface of eosinophils and basophils." ([DailyMed: Fasenra (benralizumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=da6aca1a-19ed-44a4-abb7-696c7d58b784), version du 2026-05-13 ; consulté le 2026-11-19). D'après les informations connues, le bénralizumab cible la sous-unité alpha du récepteur de l'IL-5 (IL5RA) et déplète les éosinophiles et les basophiles par cytotoxicité cellulaire dépendante des anticorps (ADCC).

La thrombopénie immunitaire repose sur la destruction des plaquettes par des auto-anticorps et des lymphocytes T. Aucun lien mécanistique clair avec la déplétion des éosinophiles n'est établi dans les données disponibles. Le score élevé du modèle reste donc une indication computationnelle à interpréter avec prudence, et la plausibilité biologique de cette prédiction est faible en l'état.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63562134 | FASENRA 30 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée dans les données locales |
| 63094493 | FASENRA 30 mg, solution injectable en stylo prérempli | Solution injectable | Non renseignée dans les données locales |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une seule entrée de pharmacologie est répertoriée, correspondant à la cible du médicament (sous-unité alpha du récepteur de l'IL-5). Aucune interaction médicamenteuse cliniquement classée n'est documentée.

Veuillez consulter la notice pour les mises en garde et contre-indications.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication portant sur cette maladie, et sans lien mécanistique évident avec la déplétion des éosinophiles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et justification biologique d'un rôle de l'IL-5Rα dans la thrombopénie immunitaire
- Études précliniques ou observationnelles portant directement sur cette maladie
- Mises en garde et contre-indications issues de la notice ANSM
- Évaluation de sécurité chez des patients ayant une thrombopénie

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Fasenra (benralizumab) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=da6aca1a-19ed-44a4-abb7-696c7d58b784) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

