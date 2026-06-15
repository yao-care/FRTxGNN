---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Calcitriol : Des Troubles du Métabolisme Calcique au Rachitisme Hypophosphatémique Héréditaire

## Résumé en Une Phrase

Calcitriol est la forme biologiquement active de la vitamine D (1,25-dihydroxyvitamine D₃), classiquement prescrit pour les troubles du métabolisme calcique liés à l'insuffisance rénale chronique et à l'hypoparathyroïdie.
Le modèle TxGNN prédit 7 nouvelles indications potentielles ; la mieux étayée par des preuves est le **Rachitisme Hypophosphatémique Héréditaire** (score 99,28 %),
avec **7 essais cliniques** et **20 publications** documentant l'utilisation directe de calcitriol dans cette pathologie.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans ce dossier (usage classique : troubles du métabolisme Ca/P) |
| Nouvelle Indication Prédite | Rachitisme Hypophosphatémique Héréditaire (rang 7) |
| Score de Prédiction TxGNN | 99,28 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé (0 AMM répertoriée) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

> ⚠️ **Note sur la prédiction rang 1 :** Le modèle TxGNN attribue le rang 1 (score 99,96 %) au terme « *obsolete vitamin D deficiency* » — terme ontologique désormais obsolète correspondant à l'indication thérapeutique intrinsèque de calcitriol (code ICD-10 courant : E55). Cette prédiction ne constitue pas un repositionnement au sens strict. Aucune donnée d'essai clinique ni de littérature n'est disponible pour ce terme dans ce dossier. La présente évaluation porte sur l'indication la plus pertinente pour le repositionnement : le rachitisme hypophosphatémique héréditaire (rang 7).

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de calcitriol ne sont pas renseignées dans ce dossier. Sur la base des connaissances établies, calcitriol est le métabolite actif terminal de la vitamine D, synthétisé dans le rein à partir du 25(OH)D par l'enzyme 1α-hydroxylase, sous le contrôle de la PTH. En se liant au récepteur de la vitamine D (VDR), il régule l'absorption intestinale du calcium et du phosphore, la minéralisation osseuse et la sécrétion de PTH.

Le rachitisme hypophosphatémique héréditaire — principalement sous sa forme liée à l'X (XLH, mutation *PHEX*) — présente une surproduction de FGF23 qui inhibe simultanément la réabsorption rénale du phosphore et la synthèse rénale de calcitriol. Il en résulte une hypophosphatémie chronique associée à des concentrations de calcitriol paradoxalement basses ou inadéquatement normales, entraînant une minéralisation osseuse déficiente (rachitisme chez l'enfant, ostéomalacie chez l'adulte).

