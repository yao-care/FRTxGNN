---
layout: default
title: Panitumumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 575
evidence_level: L5
indication_count: 2
---

# Panitumumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Panitumumab : Du Cancer Colorectal Métastatique à l'Ostéoporose Médicamenteuse

## Résumé en Une Phrase

Panitumumab est un anticorps monoclonal initialement utilisé pour le traitement du cancer colorectal métastatique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ostéoporose médicamenteuse**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Néoplasme malin métastatique du côlon (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Ostéoporose médicamenteuse |
| Score de Prédiction TxGNN | 99,13 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulée (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations générales connues, le panitumumab est un anticorps monoclonal dirigé contre le récepteur de l'EGFR, dont l'efficacité dans le cancer colorectal métastatique est établie. Les données compilées pour ce rapport ne permettent pas de construire un lien mécanistique avec l'ostéoporose médicamenteuse.

La signalisation de l'EGFR a été évoquée dans la régulation du remodelage osseux (ostéoblastes et ostéoclastes), mais il s'agit d'un contexte général, non d'une preuve issue des données fournies. Le score élevé de TxGNN (0,991) reste une prédiction computationnelle.

Par ailleurs, l'inhibition de l'EGFR pourrait plutôt perturber l'homéostasie osseuse et minérale (l'hypomagnésémie et l'hypocalcémie sont des effets indésirables connus du panitumumab). Cela plaide pour la prudence en matière de sécurité plutôt que pour un bénéfice thérapeutique.

**Seconde prédiction (pour information) :** la rétinopathie diabétique non proliférante sévère (score 99,05 %, niveau L5, décision Hold). Aucun lien mécanistique n'est étayé par les données. Un anticorps systémique à toxicité cutanée et électrolytique notable, sans AMM active en France, se heurterait à des obstacles pratiques pour une indication oculaire chronique, où des options établies existent déjà (anti-VEGF, laser, contrôle glycémique).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66403621 (annulée) | VECTIBIX 20 mg/ml, solution à diluer pour perfusion (AMGEN EUROPE) | Solution à diluer pour perfusion | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-EGFR) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Électrolytes (magnésium, calcium), selon les effets indésirables connus ; pour le reste, consulter la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 27 interactions recensées. Parmi les principales :
  - **Majeures** : bevacizumab, irinotécan (y compris liposomal), amiodarone, trioxyde d'arsenic, dofétilide, dronédarone, dropéridol, acide aminolévulinique, lévacétylméthadol.
  - **Modérées** : inhibiteurs de la pompe à protons (oméprazole, ésoméprazole, lansoprazole, dexlansoprazole, pantoprazole, rabéprazole), méthoxsalène, acide aminolévulinique (topique), disopyramide, idélalisib.

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, sans données de mécanisme d'action, et avec un signal de sécurité plausible (troubles du magnésium et du calcium) allant à l'encontre d'un bénéfice osseux. L'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Études précliniques sur le rôle de l'EGFR dans l'os et sur l'effet du panitumumab sur le métabolisme osseux
- Revue de la littérature et des registres d'essais pour l'ostéoporose médicamenteuse
- Clarification de la disponibilité commerciale du produit en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

