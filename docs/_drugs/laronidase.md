---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 2
---

# Laronidase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Laronidase : De la Mucopolysaccharidose de Type I à la Maladie de Surcharge Lysosomale avec Atteinte Squelettique

## Résumé en Une Phrase

Laronidase (DrugBank DB00090) est une α-L-iduronidase humaine recombinante, enzymothérapie substitutive initialement développée pour la mucopolysaccharidose de type I (MPS I — syndromes de Hurler, Hurler-Scheie et Scheie). Le modèle TxGNN prédit une efficacité pour la **maladie de surcharge lysosomale avec atteinte squelettique**, avec un score de **99.31%**, mais **aucun essai clinique** dédié n'est enregistré et les **4 publications** associées documentent en réalité l'usage déjà connu de laronidase dans la MPS I plutôt qu'une indication véritablement nouvelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mucopolysaccharidose de type I (MPS I — Hurler / Hurler-Scheie / Scheie) *(déduite de la littérature associée ; aucun texte d'indication d'AMM structuré disponible)* |
| Nouvelle Indication Prédite | Lysosomal storage disease with skeletal involvement |
| Score de Prédiction TxGNN | 99.31% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non commercialisé (0 AMM enregistrée dans ce jeu de données) |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues issues de la littérature, laronidase fait partie de la classe des enzymothérapies substitutives (recombinant human α-L-iduronidase) : elle est captée par les cellules déficientes via les récepteurs mannose-6-phosphate, transportée vers les lysosomes, et y clive les glycosaminoglycanes (dermatan sulfate, heparan sulfate) accumulés. Son efficacité dans la mucopolysaccharidose de type I est établie de longue date (mise sur le marché sous le nom Aldurazyme).

La « maladie de surcharge lysosomale avec atteinte squelettique » prédite par TxGNN n'est pas, à l'examen, une pathologie distincte : l'atteinte squelettique (dysostosis multiplex) est une manifestation clinique caractéristique de la MPS I elle-même, l'indication déjà connue de laronidase. Il ne s'agit donc vraisemblablement pas d'un véritable signal de repositionnement, mais d'une reformulation phénotypique de l'indication existante — le modèle a probablement capturé la relation MPS I ↔ atteinte squelettique déjà présente dans les données d'entraînement plutôt qu'une extension thérapeutique réelle.

Par ailleurs, le statut « non commercialisé » et les 0 AMM enregistrées pour la France dans ce jeu de données sont à interpréter avec prudence : ils reflètent probablement une lacune de la source de données utilisée plutôt que l'absence réelle du médicament sur le marché, puisque la littérature associée traite explicitement d'un produit déjà en usage clinique documenté (essais multicentriques, suivis de patients sur plusieurs années).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour l'indication « lysosomal storage disease with skeletal involvement ».

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Revue | BioDrugs | Présentation du développement de laronidase (α-L-iduronidase recombinante) pour la MPS I ; désignations orphelines US/UE et statut fast-track FDA |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Revue | Pediatr Endocrinol Rev | Revue de la MPS I (déficit en α-L-iduronidase), spectre clinique Hurler/Scheie/Hurler-Scheie, diagnostic par GAG urinaires |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | Étude mécanistique (in vitro) | Biol Pharm Bull | Captation dose-dépendante de laronidase par fibroblastes/ostéoblastes MPS I via récepteurs mannose-6-phosphate, transport lysosomal et clivage des substrats accumulés |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Rapport de cas | Pediatr Neurol | Suivi de 6,5 ans d'un patient atteint du syndrome de Scheie sous enzymothérapie substitutive débutée à 2,5 ans ; déclin de l'état général après amélioration initiale, progression de la maladie malgré le traitement |

---

## Considérations de Securite

Veuillez consulter la notice pour les informations de sécurité. *(Lacune bloquante identifiée : les mises en garde, contre-indications et interactions médicamenteuses de la notice TFDA/française ne sont actuellement pas disponibles dans ce dossier — DG001.)*

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- L'indication prédite chevauche largement l'usage déjà établi de laronidase dans la MPS I (l'atteinte squelettique est une manifestation classique de cette maladie), ce qui remet en question l'existence d'un véritable signal de repositionnement plutôt qu'une reformulation de l'indication connue.
- Aucun essai clinique dédié n'est enregistré, et une lacune bloquante empêche toute évaluation de sécurité initiale (S1) : la notice TFDA (mises en garde, contre-indications) est absente.
- Un second candidat prédit par TxGNN pour ce médicament (syndrome de Sanfilippo/MPS III, score 99.22%) a été examiné et doit être écarté : les 8 publications associées portent en réalité toutes sur la MPS I et non sur le syndrome de Sanfilippo, très probablement un faux positif lié à la cooccurrence du terme « mucopolysaccharidose » — l'α-L-iduronidase n'a aucune spécificité de substrat pertinente pour la MPS III (déficit en SGSH/NAGLU/HGSNAT/GNS) et ne franchit pas la barrière hémato-encéphalique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice TFDA/française (mises en garde, contre-indications, DDI) — lacune bloquante actuelle (DG001)
- Clarifier le statut réel de commercialisation en France (vérifier si l'absence d'AMM dans ce jeu de données reflète la réalité du marché ou une lacune de la base source)
- Confirmer si « maladie de surcharge lysosomale avec atteinte squelettique » désigne un sous-groupe clinique réellement distinct de l'indication MPS I déjà approuvée, ou une simple reformulation du phénotype existant
- Ne pas poursuivre la piste du syndrome de Sanfilippo (MPS III) sur la base des données actuelles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

