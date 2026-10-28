---
layout: default
title: Lanadelumab
parent: Preuves élevées (L1-L2)
nav_order: 434
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "lanadelumab"
predicted_indications: ["C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "pancreatitis", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "Glanzmann thrombasthenia", "antisynthetase syndrome", "focal myositis", "Scott syndrome"]
description: "Lanadelumab : nouvelle indication prédite, Déficience en inhibiteur de C1 (C1 inhibitor deficiency) (niveau de preuve L1). Indication d'origine : Non renseignée dans les données locales"
---

# Lanadelumab
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

## Lanadelumab: Déficience en inhibiteur de C1 (C1 inhibitor deficiency)
{: .text-alpha }

## Résumé en Une Phrase

Lanadélumab est un anticorps monoclonal humain dirigé contre la kallicréine plasmatique, initialement utilisé pour la prévention des crises d'angio-œdème héréditaire (AOH).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **déficience en inhibiteur de C1**, avec **5 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il faut toutefois noter que cette indication prédite correspond en pratique à l'indication d'origine du médicament : il ne s'agit pas d'un repositionnement au sens strict, mais plutôt d'une validation de la prédiction du modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Déficience en inhibiteur de C1 (C1 inhibitor deficiency) |
| Score de Prédiction TxGNN | 1.0000 |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. Sur la base des informations connues, le lanadélumab inhibe la kallicréine plasmatique : il se lie à la kallicréine (gène *KLKB1*) sans se fixer à la prékallicréine.

Dans la déficience en inhibiteur de C1 (mutations de *SERPING1*), l'activité de la kallicréine plasmatique n'est plus contrôlée. Cela entraîne une production excessive de bradykinine, un vasodilatateur responsable des crises de gonflement. En bloquant la kallicréine, le lanadélumab agit directement sur cette voie, ce qui explique la cohérence biologique de la prédiction.

Cette indication coïncide avec l'usage d'origine du médicament. La forte concordance du modèle illustre donc surtout sa capacité à retrouver une indication déjà établie. Les autres indications prédites (rangs 2 à 10, par exemple pancréatite, maladie de Glanzmann ou myosite focale) ne reposent sur aucun essai ni publication, et pour la plupart sans lien mécanistique plausible : elles restent au niveau L5 (« Hold »).

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Terminé | 20 | Étude ouverte multicentrique sur la sécurité, la pharmacocinétique et l'efficacité chez des patients chinois atteints d'AOH (26 semaines de traitement) |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Terminé | 21 | Étude SPRING : sécurité, pharmacocinétique et efficacité chez des enfants de 2 à <12 ans atteints d'AOH |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Terminé | 12 | Étude ouverte d'efficacité et de sécurité chez des patients japonais atteints d'AOH de type I ou II |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | N/A | Actif, ne recrute plus | 155 | Enquête japonaise post-commercialisation sur la sécurité et l'efficacité à long terme (non interventionnelle) |
| [NCT04583007](https://clinicaltrials.gov/study/NCT04583007) | N/A | Plus disponible | N/A | Programme d'accès élargi pour la prévention des crises d'AOH chez l'enfant de 2 à <12 ans et dans l'angio-œdème non histaminergique à C1-INH normal |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | ECR | JAMA | Essai randomisé contre placebo (HELP) : prévention des crises d'AOH par le lanadélumab |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Extension ouverte | Allergy | Étude HELP OLE : efficacité et sécurité à long terme chez les patients ≥12 ans atteints d'AOH de type 1/2 |
| [40504359](https://pubmed.ncbi.nlm.nih.gov/40504359/) | 2025 | Étude en vie réelle (phase 4) | Adv Ther | EMPOWER : efficacité et tolérance soutenues jusqu'à 36 mois |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Méta-analyse en réseau | Drugs R D | Comparaison indirecte des traitements de prophylaxie à long terme de l'AOH |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Comparaison indirecte | J Comp Eff Res | Lanadélumab vs inhibiteur de C1-estérase chez l'enfant <12 ans |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Revue systématique | Clin Rev Allergy Immunol | Crises survenant sous prophylaxie à long terme dans l'AOH de type I/II |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Revue / analyse post hoc | BioDrugs | Lanadélumab dans l'AOH avec déficience en C1-INH : études précliniques et de phase I |
| [31560114](https://pubmed.ncbi.nlm.nih.gov/31560114/) | 2019 | Revue | Drugs | Réduction significative des crises vs placebo dans l'essai pivot HELP |
| [40769455](https://pubmed.ncbi.nlm.nih.gov/40769455/) | 2025 | Données en vie réelle | Ann Allergy Asthma Immunol | Contrôle de la maladie et qualité de vie selon le niveau d'activité de l'AOH |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Rapport de cas | J Allergy Clin Immunol Pract | Efficacité du lanadélumab dans l'angio-œdème acquis avec déficience en C1-INH |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63473155 | TAKHZYRO 300 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM active) |
| 61988861 | TAKHZYRO 300 mg, solution injectable | Solution injectable | Non renseignée (AMM active) |
| 67650090 | TAKHZYRO 150 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM active) |

Les trois AMM, détenues par Takeda Pharmaceuticals International (Irlande), sont valides : le médicament est commercialisé dans ce pays (3 AMM valides sur 3).

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une seule interaction de nature pharmacologique est recensée, avec la cible du médicament, la kallicréine B1 (*KLKB1*), qu'il inhibe par conception. Aucun niveau de gravité n'est renseigné.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 terminés, un essai randomisé contre placebo (HELP, JAMA 2018), des données d'extension à long terme et des données en vie réelle soutiennent l'efficacité du lanadélumab dans l'AOH par déficience en C1-INH. Toutefois, cette indication est celle d'origine du médicament, et les trois AMM françaises sont annulées. Les garde-fous portent donc sur le statut réglementaire et sur l'absence de données de sécurité issues de la notice.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle (mises en garde et contre-indications), actuellement manquante et bloquante pour le dépistage de sécurité
- Clarifier la raison de l'annulation des AMM françaises et le statut d'accès actuel au médicament en France (par exemple via une autre procédure d'autorisation)
- Compléter les données sur le mécanisme d'action (DrugBank)
- Ne pas poursuivre les autres indications prédites (rangs 2 à 10) sans preuves : elles restent en « Hold » (niveau L5)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

