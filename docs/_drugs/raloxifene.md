---
layout: default
title: Raloxifene
parent: Prédiction du modèle uniquement (L5)
nav_order: 646
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "raloxifene"
predicted_indications: ["duodenal ulcer (disease)", "hypoalphalipoproteinemia", "duodenal obstruction", "duodenogastric reflux"]
description: "Raloxifene : nouvelle indication prédite, Ulcère duodénal (duodenal ulcer (disease)) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Raloxifene
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Raloxifene: Ulcère duodénal (duodenal ulcer (disease))
{: .text-alpha }

## Résumé en Une Phrase

Le raloxifène est un modulateur sélectif des récepteurs des œstrogènes (SERM), initialement utilisé pour le traitement de l'ostéoporose postménopausique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ulcère duodénal**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Ulcère duodénal (duodenal ulcer (disease)) |
| Score de Prédiction TxGNN | 0.9972 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le raloxifène est un SERM : il exerce une activité agoniste œstrogénique sur l'os et une activité antagoniste dans le sein et l'utérus. Son efficacité dans l'ostéoporose postménopausique est établie.

Aucun lien mécanistique n'est démontré entre cette action et l'ulcère duodénal. Une éventuelle implication de la signalisation des récepteurs des œstrogènes dans la protection de la muqueuse gastroduodénale reste purement spéculative et n'est pas appuyée par les données disponibles. Le score élevé (0,9972) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ni un signal thérapeutique confirmé.

Trois autres prédictions figurent dans les données, toutes de niveau L5 et sans essai ni publication : l'hypoalphalipoprotéinémie (score 0,9965), l'obstruction duodénale (0,9964, peu plausible car il s'agit d'une affection structurelle) et le reflux duodénogastrique (0,9959). Ces pistes ne sont pas détaillées ici.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69445593 (annulée) | OPTRUMA 60 mg, comprimé pelliculé (ELI LILLY NEDERLAND BV, Pays-Bas) | Comprimé pelliculé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : hypertension, maladie hépatique, maladie de la vésicule biliaire, fibrillation auriculaire, hypertriglycéridémie, thrombophlébite, maladie coronarienne, accident vasculaire cérébral et troubles cérébrovasculaires, infarctus cérébral, embolie pulmonaire, occlusion de l'artère rétinienne, thrombophilie, insuffisance rénale, accident ischémique transitoire, insuffisance vertébrobasilaire, syndrome des antiphospholipides.
- **Interactions médicamenteuses** : 129 interactions recensées, dont les 20 premières (niveau de gravité non précisé) concernent notamment le calcitriol, le pantoprazole, le glimépiride, la mésalazine, la doxycycline, le clotrimazole, la morphine, la metformine, l'oméprazole, le lansoprazole, le sucralfate, la rosiglitazone, la vancomycine, le lactulose, la triamcinolone, la simvastatine, la nystatine, le natéglinide, la scopolamine et la tétracycline.

Les mises en garde et contre-indications de la notice ANSM n'ont pas pu être exploitées ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (L5), sans essai clinique, sans publication ni lien mécanistique établi. De plus, la seule AMM française est annulée et le profil de sécurité (risques thromboemboliques et cardiovasculaires notamment) n'a pas pu être vérifié à partir de la notice.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde et contre-indications), étape bloquante pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Revue de la littérature et des registres d'essais sur le raloxifène dans l'ulcère duodénal
- Études précliniques permettant d'évaluer la plausibilité biologique
- Clarification du statut réglementaire, l'AMM étant annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

