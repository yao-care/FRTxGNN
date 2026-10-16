---
layout: default
title: Roxadustat
parent: Prédiction du modèle uniquement (L5)
nav_order: 683
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Roxadustat : nouvelle indication prédite, Syndrome de l'œil sec (niveau de preuve L5). Indication d'origine : Anémie réfractaire"
---

# Roxadustat
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Roxadustat : De l'anémie réfractaire au syndrome de l'œil sec

## Résumé en Une Phrase

Roxadustat est un inhibiteur de la prolyl-hydroxylase du facteur induit par l'hypoxie (HIF-PH), initialement utilisé pour traiter l'anémie réfractaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de l'œil sec**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Anémie réfractaire (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Syndrome de l'œil sec |
| Score de Prédiction TxGNN | 99,51 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 5 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier compilé. D'après les informations connues, roxadustat inhibe les prolyl-hydroxylases (EGLN1-3), ce qui stabilise HIF-1α et HIF-2α. Cette stabilisation stimule la production d'érythropoïétine, d'où son utilisation dans l'anémie liée à l'insuffisance rénale chronique. L'EMA l'a approuvé dans cette indication en août 2021.

Sur le plan théorique, l'activation de HIF pourrait influencer la réponse à l'hypoxie de la cornée, la réparation épithéliale et l'inflammation de la surface oculaire. Toutefois, ce lien reste spéculatif : aucune donnée clinique ou bibliographique ne le confirme, et le score élevé du modèle (0,995) ne renseigne pas sur le sens de l'effet.

Par ailleurs, une activation systémique de HIF soulève des préoccupations théoriques (angiogenèse, thrombose) peu compatibles avec une affection bénigne de la surface oculaire. La similarité avec l'indication d'origine n'a pas pu être évaluée.

## Autres Indications Prédites (à titre d'information)

| Rang | Indication | Score TxGNN | Niveau de Preuve | Commentaire |
|------|------|------|------|------|
| 2 | Maladie osseuse de Paget | 99,12 % | L5 | Rôle de HIF dans le remodelage osseux, mais lien spéculatif et sens de l'effet incertain |
| 3 | Dentinogenèse imparfaite | 99,06 % | L5 | Aucun mécanisme clair ; probablement une proximité dans le graphe de connaissances |
| 4 | Carcinome épidermoïde | 99,02 % | L5 | L'activation de HIF est associée à la progression tumorale : risque potentiel plutôt que bénéfice |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 5 AMM du produit EVRENZO (Astellas Pharma Europe, Pays-Bas) sont toutes annulées. Le texte des indications approuvées n'est pas disponible.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69086973 | EVRENZO 70 mg | Comprimé pelliculé | Annulée |
| 66917067 | EVRENZO 20 mg | Comprimé pelliculé | Annulée |
| 65259762 | EVRENZO 50 mg | Comprimé pelliculé | Annulée |
| 67935673 | EVRENZO 150 mg | Comprimé pelliculé | Annulée |
| 63274908 | EVRENZO 100 mg | Comprimé pelliculé | Annulée |

## Considérations de Sécurité

- **Interactions et pharmacologie** : une interaction pharmacologique est répertoriée avec la cible EGLN2 (egl-9 family hypoxia inducible factor 2), cohérente avec le mécanisme d'inhibition des HIF-prolyl-hydroxylases. Aucun niveau de gravité n'est précisé.
- **Préoccupations théoriques** : l'activation systémique de HIF pourrait favoriser l'angiogenèse et la thrombose, et être défavorable dans les contextes tumoraux (notamment le carcinome épidermoïde).

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées, qui n'ont pas pu être obtenues pour ce rapport.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Les données de sécurité issues de la notice sont absentes, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), étape bloquante pour le criblage de sécurité
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank)
- Réaliser une revue de la littérature et des études précliniques sur le rôle de HIF dans l'œil sec
- Évaluer la compatibilité de voie d'administration (une voie topique oculaire serait plus adaptée qu'une voie systémique)
- Clarifier le statut réglementaire en France, toutes les AMM étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

