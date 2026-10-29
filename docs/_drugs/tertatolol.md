---
layout: default
title: Tertatolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 747
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-29
description: "Tertatolol : nouvelle indication prédite, Dyskinésie linguo-faciale-buccale (niveau de preuve L5). Indication d'origine : Non renseignée"
monitor_inn: "TERTATOLOL"
predicted_indications: ["lingual-facial-buccal dyskinesia", "chronic tic disorder", "psychogenic movement disorders", "benign shuddering attacks", "extrapyramidal and movement disease", "primary orthostatic tremor", "tremor-nystagmus-duodenal ulcer syndrome", "benign paroxysmal tonic upgaze of childhood with ataxia"]
---

# Tertatolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Tertatolol : De l'indication originale non documentée à la dyskinésie linguo-faciale-buccale
{: .text-alpha }

## Résumé en Une Phrase

Tertatolol est un bêtabloquant non sélectif, pour lequel aucune indication d'origine n'est renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dyskinésie linguo-faciale-buccale**,
mais cette prédiction ne repose que sur le score du modèle : **aucun essai clinique** et **une seule publication préclinique** (chez le rongeur) sont disponibles.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée |
| Nouvelle Indication Prédite | Dyskinésie linguo-faciale-buccale |
| Score de Prédiction TxGNN | 0,9916 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé (aucune autorisation enregistrée) |
| Nombre d'AMM | 0 (valides : 0) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le tertatolol est un antagoniste bêta-adrénergique non sélectif, qui aurait aussi une affinité pour les récepteurs 5-HT1A/5-HT1B.

La seule publication associée (PMID 8788480, 1996) est une étude de pharmacologie chez le rongeur sur des agonistes et antagonistes 5-HT1A dans la nociception. Elle ne traite pas de la dyskinésie : le lien avec la dyskinésie orofaciale reste donc spéculatif. Les bêtabloquants ont un historique d'usage dans le tremblement et l'akathisie, mais rien dans les données ne soutient un effet dans les dyskinésies tardives ou orofaciales.

Le score élevé (0,9916) est une prédiction purement computationnelle issue du modèle TxGNN (apprentissage profond). Il peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique propre au médicament.

### Autres indications prédites (pour information)

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve | Remarque |
|------|------|------|------|------|
| 2 | Tic chronique | 0,9912 | L5 | Aucune donnée ; les agonistes alpha-2 sont la classe adrénergique de référence, pas les bêtabloquants |
| 3 | Troubles du mouvement psychogènes | 0,9910 | L5 | Aucune donnée ; prise en charge surtout non médicamenteuse |
| 4 | Frissons bénins du nourrisson (« shuddering attacks ») | 0,9909 | L5 | Affection bénigne et spontanément résolutive, rapport bénéfice-risque défavorable |
| 5 | Maladie extrapyramidale et des mouvements | 0,9909 | L5 | Catégorie large, sans hypothèse mécanistique précise |
| 6 | Tremblement orthostatique primaire | 0,9905 | L5 | Réponse habituellement médiocre aux bêtabloquants (clonazépam, gabapentine privilégiés) |
| 7 | Syndrome tremblement-nystagmus-ulcère duodénal | 0,9903 | L5 | Syndrome extrêmement rare, aucune donnée |
| 8 | Élévation tonique paroxystique bénigne du regard avec ataxie | 0,9902 | L5 | Affection pédiatrique rare, souvent spontanément résolutive, aucune donnée |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8788480](https://pubmed.ncbi.nlm.nih.gov/8788480/) | 1996 | Préclinique (pharmacologie chez le rongeur) | Behavioural Brain Research | Chez la souris, les agonistes 5-HT1A (8-OH-DPAT, flesinoxan) inhibent les deux phases du léchage induit par la formaline. Les antagonistes, dont le tertatolol, sont plus puissants sur la phase tardive et n'induisent une ataxie qu'à très fortes doses. Aucun lien avec la dyskinésie. |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune donnée d'interaction médicamenteuse n'a été retrouvée pour ce médicament.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5) : aucun essai clinique, et une seule étude préclinique sans rapport direct avec la dyskinésie.
- Statut de commercialisation : non commercialisé. Les données de sécurité réglementaires sont manquantes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (ou d'une autorité équivalente), indispensables avant tout examen de sécurité
- Des données détaillées sur le mécanisme d'action (via DrugBank)
- Des preuves cliniques ou précliniques directement liées à la dyskinésie orofaciale ou aux autres indications prédites
- La confirmation de l'indication d'origine et du statut réglementaire du médicament
- Une évaluation de la faisabilité (voie d'administration, disponibilité du produit), compte tenu de l'absence d'AMM en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

