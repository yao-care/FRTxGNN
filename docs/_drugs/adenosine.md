---
layout: default
title: Adenosine
parent: Prédiction du modèle uniquement (L5)
nav_order: 28
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Adenosine : nouvelle indication prédite, Bloc de branche (terme obsolète) (niveau de preuve L5). Indication d'origine : Tachycardie ventriculaire"
monitor_inn: "adenosine"
predicted_indications: ["obsolete bundle branch block"]
---

# Adenosine
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

## Adénosine : De la Tachycardie Ventriculaire au Bloc de Branche (terme obsolète)
{: .text-alpha }

## Résumé en Une Phrase

L'adénosine est un antiarythmique injectable, rattaché dans la base de connaissances du modèle à la **tachycardie ventriculaire**.
Le modèle TxGNN lui prédit une efficacité potentielle dans le **bloc de branche (terme désormais obsolète)**, avec un score très élevé.
Cette prédiction repose uniquement sur le calcul : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tachycardie ventriculaire (d'après le graphe de connaissances, le texte d'indication des AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Bloc de branche (terme obsolète) |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances générales, l'adénosine ralentit la conduction du nœud auriculo-ventriculaire (AV) en agissant sur les récepteurs A1. Cette propriété explique son usage dans les tachycardies.

**Cette prédiction paraît toutefois peu plausible sur le plan mécanistique.** Le bloc de branche est un trouble de conduction situé en aval du nœud AV, dans le système His-Purkinje. Ralentir la conduction au niveau du nœud AV ne corrigerait pas ce type de défaut et pourrait même aggraver un trouble de conduction.

Le libellé « obsolète » indique un terme d'ontologie abandonné, qui peut renvoyer à des notions actuelles de troubles de la conduction. Le score élevé reflète donc probablement un artefact du graphe ou de l'ontologie plutôt qu'un véritable signal thérapeutique. Aucune similarité avec l'indication d'origine n'a pu être évaluée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Autre Hypothèse Prédite Plus Documentée : la Tachycardie Ventriculaire Polymorphe Catécholaminergique (TVPC)

Le modèle propose aussi la **tachycardie ventriculaire polymorphe catécholaminergique** (score 99,42 %, niveau de preuve **L4**, statut « question de recherche »). Elle est signalée ici car elle repose sur un peu plus de données que la prédiction principale.

**Raisonnement mécanistique.** La TVPC provient d'une fuite de calcium du réticulum sarcoplasmique, qui déclenche des post-dépolarisations tardives et une activité déclenchée. L'adénosine et l'ATP, via les récepteurs A1, s'opposent à cette activité déclenchée dépendante de l'AMPc et des catécholamines. Cela donne un mécanisme plausible pour interrompre ces arythmies.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Rapport de cas | Heart Rhythm | L'adénosine triphosphate (ATP) a interrompu une tachycardie ventriculaire bidirectionnelle chez un patient atteint de TVPC (seule preuve directe) |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Revue (consensus d'experts) | Europace | Rôle diagnostique des tests de provocation pharmacologique en électrophysiologie cardiaque, dont l'adénosine |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Revue | J Assoc Physicians India | Reconnaissance et prise en charge des tachycardies ventriculaires sur cœur structurellement normal |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Revue | Paediatr Anaesth | Arythmies pédiatriques, à l'usage des anesthésistes |

Les autres publications recensées portent sur la physiopathologie de la TVPC et sur des modèles génétiques ou cellulaires (préclinique), sans traitement par adénosine.

**Limites importantes :**
- Le rapport de cas concerne l'**ATP** et non l'adénosine elle-même.
- L'interruption d'un épisode aigu ne démontre pas un bénéfice thérapeutique à long terme.
- La prise en charge standard de la TVPC repose sur les bêta-bloquants, la flécaïnide, le défibrillateur implantable (DAI) ou la dénervation sympathique.

---

## Informations de Marché en France

Le texte d'indication n'est pas renseigné pour ces AMM. Aucune n'est actuellement valide.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 67537114 | ADENOSINE HIKMA 6 mg/2 mL | Solution injectable | Annulée |
| 61855583 | ADENOSCAN 30 mg/10 mL | Solution pour perfusion | Annulée |
| 60710318 | KRENOSIN 6 mg/2 mL | Solution injectable | Annulée |
| 63052537 | ADENOSINE MEDISOL 6 mg/2 mL | Solution injectable | Annulée |

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications relevées dans le graphe de connaissances** (et non dans la notice) :
  - Maladies respiratoires : bronchopneumopathie chronique obstructive (BPCO, dont forme sévère à début précoce), asthme (y compris intrinsèque et allergique), emphysème pulmonaire, insuffisance respiratoire.
  - Maladies cardiaques ou valvulaires : sténose aortique (dont supravalvulaire) et maladie de la valve aortique, sténose mitrale, insuffisance de la valve pulmonaire, syndrome coronarien aigu, maladie coronarienne, péricardite.
  - Troubles de la conduction ou du rythme : bloc auriculo-ventriculaire, maladie du sinus (dont forme familiale).
  - Autres : hypotension, maladie du système nerveux autonome, syndrome de Horner.
- **Interactions médicamenteuses** : 138 interactions sont recensées. Les principales sont :
  - **Majeures** : cisapride, dolasétron, papavérine.
  - **Modérées** : famotidine, clarithromycine, granisétron, lévofloxacine, ondansétron, palonosétron.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour l'indication principale prédite (bloc de branche, terme obsolète), le score élevé repose uniquement sur le calcul, sans essai ni publication. Le mécanisme de l'adénosine ne soutient pas cette prédiction, qui est probablement un artefact d'ontologie.
- Les quatre AMM françaises sont annulées. L'hypothèse alternative de la TVPC (niveau L4) ne repose que sur un rapport de cas portant sur l'ATP, ce qui en fait au mieux une question de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- Faire correspondre le terme obsolète à un concept actuel de trouble de la conduction, puis réévaluer la prédiction.
- Récupérer les mises en garde et contre-indications de la notice ANSM (l'absence de ces données bloque le criblage de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Pour la TVPC, mener une revue ciblée de la littérature sur l'adénosine (et non l'ATP), puis envisager des études précliniques ou de petites études de preuve de concept.
- Clarifier la situation réglementaire (AMM annulées) avant toute démarche de développement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

