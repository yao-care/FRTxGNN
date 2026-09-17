---
layout: default
title: Fluconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 129
evidence_level: L5
indication_count: 1
---

# Fluconazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Fluconazole : Des Infections Fongiques à la Kératoconjonctivite Épithéliale Ponctuée

## Résumé en Une Phrase

Le Fluconazole est un antifongique systémique initialement utilisé pour le traitement des infections à *Candida* et des infections fongiques invasives.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Kératoconjonctivite Épithéliale Ponctuée (Punctate Epithelial Keratoconjunctivitis)**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction — la prédiction repose exclusivement sur la structure du graphe de connaissances.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Données réglementaires françaises non disponibles (0 AMM enregistrée) |
| Nouvelle Indication Prédite | Kératoconjonctivite Épithéliale Ponctuée |
| Score de Prédiction TxGNN | 99,24% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé (0 AMM) |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le Fluconazole est un antifongique triazolé qui agit en inhibant la CYP51 fongique (lanostérol 14α-déméthylase), bloquant ainsi la biosynthèse de l'ergostérol, composant essentiel de la membrane cellulaire fongique. Cette action confère une activité bactéricide contre les principaux agents de kératite fongique (*Candida*, *Aspergillus*, *Fusarium*).

La kératoconjonctivite épithéliale ponctuée (KEP) est un syndrome clinique caractérisé par des lésions punctiformes de l'épithélium cornéo-conjonctival. Sa principale étiologie est **non fongique** : adénovirus, herpès simplex (HSV), syndrome de l'œil sec, et toxicité aux conservateurs des collyres. Les causes fongiques ne représentent qu'une fraction marginale des cas.

Le lien mécanistique est donc **indirect et conditionnel** : le Fluconazole ne présente une base pharmacologique rationnelle que dans le sous-groupe de KEP d'étiologie fongique confirmée. Le score TxGNN élevé (0,992) reflète vraisemblablement la proximité topologique dans le graphe de connaissances entre « maladies de la surface oculaire d'origine fongique » et « antifongiques », plutôt qu'une spécificité prédictive pour la KEP elle-même. En l'absence de données cliniques et de littérature, cette prédiction ne peut être retenue sans validation complémentaire.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Aucune AMM française enregistrée pour le Fluconazole dans la base de données consultée.

> **Note** : Le Fluconazole est pourtant un médicament largement commercialisé en France sous plusieurs spécialités (ex. Triflucan®, génériques). L'absence de données dans ce pack suggère une lacune de collecte réglementaire (DG001 — statut Blocking) plutôt qu'une absence réelle sur le marché.

---

## Considérations de Sécurité

Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) n'ont pas été collectées dans ce pack d'évidences.

> Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN est classée en niveau de preuve **L5** (modèle seul, aucune étude clinique ni publication disponible), et le lien mécanistique entre le Fluconazole et la KEP est conditionnel — valide uniquement pour la sous-population à étiologie fongique confirmée, qui est minoritaire dans cette indication. Le dossier présente également deux lacunes bloquantes (DG001 : absence de fiche de sécurité ANSM ; DG002 : absence de MOA documenté) qui empêchent toute évaluation complète.

**Pour avancer, les éléments suivants sont nécessaires :**
- **[Priorité Blocking]** Récupérer la fiche de sécurité ANSM / notice française (DG001) pour compléter les données de mises en garde et contre-indications
- **[Priorité High]** Documenter le mécanisme d'action complet via DrugBank API (DG002)
- Rechercher des publications sur l'usage ophtalmique du Fluconazole (kératite fongique, usage topique en collyre)
- Évaluer la faisabilité d'une formulation ophtalmique (voie topique oculaire) adaptée à la KEP
- Confirmer si des cas cliniques de KEP fongique traités par Fluconazole existent dans la littérature de casuis
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

