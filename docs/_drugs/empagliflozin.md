---
layout: default
title: Empagliflozin
parent: Prédiction du modèle uniquement (L5)
nav_order: 280
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Empagliflozin : nouvelle indication prédite, Syndrome de la personne raide classique (niveau de preuve L5). Indication d'origine : Diabète de type 2"
---

# Empagliflozin
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

# Empagliflozine : Du Diabète de Type 2 au Syndrome de la Personne Raide Classique

## Résumé en Une Phrase

L'empagliflozine est un inhibiteur du SGLT2, initialement utilisé pour le traitement du diabète de type 2.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de la personne raide classique**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Diabète de type 2 |
| Nouvelle Indication Prédite | Syndrome de la personne raide classique |
| Score de Prédiction TxGNN | 99,06 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

*Remarque : le texte d'indication approuvée n'est pas renseigné dans les AMM compilées ; l'indication originale provient des relations d'indication du graphe de connaissances.*

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, l'empagliflozine est un inhibiteur du SGLT2 qui abaisse la glycémie en bloquant la réabsorption rénale du glucose, indépendamment de l'insuline. Son efficacité dans le diabète de type 2 est établie.

Aucun lien mécanistique solide n'a été identifié avec le syndrome de la personne raide, une maladie neurologique auto-immune généralement associée aux anticorps anti-GAD65, avec une altération de l'inhibition GABAergique. Une piste spéculative est la co-occurrence fréquente de ce syndrome avec le diabète auto-immun (type 1), ce qui pourrait expliquer le rapprochement fait par le modèle. Il s'agit d'une association de comorbidité et non d'un argument thérapeutique : l'inhibition du SGLT2 n'a aucun effet connu sur la signalisation GABA ni sur la pathologie auto-immune.

Deux autres prédictions de score très proche ont été générées : le **syndrome du membre raide focal** (99,06 %, variante localisée du même spectre, probablement tirée du même voisinage dans le graphe plutôt que de preuves indépendantes) et l'**opsismodysplasie** (99,03 %, dysplasie squelettique rare liée à INPPL1/SHIP2, avec un lien très hypothétique avec la signalisation PI3K/AKT et insulinique). Aucune ne repose sur une justification pharmacologique établie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69963066 | JARDIANCE 25 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 67947145 | JARDIANCE 10 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 64866745 | SYNJARDY 12,5 mg/1000 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 60901946 | SYNJARDY 5 mg/1000 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |

Les quatre AMM sont annulées ; aucune AMM valide n'est recensée dans les données compilées.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 369 interactions sont recensées. Parmi les premières listées, la plupart sont de niveau **modéré** : phényléphrine, acébutolol, acétazolamide, formotérol, pseudoéphédrine, nifédipine, épinéphrine, éthinylestradiol, hydrocortisone, salbutamol, éthanol, fosamprénavir, fosinopril, fosphénytoïne, fostamatinib, fostémsavir, furosémide, géméfloxacine. Deux sont de niveau **mineur** : hydrocortisone (topique) et alclométasone (topique). Cette liste est partielle et ne reflète pas l'ensemble des 369 interactions.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, et sans lien mécanistique plausible. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont manquantes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (donnée bloquante)
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank)
- Rechercher des études précliniques ou des cas rapportés reliant l'inhibition du SGLT2 au syndrome de la personne raide
- Vérifier le statut réglementaire actuel de l'empagliflozine en France (les AMM compilées sont toutes annulées)
- Confirmer la prédiction de manière indépendante avant toute évaluation clinique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

