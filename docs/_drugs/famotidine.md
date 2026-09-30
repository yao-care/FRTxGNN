---
layout: default
title: Famotidine
parent: Preuves modérées (L3-L4)
nav_order: 126
evidence_level: L4
indication_count: 10
---

# Famotidine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Famotidine : De l'Ulcère Peptique au Reflux Duodéno-Gastrique

## Résumé en Une Phrase

La famotidine est un antagoniste des récepteurs H2 de l'histamine, connu pour réduire l'acidité gastrique et utilisé classiquement dans les ulcères gastroduodénaux (d'après la littérature, car les AMM françaises ne renseignent pas de texte d'indication).
Le modèle TxGNN prédit qu'elle pourrait être utile dans le **reflux duodéno-gastrique**.
Cette piste repose aujourd'hui sur **0 essai clinique** et **2 publications**, toutes deux de faible niveau de preuve.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM ; usage classique dans les ulcères gastroduodénaux d'après la littérature |
| Nouvelle Indication Prédite | Reflux duodéno-gastrique |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, la famotidine appartient à la classe des antagonistes H2. Elle diminue la sécrétion d'acide gastrique, et son efficacité dans les maladies liées à l'acidité (ulcère) est documentée.

Le lien avec le reflux duodéno-gastrique est **indirect et symptomatique**. Bloquer les récepteurs H2 réduit l'acidité et peut limiter les lésions causées par le contenu duodénal qui remonte dans l'estomac. En revanche, la famotidine n'agit ni sur le reflux biliaire ni sur la motricité duodéno-gastrique, qui sont les causes du reflux.

Le score TxGNN très élevé traduit surtout la proximité du médicament avec les maladies gastroduodénales dans le graphe de connaissances. Il ne démontre pas une efficacité sur la cause du reflux.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Étude clinique (patients en réanimation ; conception peu claire) | World J Gastroenterol | Étude de l'effet de la famotidine sur le reflux gastro-œsophagien et duodéno-gastro-œsophagien, et de ses mécanismes possibles. Les résultats chiffrés ne figurent pas dans l'extrait disponible. |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Étude clinique / article de synthèse | Eksp Klin Gastroenterol | Évaluation de la famotidine 20 mg 2 fois par jour aux stades précoces de la maladie de reflux gastroduodénal (stades 0 et 1 de Savary-Miller modifiée). Les résultats chiffrés ne figurent pas dans l'extrait disponible. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 67557907 | FAMOTIDINE EG 40 mg, comprimé pelliculé | Comprimé pelliculé |
| 60005856 | FAMOTIDINE EG 20 mg, comprimé pelliculé | Comprimé pelliculé |

Les deux AMM appartiennent à EG LABO - Laboratoires Eurogenerics. Le texte d'indication approuvée n'est pas renseigné dans les données reçues.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique, et seulement deux publications de faible niveau de preuve, sans résultats chiffrés disponibles. Le mécanisme n'est que symptomatique (baisse de l'acidité) et ne traite pas la cause du reflux.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde et contre-indications de la notice ANSM (manque bloquant pour toute évaluation de sécurité).
- Compléter les données de mécanisme d'action (MOA), par exemple via l'API DrugBank.
- Retrouver les résultats détaillés des deux publications, puis chercher des essais contrôlés ciblant le reflux duodéno-gastrique.

**À noter :** d'autres indications prédites pour la famotidine sont bien mieux étayées que celle-ci. C'est le cas de la **maladie ulcéreuse peptique** (11 essais cliniques, niveau L1, décision « Proceed with Guardrails », avec la réserve que les inhibiteurs de la pompe à protons pourraient être supérieurs pour prévenir les récidives d'ulcère liées à l'aspirine). C'est aussi le cas de l'**ulcère peptique actif** et de la **gastroduodénite** (niveau L2). Ces pistes méritent d'être évaluées en priorité.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

