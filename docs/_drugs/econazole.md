---
layout: default
title: Econazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 268
evidence_level: L5
indication_count: 2
monitor_inn: "econazole"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
last_modified_at: 2026-10-31
description: "Econazole : nouvelle indication prédite, Infection ectothrix (ectothrix infectious disease) (niveau de preuve L5). Indication d'origine : Aucun texte d'indication n'est disponible dans les AMM compil…"
---

# Econazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Éconazole : Des mycoses cutanées à dermatophytes à l'infection ectothrix
{: .text-alpha }

## Résumé en Une Phrase

L'éconazole est un antifongique imidazolé à usage local, initialement utilisé pour traiter les mycoses cutanées (pied d'athlète, teigne du corps, candidose cutanée, pityriasis versicolor).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection ectothrix** (infection du cheveu par des dermatophytes), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Aucun texte d'indication n'est disponible dans les AMM compilées ; la relation enregistrée dans le graphe de connaissances est : pied d'athlète (tinea pedis), teigne du corps, candidose cutanée, pityriasis versicolor |
| Nouvelle Indication Prédite | Infection ectothrix (ectothrix infectious disease) |
| Score de Prédiction TxGNN | 0,9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales sur la classe, les imidazolés inhibent la lanostérol 14-alpha-déméthylase des champignons et perturbent la synthèse de l'ergostérol. Ce mécanisme n'est pas confirmé par les données fournies.

L'infection ectothrix est une infection dermatophytique du cheveu, où les arthroconidies forment un manchon à l'extérieur de la tige pilaire. Son score de 0.9997 provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Une limite importante : la pénétration d'un traitement local dans le follicule et la tige pilaire est réputée limitée, et les teignes du cuir chevelu nécessitent en général un traitement systémique. Cette limite relève de connaissances générales et n'est pas étayée par les données compilées. La prédiction pour l'infection endothrix (score 0,9997), où le champignon se développe à l'intérieur du cheveu, soulève la même difficulté, en plus marquée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

L'éconazole est commercialisé en France sous de nombreuses formes. Les données compilées recensent au moins 20 AMM (19 valides, 1 annulée) ; la liste peut être partielle. Le texte des indications approuvées n'est pas renseigné dans ces enregistrements. Voici cinq AMM représentatives :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62326387 | PEVARYL 1 POUR CENT, solution pour application locale en flacon pulvérisateur | Solution pour application | Non renseignée |
| 61685323 | PEVARYL 1 %, crème | Crème | Non renseignée |
| 66614426 | ECONAZOLE BIOGARAN L.P. 150 mg | Ovule à libération prolongée | Non renseignée |
| 64190434 | ECONAZOLE ARROW 1 % | Émulsion pour application cutanée | Non renseignée |
| 61729741 | MYCOSEDERMYL 1 POUR CENT | Crème | Non renseignée |

## Considérations de Sécurité

**Interactions Médicamenteuses** : 41 interactions sont recensées dans la base DDInter, toutes de niveau de gravité non précisé. Parmi les premières : clotrimazole, metformine, oméprazole, rosiglitazone, lansoprazole, lopéramide, glipizide, dexaméthasone, héparine et fluconazole.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucune étude citée ne porte directement sur l'infection ectothrix. Elle s'explique surtout par la proximité avec les dermatophytoses cutanées, et la pénétration pilaire d'un produit local est incertaine.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank)
- Mises en garde et contre-indications issues des notices de l'ANSM
- Études de pénétration de l'éconazole dans le follicule et la tige pilaire
- Recherche d'essais cliniques ou de publications portant sur les teignes ectothrix et endothrix traitées par éconazole
- Évaluation de la compatibilité des voies d'administration (actuellement non évaluée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

