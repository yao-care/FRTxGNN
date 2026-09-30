---
layout: default
title: Sulindac
parent: Prédiction du modèle uniquement (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Sulindac
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

# Sulindac : D'un anti-inflammatoire non stéroïdien à la Dysplasie Acromésomélique de type Hunter-Thompson

## Résumé en Une Phrase

Sulindac est un anti-inflammatoire non stéroïdien (AINS, inhibiteur des cyclooxygénases), commercialisé en France sous le nom ARTHROCINE. Le texte de l'indication approuvée n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dysplasie acromésomélique de type Hunter-Thompson**, une maladie osseuse génétique rare.
Cette prédiction ne repose sur **aucun essai clinique** et **aucune publication** : c'est une prédiction du modèle seul.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sulindac appartient à la classe des AINS et agit en inhibant les cyclooxygénases (COX), ce qui réduit la production de prostaglandines inflammatoires. Son usage est lié à des affections inflammatoires et douloureuses de l'appareil locomoteur.

La dysplasie acromésomélique de type Hunter-Thompson est une maladie squelettique liée à la voie CDMP1/GDF5, qui régule le développement du cartilage et des os. Aucun lien mécanistique n'est étayé par les données fournies : la voie GDF5 n'a pas de rapport connu avec l'inhibition des COX. Le seul signal en faveur de cette association est le score élevé du modèle (0,999), sans confirmation clinique ni bibliographique.

Cette prédiction doit donc être considérée comme une hypothèse à vérifier, non comme une piste étayée. Les neuf autres indications prédites pour ce médicament, dont la vascularite rhumatoïde, sont également de niveau L5, sans essai ni publication. La vascularite rhumatoïde est la plus plausible sur le plan biologique, mais le lien reste indirect.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 65862059 | ARTHROCINE 100 mg, comprimé | Comprimé | MEDAC |
| 62028152 | ARTHROCINE 200 mg, comprimé sécable | Comprimé sécable | MEDAC |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été trouvée dans les données consultées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible avec le mécanisme d'un AINS.
- Les données de sécurité issues de la notice ANSM et le mécanisme d'action détaillé manquent, ce qui empêche un examen de sécurité sérieux.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indication approuvée)
- Compléter les données sur le mécanisme d'action via DrugBank
- Rechercher dans la littérature et les registres d'essais tout lien entre les AINS et les dysplasies de la voie GDF5
- Évaluer si un rationnel préclinique (modèle cellulaire ou animal) justifie de poursuivre
- Réexaminer la prédiction de la vascularite rhumatoïde, biologiquement plus plausible, si une priorisation est envisagée

---

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

