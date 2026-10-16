---
layout: default
title: Dexketoprofen
parent: Prédiction du modèle uniquement (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dexketoprofen : nouvelle indication prédite, Migraine (migraine disorder) (niveau de preuve L5). Indication d'origine : Non renseignée dans les AMM disponibles"
monitor_inn: "dexketoprofen"
predicted_indications: ["tendinitis", "fibromyalgia", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis", "migraine disorder", "headache disorder", "migraine with brainstem aura", "exostosis", "congenital hypotrichosis milia"]
---

# Dexketoprofen
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

# Dexképrofène : De l'indication d'origine non documentée à la Migraine

## Résumé en Une Phrase

La dexkétoprofène est un anti-inflammatoire non stéroïdien (AINS) commercialisé en France sous le nom KETESSE, mais le texte de l'indication d'origine n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **migraine** (rang 6 des prédictions), avec **5 essais cliniques** et **20 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM disponibles |
| Nouvelle Indication Prédite | Migraine (*migraine disorder*) |
| Score de Prédiction TxGNN | 99,87 % |
| Niveau de Preuve | L1 (selon le classement des données ; voir réserves ci-dessous) |
| Statut de Marché en France | Uniquement annulé (toutes les AMM sont annulées) |
| Nombre d'AMM | 5 |
| Décision Recommandée | Proceed with Guardrails |

**Remarque sur la sélection :** la première prédiction du classement (tendinite, score 99,90 %) ne repose que sur une étude de douleur musculo-squelettique non spécifique à la tendinite (niveau L4, Hold). La migraine est retenue ici car c'est l'indication prédite la mieux documentée.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances générales, la dexkétoprofène est un AINS qui inhibe les cyclooxygénases (COX-1/COX-2) et réduit la synthèse des prostaglandines, ce qui diminue l'inflammation et la douleur.

Cette action sur les prostaglandines et l'inflammation neurogène est impliquée dans la douleur migraineuse. La dexkétoprofène, déjà utilisée comme antalgique, peut donc raisonnablement s'appliquer à la crise de migraine aiguë. Plusieurs essais randomisés, dont un essai de phase 4 contrôlé contre placebo, et une méta-analyse d'essais randomisés ont évalué ce médicament dans cette situation.

**Réserves :** les essais sont de phase 4 (post-commercialisation) et non de phase 3 ; plusieurs sont des comparaisons avec un traitement actif aux urgences ; et le statut de marché « annulé » impose de vérifier le contexte réglementaire et la disponibilité. L'étape de décision est limitée à S2 car aucune indication autorisée et actuellement commercialisée n'est établie.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02159547](https://clinicaltrials.gov/study/NCT02159547) | Phase 4 | Terminé | 224 | Dexkétoprofène IV contre placebo dans la crise de migraine aux urgences (preuve la plus directe) |
| [NCT01730326](https://clinicaltrials.gov/study/NCT01730326) | Phase 4 | Terminé | 200 | Dexkétoprofène IV contre paracétamol dans la céphalée de la crise migraineuse aiguë |
| [NCT04372264](https://clinicaltrials.gov/study/NCT04372264) | Phase 4 | Inconnu | 210 | Paracétamol, dexkétoprofène et ibuprofène IV sur l'EVA de la douleur migraineuse |
| [NCT04533568](https://clinicaltrials.gov/study/NCT04533568) | Phase 4 | Terminé | 160 | Ibuprofène IV contre dexkétoprofène IV dans la céphalée migraineuse aux urgences |
| [NCT04252521](https://clinicaltrials.gov/study/NCT04252521) | Non applicable | Terminé | 150 | Métoclopramide, dexkétoprofène trométamol et leur association dans la migraine aiguë |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31725614](https://pubmed.ncbi.nlm.nih.gov/31725614/) | 2019 | Méta-analyse | Medicine | Efficacité de la dexkétoprofène contre placebo dans la crise de migraine (résultat décrit comme controversé) |
| [25944813](https://pubmed.ncbi.nlm.nih.gov/25944813/) | 2016 | ECR | Cephalalgia | Dexkétoprofène IV contre placebo dans la migraine aux urgences |
| [24412801](https://pubmed.ncbi.nlm.nih.gov/24412801/) | 2014 | ECR phase II | J Pain | Dexkétoprofène trométamol 25 mg et 50 mg contre placebo, étude croisée en double aveugle (93 patients) |
| [24394884](https://pubmed.ncbi.nlm.nih.gov/24394884/) | 2014 | ECR | Emerg Med J | Paracétamol IV contre dexkétoprofène dans la crise de migraine aux urgences |
| [32359776](https://pubmed.ncbi.nlm.nih.gov/32359776/) | 2020 | ECR | Am J Emerg Med | Métoclopramide, dexkétoprofène et leur association dans la migraine aiguë |
| [24363238](https://pubmed.ncbi.nlm.nih.gov/24363238/) | 2014 | ECR | Cephalalgia | Association frovatriptan + dexkétoprofène contre frovatriptan seul |
| [34085549](https://pubmed.ncbi.nlm.nih.gov/34085549/) | 2021 | ECR | Ann Saudi Med | Mésothérapie intradermique contre dexkétoprofène IV dans la migraine sans aura |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Recommandation | Headache | Mise à jour 2025 des recommandations de l'American Headache Society sur les traitements parentéraux de la migraine aux urgences |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | Méta-analyse en réseau | BMC Neurol | Efficacité et sécurité du métoclopramide comparé à d'autres antimigraineux |
| [25056381](https://pubmed.ncbi.nlm.nih.gov/25056381/) | 2014 | ECR | Expert Rev Neurother | Efficacité et tolérance du frovatriptan et de la dexkétoprofène dans la crise de migraine |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64613432 | KETESSE 25 mg, granulés pour solution buvable | Granulés pour solution buvable | Non renseignée (AMM annulée) |
| 63929235 | KETESSE 25 mg, solution buvable en sachet | Solution buvable | Non renseignée (AMM annulée) |
| 62128284 | KETESSE 25 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 60205458 | KETESSE 50 mg/2 ml, solution injectable/pour perfusion | Solution injectable ou pour perfusion | Non renseignée (AMM annulée) |
| 60162494 | SKUDEXUM 75 mg/25 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées, et les mises en garde et contre-indications de la notice ANSM n'ont pas pu être obtenues.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais randomisés (dont un essai de phase 4 contrôlé contre placebo) et une méta-analyse soutiennent l'usage de la dexkétoprofène dans la crise de migraine aiguë. Toutefois, il s'agit d'essais de phase 4, souvent contre comparateur actif, les AMM françaises sont toutes annulées et les données de sécurité de la notice manquent. La prudence s'impose.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice ANSM (mises en garde, contre-indications), une lacune bloquante pour l'évaluation de sécurité
- Compléter les données sur le mécanisme d'action (DrugBank)
- Vérifier la raison de l'annulation des AMM et la disponibilité actuelle du produit en France
- Confirmer l'efficacité par un essai de phase 3 ou une analyse critique de la méta-analyse, dont les conclusions sont décrites comme controversées
- Définir la voie d'administration adaptée (la compatibilité des voies n'est pas encore évaluée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

