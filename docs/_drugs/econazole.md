---
layout: default
title: Econazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 268
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Econazole : nouvelle indication prédite, Granulome de Majocchi (niveau de preuve L5). Indication d'origine : Mycoses cutanées superficielles (pied d'athlète, teigne du corps…"
monitor_inn: "econazole"
predicted_indications: ["Majocchi granuloma", "ectothrix infectious disease", "endothrix infectious disease", "superficial mycosis", "dermatophytosis of scalp or beard", "tinea profunda", "vulvovaginal candidiasis"]
---

# Econazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Éconazole : Des mycoses cutanées superficielles au granulome de Majocchi

## Résumé en Une Phrase

L'éconazole est un antifongique imidazolé à usage local, initialement utilisé contre les mycoses cutanées (pied d'athlète, teigne du corps, candidose cutanée, pityriasis versicolor).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **granulome de Majocchi**, une infection profonde des follicules pileux par des dermatophytes,
mais **aucun essai clinique** et **une seule publication** (un rapport de cas) soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mycoses cutanées superficielles (pied d'athlète, teigne du corps, candidose cutanée, pityriasis versicolor) d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné |
| Nouvelle Indication Prédite | Granulome de Majocchi |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 (prédiction du modèle essentiellement ; un seul rapport de cas, sans valeur de preuve de niveau L3) |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

> Remarque : le système de notation interne du dossier classe cette indication en L4 ; au regard des règles de ce rapport (aucune étude de mécanisme ni étude préclinique, un seul rapport de cas), L5 est retenu comme plus prudent.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, l'éconazole appartient à la classe des azolés : il inhibe la lanostérol 14-alpha-déméthylase fongique, bloque la synthèse de l'ergostérol et altère la membrane du champignon.

Le granulome de Majocchi est une infection dermatophytique profonde des follicules pileux et du derme, le plus souvent due à *Trichophyton rubrum*. Il s'agit des mêmes familles de champignons que celles visées par les indications cutanées déjà connues de l'éconazole. Le lien biologique est donc cohérent.

Une réserve importante s'impose : l'atteinte folliculaire profonde nécessite généralement un traitement antifongique systémique, car les agents topiques pénètrent mal. Un médicament à application locale comme l'éconazole risque donc d'être insuffisant seul.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37899944](https://pubmed.ncbi.nlm.nih.gov/37899944/) | 2023 | Rapport de cas | Case Reports in Dermatology | Homme de 54 ans ; le granulome de Majocchi, « grand imitateur », peut être confondu avec un eczéma ou un psoriasis et mal traité par corticoïdes topiques, d'où un tableau de teigne incognito |

Cette publication décrit le diagnostic de la maladie et ne fournit pas de preuve d'efficacité de l'éconazole.

## Autres Indications Prédites (pour information)

| Maladie prédite | Score TxGNN | Preuves | Remarque |
|------|------|------|------|
| Infection ectothrix | 99,97 % | Aucune | Prédiction seule ; infection du poil, traitement généralement systémique |
| Infection endothrix | 99,97 % | Aucune | Prédiction seule ; pénétration topique limitée |
| Mycose superficielle | 99,97 % | 17 publications, surtout des revues sur d'autres azolés | Chevauche les indications existantes ; pas un vrai repositionnement |
| Dermatophytose du cuir chevelu ou de la barbe | 99,97 % | 8 publications indirectes (cas, revues, sensibilité) | Traitement systémique habituel (griseofulvine, terbinafine) |
| Tinea profunda | 99,96 % | Aucune | Prédiction seule ; traitement systémique de référence |
| Candidose vulvovaginale | 99,50 % | 19 publications dont des comparaisons éconazole/clotrimazole (1980-1994) et une étude multicentrique de 996 cas (1976) | Preuves cliniques anciennes, niveau L3 ; azolé résistant à surveiller |

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées. Le texte d'indication approuvée n'est pas renseigné dans les données. Les cinq premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62326387 | PEVARYL 1 POUR CENT, solution pour application locale en flacon pulvérisateur | Solution pour application | Non renseignée |
| 66614426 | ECONAZOLE BIOGARAN L.P. 150 mg | Ovule à libération prolongée | Non renseignée |
| 64190434 | ECONAZOLE ARROW 1 % | Émulsion pour application cutanée | Non renseignée |
| 61729741 | MYCOSEDERMYL 1 POUR CENT | Crème | Non renseignée |
| 68956300 | ECONAZOLE ZYDUS L.P. 150 mg | Ovule à libération prolongée | Non renseignée |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 41 interactions sont répertoriées, mais leur niveau de gravité est « inconnu ». Parmi celles listées : clotrimazole, metformine, oméprazole, rosiglitazone, lansoprazole, lopéramide, glipizide, dexaméthasone, clopidogrel, héparine, fluticasone, lévothyroxine, diazépam, lorazépam, fluconazole.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais la seule preuve est un rapport de cas diagnostique, sans essai clinique. La pénétration topique limitée dans les infections folliculaires profondes rend l'éconazole local peu adapté. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Des données d'efficacité clinique de l'éconazole dans le granulome de Majocchi (séries de cas, essais), ainsi qu'une évaluation de la pénétration cutanée profonde et de la compatibilité de voie d'administration
- Si l'objectif est la candidose vulvovaginale, qui dispose des preuves cliniques les plus solides, une revue de ces études anciennes, des données de résistance actuelles et une analyse de l'intérêt réglementaire compte tenu du statut annulé des AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

