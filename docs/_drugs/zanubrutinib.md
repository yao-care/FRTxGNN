---
layout: default
title: Zanubrutinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 337
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Zanubrutinib : Des Hémopathies à Cellules B à la Leucémie Myéloïde

## Résumé en Une Phrase

Le zanubrutinib est un inhibiteur de la tyrosine kinase de Bruton (BTK) de nouvelle génération. La littérature fournie le montre utilisé dans des hémopathies lymphoïdes B (leucémie lymphoïde chronique, macroglobulinémie de Waldenström), mais l'indication originale n'est pas renseignée dans les données réglementaires.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **leucémie myéloïde**.
Aucune donnée ne le teste dans cette maladie : **2 essais cliniques** (sans données propres au zanubrutinib) et **9 publications** (presque toutes sur des maladies lymphoïdes ou sur la sécurité du médicament) sont associés, ce qui suggère un artefact de correspondance de termes.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Leucémie myéloïde |
| Score de Prédiction TxGNN | 99,65 % (rang 2982) |
| Niveau de Preuve | L4 (indirect, au niveau de la classe, selon l'Evidence Pack) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le zanubrutinib est un inhibiteur sélectif de BTK de nouvelle génération, dont l'efficacité a été étudiée dans les hémopathies lymphoïdes B. Mécanistiquement, il pourrait être applicable à la leucémie myéloïde, mais ce lien n'est pas démontré.

La seule justification biologique plausible relève de la classe : la signalisation BTK est présente dans certains blastes de leucémie aiguë myéloïde (LAM), et le CG-806 (luxeptinib), un inhibiteur non covalent de BTK/FLT3, a été testé dans la LAM. Aucune donnée clinique ou préclinique propre au zanubrutinib dans la LAM n'est fournie.

Le score TxGNN est très élevé, mais les 9 publications concernent presque toutes des maladies lymphoïdes (LLC/LPL) ou la sécurité du médicament. Le lien prédit reflète probablement un artefact de correspondance du terme « leucémie », et non une preuve d'efficacité.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1 | Arrêté | 45 | CG-806 (luxeptinib, inhibiteur BTK/FLT3 non covalent) dans la LAM en rechute/réfractaire ou les SMD à haut risque. Pertinence B : justification de classe, mais médicament différent, essai arrêté, sans donnée sur le zanubrutinib |
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Terminé | 86 | PRT2527 (inhibiteur de CDK9) seul ou associé au zanubrutinib ou au vénétoclax dans les hémopathies en rechute/réfractaires. Pertinence C : le zanubrutinib n'est qu'un partenaire d'association, pas un agent testé |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | ECR | J Clin Oncol | SEQUOIA (phase 3) : zanubrutinib vs bendamustine-rituximab dans la LLC/LPS non traitée, suivi médian de 5 ans |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohorte | Blood Adv | Zanubrutinib bien toléré et efficace chez les patients LLC/LPS intolérants à l'ibrutinib ou à l'acalabrutinib (phase 2) |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohorte | Blood Adv | Analyse de plusieurs études chez 301 patients LLC/LPS avec del(17p) et/ou mutation TP53 |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohorte | Lancet Haematol | Phase 2 à bras unique : zanubrutinib chez des patients avec hémopathies B intolérants à d'autres inhibiteurs de BTK |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Revue | Pharmaceutics | Revue des inhibiteurs de tyrosine kinase dans les leucémies chroniques (LMC et LLC) |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Revue | Leukemia | Prise en charge de la macroglobulinémie de Waldenström par les inhibiteurs de BTK |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Revue | Clin Lymphoma Myeloma Leuk | Réactivation du virus de l'hépatite B chez des patients sous inhibiteurs de BTK (ibrutinib, acalabrutinib, zanubrutinib) |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Revue | Anticancer Agents Med Chem | Méthodes de synthèse de médicaments anticancéreux approuvés par la FDA (2018-2021), sans donnée d'efficacité |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Rapport de cas | Front Immunol | Cas rare de coexistence d'une macroglobulinémie de Waldenström et d'une LAL-B |

Aucune de ces publications n'évalue le zanubrutinib dans la leucémie myéloïde.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 65919841 | BRUKINSA 80 mg, gélule (BEONE MEDICINES IRELAND) | Gélule |

Le texte de l'indication approuvée n'est pas renseigné dans les données.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de BTK) |

Veuillez consulter les mises en garde et précautions de la notice pour le risque de myélosuppression, l'émétogénicité, la surveillance biologique et la protection de manipulation.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

La littérature signale par ailleurs des cas de réactivation du virus de l'hépatite B chez des patients traités par inhibiteurs de BTK, zanubrutinib compris (PMID 37150651).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Malgré un score TxGNN très élevé (99,65 %), aucune preuve propre au zanubrutinib n'existe dans la leucémie myéloïde. Le lien prédit relève probablement d'un artefact de correspondance de termes avec les leucémies lymphoïdes.
- Les seules données pertinentes portent sur d'autres médicaments (CG-806) ou sur le zanubrutinib comme simple partenaire d'association.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de sécurité de la notice ANSM (mises en garde, contre-indications), actuellement bloquantes pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Indication originale approuvée en France (texte de l'AMM)
- Données précliniques du zanubrutinib dans la LAM (lignées cellulaires, modèles) pour établir un lien mécanistique
- Pour les prédictions de rang 2 à 6 (niveau L5, sans preuve), toute évaluation supplémentaire reste prématurée

*Ces résultats sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

