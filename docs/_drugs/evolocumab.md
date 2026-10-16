---
layout: default
title: Evolocumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 312
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Evolocumab : nouvelle indication prédite, Forme symptomatique de l'hémophilie chez les porteuses (niveau de preuve L5). Indication d'origine : Hypercholestérolémie familiale homozygote"
---

# Evolocumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Evolocumab : De l'Hypercholestérolémie Familiale Homozygote à l'Hémophilie Symptomatique chez les Porteuses

## Résumé en Une Phrase

Evolocumab est un anticorps monoclonal inhibiteur de PCSK9, initialement utilisé pour traiter l'hypercholestérolémie familiale homozygote et les dyslipidémies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **forme symptomatique de l'hémophilie chez les porteuses**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypercholestérolémie familiale homozygote ; dyslipidémie syndromique (le texte d'indication de l'AMM n'est pas renseigné ; les indications proviennent du graphe de connaissances) |
| Nouvelle Indication Prédite | Forme symptomatique de l'hémophilie chez les porteuses |
| Score de Prédiction TxGNN | 99,82 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, evolocumab est un anticorps monoclonal qui inhibe PCSK9, augmente la disponibilité des récepteurs du LDL et abaisse le LDL-cholestérol. Son efficacité dans l'hypercholestérolémie familiale est établie.

**Le lien mécanistique avec la nouvelle indication est très faible, voire inexistant.** Les symptômes hémorragiques des porteuses d'hémophilie résultent d'une activité réduite du facteur VIII ou IX, liée à des variants portés par le chromosome X et à une inactivation biaisée de ce chromosome. L'inhibition de PCSK9 n'agit pas sur la cascade de coagulation. Le score élevé du modèle (0,998) reflète uniquement une proximité dans le graphe de connaissances, sans support clinique ou bibliographique.

À titre de comparaison, les autres prédictions du modèle (déficit en apolipoprotéine C-II, purpura thrombopénique, déficit en facteur XI, hémophilie A avec anomalie vasculaire, « maladie de l'activité catalytique ») ne disposent pas non plus de preuves. Seul le déficit en apoC-II présente un lien indirect, limité au métabolisme lipidique en général.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60966449 | REPATHA 140 mg, solution injectable en stylo prérempli (AMGEN EUROPE) | Solution injectable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une seule entrée de pharmacologie est enregistrée, correspondant à la cible d'evolocumab, la protéine PCSK9 (proprotein convertase subtilisin/kexin type 9). Il s'agit de l'interaction avec sa cible et non d'une interaction médicamenteuse cliniquement significative ; aucun niveau de gravité n'est précisé.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique, aucune publication, et aucun mécanisme plausible reliant l'inhibition de PCSK9 à l'hémophilie des porteuses. De plus, la seule AMM française recensée est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (étape bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Des données précliniques ou cliniques justifiant un lien biologique avec la coagulation, sans quoi il est préférable de réorienter l'évaluation vers des indications plus proches du métabolisme lipidique
- La clarification du statut réglementaire actuel d'evolocumab en France (la présentation répertoriée est annulée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

