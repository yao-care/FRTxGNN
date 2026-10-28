---
layout: default
title: Tioconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 764
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "TIOCONAZOLE"
predicted_indications: ["vulvovaginitis", "vulvitis", "postmenopausal atrophic vaginitis"]
description: "Tioconazole : nouvelle indication prédite, Vulvovaginite (vulvovaginitis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
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

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Tioconazole: Vulvovaginite (vulvovaginitis)
{: .text-alpha }

## Résumé en Une Phrase

Le tioconazole est un antifongique imidazolé à usage topique, initialement utilisé pour le traitement de la candidose vulvovaginale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **vulvovaginite**, mais cette indication est très proche de l'indication d'origine : il s'agit davantage d'un usage dans le cadre de l'indication connue que d'un véritable repositionnement.
Aucun essai clinique n'est enregistré ; **20 publications** sont associées à cette prédiction, dont quelques essais comparatifs anciens (années 1980).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Vulvovaginite (vulvovaginitis) |
| Score de Prédiction TxGNN | 0.9923 |
| Niveau de Preuve | L5 (selon l'évaluation compilée ; essais anciens, majoritairement ouverts) |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la fiche du médicament. D'après les données pharmacologiques compilées, le tioconazole est un antifongique azolé : il inhibe la lanostérol 14-α-déméthylase fongique (CYP51/ERG11), enzyme qui transforme le lanostérol en ergostérol, composant essentiel de la membrane du champignon. Sans ergostérol, le champignon ne survit pas. Le tioconazole inhibe aussi une enzyme humaine, le CYP8B1, impliquée dans la synthèse des acides biliaires.

La candidose vulvovaginale est une forme de vulvovaginite d'origine fongique. La prédiction est donc cohérente : l'efficacité est attendue dans les vulvovaginites fongiques, mais pas dans les formes bactériennes, à trichomonas ou non infectieuses.

Deux autres prédictions de moindre rang sont à noter :
- **Vulvite** (score 0,9920, niveau L3) : plausible uniquement pour les formes associées à une infection à *Candida*. La littérature porte sur la candidose vaginale, pas sur la vulvite en tant qu'entité distincte ; les preuves sont donc indirectes.
- **Vaginite atrophique post-ménopausique** (score 0,9919, niveau L5) : cette pathologie découle d'une carence œstrogénique, sans lien mécanistique clair avec un antifongique. Le score élevé semble refléter la proximité dans le réseau avec d'autres vaginites plutôt qu'un vrai mécanisme thérapeutique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Sélection des publications les plus pertinentes (priorité aux essais randomisés) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | ECR comparatif | Antimicrob Agents Chemother | 80 patientes : tioconazole en dose unique (pommade 6,5 %) vs clotrimazole 3 jours ; 84 % vs 85 % asymptomatiques à 4 semaines |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | ECR (double aveugle, contre placebo) | Gynakol Rundsch | Comparaison tioconazole vs placebo dans la candidose vaginale, avec évaluation de l'absorption systémique |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Essai randomisé ouvert | J Int Med Res | 40 patientes : tioconazole topique en dose unique vs kétoconazole oral 5 jours ; éradication dans les deux groupes, réponse des symptômes plus rapide avec le topique |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Revue | Drugs | Les essais ouverts et contrôlés ont montré l'efficacité et la sécurité des préparations topiques dans les mycoses superficielles et la candidose vaginale |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Revue | Expert Rev Anti Infect Ther | Options antifongiques azolées non invasives pour la candidose vulvovaginale, y compris les formes récidivantes |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Étude clinique | Acta Obstet Gynecol Scand | Crème vaginale à 2 % : taux de guérison mycologique de 88,5 % chez 29 femmes symptomatiques |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Essai comparatif ouvert | Gynakol Rundsch | Tioconazole vs éconazole, traitement de 3 jours |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Essai comparatif ouvert | Gynakol Rundsch | Crème de tioconazole vs ovules d'éconazole, traitement de 3 jours |
| [3216880](https://pubmed.ncbi.nlm.nih.gov/3216880/) | 1988 | Étude clinique | Mycoses | Tioconazole dans la candidose vaginale |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Étude ouverte non comparative | J Int Med Res | 20 patientes avec infection à *T. vaginalis* (certaines mixtes) : 95 % de guérison au premier suivi |

Les autres publications recensées sont des études de formulation, de résistance, de diagnostic ou précliniques, sans valeur directe pour l'efficacité.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67466927 | GYNO TROSYD 300 mg, ovule (TEOFARMA) | Ovule | Non renseignée (AMM active) |
| 69571802 | TROSYD, crème dermatologique (TEOFARMA) | Crème | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Interactions médicamenteuses** : deux signaux ont été relevés : l'oméprazole (niveau de gravité inconnu) et le CYP8B1 (cible enzymatique humaine inhibée par le tioconazole, sans niveau de gravité défini).

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves proviennent surtout d'essais anciens (1983-1988) portant sur la candidose vaginale, soit l'indication d'origine, et non sur un véritable nouvel usage. De plus, les deux AMM françaises sont annulées, ce qui limite la disponibilité pratique, et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), point bloquant pour l'évaluation de la sécurité
- Compléter les données sur le mécanisme d'action (DrugBank)
- Préciser la définition de « vulvovaginite » visée (fongique uniquement) et confirmer la pertinence des publications
- Vérifier la disponibilité réelle du produit en France (AMM annulées) ou l'existence d'alternatives azolées commercialisées
- Écarter la vaginite atrophique post-ménopausique, sans fondement mécanistique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

