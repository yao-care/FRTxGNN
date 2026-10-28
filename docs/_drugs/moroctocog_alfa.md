---
layout: default
title: Moroctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 515
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
description: "Moroctocog Alfa : nouvelle indication prédite, Trouble primaire de la libération plaquettaire (primary release disorder of platelets) (niveau de preuve L5). Indication d'origine : Non renseignée dans…"
---

# Moroctocog Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Moroctocog Alfa: Trouble primaire de la libération plaquettaire (primary release disorder of platelets)
{: .text-alpha }

## Résumé en Une Phrase

Moroctocog alfa est un facteur VIII de coagulation recombinant (délété du domaine B), initialement utilisé pour le traitement de l'hémophilie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble primaire de la libération plaquettaire**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 0.9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 5 sur 5) |
| Nombre d'AMM | 5 (valides : 5) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, moroctocog alfa est un facteur VIII recombinant dont l'efficacité dans l'hémophilie repose sur le remplacement du facteur VIII déficient.

Le lien avec la nouvelle indication est faible. Le trouble primaire de la libération plaquettaire est un défaut intrinsèque de la fonction plaquettaire (sécrétion), que le remplacement du facteur VIII ne corrige pas. Le score élevé (0,9997) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, probablement liées à l'association commune « trouble hémorragique », et non une preuve biologique ni un mécanisme démontré.

Les autres indications prédites par le modèle présentent le même problème :

| Rang | Indication prédite | Score TxGNN | Plausibilité mécanistique |
|------|------|------|------|
| 2 | Pseudo-maladie de von Willebrand | 0,9997 | Faible : défaut de GPIbα plaquettaire ; lien ténu via l'axe VWF-FVIII |
| 3 | Thrombasthénie de Glanzmann | 0,9996 | Faible : déficit d'intégrine αIIbβ3 ; prise en charge par transfusion plaquettaire et FVIIa recombinant |
| 4 | Déficit acquis en facteur de coagulation | 0,9988 | La plus plausible en théorie, mais les auto-anticorps inhibiteurs neutralisent le FVIII perfusé ; catégorie large et hétérogène |
| 5 | Syndrome de Scott | 0,9986 | Faible : défaut de TMEM16F (ANO6), le FVIII ne restaure pas la surface plaquettaire procoagulante |
| 6 | Diathèse hémorragique par défaut de récepteur du collagène | 0,9973 | Faible : défaut de GPVI ou α2β1 |
| 7 | Trouble hémorragique par thrombopénie constitutionnelle | 0,9972 | Très faible : saignement lié au nombre/à la fonction plaquettaire |
| 8 | « Flood factor deficiency » | 0,9911 | Indéterminée : entité non reconnue, possible artefact de données ou d'ontologie, à vérifier |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64968807 | REFACTO AF 2000 UI | Poudre et solvant pour solution injectable en seringue préremplie | Non renseignée (AMM active) |
| 60106606 | REFACTO AF 250 UI | Poudre et solvant pour solution injectable en seringue préremplie | Non renseignée (AMM active) |
| 62981909 | REFACTO AF 1000 UI | Poudre et solvant pour solution injectable en seringue préremplie | Non renseignée (AMM active) |
| 66743830 | REFACTO AF 3000 UI | Poudre et solvant pour solution injectable en seringue préremplie | Non renseignée (AMM active) |
| 60937230 | REFACTO AF 500 UI | Poudre et solvant pour solution injectable en seringue préremplie | Non renseignée (AMM active) |

Le titulaire de ces AMM est PFIZER EUROPE MA EEIG (Belgique).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle, sans essai clinique ni publication, et le mécanisme du facteur VIII ne correspond pas aux défauts plaquettaires visés. Aucune AMM n'est en vigueur en France et les données de sécurité sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice de l'ANSM (lacune bloquante pour tout examen de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Vérification de l'entité « flood factor deficiency » avant toute évaluation
- Pour la piste la plus plausible (déficit acquis en facteur de coagulation) : revue de la littérature et évaluation de l'impact des inhibiteurs
- Données précliniques ou cliniques démontrant un bénéfice dans l'une des indications prédites
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

