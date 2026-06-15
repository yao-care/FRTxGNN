---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Le skill txgnn-pipeline concerne la gestion du pipeline de modèles — pas la rédaction de rapports. Je vais directement générer le rapport selon le format défini.

---

# Asfotase Alfa : De l'Hypophosphatasie au Trouble de la Phosphorylation Oxydative Mitochondriale d'Origine Nucléaire

## Résumé en Une Phrase

Asfotase alfa (Strensiq®) est une enzyme de remplacement recombinante ciblant la phosphatase alcaline non spécifique des tissus (TNSALP), dont l'indication mondialement approuvée est l'hypophosphatasie (HPP) — une maladie osseuse métabolique héréditaire rare — bien qu'aucune AMM ne soit enregistrée en France à ce jour.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble de la Phosphorylation Oxydative Mitochondriale lié à des Anomalies de l'ADN Nucléaire**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction — il s'agit d'une prédiction computationnelle pure sans validation externe.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Hypophosphatasie (HPP) — aucune AMM enregistrée en France |
| Nouvelle Indication Prédite | Trouble de la phosphorylation oxydative mitochondriale (anomalie ADN nucléaire) |
| Score de Prédiction TxGNN | 99,95% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, Asfotase alfa est une phosphatase alcaline non spécifique des tissus recombinante humaine (TNSALP) fusionnée à un domaine de ciblage osseux (deca-aspartate). Son efficacité dans l'hypophosphatasie repose sur l'hydrolyse du pyrophosphate inorganique (PPi) — un inhibiteur endogène de la minéralisation osseuse — ainsi que du pyridoxal-5'-phosphate (PLP) et de la phosphoéthanolamine (PEA). La restauration de l'activité TNSALP permet la minéralisation normale de l'os et des cartilages.

Le lien mécanistique avec les troubles de la phosphorylation oxydative mitochondriale (OXPHOS) est extrêmement ténu. Le PPi est effectivement un sous-produit de réactions de biosynthèse mitochondriale, ce qui crée une connexion théorique très indirecte. Cependant, le défaut central des maladies OXPHOS réside dans des mutations de gènes codant pour les complexes de la chaîne respiratoire (I à V) ou des facteurs d'assemblage, un mécanisme pathogénique fondamentalement distinct de la voie TNSALP/phosphate. Asfotase alfa ne peut pas corriger un déficit de la chaîne respiratoire.

L'analyse de la rationale fournie indique que ce score élevé (99,95%) reflète très probablement une **proximité topologique dans le graphe de connaissances biomédicales** — les nœuds de maladies rares à phénotype métabolique ou osseux se trouvent structurellement proches dans le graphe — plutôt qu'une réelle relation biologique exploitable. Ce phénomène est confirmé par l'absence totale de preuves cliniques ou de littérature pour l'ensemble des 10 indications prédites dans ce rapport.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Analyse des 10 Indications Prédites

Pour information, voici l'ensemble des 10 candidats identifiés par TxGNN, tous classés L5/Hold, avec une évaluation de la plausibilité mécanistique :

| Rang | Indication | Score TxGNN | Lien Mécanistique | Décision |
|---|---|---|---|---|
| 1 | Trouble OXPHOS mitochondrial (ADN nucléaire) | 99,95% | Très faible — PPi comme sous-produit mitochondrial, sans pertinence pour les déficits OXPHOS | Hold |
| 2 | Syndrome de Steel | 99,91% | Nul — déficit en COL27A1 (collagène), sans lien avec la voie ALP | Hold |
| 3 | Insuffisance pancréatique exocrine | 99,89% | Nul — déficit en lipase/amylase pancréatique, voie sans intersection avec TNSALP | Hold |
| 4 | Syndrome de Scheie (MPS IS) | 99,85% | Nul — déficit en IDUA, accumulation de GAG lysosomal, mécanisme distinct | Hold |
| 5 | Syndrome de Hurler (MPS IH) | 99,75% | Nul — même famille que Scheie, phénotype osseux superficiellement similaire (faux signal) | Hold |
| 6 | Maladie de surcharge lysosomale avec atteinte squelettique | 99,73% | Très faible indirect — certains LSD peuvent avoir des perturbations secondaires du métabolisme phosphocalcique | Hold |
| 7 | Déficit familial en ApoC-II | 99,71% | Nul — hypertriglycéridémie, aucun lien avec le métabolisme phosphate/ALP | Hold |
| 8 | Varices œsophagiennes avec hémorragie | 99,68% | Nul — hypertension portale/cirrhose, mécanisme vasculaire sans lien avec TNSALP | Hold |
| 9 | Varices œsophagiennes sans hémorragie | 99,68% | Nul — même score que rang 8 (artefact de fusion de nœuds dans le graphe) | Hold |
| 10 | Cystinose | 99,65% | **Faible mais le plus élevé** — syndrome de Fanconi → phosphaturie → métabolisme du phosphate indirect | Hold |

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité (mises en garde, contre-indications et interactions médicamenteuses).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'ensemble des 10 indications prédites est classé L5 (prédiction computationnelle uniquement, sans aucune étude réelle) avec une décision unanime de suspension. L'analyse mécanistique systématique confirme que les scores élevés résultent en grande partie d'artefacts topologiques dans le graphe de connaissances : les maladies identifiées partagent des phénotypes squelettiques ou métaboliques superficiellement similaires à l'HPP, mais leurs mécanismes pathogéniques (déficits enzymatiques lysosomaux, mutations de la chaîne respiratoire, défauts de collagène, hypertension portale) sont fondamentalement distincts de la voie TNSALP/PPi sur laquelle agit Asfotase alfa.

**Pour avancer, les éléments suivants sont nécessaires :**

- **Données réglementaires** : Vérifier l'enregistrement EMA (Strensiq® a obtenu une AMM européenne en 2015) pour corriger le statut de marché France — celui-ci est vraisemblablement inexact dans ce dossier
- **Mécanisme d'action (MOA)** : Récupérer les données complètes via l'API DrugBank (DB09105) pour valider les substrats cibles et les voies biologiques
- **Sécurité** : Obtenir la notice EMA/TFDA officielle pour les mises en garde, contre-indications et données de tolérance à long terme
- **Piste prioritaire (si repositionnement souhaité)** : La **cystinose** (rang 10) est la seule candidate avec un lien mécanistique indirect identifiable (syndrome de Fanconi → phosphaturie → déséquilibre phosphocalcique), mais nécessiterait des études précliniques dédiées avant tout développement clinique — le traitement standard étant la supplémentation en phosphate, non la substitution enzymatique ALP
- **Révision du pipeline TxGNN** : Investiguer l'inflation des scores pour les maladies rares à phénotype osseux afin de distinguer proximité topologique et plausibilité biologique réelle
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

