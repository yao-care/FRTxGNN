---
layout: default
title: Mizolastine
parent: Prédiction du modèle uniquement (L5)
nav_order: 508
evidence_level: L5
indication_count: 10
---

# Mizolastine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Mizolastine : De la rhinite allergique à la porphyrie aiguë intermittente

## Résumé en Une Phrase

Mizolastine est un antihistaminique de seconde génération (antagoniste sélectif des récepteurs H1), initialement utilisé pour traiter la rhinite allergique et la rhinite vasomotrice.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **porphyrie aiguë intermittente**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction issue uniquement du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique, rhinite vasomotrice (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Porphyrie aiguë intermittente |
| Score de Prédiction TxGNN | 99,76 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré du marché (AMM annulées uniquement) |
| Nombre d'AMM | 2 (0 valide, 2 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la fiche source. D'après les connaissances pharmacologiques générales, mizolastine est un antagoniste sélectif des récepteurs H1 de l'histamine, dont l'efficacité dans les affections allergiques nasales est le fondement de son usage d'origine.

Pour la porphyrie aiguë intermittente, **aucun lien mécanistique n'est établi**. Cette maladie est un trouble de la biosynthèse de l'hème (déficit en PBGD/HMBS), et les antihistaminiques ne sont pas connus pour modifier le métabolisme des porphyrines. Le score élevé (99,76 %) reflète une proximité dans le graphe de connaissances, et non une plausibilité biologique démontrée.

Les neuf autres prédictions suivent la même logique. Il s'agit principalement de troubles du mouvement (troubles moteurs psychogènes, dyskinésie linguo-facio-buccale, tics chroniques, tremblement orthostatique primaire, etc.) ainsi que de maladies métaboliques ou rares (déficit en carbamoyl-phosphate synthétase I). Aucune n'a de mécanisme étayé : mizolastine pénètre peu dans le cerveau et n'a pas d'activité anticholinergique notable.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 64991179 | MIZOLLEN 10 mg, comprimé à libération modifiée (DESMA PHARMA) | Comprimé pelliculé à libération modifiée | Non renseignée | Annulée |
| 65120823 | MIZOCLER 10 mg, comprimé pelliculé à libération modifiée (DESMA PHARMA) | Comprimé pelliculé à libération modifiée | Non renseignée | Annulée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : aucune interaction médicamenteuse cliniquement documentée. La seule entrée disponible concerne la pharmacologie de la cible : mizolastine se lie au récepteur H1 de l'histamine (gène HRH1). Il n'est pas approuvé aux États-Unis.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique, aucune publication, aucun lien mécanistique plausible. De plus, les deux AMM françaises sont annulées et les données de sécurité de la notice sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (ANSM) : élément bloquant pour tout examen de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank) afin d'analyser d'éventuels liens mécanistiques
- Mener une revue de littérature et des études précliniques ciblées pour déterminer si une hypothèse biologique crédible existe pour la porphyrie aiguë intermittente
- Clarifier la disponibilité du produit en France, les AMM étant toutes annulées
- Évaluer, parmi les autres indications prédites, s'il en existe une avec un fondement mécanistique plus solide
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

