---
layout: default
title: Piroxicam
parent: Prédiction du modèle uniquement (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam : De l'Indication Originale Non Renseignée au Syndrome de Microphtalmie Colobomateuse avec Dysplasie Rhizomélique

## Résumé en Une Phrase

Le piroxicam est un anti-inflammatoire non stéroïdien (AINS), inhibiteur non sélectif des COX, commercialisé en France. Les données fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de microphtalmie colobomateuse avec dysplasie rhizomélique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette prédiction. Il s'agit d'un signal issu du modèle uniquement, sans lien mécanistique plausible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM fournies |
| Nouvelle Indication Prédite | Syndrome de microphtalmie colobomateuse avec dysplasie rhizomélique |
| Score de Prédiction TxGNN | 99,996 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 13 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le piroxicam est connu comme inhibiteur non sélectif de la cyclo-oxygénase (COX-1 et COX-2). Il réduit la synthèse des prostaglandines, donc l'inflammation et la douleur.

Cette prédiction **n'est pas raisonnable sur le plan mécanistique**. Le syndrome de microphtalmie colobomateuse avec dysplasie rhizomélique est une maladie génétique rare du développement. L'inhibition des COX n'agit pas sur sa physiopathologie. Le score TxGNN très élevé (99,996 %) reste une sortie de modèle, probablement un artefact du graphe de connaissances.

Les neuf autres prédictions en tête de liste sont dans la même situation. Ce sont des dysplasies squelettiques ou malformations congénitales (syndactylie-brachydactylie, dysplasie acromésomélique de type Hunter-Thompson, brachyolmie, pseudoachondroplasie, etc.), plus le syndrome WHIM. Aucune ne présente de lien plausible avec l'inhibition des prostaglandines.

La seule prédiction du classement qui bénéficie d'un début de soutien est l'**arthrite juvénile idiopathique** (rang 10, score 99,93 %). Le mécanisme est biologiquement plausible : réduction de l'inflammation articulaire médiée par les prostaglandines. Des études anciennes testent directement le piroxicam dans cette maladie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le syndrome de microphtalmie colobomateuse avec dysplasie rhizomélique.

À titre de comparaison, voici les publications les plus pertinentes pour l'arthrite juvénile idiopathique (rang 10 du classement, niveau L3) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Revue systématique / méta-analyse en réseau | World J Clin Cases | Comparaison de plusieurs AINS dans l'AIJ ; la méthode optimale n'était pas encore établie |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Revue systématique / méta-analyse en réseau | Indian Pediatr | Efficacité et sécurité comparées de neuf AINS dans l'AIJ |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Essai randomisé | Eur J Rheumatol Inflamm | 26 patients, piroxicam vs naproxène dans l'arthrite rhumatoïde juvénile |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | ECR croisé en double aveugle | Br J Rheumatol | 47 enfants, piroxicam vs naproxène, pas de différence significative entre les deux traitements |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Étude pharmacocinétique | Eur J Clin Pharmacol | Pharmacocinétique à l'état d'équilibre chez 10 enfants atteints de maladies rhumatismales (demi-vie moyenne d'environ 33 h) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67214342 | FELDENE DISPERSIBLE 20 mg | Comprimé dispersible sécable | Non renseignée |
| 68659391 | PIROXICAM BIOGARAN 10 mg | Gélule | Non renseignée |
| 62408891 | PIROXICAM PFIZER 20 mg/1 ml | Solution injectable en ampoule (IM) | Non renseignée |
| 67785736 | PIROXICAM VIATRIS 20 mg | Comprimé dispersible sécable | Non renseignée |
| 69721369 | PIROXICAM TEVA 20 mg/1 ml | Solution injectable (IM) | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction en tête de liste repose uniquement sur le score du modèle (niveau L5), sans essai ni publication et sans lien mécanistique plausible avec l'inhibition des COX.
- Les données de sécurité de la notice ANSM sont absentes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications). Ce point est bloquant.
- Obtenir les données détaillées sur le mécanisme d'action, par exemple via l'API DrugBank.
- Renseigner les indications approuvées de chaque AMM afin d'établir l'indication d'origine.
- Réorienter l'évaluation vers l'arthrite juvénile idiopathique, seule prédiction avec un soutien bibliographique (L3). Il faudrait vérifier si cette indication est déjà approuvée en France et examiner en détail les deux études pédiatriques comparant le piroxicam au naproxène.
- Ne pas poursuivre les prédictions de maladies génétiques rares (dysplasies, malformations, syndrome WHIM) sans nouvelle preuve.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

