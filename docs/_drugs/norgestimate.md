---
layout: default
title: Norgestimate
parent: Prédiction du modèle uniquement (L5)
nav_order: 548
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Norgestimate : nouvelle indication prédite, Zinc plasmatique élevé (niveau de preuve L5). Indication d'origine : Acné"
---

# Norgestimate
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

# Norgestimate : De l'Acné à l'Élévation du Zinc Plasmatique

## Résumé en Une Phrase

Norgestimate est un progestatif, généralement associé à l'éthinylestradiol dans les contraceptifs oraux. Les données compilées le rattachent à l'acné, à l'ostéoporose postménopausique et à l'atrophie vulvo-vaginale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour **l'élévation du zinc plasmatique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Acné (les autorisations françaises ne renseignent aucun texte d'indication ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Zinc plasmatique élevé |
| Score de Prédiction TxGNN | 99,06 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations toutes annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le norgestimate est un progestatif utilisé en association avec un estrogène dans les contraceptifs oraux. Son usage est établi pour la contraception, et le graphe de connaissances lui associe l'acné, l'ostéoporose et l'atrophie vulvo-vaginale.

Le seul soutien à cette prédiction est un score élevé du modèle. Les produits contenant des estrogènes peuvent influencer les protéines circulantes qui lient le zinc et le cuivre, mais cette association est indirecte et spéculative. Elle ne démontre pas que le médicament traite ou corrige un excès de zinc plasmatique.

Il faut aussi noter qu'un zinc plasmatique élevé est avant tout un constat biologique. Il résulte le plus souvent d'un apport excessif, d'une supplémentation ou d'une exposition, et non d'une maladie traitable par voie hormonale. C'est donc une cible thérapeutique discutable. La similarité avec les indications d'origine et la compatibilité des voies d'administration restent à évaluer.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 7 autorisations recensées sont toutes annulées ; aucune n'est en cours de validité. Le texte d'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65464991 | NARAVELA 250 µg/35 µg, comprimé | Comprimé | Annulée |
| 67592737 | TRINARA CONTINU, comprimé pelliculé | Comprimé | Annulée |
| 68322762 | TRIAFEMI, comprimé | Comprimé (3 types) | Annulée |
| 69274060 | TRINARA, comprimé pelliculé | Comprimé pelliculé (3 types) | Annulée |
| 66449857 | OPTIKINZY 250 µg/35 µg, comprimé | Comprimé (2 types) | Annulée |

Deux autres autorisations, également annulées, ne sont pas détaillées ici : TRIAFEMI CONTINU (69090320) et FEMI (69140061).

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de notice) : hypertension, épilepsie, troubles anxieux, porphyries, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, hyperglycémie et diabète (dont acidocétose), hypothyroïdie, lupus érythémateux systémique, asthme, hypertriglycéridémie, hypercalcémie et troubles du métabolisme du phosphore, ainsi que carcinome mammaire féminin.
- **Interactions médicamenteuses** : 38 interactions recensées. Parmi celles listées, les interactions **majeures** concernent le sugammadex, la griséofulvine, le bexarotène, le brigatinib, le dabrafénib et l'encorafénib. Des interactions modérées concernent notamment la metréleptine, le miltéfosine, l'adalimumab, l'alefacept, l'anakinra, la cladribine, le canakinumab, le certolizumab pégol, l'émapalumab, l'énasidénib et l'entrectinib. Des interactions mineures concernent la rosuvastatine et l'éthanol.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai, sans publication ni mécanisme établi. De plus, la cible (un zinc plasmatique élevé) est surtout un constat biologique, et non une maladie traitable par un progestatif. Aucune autorisation française n'est en vigueur, et plusieurs contre-indications potentielles sont notables.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Les données sur le mécanisme d'action, à interroger dans DrugBank
- Une justification clinique de la pertinence de l'indication prédite, puis une revue de la littérature sur les estrogènes/progestatifs et le zinc plasmatique
- L'évaluation de la similarité avec les indications d'origine et de la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

