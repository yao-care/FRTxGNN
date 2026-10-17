---
layout: default
title: Asfotase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Asfotase Alfa : nouvelle indication prédite, Trouble de la phosphorylation oxydative mitochondriale dû à des anoma… (niveau de preuve L5). Indication d'origine : Hypophosphatasie"
monitor_inn: "ASFOTASE ALFA"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Steel syndrome", "exocrine pancreatic insufficiency", "Scheie syndrome", "Hurler syndrome", "lysosomal storage disease with skeletal involvement", "familial apolipoprotein C-II deficiency", "esophageal varices with bleeding", "esophageal varices without bleeding", "cystinosis"]
---

# Asfotase Alfa
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

# Asfotase alfa : De l'hypophosphatasie au trouble de la phosphorylation oxydative mitochondriale (ADN nucléaire)

## Resume en Une Phrase

Asfotase alfa est une enzyme recombinante (protéine de fusion de la phosphatase alcaline tissu-non spécifique, TNSALP), initialement utilisée pour le traitement de l'hypophosphatasie.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Hypophosphatasie (source : graphe de connaissances TxGNN ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Predite | Trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire |
| Score de Prediction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, asfotase alfa est une enzyme recombinante TNSALP qui dégrade des substrats extracellulaires tels que le pyrophosphate inorganique et le pyridoxal-5'-phosphate, ce qui rétablit la minéralisation osseuse dans l'hypophosphatasie.

**Aucun lien mécanistique n'est établi** avec la nouvelle indication. Les troubles de la phosphorylation oxydative liés à l'ADN nucléaire sont des déficits bioénergétiques intracellulaires, et une enzyme extracellulaire n'a pas de voie évidente pour les corriger. Le score élevé de TxGNN (99,95 %) reflète uniquement une association dans le graphe de connaissances et ne constitue pas une preuve de plausibilité biologique. La similarité avec l'indication d'origine reste à évaluer.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 64450234 | STRENSIQ 40 mg/ml, solution injectable (ALEXION EUROPE) | Solution injectable | Non renseignée (AMM annulée) |
| 69258437 | STRENSIQ 100 mg/ml, solution injectable (ALEXION EUROPE) | Solution injectable | Non renseignée (AMM annulée) |

## Considerations de Securite

Veuillez consulter la notice pour les informations de sécurité.

## Autres Predictions du Modele (Information)

Les neuf prédictions suivantes présentent également un niveau de preuve L5, sans essai ni publication, et une recommandation Hold. Les mécanismes plausibles sont absents ou purement thématiques (remplacement enzymatique, atteinte squelettique).

| Rang | Maladie predite | Score TxGNN | Remarque |
|------|------|------|------|
| 2 | Syndrome de Steel | 99,91 % | Lien indirect via la minéralisation osseuse, non étayé |
| 3 | Insuffisance pancréatique exocrine | 99,89 % | Association générique « enzyme de remplacement » |
| 4 | Syndrome de Scheie | 99,85 % | Traitement spécifique existant (laronidase) ; pas d'action sur l'IDUA |
| 5 | Syndrome de Hurler | 99,75 % | Même constat que Scheie |
| 6 | Maladie lysosomale avec atteinte squelettique | 99,73 % | Catégorie large ; bénéfice spéculatif |
| 7 | Déficit familial en apolipoprotéine C-II | 99,71 % | Aucun rôle dans le métabolisme lipoprotéique |
| 8 | Varices œsophagiennes avec saignement | 99,68 % | Probable artefact du graphe |
| 9 | Varices œsophagiennes sans saignement | 99,68 % | Score identique au précédent : signal de graphe partagé |
| 10 | Cystinose | 99,65 % | Lien superficiel ; pas d'action sur l'accumulation de cystine |

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique, sans publication ni lien mécanistique plausible. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice font défaut, ce qui bloque l'étape de revue de sécurité.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Démontrer un lien mécanistique entre l'activité TNSALP et les troubles de la phosphorylation oxydative (études précliniques)
- Vérifier le statut de commercialisation actuel du produit en France (AMM annulées) et la compatibilité des voies d'administration
- Rechercher d'éventuelles études publiées ou en cours, absentes des données actuelles
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

