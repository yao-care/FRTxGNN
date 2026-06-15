---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 1
---

# Glucagon
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

# Glucagon : Du Traitement de l'Hypoglycémie au Syndrome de l'Intestin Irritable

## Résumé en Une Phrase

Le Glucagon est une hormone peptidique endogène, historiquement utilisée en urgence pour le traitement de l'hypoglycémie sévère et comme antispasmodique intestinal en endoscopie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Syndrome de l'Intestin Irritable (SII)**,
avec **11 essais cliniques** et **20 publications** identifiés — toutefois, la quasi-totalité des preuves porte sur la voie GLP-1 (et non sur le glucagon lui-même), ce qui soulève une importante question de spécificité mécanistique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Traitement de l'hypoglycémie sévère ; antispasmodique intestinal (usage endoscopique) |
| Nouvelle Indication Prédite | Syndrome de l'Intestin Irritable (IBS) |
| Score de Prédiction TxGNN | 99,24 % |
| Niveau de Preuve | L3 — études observationnelles et revues systématiques (voie GLP-1) |
| Statut de Marché en France | ✗ Non commercialisé (0 AMM identifiée) |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le Glucagon (DB00040) et le GLP-1 (glucagon-like peptide-1) partagent une origine génomique commune : tous deux sont des produits du gène *proglucagon*, découpé différemment selon les tissus (pancréas pour le glucagon, intestin L pour le GLP-1). Cette parenté moléculaire est probablement à l'origine du score TxGNN élevé — le modèle a pu associer des caractéristiques de réseau liées aux deux entités, sans distinguer leurs récepteurs respectifs (GCGR pour le glucagon, GLP-1R pour le GLP-1).

Sur le plan mécanistique, le glucagon agit via le GCGR et possède un effet relaxant bien documenté sur le muscle lisse gastro-intestinal, utilisé cliniquement pour réduire les spasmes lors des endoscopies. Ce mécanisme antispasmodique est conceptuellement pertinent dans le SII, où l'hypercontractilité et la douleur viscérale sont centrales. En revanche, le GLP-1 — lui aussi impliqué dans la motilité intestinale — ralentit la vidange gastrique, module la sensibilité viscérale et réduit la douleur abdominale via le GLP-1R.

**La limite critique** est que l'ensemble des preuves cliniques disponibles (ROSE-010, exendin-4, liraglutide) concerne exclusivement la voie GLP-1R, et non le récepteur glucagon (GCGR). Il n'existe actuellement aucun essai clinique évaluant directement le glucagon (DB00040) comme traitement du SII. La prédiction TxGNN est donc mécanistiquement plausible par analogie, mais n'est pas directement supportée par des données cliniques propres à cette molécule.

---

## Preuves d'Essais Cliniques

