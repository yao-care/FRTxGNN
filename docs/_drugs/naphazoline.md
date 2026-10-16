---
layout: default
title: Naphazoline
parent: Prédiction du modèle uniquement (L5)
nav_order: 524
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Naphazoline : nouvelle indication prédite, Hypotrichose simple du cuir chevelu (niveau de preuve L5). Indication d'origine : Non renseignée dans les AMM (usage connu : rougeur oculaire…"
monitor_inn: "naphazoline"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Naphazoline
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

# Naphazoline : D'un décongestionnant vasoconstricteur à l'hypotrichose simple du cuir chevelu

## Résumé en Une Phrase

Naphazoline est un vasoconstricteur agoniste alpha-adrénergique de la famille des imidazolines, utilisé en ophtalmologie pour réduire la rougeur oculaire et en décongestion nasale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypotrichose simple du cuir chevelu**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (usage connu : rougeur oculaire, décongestion) |
| Nouvelle Indication Prédite | Hypotrichose simple du cuir chevelu |
| Score de Prédiction TxGNN | 99,83 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la naphazoline agit sur les récepteurs alpha-adrénergiques (α1A, α2A, α2C) et provoque une vasoconstriction qui réduit la rougeur des yeux en resserrant les vaisseaux dilatés.

La prédiction de TxGNN repose uniquement sur la proximité dans le graphe de connaissances. L'hypotrichose simple est une maladie génétique du développement du follicule pileux (variants de CDSN, APCDD1, RPL21, par exemple). Une vasoconstriction topique ne devrait pas corriger ce type de défaut, et aucune activité favorisant la croissance du follicule n'est documentée.

Les autres prédictions du classement présentent le même problème. Pour l'alopécie, les traitements établis (minoxidil, finastéride, inhibiteurs de JAK) agissent par vasodilatation, inhibition de la 5-alpha-réductase ou modulation immunitaire, un mécanisme opposé à la vasoconstriction de la naphazoline. Les prédictions pour les glaucomes (à angle ouvert et héréditaire primaire) ne sont pas non plus étayées. Une plausibilité très faible existe au niveau de la classe des agonistes alpha (brimonidine), mais la naphazoline n'est pas un hypotenseur oculaire établi.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 67338728 | COLLYRE BLEU LAITER, flacon | Collyre | Non renseignée | Annulée |
| 62545178 | XYLOCAINE 5 POUR CENT A LA NAPHAZOLINE, solution pour application muqueuse | Solution pour application | Non renseignée | Annulée |
| 69345098 | DERINOX, solution pour pulvérisation nasale | Solution pour pulvérisation | Non renseignée | Annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de notice) : hypertension, hyperglycémie, diabète et acidocétose diabétique, glaucome à angle fermé, maladies cardiovasculaires, hyperthyroïdie (dont maladie de Basedow et thyréotoxicose), infections oculaires et conjonctivite.
- **Cibles pharmacologiques** : récepteurs α1A, α2A et α2C humains. Cela explique les effets sympathomimétiques, avec notamment un risque de déclencher une fermeture de l'angle chez les yeux prédisposés.
- **Interactions médicamenteuses** : aucune interaction médicament-médicament cliniquement qualifiée n'est disponible. Seules des données de cibles pharmacologiques ont été compilées.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Le mécanisme vasoconstricteur n'a pas de lien plausible avec les troubles du développement du follicule pileux, et il est même opposé à celui des traitements établis de l'alopécie.
- Toutes les AMM françaises sont annulées, et les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles issues des notices de l'ANSM (point bloquant)
- Les données détaillées sur le mécanisme d'action
- Des études précliniques sur la croissance du follicule pileux, pour justifier tout travail ultérieur
- Une évaluation de la compatibilité des voies d'administration (topique cutanée contre formes ophtalmique et nasale existantes)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

