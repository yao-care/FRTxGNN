---
layout: default
title: Ranibizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 651
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ranibizumab : nouvelle indication prédite, Rétinopathie diabétique non proliférante sévère (niveau de preuve L5). Indication d'origine : Rétinopathie diabétique"
monitor_inn: "RANIBIZUMAB"
predicted_indications: ["immature cataract", "mature cataract", "tetanic cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "hemorrhagic disease of newborn"]
---

# Ranibizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Ranibizumab : De la rétinopathie diabétique à la rétinopathie diabétique non proliférante sévère

## Résumé en Une Phrase

Le ranibizumab est un fragment d'anticorps anti-VEGF, initialement utilisé pour traiter des maladies vasculaires de la rétine (rétinopathie diabétique, œdème maculaire diabétique, dégénérescence maculaire).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **rétinopathie diabétique non proliférante sévère**,
avec **19 publications** soutenant actuellement cette direction, mais **aucun essai clinique enregistré** dans les données compilées pour cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rétinopathie diabétique (selon le graphe de connaissances ; texte d'indication de l'AMM non renseigné) |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L1 (à confirmer, voir ci-dessous) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, le ranibizumab fait partie de la classe des anti-VEGF (fragment d'anticorps dirigé contre le VEGF-A). Son efficacité dans la rétinopathie diabétique et l'œdème maculaire diabétique est documentée, et mécanistiquement il est applicable à la rétinopathie non proliférante sévère.

Le VEGF favorise la perméabilité vasculaire rétinienne et la néovascularisation dans la rétinopathie diabétique. Des taux élevés de VEGF sériques et vitréens sont décrits dans cette maladie. La forme non proliférante sévère est un stade de la même maladie que l'indication d'origine : le lien est donc direct.

La littérature comprend des analyses post hoc des essais de phase 3 RIDE/RISE montrant une régression de la sévérité de la rétinopathie sous ranibizumab, ainsi qu'un essai randomisé du système de délivrance par port (PAVILION) dans la rétinopathie diabétique non proliférante. **Réserve :** aucun essai enregistré n'accompagne cette indication, et le niveau L1 repose sur les titres de publications, dont la conception et la phase n'ont pas été vérifiées à partir des résumés.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour cette indication.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | ECR | JAMA Ophthalmol | Système de délivrance par port de ranibizumab vs surveillance dans la RD non proliférante sans œdème maculaire (essai PAVILION) |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Méta-analyse (post hoc d'ECR) | Ophthalmol Retina | Lien entre la sévérité initiale de la RD et le délai de résolution de l'œdème maculaire sous ranibizumab |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Analyse post hoc d'ECR | Clin Ophthalmol | Prédicteurs de régression précoce de la RD dans RIDE/RISE |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Extension ouverte d'ECR | BMJ Open Ophthalmol | Évolution du score de sévérité de la RD avec un traitement moins fréquent après induction |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Analyse secondaire d'ECR | JAMA Ophthalmol | Évolution de la RD à 2 ans : aflibercept, bévacizumab et ranibizumab |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Analyse d'ECR (DRCR.net Protocole I) | Retina | Changements de sévérité de la RD à 5 ans sous ranibizumab |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Revue systématique et méta-analyse | Health Technol Assess | Anti-VEGF vs photocoagulation laser dans la RD |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Revue systématique et méta-analyse | Eur J Pharmacol | Système de délivrance par port de ranibizumab dans la RD et l'œdème maculaire diabétique |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Revue | Expert Opin Biol Ther | Ranibizumab dans le traitement de la rétinopathie diabétique |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | Cohorte rétrospective | Front Endocrinol | Nomogramme prédictif de réponse à l'anti-VEGF + laser dans la RD non proliférante sévère |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68654266 | BYOOVIZ 10 mg/mL | Solution injectable | Non renseignée (AMM annulée) |
| 64339586 | LUCENTIS 10 mg/ml, seringue préremplie | Solution injectable | Non renseignée (AMM annulée) |
| 68594506 | RANIVISIO 10 mg/mL, seringue préremplie | Solution injectable | Non renseignée (AMM annulée) |
| 64389258 | RANIVISIO 10 mg/mL | Solution injectable | Non renseignée (AMM annulée) |
| 67026689 | XIMLUCI 10 mg/mL | Solution injectable | Non renseignée (AMM annulée) |

Une sixième AMM annulée existe (RIMMYRAH 10 mg/ml, solution injectable, n° 61190863). Aucune AMM n'est actuellement valide.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : infection oculaire, conjonctivite.

Pour le reste, veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le lien mécanistique est direct (anti-VEGF dans une rétinopathie VEGF-dépendante) et la littérature inclut des analyses d'essais de phase 3 (RIDE/RISE) et un ECR dans la RD non proliférante. Toutefois, aucun essai enregistré n'est fourni, le niveau L1 n'a pas été vérifié sur les résumés, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmer directement la conception, la phase et les résultats des essais (RIDE/RISE, PAVILION)
- Vérifier la disponibilité et le statut réglementaire actuels en France (AMM annulées ; autres procédures éventuelles)
- Obtenir la notice (mises en garde, contre-indications) auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action

## Autres indications prédites (non retenues)

Les autres prédictions (cataractes de divers types, maladie hémorragique du nouveau-né) présentent des scores TxGNN élevés (jusqu'à 99,99 %) mais **aucune plausibilité biologique** : preuves indirectes ou absentes, probablement dues à la proximité dans le graphe de connaissances. Décision : **Hold**. À noter, un cas de syndrome de blocage capsulaire après injection de ranibizumab a été rapporté (effet indésirable, pas un bénéfice thérapeutique).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