> ⚠️ **Note d'interprétation :** Aucun essai clinique identifié n'évalue directement le glucagon (GCGR) dans le SII. Les essais ci-dessous portent sur des agonistes GLP-1R (voie parente) ou ont une pertinence indirecte de grade B/C.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Terminé | 52 | ROSE-010 (agoniste GLP-1R) retarde la vidange gastrique et améliore l'accommodation gastrique chez les femmes avec SII à prédominance constipation (IBS-C) |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Terminé | 12 | Comparaison GLP-1 natif vs analogue ROSE-010 sur la motilité intestinale postprandiale in vivo ; mise en évidence du rôle inhibiteur de la voie GLP-1R sur le péristaltisme |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminé (arrêté prématurément) | 8 | Liraglutide (GLP-1RA) chez patients avec anastomose iléo-anale (IPAA) et haute fréquence intestinale ; étude croisée randomisée contre placebo — arrêtée pour effectif insuffisant |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | NA | Terminé | 66 | Entraînement continu modéré vs intervalles intenses sur le microbiote intestinal et le GLP-1 chez patients pré-diabétiques obèses avec SII — valeur documentaire de fond |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | NA | Terminé | 37 | Mode d'action du butyrate dans le côlon humain ; lié au SII via la dysbiose — non pertinent pour glucagon |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | NA | Terminé | 12 | Hypoglycémie réactive idiopathique et FOS ; glucagon utilisé comme marqueur physiologique de mesure, non comme médicament |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Revue systématique & méta-analyse | Frontiers in Endocrinology | Les GLP-1RA améliorent les symptômes du SII ; GLP-1 et son analogue ROSE-010 inhibent le complexe moteur migrant et réduisent la motilité GI |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | ECR / Étude clinique | Scand J Gastroenterology | ROSE-010 réduit significativement la douleur lors des crises de SII ; analyse croisée pour identifier la sous-population la plus sensible au traitement |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | ECR randomisé en double aveugle | Am J Physiol Gastrointest Liver Physiol | ROSE-010 (30–300 µg sc) retarde la vidange gastrique et réduit la motilité colique chez les femmes IBS-C — étude de pharmacodynamique complète |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Revue | Experimental Physiology | Les cellules L intestinales sécrètent le GLP-1 en réponse aux nutriments et facteurs microbiens ; rôle pathophysiologique central du GLP-1 dans le SII, incluant la douleur viscérale et la perméabilité intestinale |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Étude clinique | Clinics Res Hepatol Gastroenterol | Taux de GLP-1 circulant abaissés corrèlent avec la douleur abdominale chez les patients IBS-C ; expression du récepteur GLP-1 réduite dans le côlon |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Préclinique (modèle animal) | Neurogastroenterol Motility | Exendin-4 (GLP-1RA) améliore la dysfonction gastro-intestinale dans le modèle rat Wistar Kyoto de SII ; activation des neurones myentériques comme mécanisme sous-jacent |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Étude en vie réelle | Annals of Gastroenterology | Patterns de prescription et d'arrêt des GLP-1RA chez les patients SII ; les effets GI indésirables expliquent une fréquence d'arrêt élevée dans cette population |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Revue systématique | J Headache Pain | GLP-1 inhibe la sécrétion de glucagon et ralentit la vidange gastrique ; potentiel thérapeutique élargi via les voies neuronales de la douleur |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Préclinique | Int J Mol Medicine | Rôle du GLP-1 dans la pathogenèse des modèles expérimentaux de SII-C et SII-D chez le rat ; expression du récepteur GLP-1 modifiée selon le sous-type |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Préclinique / Formulation | Adv Exp Med Biol | GLP-1 aérosolisé pour le diabète et le SII — suggère que l'administration pulmonaire du GLP-1 pourrait contourner la dégradation par la DPP-4 |

---

## Informations de Marché en France

> **Glucagon (DB00040) ne dispose d'aucune AMM enregistrée en France dans la base de données consultée.** Le médicament est connu en Europe sous des spécialités comme GlucaGen® (Novo Nordisk) pour le traitement de l'hypoglycémie sévère, mais aucune autorisation n'a été identifiée dans le périmètre de cette recherche réglementaire.

---

## Considérations de Sécurité

Les données détaillées de sécurité (mises en garde, contre-indications, interactions médicamenteuses) n'ont pas été disponibles dans ce paquet de preuves.

> Veuillez consulter la notice officielle GlucaGen® (EMA/ANSM) pour les informations de sécurité complètes, notamment les contre-indications chez les patients phéochromocytome et les interactions avec les anticoagulants de type warfarine.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN de 99,24 % est probablement attribuable à une confusion d'entités dans le graphe de connaissances entre le glucagon (GCGR) et le GLP-1/GLP-1R, deux dérivés du même gène proglucagon mais agissant via des récepteurs distincts. L'intégralité des preuves cliniques disponibles (ROSE-010, exendin-4, liraglutide) concerne la voie GLP-1R et ne constitue qu'un soutien indirect pour le glucagon lui-même — il n'existe aucun essai clinique évaluant directement DB00040 comme traitement du SII.

**Pour avancer, les éléments suivants sont nécessaires :**

- **Clarification mécanistique prioritaire** : Confirmer si la cible thérapeutique visée est le GCGR (glucagon natif) ou le GLP-1R (analogue) — ces deux voies nécessitent des molécules différentes et des stratégies de développement distinctes
- **Revue bibliographique ciblée GCGR × SII** : Rechercher des données précliniques spécifiques à l'antagonisme ou à l'agonisme GCGR dans des modèles de douleur viscérale ou de motilité colique
- **Fiche de sécurité complète** : Télécharger et analyser la notice GlucaGen® (EMA) pour compléter les données DG001 (mises en garde/contre-indications)
- **Données MOA DrugBank** : Interroger l'API DrugBank pour compléter DG002 et confirmer les cibles moléculaires primaires et secondaires du glucagon
- **Évaluation réglementaire** : Vérifier le statut AMM en France/Europe pour le glucagon natif (GlucaGen®, Baqsimi®) et si une extension d'indication SII est réglementairement envisageable
- **Si confirmation GLP-1R** : Réorienter le candidat vers un agoniste GLP-1R approuvé (semaglutide, liraglutide) dont les données IBS sont plus solides et l'approbation européenne déjà obtenue pour d'autres indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

