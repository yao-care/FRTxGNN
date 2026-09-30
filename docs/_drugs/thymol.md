---
layout: default
title: Thymol
parent: Prédiction du modèle uniquement (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Thymol
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

# Thymol : Des Usages Locaux ORL et Buccaux à l'Anévrisme du Septum Interventriculaire

## Résumé en Une Phrase

Le thymol est un composé phénolique d'origine végétale (thym). Il est commercialisé en France dans des produits à usage local : inhalation par vapeur, pommade et solution buccale. Le modèle TxGNN le prédit comme potentiellement efficace pour l'**anévrisme du septum interventriculaire**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette indication : la prédiction repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données AMM disponibles (produits à usage local : inhalation, pommade, solution buccale) |
| Nouvelle Indication Prédite | Anévrisme du septum interventriculaire |
| Score de Prédiction TxGNN | 99,25 % (rang 5086) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le thymol est un monoterpène phénolique aux propriétés antioxydantes, anti-inflammatoires et antimicrobiennes. Il module aussi certains canaux TRP. Il est utilisé dans des produits ORL et d'hygiène buccale.

**Aucun lien mécanistique plausible n'a pu être identifié** avec la nouvelle indication. L'anévrisme du septum interventriculaire est une anomalie cardiaque structurelle, et les activités connues du thymol n'agissent pas sur ce type de lésion. Le score de 99,25 % est une prédiction issue d'un graphe de connaissances, sans confirmation expérimentale ou clinique. Il doit donc être interprété avec beaucoup de prudence.

Les autres prédictions du même classement (valvulopathie pulmonaire, syndrome de Laubry-Pezzi, syndrome de Pierre Robin, délétions chromosomiques, etc.) ont aussi des scores supérieurs à 99 %. Elles sont toutes de niveau L5 et sans lien mécanistique identifié, ce qui suggère un biais systématique du modèle pour ce médicament.

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
| 64424727 | PERUBORE INHALATION | Capsule pour inhalation par vapeur | Laboratoires Mayoly Spindler |
| 64072763 | VICKS VAPORUB | Pommade | Laboratoire Vicks |
| 61989408 | GLYCO-THYMOLINE 55 | Solution buccale | SERP |

Le texte des indications approuvées n'est pas renseigné dans les données reçues pour ces trois AMM.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été trouvée dans la base interrogée.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 : aucun essai, aucune publication, et aucun lien mécanistique plausible avec une malformation cardiaque structurelle.
- Les données de sécurité de la notice ne sont pas disponibles, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les notices ANSM (mises en garde, contre-indications) des trois produits.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via l'API DrugBank).
- Préciser les indications approuvées de chaque AMM.
- Réexaminer les prédictions avec un critère de plausibilité biologique. Le classement actuel ne contient aucune candidate avec un lien mécanistique identifié.

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

