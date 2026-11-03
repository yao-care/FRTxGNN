---
layout: default
title: Tioconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 764
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-03
monitor_inn: "TIOCONAZOLE"
predicted_indications: ["vulvitis", "postmenopausal atrophic vaginitis"]
description: "Tioconazole : nouvelle indication prédite, Vulvite (vulvitis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Tioconazole
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

## Tioconazole: Vulvite (vulvitis)
{: .text-alpha }

## Résumé en Une Phrase

Le tioconazole est un antifongique azolé d'usage local (ovule et crème dermatologique).
Le modèle TxGNN prédit qu'il pourrait être utile dans la **vulvite (vulvitis)**, mais les données compilées pour ce rapport ne contiennent **aucun essai clinique** et **aucune étude portant directement sur la vulvite** ; les publications disponibles (20) concernent la candidose vaginale et restent indirectes.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Vulvite (vulvitis) |
| Score de Prédiction TxGNN | 0.9920 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier compilé. Les références pharmacologiques indiquent toutefois que le tioconazole cible la lanostérol 14-α déméthylase (CYP51/ERG11) chez les champignons et levures : en bloquant la synthèse de l'ergostérol, composant essentiel de la membrane fongique, il empêche la survie du pathogène. Il inhibe aussi une enzyme humaine, la CYP8B1, impliquée dans la synthèse des acides biliaires.

Une vulvite s'accompagne souvent d'une infection à *Candida*. Dans ce cas, un mécanisme azolé antifongique est plausible. Le lien reste cependant **indirect** : la littérature récupérée porte sur la candidose vaginale et non sur la vulvite en tant qu'entité distincte. Aucune efficacité n'est démontrée dans les vulvites non fongiques (irritatives, de contact, allergiques).

Aucune étude citée ne portant directement sur la vulvite, le niveau de preuve est plafonné à L5, même si le score du modèle est élevé.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Les publications ci-dessous concernent la candidose vaginale ou le tioconazole en général ; aucune n'étudie directement la vulvite.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | Essai randomisé comparatif | Antimicrob Agents Chemother | Tioconazole en dose unique (80 patientes) : 84 % d'absence de symptômes à 4 semaines, contre 85 % avec le clotrimazole sur 3 jours |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | ECR double aveugle vs placebo | Gynakol Rundsch | Comparaison tioconazole/placebo dans la candidose vaginale, avec évaluation de l'absorption systémique |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Revue | Drugs | Large spectre antimicrobien in vitro ; efficacité et bonne tolérance des préparations topiques dans les mycoses superficielles |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Étude clinique | Acta Obstet Gynecol Scand | Crème vaginale à 2 % pendant 3 jours : taux de guérison mycologique de 88,5 % |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Essai randomisé ouvert | J Int Med Res | Tioconazole topique en dose unique vs kétoconazole oral 5 jours (40 patientes) : éradication dans les deux groupes, réponse symptomatique plus rapide en topique |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Étude ouverte non comparative | J Int Med Res | Crème à 2 % dans l'infection à *Trichomonas vaginalis* ou mixte : 95 % de guérison (19/20) |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Revue | Expert Rev Anti Infect Ther | Perspectives des azolés non invasifs dans la candidose vulvovaginale |

## Informations de Marché en France

Le tioconazole est commercialisé en France. Les deux AMM recensées sont valides.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67466927 | GYNO TROSYD 300 mg, ovule (TEOFARMA) | Ovule | Non renseignée (AMM active) |
| 69571802 | TROSYD, crème dermatologique (TEOFARMA) | Crème | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 2 interactions recensées. L'interaction avec l'oméprazole est de niveau non précisé. Le tioconazole inhibe par ailleurs l'enzyme humaine CYP8B1 (voie de synthèse des acides biliaires), sans niveau de gravité défini.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN est élevé (0,9920), mais aucun essai clinique ni aucune étude ne porte directement sur la vulvite. Les données disponibles concernent la candidose vaginale, et le lien mécanistique n'est plausible que pour une vulvite d'origine fongique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études cliniques ciblant spécifiquement la vulvite, en distinguant les formes fongiques des formes non infectieuses
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice officielle
- Évaluation de l'adéquation des formes disponibles (ovule, crème) à une atteinte vulvaire

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

