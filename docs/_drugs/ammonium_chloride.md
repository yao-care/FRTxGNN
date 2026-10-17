---
layout: default
title: Ammonium Chloride
parent: Prédiction du modèle uniquement (L5)
nav_order: 60
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Ammonium Chloride : nouvelle indication prédite, Laryngopharyngite aiguë (niveau de preuve L5). Indication d'origine : Pharyngite, rhume, rhinopharyngite"
monitor_inn: "Ammonium chloride"
predicted_indications: ["acute laryngopharyngitis", "nasal cavity disease"]
---

# Ammonium Chloride
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

# Chlorure d'ammonium : De la pharyngite à la laryngopharyngite aiguë

## Résumé en Une Phrase

Le chlorure d'ammonium était initialement associé au traitement de la pharyngite, du rhume et de la rhinopharyngite.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **laryngopharyngite aiguë**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pharyngite, rhume, rhinopharyngite (selon le graphe de connaissances ; aucun texte d'indication n'est disponible dans les AMM) |
| Nouvelle Indication Prédite | Laryngopharyngite aiguë |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le chlorure d'ammonium est traditionnellement utilisé comme expectorant, ce qui pourrait fluidifier les sécrétions des voies respiratoires supérieures. Ce lien ne peut toutefois pas être vérifié avec les données compilées pour ce rapport.

La laryngopharyngite aiguë est très proche des indications d'origine (pharyngite, rhinopharyngite, rhume) : toutes sont des affections des voies aériennes supérieures. Le score élevé reflète probablement la proximité avec ces indications connues dans le graphe de connaissances plutôt qu'un véritable signal thérapeutique nouveau.

Il ne s'agit donc pas d'un vrai candidat au repositionnement : l'indication prédite recoupe les usages déjà connus. Une seconde prédiction, « maladie de la cavité nasale » (score 99,94 %), est également de niveau L5 ; il s'agit d'une catégorie anatomique très large, difficile à transformer en hypothèse clinique testable.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les quatre AMM identifiées sont toutes annulées ; aucune n'est valide actuellement. Le texte de l'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63262521 | Solution injectable d'oligo-éléments Aguettant enfants et nourrissons | Solution injectable pour perfusion | Non renseignée |
| 68575185 | Pediaven AP-HP G15 | Solution pour perfusion | Non renseignée |
| 67678175 | Pediaven AP-HP G20 | Solution pour perfusion | Non renseignée |
| 62083608 | Pediaven AP-HP G25 | Solution pour perfusion | Non renseignée |

## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, et non du texte de la notice)** : hypertension, insuffisance hépatique, insuffisance rénale et anurie, épilepsie, insomnie, insuffisance surrénalienne (maladie d'Addison), ulcère gastroduodénal, hyperplasie bénigne de la prostate, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, hypertension oculaire, glaucome à angle fermé, arrêt cardiaque soudain, troubles de la conduction cardiaque, hyperthyroïdie (maladie de Basedow, thyrotoxicose), obstruction du col vésical, œdème pulmonaire, ischémie myocardique, maladie coronarienne, troubles anxieux (agoraphobie, trouble obsessionnel compulsif), entérocolite nécrosante.
- **Interactions Médicamenteuses** : 21 interactions connues.
  - *Modérées* : amphétamine, dextroamphétamine, lisdexamfétamine, métamfétamine, benzphétamine.
  - *Mineures* : éphédrine (y compris nasale), pseudoéphédrine, antidépresseurs tricycliques (amitriptyline, clomipramine, désipramine, doxépine y compris topique, imipramine, nortriptyline, protriptyline, trimipramine), méthadone, méxilétine, flécaïnide.

Les mises en garde de la notice officielle ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et recoupe les indications déjà connues. Le statut de marché (AMM toutes annulées) et la liste étendue de contre-indications du graphe de connaissances renforcent la prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications officielles de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données sur le mécanisme d'action (par exemple via DrugBank)
- Définition d'une hypothèse clinique précise (sous-type de maladie plus étroit, voie d'administration compatible)
- Recherche d'essais cliniques et de publications ciblés sur la laryngopharyngite aiguë
- Examen de l'intérêt réel du repositionnement, vu le chevauchement avec les indications existantes
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

