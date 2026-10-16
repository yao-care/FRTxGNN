---
layout: default
title: Fenticonazole
parent: Preuves modérées (L3-L4)
nav_order: 324
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Fenticonazole : nouvelle indication prédite, Vulvovaginite à Trichomonas (niveau de preuve L4). Indication d'origine : Candidose vulvovaginale"
monitor_inn: "fenticonazole"
predicted_indications: ["trichomonal vulvovaginitis", "postmenopausal atrophic vaginitis", "vulvovaginitis", "vulvitis", "herpetic vulvovaginitis", "vaginitis (disease)"]
---

# Fenticonazole
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **6** 
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

# Fenticonazole : De la candidose vulvovaginale à la vulvovaginite à Trichomonas

## Résumé en Une Phrase

Le fenticonazole est un antifongique imidazolé à usage local, initialement utilisé pour le traitement de la candidose vulvovaginale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **vulvovaginite à Trichomonas**, mais aucun essai clinique ni aucune publication ne soutient directement cette indication : la prédiction repose uniquement sur le modèle.
Parmi les autres indications prédites, la **vulvovaginite** (non spécifiée) est la mieux documentée, avec **18 publications** (dont plusieurs essais comparatifs), mais elle correspond en grande partie à l'usage déjà établi.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Candidose vulvovaginale (source : graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Vulvovaginite à Trichomonas |
| Score de Prédiction TxGNN | 99,50 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. D'après la littérature disponible (revue de 2008), le fenticonazole est un dérivé imidazolé à large spectre antimycosique. Il agirait de trois façons : inhibition de la sécrétion de protéase acide par *Candida albicans*, atteinte de la membrane cytoplasmique, et blocage des cytochrome-oxydases et peroxydases. Une activité antibactérienne, notamment sur les bactéries à Gram positif, a également été décrite.

Le lien avec la trichomonase est toutefois indirect. *Trichomonas vaginalis* est un protozoaire, et son traitement standard repose sur les 5-nitroimidazoles (métronidazole, tinidazole), dont l'activité dépend de la réduction du groupement nitro, absent du fenticonazole. Une activité antitrichomonas in vitro a été rapportée pour certains imidazolés topiques, mais elle n'est pas documentée ici pour le fenticonazole.

Les deux publications associées sont une revue générale et un essai ouvert sur la vulvovaginite (population surtout candidosique, 101 patientes, schéma de 1 g en 2 jours incluant des infections mixtes avec *T. vaginalis*). Aucune ne fournit de données d'efficacité clairement spécifiques à *Trichomonas*. Le score élevé du modèle (0,995) reste donc une simple prédiction.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Publications associées à l'indication prédite principale (vulvovaginite à Trichomonas) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15216954](https://pubmed.ncbi.nlm.nih.gov/15216954/) | 2004 | Essai clinique ouvert (pilote) | J Chemother | Ovules de fenticonazole 1 g aux jours 1 et 3 chez 101 femmes atteintes de vulvovaginite à infections simples ou mixtes (*Candida*, *Trichomonas*, *Gardnerella*) ; population principalement candidosique |
| [18840006](https://pubmed.ncbi.nlm.nih.gov/18840006/) | 2008 | Revue | Drugs | Revue du rôle du fenticonazole topique en dermatologie et gynécologie : large spectre antimycosique, action antibactérienne |

Pour information, la vulvovaginite (non spécifiée, rang 3) dispose d'un corpus plus large, essentiellement sur la candidose : essais comparatifs contre clotrimazole (PMID [2680285](https://pubmed.ncbi.nlm.nih.gov/2680285/), [2202548](https://pubmed.ncbi.nlm.nih.gov/2202548/)), miconazole ([12017948](https://pubmed.ncbi.nlm.nih.gov/12017948/)) et fluconazole ([22481619](https://pubmed.ncbi.nlm.nih.gov/22481619/)), ainsi qu'une étude de sensibilité in vitro (EUCAST/CLSI, 260 isolats, [19223627](https://pubmed.ncbi.nlm.nih.gov/19223627/)).

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60010967 | TERLOMEXIN 200 mg, capsule molle vaginale | Capsule molle | Non renseignée (AMM annulée) |
| 69960586 | LOMEXIN 600 mg, capsule molle vaginale | Capsule molle | Non renseignée (AMM annulée) |
| 63987103 | LOMEXIN 2 %, crème | Crème | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

À titre indicatif, une étude pharmacocinétique de 1991 (PMID [2019858](https://pubmed.ncbi.nlm.nih.gov/2019858/)) rapporte une absorption systémique minimale après administration vaginale de 1 g. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la vulvovaginite à Trichomonas repose uniquement sur le modèle (niveau L4) : le mécanisme est indirect, il n'existe aucun essai enregistré et aucune donnée d'efficacité spécifique à *Trichomonas*. De plus, toutes les AMM françaises sont annulées, ce qui limite le développement pratique.
- Les autres prédictions ne sont pas plus favorables : atrophie vaginale postménopausique et vulvovaginite herpétique (niveau L5, sans mécanisme plausible), tandis que vulvovaginite, vulvite et vaginite (niveau L3, « question de recherche ») reposent surtout sur des données candidosiques, donc proches de l'usage d'origine plutôt que d'un vrai repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de sécurité de la notice ANSM (mises en garde, contre-indications) : lacune bloquante pour tout passage à l'étape de criblage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Données in vitro ou cliniques spécifiques à *Trichomonas vaginalis*, comparées au métronidazole
- Pour la vulvovaginite mixte (bactérienne + fongique), des essais cliniques contrôlés confirmant l'activité antibactérienne observée in vitro
- Clarification de la situation réglementaire (AMM annulées) et des voies d'administration disponibles
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

