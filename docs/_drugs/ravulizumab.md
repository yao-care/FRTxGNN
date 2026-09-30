---
layout: default
title: Ravulizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab : De l'inhibition du complément C5 à la neutropénie congénitale sévère autosomique récessive par déficit en G6PC3

## Résumé en Une Phrase

Ravulizumab est un inhibiteur du composant C5 du complément, commercialisé en France sous le nom ULTOMIRIS. L'indication originale n'est pas renseignée dans les données ANSM disponibles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **neutropénie congénitale sévère autosomique récessive par déficit en G6PC3**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (texte d'indication vide) |
| Nouvelle Indication Prédite | Neutropénie congénitale sévère autosomique récessive par déficit en G6PC3 |
| Score de Prédiction TxGNN | 99,96 % (rang 628) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations de l'analyse, le ravulizumab inhibe le composant C5 du complément. Il agit donc sur les maladies où le complément détruit les cellules, comme l'hémolyse de l'hémoglobinurie paroxystique nocturne.

Le lien avec la nouvelle indication est faible. Le déficit en G6PC3 est un défaut métabolique de la glucose-6-phosphatase des neutrophiles, sans rôle connu du complément C5. Le score TxGNN élevé provient d'une prédiction fondée sur le graphe de connaissances, sans étude réelle à l'appui.

**Prudence :** on ne peut pas parler ici de mécanisme plausible, seulement d'un signal statistique du modèle. Les neuf autres indications prédites (rangs 2 à 10) sont aussi de niveau L5, avec une décision Hold. Elles comprennent la neutropénie cyclique (hématopoïèse cyclique), l'hyperoxalurie primaire, la neutropénie congénitale sévère et l'anémie mégaloblastique. Aucune n'a de lien mécanistique établi avec l'inhibition de C5.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64265627 | ULTOMIRIS 1100 mg/11 mL | Solution à diluer pour perfusion | Non précisée dans les données |
| 61808523 | ULTOMIRIS 300 mg/3 mL | Solution à diluer pour perfusion | Non précisée dans les données |

Le titulaire des deux AMM est ALEXION EUROPE.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

La recherche d'interactions médicamenteuses n'a retourné aucun résultat. Cela ne prouve pas l'absence d'interactions.

L'analyse du rang 6 (déficit en p14) rappelle que l'inhibition de C5 augmente le risque d'infections, notamment par des bactéries encapsulées. Ce risque est particulièrement préoccupant chez un patient déjà immunodéficient. Il concerne aussi les patients atteints de neutropénie.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5, stade S0) : aucun essai, aucune publication, et aucun lien mécanistique entre l'inhibition de C5 et le déficit en G6PC3.
- Les informations de sécurité et les indications de l'AMM manquent, ce qui bloque le passage à l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indications autorisées).
- Compléter les données sur le mécanisme d'action via DrugBank.
- Rechercher dans la littérature un rôle du complément dans la physiopathologie de la neutropénie liée à G6PC3. En l'absence de tout signal, abandonner cette piste.
- Évaluer le risque infectieux d'un blocage de C5 chez des patients neutropéniques avant toute étude.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

