---
layout: default
title: Prucalopride
parent: Prédiction du modèle uniquement (L5)
nav_order: 639
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
description: "Prucalopride : nouvelle indication prédite, Hypoalphalipoprotéinémie (hypoalphalipoproteinemia) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Prucalopride
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

## Prucalopride: Hypoalphalipoprotéinémie (hypoalphalipoproteinemia)
{: .text-alpha }

## Résumé en Une Phrase

La prucalopride est un agoniste sélectif des récepteurs 5-HT4, initialement utilisé pour le traitement de la constipation chronique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypoalphalipoprotéinémie**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypoalphalipoprotéinémie (hypoalphalipoproteinemia) |
| Score de Prédiction TxGNN | 0.9982 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la prucalopride est un agoniste sélectif des récepteurs 5-HT4 (gène HTR4) agissant sur la motilité gastro-intestinale. Son usage établi est le traitement de la constipation chronique chez l'adulte lorsque les laxatifs sont inefficaces.

**Cette prédiction n'est pas étayée mécanistiquement.** Aucun lien crédible n'est identifié entre l'agonisme 5-HT4 et le métabolisme des HDL ou la régulation de l'ApoA-I. Le score élevé du modèle TxGNN est une prédiction purement computationnelle, sans essai ni publication à l'appui. La similarité avec l'indication d'origine n'a pas été évaluée.

Pour information, les autres prédictions du modèle ne sont pas mieux soutenues. Les plus proches d'une logique symptomatique sont l'amylose (score 0,9962) et l'amylose primaire (0,9956), où une atteinte digestive peut provoquer une dysmotilité qu'un prokinétique pourrait théoriquement soulager. Il s'agirait d'un effet symptomatique et non d'une modification de la maladie ; ces pistes sont classées « question de recherche » (niveau L4). Les prédictions pour l'hypercholestérolémie familiale homozygote, l'ulcère duodénal, la candidose buccale, la strongyloïdose et l'infection par le VIH ne reposent sur aucun mécanisme plausible.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hypoalphalipoprotéinémie.

À titre indicatif, deux publications ont été retrouvées pour les prédictions liées à l'amylose, sans évaluer l'efficacité de la prucalopride :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Rapport de cas | Cureus | Amylose révélée par une pseudo-obstruction intestinale chronique chez un homme de 61 ans, après plusieurs laparotomies exploratrices sans diagnostic |
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Cohorte | Turk J Gastroenterol | Les troubles moteurs digestifs spécifiques (gastroparésie, pseudo-obstruction, inertie colique) sont souvent pris à tort pour des troubles fonctionnels |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69471136 | RESOLOR 1 mg, comprimé pelliculé (active) | Comprimé pelliculé | Non renseignée |
| 63947653 | RESOLOR 2 mg, comprimé pelliculé (active) | Comprimé pelliculé | Non renseignée |

Le médicament est commercialisé en France : les 2 AMM sont valides (2 sur 2).

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : rectocolite hémorragique, maladie inflammatoire chronique de l'intestin, perforation intestinale.
- **Cible pharmacologique** : récepteur 5-HT4 (HTR4) ; aucune interaction médicamenteuse cliniquement documentée n'a été retrouvée.

Les mises en garde et contre-indications de la notice ANSM ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible entre l'agonisme 5-HT4 et le métabolisme des HDL.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), actuellement manquante et bloquante pour le dépistage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Une hypothèse biologique crédible reliant le récepteur 5-HT4 au métabolisme lipidique, avec des données précliniques
- Si une piste symptomatique est explorée, étudier en priorité la dysmotilité digestive liée à l'amylose comme question de recherche, et non l'hypoalphalipoprotéinémie
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

