---
layout: default
title: Toremifene
parent: Prédiction du modèle uniquement (L5)
nav_order: 775
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Toremifene : nouvelle indication prédite, Infection par le VIH (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "toremifene"
predicted_indications: ["HIV infectious disease"]
---

# Toremifene
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Torémifène : Du Cancer du Sein à l'Infection par le VIH

## Résumé en Une Phrase

Le torémifène est un modulateur sélectif des récepteurs aux œstrogènes, connu comme médicament du cancer du sein. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le VIH**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **une seule publication préclinique** (portant sur une infection fongique, la cryptococcose) la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Infection par le VIH |
| Score de Prédiction TxGNN | 99,41 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. Le torémifène appartient à la classe des antagonistes/modulateurs des récepteurs aux œstrogènes (apparentée au tamoxifène). Il est utilisé dans le cancer du sein, mais cette indication n'est pas documentée dans les données d'AMM disponibles.

Le seul élément de soutien est une étude préclinique de 2014 (PMID 24520056) montrant que les antagonistes des récepteurs aux œstrogènes, dont le torémifène et le tamoxifène, ont une activité fongicide contre *Cryptococcus*, se lient directement à des protéines à domaine EF-hand et agissent en synergie avec le fluconazole. La cryptococcose est une infection opportuniste majeure chez les personnes atteintes de VIH/sida avancé : il existe donc un lien indirect avec le contexte du VIH.

Toutefois, cette étude ne démontre ni activité anti-VIH, ni effet sur la réplication virale, ni bénéfice clinique chez des patients infectés. Aucun pont mécanistique direct vers le VIH ne peut être établi à partir des données disponibles. Un éventuel bénéfice serait au mieux adjuvant, contre une co-infection, et non contre le VIH lui-même.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24520056](https://pubmed.ncbi.nlm.nih.gov/24520056/) | 2014 | Étude préclinique (in vitro / mécanistique) | mBio | Le tamoxifène et le torémifène sont fongicides contre *Cryptococcus* et agissent en synergie avec le fluconazole et l'amphotéricine B in vitro ; liaison directe à des protéines EF-hand. Aucune donnée sur le VIH. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60433369 | FARESTON 60 mg, comprimé (ORION CORPORATION) – AMM annulée | Comprimé | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Hormonothérapie (modulateur sélectif des récepteurs aux œstrogènes), non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible à priori ; thrombopénie et leucopénie figurent toutefois parmi les contre-indications relevées dans le graphe de connaissances |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | NFS, fonction hépatique, calcémie, kaliémie, ECG (intervalle QT) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : syndrome du QT long (y compris familial), torsades de pointes, thrombopénie, déficit en potassium, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, leucopénie, hyperplasie de l'endomètre.
- **Interactions médicamenteuses** : 350 interactions recensées. Parmi les interactions **majeures** : dexaméthasone, clarithromycine, lévofloxacine, dolasétron, palonosétron, acide picosulfurique, polyéthylène glycol (3350 avec électrolytes) et sulfate de sodium. Plusieurs de ces associations touchent le risque d'allongement du QT ou de troubles électrolytiques. Des interactions modérées existent notamment avec la famotidine, la cimétidine, le miconazole, l'aprépitant, le lopéramide, le pioglitazone, le natéglinide, le lactulose et le lactitol.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être compilées : veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5). La seule publication est préclinique, concerne la cryptococcose et non le VIH, et aucun essai clinique n'existe. Les données de sécurité officielles sont absentes, et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) afin de réaliser le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank) et la ou les indications d'origine
- Générer des preuves directes d'activité anti-VIH (études in vitro sur la réplication virale), ou reformuler l'hypothèse vers la cryptococcose associée au VIH
- Évaluer le risque de QT et les interactions chez les patients VIH polymédiqués
- Clarifier la faisabilité d'approvisionnement, l'AMM française étant annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

