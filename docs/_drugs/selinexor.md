---
layout: default
title: Selinexor
parent: Prédiction du modèle uniquement (L5)
nav_order: 696
evidence_level: L5
indication_count: 1
---

# Selinexor
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

# Selinexor : D'une indication non documentée à l'ostéoporose médicamenteuse

## Résumé en Une Phrase

Selinexor est un inhibiteur sélectif de l'export nucléaire (XPO1), commercialisé en France sous le nom NEXPOVIO (comprimé pelliculé). Les données compilées pour ce rapport ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ostéoporose médicamenteuse**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible (texte d'indication absent de l'AMM) |
| Nouvelle Indication Prédite | Ostéoporose médicamenteuse |
| Score de Prédiction TxGNN | 99,22 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulé (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, selinexor est un inhibiteur sélectif de l'export nucléaire qui bloque XPO1 (exportine-1) et retient dans le noyau des protéines suppresseurs de tumeur. Cette description n'a pas été vérifiée à partir du dossier fourni.

Un lien avec la biologie osseuse est plausible mais non démontré : l'inhibition de XPO1 pourrait moduler les voies NF-κB et Wnt/β-caténine, ainsi que l'activité des ostéoclastes et des ostéoblastes. Des travaux précliniques dans l'atteinte osseuse du myélome multiple suggèrent un effet possible sur le remodelage osseux, mais ces éléments ne figurent pas dans les données compilées.

Il faut rester prudent : l'ostéoporose médicamenteuse est généralement un phénotype d'effet indésirable (glucocorticoïdes, inhibiteurs de l'aromatase, etc.). Le score élevé pourrait donc refléter une proximité dans le réseau avec des nœuds d'effets indésirables osseux plutôt qu'un véritable signal thérapeutique. Le sens de l'effet (protecteur ou délétère) reste non résolu.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64317942 | NEXPOVIO 20 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur sélectif de l'export nucléaire, XPO1), d'après les connaissances générales |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice (NFS, fonction hépatique et rénale à envisager) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

**Interactions médicamenteuses** : 81 interactions ont été identifiées (source : DDInter). Parmi les principales :

- **Majeures** : deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine, clozapine
- **Modérées** : chlorure de strontium Sr-89, roflumilast, chloramphénicol (y compris ophtalmique), zidovudine, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, vaccin anthrax, anatoxine tétanique, vaccin vivant contre le choléra

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur un score de modèle (niveau L5), sans essai clinique ni publication. La direction de l'effet (protecteur ou délétère) est incertaine, et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice ANSM (mises en garde et contre-indications), car l'absence de ces données bloque le criblage de sécurité
- Données sur le mécanisme d'action issues de DrugBank
- Revue de la littérature préclinique et clinique sur XPO1 et le métabolisme osseux
- Clarification du sens de l'effet (bénéfique ou délétère) pour l'ostéoporose médicamenteuse
- Confirmation de l'indication d'origine et de la situation réglementaire (AMM annulée)
- Évaluation de la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