L'administration exogène de calcitriol permet de contourner le blocage enzymatique induit par FGF23 : il stimule directement l'absorption intestinale du calcium et du phosphore via VDR, améliore la minéralisation osseuse et réduit l'hyperparathyroïdie secondaire. L'association calcitriol + supplémentation en phosphate représente le traitement conventionnel standard de l'XLH depuis les années 1980, désormais proposé en alternative ou en complément au burosumab (anticorps anti-FGF23). La prédiction TxGNN est donc biologiquement solide et cliniquement bien ancrée.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Phase 1 précoce | En cours (non recrut.) | 20 | Calcitriol en monothérapie dans XLH (adultes et enfants) : évaluation de la phosphatémie, de la minéralisation osseuse et des calcifications rénales sans supplémentation phosphatée associée |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Inconnu | 100 | Comparaison haute vs faible dose de calcitriol + phosphate neutre chez l'enfant avec XLH ; objectif : établir une posologie poids-dépendante optimale |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | En cours (non recrut.) | 27 | Étude INZ-701 dans la déficience ENPP1 : calcitriol constitue le bras contrôle représentant le traitement standard ; fournit des données comparatives indirectes |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A (observ.) | Terminé | 260 | Sécrétion inappropriée de FGF23 dans l'hypophosphatémie : documentation mécanistique de l'inhibition de la synthèse de calcitriol — base physiopathologique directe |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A (observ.) | Pas encore recrut. | 65 | Mesure de la concentration d'ATP par spectroscopie ³¹P dans le « diabète phosphaté » (XLH et autres hypophosphatémies héréditaires) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Revue / Recommandations cliniques | *Calcified Tissue Int* | Synthèse actualisée du diagnostic et du traitement de XLH ; calcitriol + phosphate confirmé comme option thérapeutique standard |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Primer / Revue de référence | *The Lancet* | Physiopathologie complète de XLH : rôle central du calcitriol, comparaison burosumab vs traitement conventionnel |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Revue clinique | *J Bone Miner Res* | Rachitisme hypophosphatémique et retard de croissance : cas illustratif et revue des stratégies thérapeutiques incluant calcitriol |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Revue | *Horm Res Paediatr* | Métabolisme de la vitamine D, rachitisme et approches thérapeutiques modernes ; contexte historique et pharmacologique |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohorte observationnelle | *J Endocrinol Invest* | Croissance et proportions corporelles de la naissance à l'âge adulte dans les rachitismes hypophosphatémiques héréditaires |
| [31863781](https://pubmed.ncbi.nlm.nih.gov/31863781/) | 2020 | Revue | *Metabolism* | Gestion de XLH chez l'adulte : rôle du calcitriol, complications musculo-squelettiques, transition vers burosumab |
| [31392510](https://pubmed.ncbi.nlm.nih.gov/31392510/) | 2020 | Revue | *Pediatr Nephrol* | Déficit de minéralisation dans XLH (os, dents, plaques de croissance) et mécanismes d'action du calcitriol |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Étude clinique interventionnelle | *J Clin Invest* | Guérison de la maladie osseuse dans XLH par calcitriol haute dose + phosphore : première démonstration directe de l'efficacité de l'association |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | ECR | *New Engl J Med* | Réponse osseuse aux sels de phosphate ± calcitriol dans le rachitisme vitamino-résistant : essai comparatif fondateur, calcitriol augmente l'absorption intestinale du phosphore |
| [17117305](https://pubmed.ncbi.nlm.nih.gov/17117305/) | 2006 | Revue | *Arq Bras Endocrinol* | Rachitisme hypophosphatémique et ostéomalacie héréditaire : physiopathologie du calcitriol bas, traitement de référence |

---

## Informations de Marché en France

Calcitriol (DB00136) ne dispose d'aucune AMM répertoriée dans la base de données réglementaire interrogée. Le statut « non commercialisé » devra être confirmé directement auprès de l'ANSM, notamment pour identifier d'éventuelles autorisations temporaires d'utilisation (ATU/AAP) ou importations parallèles.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
L'association calcitriol + supplémentation phosphatée constitue le traitement conventionnel établi du rachitisme hypophosphatémique héréditaire depuis les années 1980, avec une base pharmacologique directement ancrée dans la physiopathologie FGF23/VDR. Des essais Phase 4 (NCT03820518, N=100) et une étude de monothérapie directe (NCT03748966) confirment l'utilisation active et l'intérêt d'optimisation posologique en clinique contemporaine.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation du statut AMM France auprès de l'ANSM (aucune AMM identifiée dans la base interrogée)
- Données détaillées sur le mécanisme d'action (MOA) depuis DrugBank — priorité haute (DG002)
- Données de sécurité complètes (mises en garde, contre-indications, interactions) depuis la notice officielle — bloquant pour l'évaluation S1 (DG001)
- Résultats complets des essais NCT03820518 (Phase 4, statut inconnu) et NCT03748966 (Phase 1 précoce, toujours en cours)
- Clarification de l'ontologie rang 1 (« *obsolete vitamin D deficiency* ») vers le code ICD-10 en vigueur (E55) pour une indexation correcte dans la base de prédiction
- Plan de surveillance de sécurité pour les populations à risque spécifiques : pédiatrie (calcifications rénales dose-dépendantes), insuffisance rénale chronique, hyperparathyroïdie secondaire
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

