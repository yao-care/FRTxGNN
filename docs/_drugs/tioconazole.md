---
layout: default
title: Tioconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 312
evidence_level: L5
indication_count: 3
---

# Tioconazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Tioconazole : d'un antifongique local établi à la vulvovaginite

## Résumé en Une Phrase

Tioconazole est un antifongique imidazolé à usage local (ovule vaginal et crème dermatologique), commercialisé en France. L'indication originale n'est pas renseignée dans les données ANSM ni DrugBank. La littérature le décrit toutefois comme traitement des mycoses superficielles.
Le modèle TxGNN prédit qu'il pourrait être efficace dans la **vulvovaginite**. Cette prédiction repose sur **2 essais cliniques** indirects (autres azolés que le tioconazole) et **20 publications**, dont plusieurs études cliniques anciennes sur le tioconazole lui-même.
Il s'agit en pratique d'un usage déjà établi plutôt que d'un vrai repositionnement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Vulvovaginite |
| Score de Prédiction TxGNN | 99,23 % |
| Niveau de Preuve | L3 (voir la remarque ci-dessous) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Proceed with Guardrails |

> **Remarque sur le niveau de preuve :** le fichier source indique L1. Or le critère L1 exige au moins 2 essais de Phase 3 complets portant sur le médicament. Le seul essai de Phase 3 recensé teste la fenticonazole associée à la tinidazole, et non le tioconazole. Les études du tioconazole (années 1980) n'ont pas de phase renseignée. J'ai donc retenu L3, plus prudent.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données DrugBank sur le mécanisme d'action ne sont pas disponibles. L'analyse de la prédiction indique que le tioconazole est un antifongique imidazolé. Il inhibe la lanostérol 14-alpha-déméthylase fongique (CYP51), ce qui bloque la synthèse de l'ergostérol et fragilise la membrane du champignon.

Ce mécanisme correspond bien aux vulvovaginites d'origine fongique, en particulier à *Candida*. La revue de Clissold et Heel (Drugs, 1986) rapporte aussi une activité *in vitro* sur les dermatophytes, les levures et certains trichomonas. Plusieurs études cliniques du tioconazole portent directement sur la candidose vaginale : un essai en double aveugle contre placebo (PMID 6347833), et des comparaisons avec le clotrimazole et l'éconazole.

Cette prédiction ne vaut que pour les vulvovaginites infectieuses à levures. Elle ne couvre pas les formes non infectieuses, comme la vaginite atrophique post-ménopausique (une autre prédiction du modèle, sans essai ni publication, dont le mécanisme n'a pas de lien avec un antifongique).

## Preuves d'Essais Cliniques

Aucun de ces essais ne teste le tioconazole. Ils apportent seulement un appui au niveau de la classe des azolés et du cadre des critères d'évaluation.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06056947](https://clinicaltrials.gov/study/NCT06056947) | Phase 3 | Terminé | 577 | Fenticonazole + tinidazole + lidocaïne comparés à l'ovule Gynomax® XL dans la vaginose bactérienne, la vulvovaginite à *Candida*, la vaginite à trichomonas et les infections mixtes (essai randomisé, 3 bras) |
| [NCT03839875](https://clinicaltrials.gov/study/NCT03839875) | Phase 4 | Terminé | 116 | Ovule Gynomax® XL dans les mêmes infections vaginales (étude ouverte, bras unique, sans comparateur) |

## Preuves de la Littérature

Les résumés de plusieurs publications anciennes sont absents de la base. Dans ce cas, le tableau reprend le sujet indiqué par le titre.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | ECR (double aveugle, contre placebo) | Gynakol Rundsch | Efficacité, tolérance et absorption systémique du tioconazole comparé au placebo dans la candidose vaginale (résumé non disponible) |
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | Essai comparatif randomisé | Antimicrob Agents Chemother | 80 patientes : tioconazole 6,5 % en dose unique vs clotrimazole 3 jours. Patientes asymptomatiques à 4 semaines : 84 % (tioconazole) vs 85 % (clotrimazole) |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Essai randomisé ouvert | J Int Med Res | 40 patientes : tioconazole local 6 % en dose unique vs kétoconazole oral 5 jours. Éradication dans les deux groupes à 5 semaines, avec une réponse des symptômes plus rapide sous traitement local |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Essai comparatif ouvert | Gynakol Rundsch | Tioconazole vs éconazole en traitement de 3 jours de la candidose vaginale (résumé non disponible) |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Essai comparatif ouvert | Gynakol Rundsch | Crème de tioconazole vs ovules d'éconazole en traitement de 3 jours (résumé non disponible) |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Étude clinique | Acta Obstet Gynecol Scand | Crème vaginale de tioconazole 2 % : taux de guérison mycologique de 88,5 % chez 29 femmes symptomatiques |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Étude ouverte non comparative | J Int Med Res | Crème de tioconazole 2 % dans l'infection à *Trichomonas vaginalis* ou les infections mixtes : 95 % de guérison (19/20) à environ 7 jours |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Revue | Drugs | Large spectre antimicrobien du tioconazole. Les essais ouverts et contrôlés montrent l'efficacité et la sécurité des préparations locales dans les infections cutanées et la candidose vaginale |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Revue | Expert Rev Anti Infect Ther | Perspectives sur les azolés antifongiques non invasifs dans la candidose vulvovaginale, y compris les formes compliquées et récidivantes |
| [10990271](https://pubmed.ncbi.nlm.nih.gov/10990271/) | 2000 | Étude de laboratoire | Microb Drug Resist | Résistance croisée de souches cliniques de *C. albicans* et *C. glabrata* aux azolés en vente libre utilisés dans les vaginites |

## Informations de Marché en France

L'indication approuvée n'est pas renseignée dans les données ANSM pour ces deux AMM. Elle est donc omise du tableau.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 67466927 | GYNO TROSYD 300 mg, ovule | Ovule | TEOFARMA |
| 69571802 | TROSYD, crème dermatologique | Crème | TEOFARMA |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs études cliniques, dont un essai en double aveugle contre placebo et des comparaisons avec le clotrimazole et l'éconazole, soutiennent l'efficacité du tioconazole dans la candidose vaginale. Le mécanisme antifongique est cohérent avec cette indication, et le produit est déjà commercialisé en France sous forme d'ovule et de crème. En revanche, les essais enregistrés portent sur d'autres azolés, les études du tioconazole datent des années 1980, et les données de sécurité de la notice sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications). Cette lacune est bloquante pour l'évaluation de sécurité.
- Confirmer l'indication approuvée de chaque AMM dans le dossier réglementaire français, afin de vérifier si la vulvovaginite est déjà couverte.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Vérifier la phase et les résultats des études anciennes du tioconazole, dont les résumés sont absents.
- Pour la vulvite (prédiction de rang 2), aucune donnée ne traite ce critère séparément, et la vaginite atrophique post-ménopausique (rang 3, niveau L5) est à mettre en attente.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

