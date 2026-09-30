---
layout: default
title: Iohexol
parent: Prédiction du modèle uniquement (L5)
nav_order: 154
evidence_level: L5
indication_count: 2
---

# Iohexol
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

# Iohexol : De l'imagerie par produit de contraste à l'insomnie

## Résumé en Une Phrase

Iohexol est un produit de contraste iodé non ionique utilisé en imagerie radiologique. Le modèle TxGNN le prédit comme potentiellement efficace pour l'**insomnie**, avec un score très élevé (99,87 %). **Aucun essai clinique et aucune publication** ne soutiennent cette prédiction, qui relève très probablement d'un artefact du graphe de connaissances.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (produit de contraste iodé pour l'imagerie) |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,87 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'iohexol est un produit de contraste iodé non ionique. Il est pharmacologiquement inerte, n'est pas métabolisé et est éliminé inchangé par les reins.

Aucun lien mécanistique plausible n'a été identifié entre ce produit et l'insomnie. L'iohexol n'a aucune activité connue sur les cibles du système nerveux central qui régulent le sommeil.

Le score TxGNN très élevé est probablement un artefact du graphe de connaissances : le médicament n'a aucune indication annotée et son mécanisme d'action est absent des données. Ce score ne repose sur aucune preuve clinique ou mécanistique.

Une seconde prédiction, l'**anxiété** (score 99,25 %), présente le même profil. Les 5 essais cliniques associés utilisent l'iohexol comme sonde de mesure du débit de filtration glomérulaire ou pour le guidage par imagerie, et aucun ne l'évalue comme traitement. Dans la littérature, l'anxiété n'apparaît que comme contexte procédural ou effet indésirable. Cette prédiction est elle aussi classée L5 / Hold.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 65106581 | OMNIPAQUE 300 mg d'I/mL, solution injectable | Solution injectable |
| 63688752 | OMNIPAQUE 180 mg d'I/mL, solution injectable | Solution injectable |
| 66892062 | OMNIPAQUE 240 mg d'I/mL, solution injectable | Solution injectable |
| 67846776 | OMNIPAQUE 350 mg d'I/mL, solution injectable | Solution injectable |

Titulaire : GE Healthcare. Le texte des indications approuvées n'est pas renseigné dans les données reçues.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique, aucune publication et aucun mécanisme plausible ne la soutiennent.
- Le produit est un agent de contraste inerte sans activité sur le système nerveux central. Un score élevé sans donnée annotée est ici un signal d'artefact, pas d'opportunité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice de l'ANSM (mises en garde, contre-indications), actuellement absente, ce qui bloque le criblage de sécurité
- Données sur le mécanisme d'action (DrugBank)
- Indications approuvées des 4 AMM
- Un rationnel pharmacologique crédible avant toute étude, sans quoi cette piste ne mérite pas d'être poursuivie

*Ces résultats sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

