---
layout: default
title: Carbocisteine
parent: Prédiction du modèle uniquement (L5)
nav_order: 141
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Carbocisteine : nouvelle indication prédite, Goutte (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées (les textes d'indication de…"
monitor_inn: "carbocisteine"
predicted_indications: ["gout"]
---

# Carbocisteine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Carbocistéine : D'un mucolytique à la goutte
{: .text-alpha }

## Résumé en Une Phrase

La carbocistéine est un mucolytique utilisé pour fluidifier les sécrétions bronchiques. Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **goutte**, mais cette prédiction repose uniquement sur le score du modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées (les textes d'indication des AMM sont vides) |
| Nouvelle Indication Prédite | Goutte |
| Score de Prédiction TxGNN | 0,9967 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 18) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, la carbocistéine est un mucolytique doté de propriétés antioxydantes et anti-inflammatoires. Son indication d'origine n'est pas documentée dans les données compilées.

Un lien purement spéculatif avec la goutte pourrait passer par une réduction du stress oxydatif ou une modulation de l'inflammation médiée par les neutrophiles lors des crises déclenchées par les cristaux d'urate. Aucune donnée ne vient étayer cette hypothèse, et rien n'indique un effet sur le métabolisme ou l'excrétion de l'acide urique.

Le seul élément de soutien est donc le score élevé du modèle TxGNN. Ce score ne remplace pas une preuve clinique ou mécanistique et doit être vérifié de façon indépendante.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 20 AMM recensées sont des spécialités à base de carbocistéine seule, toutes annulées. Les textes d'indication approuvée ne sont pas disponibles. Les 5 premières :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66781076 | Carbocistéine Teva Conseil 2 % Enfants sans sucre | Solution buvable | Non renseignée |
| 64024124 | Carbocistéine UPSA 5 % Adultes sans sucre | Solution buvable | Non renseignée |
| 68902014 | Bronchex 750 mg/15 ml Adultes sans sucre | Solution buvable | Non renseignée |
| 63396673 | Humex Expectorant Carbocistéine 750 mg/10 ml Adultes sans sucre | Solution buvable | Non renseignée |
| 64077212 | Carbocistéine H2 Pharma 2 % Enfants sans sucre | Solution buvable | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indication issue du graphe de connaissances** (relation médicament-maladie du graphe PrimeKG, et non texte de notice) : ulcère gastroduodénal actif.
- **Interactions médicamenteuses** : aucune interaction trouvée dans la requête effectuée.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score TxGNN (modèle d'apprentissage profond, niveau L5), sans essai clinique, sans publication, sans mécanisme d'action documenté, et avec un lien biologique avec la goutte purement hypothétique. 18 AMM françaises sont valides et le médicament est commercialisé.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le mécanisme d'action de la carbocistéine (DrugBank)
- Obtenir les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Clarifier l'indication d'origine, absente des AMM
- Réaliser une revue de littérature et des études précliniques pour tester l'hypothèse antioxydante/anti-inflammatoire dans la goutte
- Évaluer la compatibilité des voies d'administration (voie orale uniquement connue) et la pertinence d'une réintroduction, étant donné le statut annulé des AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

