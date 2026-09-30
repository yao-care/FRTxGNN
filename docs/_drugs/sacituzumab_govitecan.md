---
layout: default
title: Sacituzumab Govitecan
parent: Prédiction du modèle uniquement (L5)
nav_order: 276
evidence_level: L5
indication_count: 4
---

# Sacituzumab Govitecan
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Sacituzumab govitécan : De l'oncologie (indication originale non renseignée) à l'ostéoporose médicamenteuse

## Résumé en Une Phrase

Sacituzumab govitécan est un conjugué anticorps-médicament (ADC) cytotoxique, dirigé contre Trop-2, qui délivre le SN-38, un inhibiteur de la topoisomérase I. Son indication originale n'est pas renseignée dans les données fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ostéoporose médicamenteuse**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Ostéoporose médicamenteuse (drug-induced osteoporosis) |
| Score de Prédiction TxGNN | 99,78 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la source. D'après les informations connues, sacituzumab govitécan cible Trop-2 et libère le SN-38, qui bloque la topoisomérase I et détruit les cellules tumorales.

**En l'état, la prédiction n'est pas étayée par un lien mécanistique.** Aucune activité protectrice pour l'os ou anti-résorptive n'est documentée pour ce médicament. La chimiothérapie cytotoxique est plus souvent associée à une perte osseuse qu'à une protection osseuse. Le score de 99,78 % provient uniquement d'un graphe de connaissances et ne peut pas être vérifié, faute de données sur le mécanisme d'action d'origine.

Le modèle a aussi proposé trois autres indications, toutes de niveau L5 et en statut Hold, sans aucun essai ni publication :

- la rétinopathie diabétique non proliférante sévère (99,69 %) ;
- la rétinopathie diabétique (99,60 %) ;
- la cataracte diabétique (99,12 %).

Pour ces trois maladies oculaires, aucun mécanisme lié à Trop-2 ou au SN-38 n'est connu. Le score élevé reflète probablement la proximité de ces maladies dans le graphe, et non une justification biologique. Exposer des patients à un ADC cytotoxique (myélosuppression, risque infectieux) est difficile à justifier dans des maladies chroniques non oncologiques, alors que des traitements établis existent.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 67719704 | TRODELVY 200 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | GILEAD SCIENCES IRELAND UC (Irlande) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Conjugué anticorps-médicament à charge cytotoxique (SN-38, inhibiteur de la topoisomérase I) |
| Risque de Myélosuppression | Présent (myélosuppression et risque infectieux signalés) ; niveau détaillé à confirmer dans la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Numération formule sanguine (NFS), fonction hépatique et rénale |
| Protection de Manipulation | Suivre les réglementations de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique plausible n'a été identifié. Le profil cytotoxique du médicament rend l'hypothèse peu vraisemblable sans nouvelle justification préclinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Les données détaillées sur le mécanisme d'action (DrugBank).
- L'indication originale approuvée, pour pouvoir analyser la relation avec la nouvelle indication.
- Des données précliniques ou cliniques montrant un effet sur le métabolisme osseux, avant toute reconsidération.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

