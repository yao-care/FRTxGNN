---
layout: default
title: Naftidrofuryl
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 1
---

# Naftidrofuryl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Naftidrofuryl : Vers une Nouvelle Piste dans l'AVC Ischémique

## Résumé en Une Phrase

L'indication d'origine du naftidrofuryl n'est pas documentée dans le dossier de preuves actuel (mécanisme d'action et indications d'origine marqués comme lacune de données). Le modèle TxGNN predit qu'il pourrait être efficace pour l'**AVC (stroke disorder)**, avec un score de prédiction de **99,65 %**, soutenu par **20 publications** (dont 3 essais contrôlés randomisés historiques et une revue systématique Cochrane), mais **aucun essai clinique enregistré** dans les registres modernes (ClinicalTrials.gov / ICTRP).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans le dossier de preuves (données manquantes) |
| Nouvelle Indication Prédite | AVC (Stroke Disorder) |
| Score de Prédiction TxGNN | 99,65 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank pour ce dossier (lacune signalée, sévérité élevée). Sur la base des informations pharmacologiques connues rapportées dans l'analyse de repositionnement, le naftidrofuryl agirait comme un **antagoniste des récepteurs sérotoninergiques 5-HT2** associé à un effet vasodilatateur modéré, capable d'améliorer le métabolisme tissulaire en hypoxie (augmentation du rapport ATP/ADP, réduction de l'accumulation de lactate).

Ce profil pharmacologique offre une justification mécanistique théorique pour une application dans l'AVC ischémique, ce qui pourrait expliquer le score TxGNN élevé (0,9965). Cependant, ce lien mécanistique reste indirect : l'indication d'origine du médicament n'est pas renseignée dans le dossier, et le médicament n'est actuellement commercialisé sur aucun marché de référence recensé dans ce dossier.

La littérature historique (années 1978–2007) montre un intérêt clinique réel et ancien pour cette piste, avec plusieurs essais randomisés en double aveugle menés spécifiquement sur l'AVC aigu et subaigu, ce qui renforce la plausibilité biologique au-delà de la seule prédiction algorithmique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement (aucun résultat dans ClinicalTrials.gov ni dans le registre ICTRP pour la combinaison naftidrofuryl / AVC).

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2285001](https://pubmed.ncbi.nlm.nih.gov/2285001/) | 1990 | ECR | Age and Ageing | Essai randomisé en double aveugle chez 100 patients avec AVC hémisphérique aigu (<72h) ; naftidrofuryl oral vs placebo pendant 12 semaines, suivi de 26 semaines |
| [3537823](https://pubmed.ncbi.nlm.nih.gov/3537823/) | 1986 | ECR | Neuroepidemiology | Essai contrôlé mono-centrique visant à établir un modèle méthodologique d'essai clinique sur l'AVC aigu avec naftidrofuryl |
| [1369722](https://pubmed.ncbi.nlm.nih.gov/1369722/) | 1990 | ECR | J Cardiovasc Pharmacol | Étude en double aveugle contrôlée par placebo chez 82 patients en phase subaiguë d'AVC invalidant ; naftidrofuryl 600 mg/j pendant 60 jours associé à aspirine + dipyridamole, évaluation des fonctions motrices |
| [17443593](https://pubmed.ncbi.nlm.nih.gov/17443593/) | 2007 | Revue Systématique | Cochrane Database Syst Rev | Revue Cochrane sur l'efficacité du naftidrofuryl dans l'AVC aigu ; preuves existantes jugées incertaines pour un usage systématique |
| [1369721](https://pubmed.ncbi.nlm.nih.gov/1369721/) | 1990 | Revue | J Cardiovasc Pharmacol | Revue et hypothèse sur le rôle du naftidrofuryl après un AVC aigu, incluant son blocage sélectif des récepteurs S2 |
| [6349963](https://pubmed.ncbi.nlm.nih.gov/6349963/) | 1983 | Revue | Drugs | Revue de la pharmacologie clinique des médicaments « cérébroactifs » (dont le naftidrofuryl) dans les troubles cérébrovasculaires |
| [7517476](https://pubmed.ncbi.nlm.nih.gov/7517476/) | 1994 | Revue | J Cardiovasc Pharmacol | Évaluation économique des traitements médicamenteux dans la maladie vasculaire périphérique et l'AVC |
| [23795817](https://pubmed.ncbi.nlm.nih.gov/23795817/) | 2013 | Revue | J Intern Med | Revue de la prise en charge médicale de l'ischémie critique des membres, incluant le risque accru d'AVC associé |
| [26742197](https://pubmed.ncbi.nlm.nih.gov/26742197/) | 2015 | Revue | Bol Asoc Med P R | Revue des thérapies non invasives de la maladie artérielle périphérique, dans un contexte cardiovasculaire incluant l'AVC |
| [3120954](https://pubmed.ncbi.nlm.nih.gov/3120954/) | 1987 | Revue | BMJ | Article discutant des nouveaux traitements potentiels pour l'AVC ischémique aigu (résumé non disponible) |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune donnée de mise en garde, contre-indication ou interaction médicamenteuse (DDI) n'est actuellement disponible dans le dossier ; la recherche DDI n'a produit aucun résultat.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Malgré un score TxGNN élevé et un corpus historique de 3 essais randomisés plus une revue Cochrane suggérant une plausibilité clinique pour l'AVC, deux lacunes bloquantes empêchent de poursuivre : l'absence totale de données de sécurité réglementaire (mises en garde, contre-indications, notice ANSM) et l'absence de commercialisation actuelle en France (0 AMM). Le dossier ne peut pas franchir l'étape d'évaluation initiale de sécurité (S1) tant que ces éléments manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice/RCP officielle (ANSM ou équivalent) pour statuer sur les mises en garde et contre-indications (lacune bloquante DG001)
- Confirmation du mécanisme d'action via DrugBank (lacune DG002)
- Clarification de l'indication d'origine du médicament (donnée absente du dossier)
- Vérification de l'existence d'essais cliniques modernes enregistrés (ClinicalTrials.gov / ICTRP) sur l'AVC, actuellement à zéro
- Requête DDI complémentaire, la recherche actuelle n'ayant donné aucun résultat
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

