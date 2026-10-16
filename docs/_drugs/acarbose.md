---
layout: default
title: Acarbose
parent: Prédiction du modèle uniquement (L5)
nav_order: 14
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Acarbose : nouvelle indication prédite, Syndrome de la personne raide (forme classique) (niveau de preuve L5). Indication d'origine : Diabète de type 2"
monitor_inn: "ACARBOSE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Acarbose
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Acarbose : Du Diabète de Type 2 au Syndrome de la Personne Raide (forme classique)

## Résumé en Une Phrase

Acarbose est un inhibiteur des alpha-glucosidases intestinales, initialement utilisé pour le traitement du diabète de type 2.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la personne raide (forme classique)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Diabète de type 2 (le texte d'indication des AMM françaises n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Syndrome de la personne raide (forme classique) |
| Score de Prédiction TxGNN | 99,65 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 13 (dont 0 valide) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'acarbose est un inhibiteur des alpha-glucosidases intestinales qui agit localement dans l'intestin en retardant l'absorption des glucides, ce qui réduit la glycémie postprandiale. Son efficacité dans le diabète de type 2 est établie.

Pour le syndrome de la personne raide, **aucun lien mécanistique clair n'est identifié**. Cette maladie auto-immune du système nerveux central est typiquement associée à des anticorps anti-GAD65 et à une altération de la signalisation GABAergique, ce qui n'a pas de rapport avec l'inhibition des alpha-glucosidases.

Le score élevé (0,996) reflète vraisemblablement une association dans le graphe de connaissances via la comorbidité diabétique (l'auto-immunité anti-GAD recoupe celle du diabète de type 1), et non un effet pharmacologique sur la maladie elle-même. La forme focale (« focal stiff limb syndrome ») obtient exactement le même score, ce qui suggère une prédiction héritée du voisinage de la maladie dans le graphe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

## Informations de Marché en France

Les 13 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas renseigné dans les données compilées. Les 5 premières sont présentées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60989978 | ACARBOSE VIATRIS 50 mg, comprimé | Comprimé | Annulée |
| 65803331 | ACARBOSE EG 100 mg, comprimé | Comprimé | Annulée |
| 69771614 | ACARBOSE SANDOZ 50 mg, comprimé | Comprimé | Annulée |
| 60946941 | ACARBOSE VIATRIS 100 mg, comprimé sécable | Comprimé sécable | Annulée |
| 67901945 | ACARBOSE ZENTIVA 100 mg, comprimé sécable | Comprimé sécable | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, pyo-uretère, maladie hépatique, cirrhose du foie, maladie de la vésicule biliaire, maladie inflammatoire chronique de l'intestin, hypoglycémie, traumatisme.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les premières listées :
  - Modérées : acétazolamide, salbutamol, aloès (feuille), alpélisib, amprénavir, aripiprazole, asénapine, asparaginases (Erwinia chrysanthemi et Escherichia coli), atazanavir, bédaquiline, bendrofluméthiazide, benzphétamine, benzthiazide, bétaméthasone.
  - Mineures : albiglutide, alclométasone (topique), acide lipoïque, amcinonide, anisindione.

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible entre l'inhibition des alpha-glucosidases intestinales et une maladie auto-immune neurologique. Toutes les AMM françaises sont par ailleurs annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA)
- Mises en garde et contre-indications issues de la notice ANSM (données bloquantes pour le criblage de sécurité)
- Preuves précliniques ou cliniques démontrant un effet sur le syndrome de la personne raide
- Éventuellement, examen des autres prédictions du classement (par exemple le syndrome de dysfonctionnement répondant à la thiamine, où l'acarbose ne serait qu'un traitement symptomatique de la composante diabétique ; ou l'agénésie pancréatique, où aucune des 11 publications retrouvées ne traite réellement de la maladie), qui présentent toutes un niveau de preuve L5
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

