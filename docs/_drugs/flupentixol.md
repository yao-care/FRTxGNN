---
layout: default
title: Flupentixol
parent: Prédiction du modèle uniquement (L5)
nav_order: 340
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Flupentixol : nouvelle indication prédite, Dystrophie rétinienne avec ou sans anomalies extraoculaires (niveau de preuve L5). Indication d'origine : Schizophrénie"
monitor_inn: "flupentixol"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "hydranencephaly (disease)", "myopia X-linked", "syndromic myopia", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy"]
---

# Flupentixol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Flupentixol : De la Schizophrénie à la Dystrophie Rétinienne (avec ou sans anomalies extraoculaires)

## Résumé en Une Phrase

Flupentixol est un antipsychotique de la famille des thioxanthènes, initialement utilisé pour le traitement de la **schizophrénie**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dystrophie rétinienne avec ou sans anomalies extraoculaires**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Schizophrénie (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Dystrophie rétinienne avec ou sans anomalies extraoculaires |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, flupentixol est un antipsychotique de type thioxanthène, dont l'efficacité dans la schizophrénie est établie. Les données pharmacologiques compilées indiquent qu'il se lie aux récepteurs dopaminergiques D1, D2, D3 et D5 (gènes DRD1, DRD2, DRD3, DRD5), avec un profil d'antagoniste dopaminergique.

À ce jour, aucun lien mécanistique n'a été établi entre ce blocage dopaminergique et les voies impliquées dans les dégénérescences rétiniennes d'origine génétique. Le score élevé du modèle TxGNN (99,99 %) repose uniquement sur des relations calculées dans le graphe de connaissances ; il ne constitue pas une preuve d'efficacité. La similarité entre l'indication d'origine (trouble psychiatrique) et la nouvelle indication (maladie génétique de la rétine) reste à évaluer.

À titre d'information, les données compilées signalent une activité antivirale in vitro (anti-SARS-CoV-2) rapportée dans des criblages de repositionnement, probablement liée à une phospholipidose induite. Cette information n'a pas de lien avec la prédiction ci-dessus.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69804637 | FLUANXOL LP 100 mg/1 ml, solution injectable (IM) | Solution injectable | Non renseignée (AMM annulée, titulaire : LUNDBECK SAS) |

## Considérations de Sécurité

**Interactions médicamenteuses / pharmacologie :** les données compilées ne rapportent aucune interaction médicamenteuse classée par niveau de gravité. Elles décrivent uniquement les cibles pharmacologiques du flupentixol : récepteurs dopaminergiques D1, D2, D3 et D5.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique, aucune publication, et aucun lien mécanistique plausible avec la dystrophie rétinienne.
- L'AMM française est annulée et les données de sécurité de la notice sont manquantes, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), étape bloquante pour l'évaluation de sécurité
- Compléter les données sur le mécanisme d'action (par exemple via l'API DrugBank)
- Établir une hypothèse mécanistique reliant le blocage dopaminergique à la physiopathologie des dystrophies rétiniennes
- Mener des études précliniques (modèles de dégénérescence rétinienne) avant toute envisagée clinique
- Clarifier la voie d'administration et la faisabilité de la formulation, au vu de l'AMM annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

