---
layout: default
title: Ivabradine
parent: Prédiction du modèle uniquement (L5)
nav_order: 419
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Ivabradine : nouvelle indication prédite, Hypertrichose (niveau de preuve L5). Indication d'origine : Non renseignée dans les données disponibles"
monitor_inn: "IVABRADINE"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ivabradine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Ivabradine : De l'Indication Originale Non Documentee à l'Hypertrichose

## Resume en Une Phrase

L'ivabradine est un médicament dont l'indication originale n'est pas renseignée dans les données compilées pour ce rapport (les trois AMM françaises recensées sont toutes annulées).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertrichose**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données disponibles |
| Nouvelle Indication Predite | Hypertrichose |
| Score de Prediction TxGNN | 99,79 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, l'ivabradine inhibe le canal HCN (courant « funny » If) du nœud sinusal, ce qui ralentit la fréquence cardiaque.

Aucun lien établi n'existe entre ce mécanisme et le cycle du follicule pilaire ou la régulation de la pousse des poils. Le score élevé de TxGNN est une prédiction issue du graphe de connaissances, probablement due à des voisins de réseau partagés (gènes de canaux ioniques ou cardiovasculaires). Elle n'est étayée par aucune donnée clinique ni bibliographique.

Les autres prédictions du modèle (syndrome d'Ambras, syndromes malformatifs avec atteinte dentaire ou parodontale, syndromes avec malformation de Dandy-Walker, anomalie génétique isolée de la tige pilaire, syndrome néphrogénique d'antidiurèse inappropriée) sont également purement computationnelles, sans essai ni publication. La dernière est la seule présentant un lien physiologique un peu plus concevable (canaux ioniques rénaux), mais il reste spéculatif.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee | Statut |
|---------|------|------|-----------|------|
| 63501124 | PROCORALAN 7,5 mg, comprimé pelliculé (Les Laboratoires Servier) | Comprimé pelliculé | Non renseignée | Annulée |
| 65486532 | IVABRADINE ALTER 7,5 mg, comprimé (Laboratoires Alter) | Comprimé | Non renseignée | Annulée |
| 61952527 | PROCORALAN 5 mg, comprimé pelliculé (Les Laboratoires Servier) | Comprimé pelliculé | Non renseignée | Annulée |

## Considerations de Securite

**Interactions Médicamenteuses** : 100 interactions ont été recensées. Les principales sont présentées ci-dessous (échantillon des données compilées).

- **Majeures** : aprépitant, clarithromycine, dolasétron, palonosétron, cisapride, clotrimazole, granisétron, lévofloxacine, ondansétron, papavérine, cobicistat.
- **Modérées** : famotidine, ranitidine (y compris citrate de bismuth), cimétidine, dexaméthasone, métréleptine, miconazole, nizatidine, troglitazone.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible avec le blocage des canaux HCN.
- Toutes les AMM françaises sont annulées, et les données de sécurité de la notice sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) afin de lever le blocage de sécurité.
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank) et l'indication originale.
- Rechercher des études précliniques ou des cas rapportés reliant l'ivabradine à l'hypertrichose ou aux affections prédites.
- Évaluer la compatibilité de la voie d'administration avec l'indication visée.
- Réévaluer la pertinence de la prédiction : l'absence de lien biologique plausible justifie de ne pas investir davantage sans nouvelles preuves.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

