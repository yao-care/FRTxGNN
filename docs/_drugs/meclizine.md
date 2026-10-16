---
layout: default
title: Meclizine
parent: Prédiction du modèle uniquement (L5)
nav_order: 476
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Meclizine : nouvelle indication prédite, Urticaire allergique (niveau de preuve L5). Indication d'origine : Vertige d'origine centrale"
---

# Meclizine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Méclozine : Du Vertige d'Origine Centrale à l'Urticaire Allergique

## Résumé en Une Phrase

La méclozine est un antihistaminique H1 de première génération à activité anticholinergique centrale, initialement utilisé pour le vertige d'origine centrale et le mal des transports.
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**urticaire allergique**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Vertige d'origine centrale ; mal des transports (selon le graphe de connaissances TxGNN, le texte de l'AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Urticaire allergique |
| Score de Prédiction TxGNN | 99,67 % |
| Niveau de Preuve | L4 (argument mécanistique indirect lié à la classe pharmacologique ; aucune étude spécifique à la méclozine) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la méclozine est un antihistaminique H1 de première génération doté d'une activité anticholinergique centrale. Son efficacité dans le vertige et le mal des transports repose sur cette action centrale.

L'urticaire allergique est une affection médiée par l'histamine, et le blocage des récepteurs H1 est le mécanisme établi du soulagement symptomatique. La prédiction est donc plausible par effet de classe. Le même raisonnement s'applique à l'urticaire au froid, également prédite (score de 99,22 %), pour laquelle les antihistaminiques H1 sont le traitement de première intention.

Toutefois, cet appui est indirect : il est extrapolé d'autres antihistaminiques H1. Les antihistaminiques de seconde génération, recommandés par les lignes directrices, sont déjà disponibles et mieux tolérés (moins de sédation et d'effets anticholinergiques). Cela limite l'intérêt pratique de repositionner la méclozine.

## Autres Indications Prédites (pour information)

| Indication Prédite | Score TxGNN | Niveau de Preuve | Recommandation |
|------|------|------|------|
| Rhume | 99,49 % | L4 | Hold |
| Maladie de la cavité nasale | 99,48 % | L5 | Hold |
| Pharyngite | 99,45 % | L5 | Hold |
| Laryngopharyngite aiguë | 99,37 % | L5 | Hold |
| Urticaire au froid | 99,22 % | L4 | Research Question |

Pour le rhume, l'effet attendu est uniquement symptomatique et modeste (rhinorrhée, éternuements), et il est contrebalancé par la sédation et les effets anticholinergiques. Pour la pharyngite et la laryngopharyngite, l'assèchement des muqueuses pourrait être contre-productif. L'indication « maladie de la cavité nasale » est trop vague pour être évaluée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60456535 | AGYRAX, comprimé sécable (GEN.ORPH) | Comprimé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hyperplasie bénigne de la prostate, glaucome à angle fermé, sténose du pylore, obstruction du col vésical. Elles sont cohérentes avec l'activité anticholinergique du médicament.
- **Interactions médicamenteuses** : 252 interactions recensées. Les plus importantes :
  - **Majeures** : chlorure de potassium, citrate de potassium.
  - **Modérées** (cumul d'effets anticholinergiques ou dépresseurs du système nerveux central) : atropine, hyoscyamine, glycopyrronium, dicyclomine, clidinium, méthscopolamine, mépenzolate, trospium, morphine, opium, lopéramide, métoclopramide, nabilone, éluxadoline, eliglustat, phénylbutyrate de glycérol.

Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'effet de classe des antihistaminiques H1 rend la prédiction pour l'urticaire allergique plausible, mais aucune donnée spécifique à la méclozine n'existe. Le profil de tolérance (sédation, effets anticholinergiques) est défavorable face aux alternatives de seconde génération. De plus, la seule AMM française est annulée, ce qui limite toute voie réglementaire immédiate.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications), lacune bloquante pour tout dépistage de sécurité
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Rechercher des études spécifiques à la méclozine dans l'urticaire (essais, séries de cas)
- Démontrer un avantage potentiel par rapport aux antihistaminiques de seconde génération
- Clarifier la situation réglementaire (AMM annulée) et la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

