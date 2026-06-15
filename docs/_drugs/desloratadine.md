---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 6
---

# Desloratadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Desloratadine : De la Rhinite Allergique à l'Urticaire au Froid

## Résumé en Une Phrase

Desloratadine est un antihistaminique de deuxième génération, antagoniste sélectif des récepteurs H1, largement utilisé dans le traitement de la rhinite allergique et de l'urticaire chronique, bien qu'aucun enregistrement réglementaire n'ait été retrouvé dans la base de données consultée.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**urticaire au froid (cold urticaria)**,
avec **3 essais cliniques** et **7 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non enregistré dans la base de données réglementaire (antihistaminique H1, rhinite allergique, urticaire chronique) |
| Nouvelle Indication Prédite | Urticaire au froid (Cold Urticaria) |
| Score de Prédiction TxGNN | 99.94% |
| Niveau de Preuve | L1 |
| Statut de Marché | ✗ Non commercialisé (base de données réglementaire consultée) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

L'urticaire au froid (cold urticaria) est une forme d'urticaire physique dans laquelle l'exposition au froid déclenche la dégranulation des mastocytes cutanés, libérant massivement de l'histamine. Cette histamine est directement responsable de l'augmentation de la perméabilité vasculaire, de la vasodilatation locale et de la formation des plaques urticariennes caractéristiques. Le mécanisme est donc univoque : urticaire induite par l'histamine → antagoniste H1 → inhibition des symptômes.

Les données détaillées sur le mécanisme d'action (MOA) ne sont pas disponibles dans l'Evidence Pack. Sur la base des informations connues, desloratadine est un antagoniste sélectif et hautement affin des récepteurs H1 de l'histamine (deuxième génération, non sédatif), actif métabolite de la loratadine. Son efficacité dans les pathologies à composante histaminique — rhinite allergique, urticaire chronique spontanée — est documentée, et ce mécanisme est mécanistiquement et directement applicable à l'urticaire au froid.

Les données d'essais cliniques disponibles sont particulièrement probantes : non seulement des études randomisées en double aveugle confirment l'efficacité de desloratadine à dose standard (5 mg), mais des données de « updosing » (10–20 mg) démontrent une relation dose-réponse avec élévation du seuil de déclenchement au froid, renforçant la plausibilité mécanistique. Cette indication est cohérente avec les recommandations actuelles de l'EAACI/GA²LEN/EDF sur l'urticaire physique.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Terminé | 30 | Étude multicentrique double aveugle à doses escaladantes (5, 10, 20 mg) de desloratadine chez des patients atteints d'urticaire au froid acquise (ACU) ; objectif : déterminer la dose inhibitrice suffisante |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Terminé | 33 | ECR randomisé double aveugle placebo-contrôlé croisé comparant 5 mg vs 20 mg de desloratadine sur les lésions d'urticaire au froid induites expérimentalement (thermographie, volumétrie, photographie) ; hypothèse : l'updosing à 20 mg est supérieur à la dose standard |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Terminé | 150 | Comparaison de 5 antihistaminiques (dont desloratadine) sur profils pharmacocinétiques et pharmacodynamiques dans une population d'Amérique latine tropicale ; soutien indirect à l'efficacité de desloratadine dans l'urticaire |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | ECR | British Journal of Dermatology | ECR sur l'escalade de doses d'antihistaminiques H1 dans l'urticaire au froid ; mesure du seuil de température critique ; démontre la variabilité de réponse et l'intérêt de l'ajustement posologique |
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | Étude clinique (ECR croisé) | J Allergy Clin Immunol | Desloratadine haute dose réduit le volume des plaques et améliore les seuils de provocation au froid vs dose standard ; ECR randomisé placebo-contrôlé croisé (Siebenhaar et al.) — étude pivot pour le concept d'updosing |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Étude clinique (preuve directe) | J Dermatological Treatment | Desloratadine 5 mg pendant 4 jours inhibe l'urticaire au froid induite par glaçons chez 12 patients ; étude ouverte pionnière confirmant l'efficacité directe |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revue | Drugs | Revue sur l'étiologie et la prise en charge de l'urticaire chronique ; place les antihistaminiques H1 (dont desloratadine) en première ligne ; contexte mécanistique et thérapeutique |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Revue comparative | Allergy | Revue comparative des antihistaminiques de 2ème génération (focus ébastine) dans rhinite allergique et urticaire chronique idiopathique ; contextualise la classe thérapeutique à laquelle appartient desloratadine |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Rapport de cas | Qatar Medical Journal | Premier cas rapporté d'urticaire au froid induite après anaphylaxie à morsure de fourmi noire ; illustre la diversité des déclencheurs de l'urticaire au froid acquise |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Série de cas | J Allergy Clin Immunol Pract | Description d'un nouveau variant : urticaire au froid food-dependent ; contextualise la complexité clinique de l'urticaire au froid et la nécessité d'une prise en charge antihistaminique adaptée |

---

## Informations de Marché

Aucun enregistrement réglementaire n'a été retrouvé pour Desloratadine dans la base de données consultée (0 AMM). Aucun tableau de licences applicable.

> **Note** : Cette absence d'enregistrement est propre à la base de données réglementaire interrogée lors de la constitution de cet Evidence Pack (résultat de recherche TFDA : 0 résultat). Desloratadine est par ailleurs commercialisé sous des noms de marque (ex. Aerius®) dans de nombreuses juridictions pour la rhinite allergique et l'urticaire chronique.

---

## Considérations de Sécurité

Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans cet Evidence Pack.

> Veuillez consulter la notice officielle du médicament pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
La prédiction TxGNN pour cold urticaria atteint 99.94 % et repose sur un rationnel mécanistique direct et solide : desloratadine est un antagoniste H1 hautement affin, et l'urticaire au froid est une pathologie à médiation histaminique clairement établie. Trois essais cliniques de Phase 4 complétés — dont deux ECR randomisés double aveugle placebo-contrôlés — et sept publications incluant un ECR et deux études cliniques directes constituent un niveau de preuve L1. La relation dose-réponse documentée (updosing 10–20 mg) renforce la crédibilité clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données complètes sur le mécanisme d'action (MOA) via DrugBank API (DG002 — sévérité High)
- Obtenir les mises en garde et contre-indications de la notice officielle (DG001 — sévérité Blocking) avant toute évaluation de sécurité formelle (S1)
- Vérifier le statut réglementaire réel dans la juridiction cible (l'absence d'enregistrement dans la base TFDA ne reflète pas nécessairement le statut dans d'autres pays)
- Définir un plan de surveillance posologique pour les protocoles de dose escaladante (10–20 mg), en particulier dans les populations pédiatriques et insuffisants rénaux/hépatiques
- Confirmer la compatibilité des voies d'administration disponibles pour une éventuelle extension d'indication (voie orale standard vs formulations nasales en développement — cf. NCT04088721)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

