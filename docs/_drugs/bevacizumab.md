---
layout: default
title: Bevacizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bevacizumab : nouvelle indication prédite, Néoplasie de l'épiglotte (niveau de preuve L5). Indication d'origine : Cancers du péritoine, de l'ovaire, du sein, du côlon métastatique…"
monitor_inn: "bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
---

# Bevacizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Bevacizumab : Des cancers du péritoine, de l'ovaire, du sein et du côlon métastatique à la néoplasie de l'épiglotte

## Résumé en Une Phrase

Le bevacizumab est un anticorps monoclonal anti-VEGF, utilisé à l'origine dans plusieurs cancers (péritoine, ovaire, sein, côlon métastatique, glioblastome).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **néoplasie de l'épiglotte**, mais **aucun essai clinique ni aucune publication** ne soutient pour l'instant cette indication précise.
Il s'agit donc d'une prédiction du modèle seule.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancers du péritoine, de l'ovaire, du sein, du côlon métastatique, glioblastome (le texte d'indication des AMM n'est pas renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Néoplasie de l'épiglotte |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations toutes annulées |
| Nombre d'AMM | 8 (aucune valide) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le bevacizumab neutralise le VEGF-A, un facteur clé de la formation de nouveaux vaisseaux (angiogenèse) qui nourrissent les tumeurs.

Ses indications d'origine sont des tumeurs solides dépendantes de l'angiogenèse. Mécanistiquement, bloquer le VEGF pourrait limiter la croissance de tumeurs de la tête et du cou, dont celles de l'épiglotte. La similarité avec les indications d'origine n'a pas été évaluée.

Ce raisonnement reste théorique : aucune donnée clinique ou bibliographique n'a été fournie pour cette indication. Le score élevé du modèle est une prédiction, pas une preuve.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 8 AMM du bevacizumab (Avastin et biosimilaires) sont toutes au statut « annulée ». Le texte d'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65303582 | AYBINTIO 25 mg/ml | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 60391646 | AVASTIN 25 mg/ml | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 62051980 | VEGZELMA 25 mg/ml | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 61409314 | MVASI 25 mg/mL | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 64586704 | ALYMSYS 25 mg/mL | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-VEGF), non cytotoxique conventionnel |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Faible (selon la classe générale des anticorps monoclonaux) |
| Éléments de Surveillance | Veuillez consulter la notice (notamment tension artérielle et protéinurie, d'après les connaissances générales sur la classe) |
| Protection de Manipulation | Veuillez consulter la notice et les recommandations de manipulation des médicaments anticancéreux |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 22 interactions ont été recensées. Les interactions de niveau **majeur** concernent :
  - la défériprone ;
  - le samarium (153Sm) lexidronam ;
  - le panitumumab ;
  - le sunitinib ;
  - la thalidomide.
- Les interactions de niveau **modéré** concernent notamment les bisphosphonates (acides alendronique, risédronique, étidronique, pamidronique, tiludronique, ibandronate), le filgrastim, le pegfilgrastim, le sargramostim, la palifermine, l'idélalisib, le romosozumab, le strontium-89, le radium-223 et le phosphate de sodium (P32).

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction pour la néoplasie de l'épiglotte repose uniquement sur le modèle (niveau L5), sans essai ni publication. De plus, les données de sécurité de la notice sont absentes et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (lacune bloquante pour le criblage de sécurité).
- Obtenir les données de mécanisme d'action via DrugBank.
- Rechercher des essais cliniques et publications spécifiques aux tumeurs de l'épiglotte et, plus largement, du larynx et de la tête et du cou.
- Clarifier la situation réglementaire en France, toutes les AMM étant annulées.

**Note sur les autres indications prédites :** une seule d'entre elles dispose de preuves substantielles : la « néoplasie kystique » (L1, via un essai de phase 3 NCT00565851 sur le cancer de l'ovaire). Elle recoupe toutefois les indications d'origine et le terme est trop large, donc ce n'est pas un véritable repositionnement. Les autres (langue, testicule, hypopharynx, plancher buccal, neuroblastome cervical, papillome inversé, mésenchymome, schwannome du foramen jugulaire) restent au niveau L4-L5, en « Hold ».
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

