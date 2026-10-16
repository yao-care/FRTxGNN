---
layout: default
title: Brodalumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brodalumab : nouvelle indication prédite, Strongyloïdose (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
---

# Brodalumab
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

# Brodalumab : De l'indication originale non documentée à la strongyloïdose

## Résumé en Une Phrase

Brodalumab est un anticorps monoclonal antagoniste du récepteur A de l'interleukine-17 (IL-17RA). Les données réglementaires compilées pour ce rapport ne précisent pas son indication originale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **strongyloïdose**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction, et la direction biologique est douteuse.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Strongyloïdose |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Brodalumab bloque le récepteur IL-17RA, ce qui inhibe la signalisation de plusieurs cytokines de la famille IL-17. Cette voie participe à l'immunité des muqueuses et à la défense contre certains pathogènes, y compris les helminthes.

Cependant, la prédiction paraît peu plausible sur le plan biologique. Le contrôle de *Strongyloides* repose surtout sur la réponse Th2 (IL-4, IL-5, IL-13, éosinophiles). Bloquer IL-17RA ne devrait pas traiter l'infection et pourrait même altérer modestement la défense de l'hôte. Le score élevé du modèle est une prédiction issue d'un graphe de connaissances, sans appui clinique ni bibliographique. Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. La relation avec l'indication originale n'a pas pu être évaluée, celle-ci n'étant pas renseignée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la strongyloïdose.

À titre informatif, pour la deuxième prédiction (« maladie oculaire »), trois publications ont été retrouvées, sans soutien d'une efficacité :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42576218](https://pubmed.ncbi.nlm.nih.gov/42576218/) | 2026 | Préclinique (modèle animal) | J Transl Med | Le blocage d'IL-17R par brodalumab limite la parodontite expérimentale (non oculaire) |
| [41770262](https://pubmed.ncbi.nlm.nih.gov/41770262/) | 2026 | Rapport de cas | Rheumatol Int | Maladie de Behçet survenue comme réaction paradoxale après l'initiation de brodalumab |
| [41916603](https://pubmed.ncbi.nlm.nih.gov/41916603/) | 2026 | Analyse de pharmacovigilance | Can J Ophthalmol | Analyse des uvéites rapportées avec des médicaments systémiques, suggérant un signal de sécurité plutôt qu'un bénéfice |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65620419 | KYNTHEUM 210 mg, solution injectable en seringue préremplie (LEO PHARMA A/S, Danemark) | Solution injectable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie de Crohn, maladie inflammatoire chronique de l'intestin, colite de Crohn.
- **Interactions médicamenteuses** : 68 interactions recensées. Parmi celles listées :
  - **Majeures** : adalimumab, baricitinib, certolizumab pegol, vaccin BCG (souche Tice, vivant).
  - **Modérées** : roflumilast, alemtuzumab, anakinra, canakinumab, alefacept, ainsi que plusieurs vaccins ou agents vivants (anthrax, adénovirus type 4, choléra, *Candida albicans*, anatoxine tétanique, *Bifidobacterium longum infantis*).
  - **Mineures** : sels de zinc (acétate, gluconate, sulfate, chlorure).

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, avec un mécanisme biologiquement douteux. De plus, l'AMM française est annulée et le profil de sécurité n'est pas documenté.
- Les autres prédictions du top 10 (maladie oculaire, névrites optiques, épisclérites, etc.) sont également en Hold : preuves absentes ou très faibles, certaines suggérant même un signal de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Indication originale documentée
- Données précliniques ou cliniques spécifiques à la strongyloïdose, ou choix d'une indication plus plausible sur le plan mécanistique
- Évaluation de la compatibilité des voies d'administration et de la similarité avec l'indication originale
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

