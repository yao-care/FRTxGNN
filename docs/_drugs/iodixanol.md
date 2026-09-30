---
layout: default
title: Iodixanol
parent: Prédiction du modèle uniquement (L5)
nav_order: 153
evidence_level: L5
indication_count: 3
---

# Iodixanol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Iodixanol : D'un agent de contraste iodé à la susceptibilité à l'arthrose

## Résumé en Une Phrase

L'iodixanol est un agent de contraste radiographique iodé iso-osmolaire, utilisé en imagerie médicale (commercialisé en France sous le nom VISIPAQUE).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **susceptibilité à l'arthrose**, mais cette prédiction repose uniquement sur un calcul de graphe : **0 essai clinique** et **0 publication** la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Susceptibilité à l'arthrose (osteoarthritis susceptibility) |
| Score de Prédiction TxGNN | 99,16 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'iodixanol est un produit de contraste iodé iso-osmolaire, utilisé pour visualiser les structures anatomiques en imagerie radiographique. Il n'a pas de pharmacologie connue de modification de la maladie ni d'action sur la susceptibilité génétique.

À ce stade, aucun lien mécanistique n'a été identifié entre l'iodixanol et la susceptibilité à l'arthrose. Le score élevé de TxGNN (99,16 %) est une prédiction issue de la structure du graphe de connaissances. Aucune étude ne la corrobore, et l'absence de données sur le mécanisme d'action limite encore l'analyse.

À titre de contexte, deux autres indications sont également prédites pour ce médicament :
- **Arthrose** (score 99,07 %) : 7 publications, toutes de nature diagnostique ou expérimentale (imagerie TDM avec produit de contraste, modélisation du transport de solutés dans le cartilage). Aucune ne teste un effet thérapeutique.
- **Polyarthrite rhumatoïde** (score 99,00 %) : une seule publication, un cas de désensibilisation à un autre produit de contraste (iohexol). Elle ne soutient pas l'hypothèse d'un bénéfice.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la susceptibilité à l'arthrose.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60960777 | VISIPAQUE 270 mg d'I/mL, solution injectable | Solution injectable | GE HEALTHCARE |
| 60567418 | VISIPAQUE 320 mg d'I/mL, solution injectable | Solution injectable | GE HEALTHCARE |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique, sans publication soutenant un effet thérapeutique et sans lien mécanistique identifié. Les publications trouvées pour l'arthrose concernent l'usage de l'iodixanol comme sonde d'imagerie, pas un effet sur la maladie.
- Les données de sécurité de la notice ANSM sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), à télécharger depuis le site de l'ANSM
- Obtenir les données sur le mécanisme d'action (MOA), par exemple via l'API DrugBank
- Rechercher un rationnel biologique plausible reliant l'iodixanol à l'arthrose. À défaut, considérer cette prédiction comme un artefact du graphe
- Documenter l'indication originale approuvée (le texte d'indication des deux AMM est vide dans les données)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

