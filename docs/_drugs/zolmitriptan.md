---
layout: default
title: Zolmitriptan
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 3
---

# Zolmitriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Zolmitriptan : De la Migraine Aiguë à la Migraine avec Aura du Tronc Cérébral

## Résumé en Une Phrase

Zolmitriptan est un triptan (agoniste sélectif des récepteurs 5-HT1B/1D), utilisé depuis les années 1990 pour le traitement aigu de la migraine. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Migraine avec Aura du Tronc Cérébral**, mais cette prédiction s'accompagne d'une réserve mécanistique importante : aucun essai clinique dédié n'existe, et **19 publications** en lien avec le sujet sont disponibles, dont certaines soulignent que ce sous-type de migraine est traditionnellement considéré comme une zone de prudence pour les triptans.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Migraine (traitement aigu) — d'après la littérature ; non commercialisé en France, aucune AMM enregistrée |
| Nouvelle Indication Prédite | Migraine avec Aura du Tronc Cérébral (*migraine with brainstem aura*, anciennement migraine basilaire) |
| Score de Prédiction TxGNN | 99.99% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données officielles de mécanisme d'action (DrugBank/TFDA) n'ont pas encore été récupérées pour ce dossier (écart de données en cours de résolution — priorité haute). Sur la base des connaissances pharmacologiques de classe disponibles dans les preuves collectées, le zolmitriptan est un agoniste sélectif des récepteurs sérotoninergiques 5-HT1B/1D, agissant à la fois au niveau central et périphérique pour inhiber l'activation trigémino-vasculaire et provoquer une vasoconstriction intracrânienne — c'est le mécanisme classique des triptans dans le traitement aigu de la migraine.

La migraine avec aura du tronc cérébral est une sous-catégorie de migraine avec aura, partageant la même physiopathologie trigémino-vasculaire de base que la migraine classique pour laquelle le zolmitriptan est efficace. C'est cette proximité mécanistique qui explique le score élevé attribué par TxGNN.

**Réserve importante** : contrairement à une extension mécanistique simple, ce sous-type a historiquement été considéré comme une contre-indication relative aux triptans. La vasoconstriction recherchée au niveau intracrânien fait craindre, en théorie, un risque vasculaire au niveau de la circulation postérieure (tronc cérébral), raison pour laquelle la plupart des recommandations et notices classent la migraine basilaire/du tronc cérébral comme une population à utiliser avec prudence plutôt qu'une indication d'extension directe. Cette prédiction doit donc être interprétée comme une piste à évaluer avec un encadrement clinique strict, et non comme une extension d'indication sans réserve.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Série de cas | Headache | Rapporte l'usage des triptans chez des patients migraineux avec symptômes neurologiques marqués (migraine basilaire / aura prolongée) |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Méta-analyse | J Headache Pain | Compare l'efficacité du frovatriptan au rizatriptan, zolmitriptan et almotriptan dans la migraine avec aura |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | ECR (sous-analyse) | Neurol Sci | Sous-groupe de 18 patients avec aura dans un essai croisé multicentrique comparant frovatriptan et zolmitriptan |
| [15581383](https://pubmed.ncbi.nlm.nih.gov/15581383/) | 2004 | ECR | CNS Drugs | Zolmitriptan 5 mg ODT : délai de réponse et durée d'efficacité dans le traitement aigu de la migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Revue/Recommandation | Headache | Évaluation par l'American Headache Society des preuves d'efficacité des traitements pharmacologiques aigus de la migraine |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Revue | Expert Opin Pharmacother | Synthèse des essais randomisés contrôlés démontrant l'efficacité du zolmitriptan (réponse à 2h, taux sans douleur) |
| [10473025](https://pubmed.ncbi.nlm.nih.gov/10473025/) | 1999 | Revue | Drugs | Revue d'ensemble de l'efficacité et de la tolérance du zolmitriptan oral 2,5-5 mg dans la migraine |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | Étude préclinique | Cephalalgia | Pharmacologie préclinique : action centrale et périphérique sur l'activation trigémino-vasculaire |
| [12864759](https://pubmed.ncbi.nlm.nih.gov/12864759/) | 2003 | Cohorte/Mécanistique | Headache | Doppler transcrânien avant/après zolmitriptan ou sumatriptan : effets sur la vélocité du flux sanguin intracrânien |
| [18624801](https://pubmed.ncbi.nlm.nih.gov/18624801/) | 2008 | ECR | Cephalalgia | Comparaison de six triptans sur la réduction de la douleur et l'allodynie précoce chez des migraineux |

---

## Considérations de Sécurité

⚠️ **Point de vigilance issu de l'analyse mécanistique** : la migraine avec aura du tronc cérébral (anciennement migraine basilaire) est traditionnellement classée comme population à prudence particulière pour les triptans, en raison d'un risque théorique de vasoconstriction au niveau de la circulation cérébrale postérieure. Ce point doit être vérifié dans le futur RCP/notice TFDA avant toute utilisation clinique.

Les mises en garde, contre-indications et interactions médicamenteuses détaillées (RCP TFDA, DDI) n'ont pas encore été récupérées pour ce dossier — écart de donnée bloquant identifié (DG001), en attente d'extraction depuis le site TFDA. Veuillez consulter la notice officielle pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le mécanisme pharmacologique du zolmitriptan est bien établi dans la migraine en général (multiples ECR/revues), et une littérature spécifique existe sur les triptans dans la migraine basilaire/avec aura prolongée. Toutefois, l'absence totale d'essai clinique dédié à cette indication précise, combinée à la réserve mécanistique classique (contre-indication relative historique), impose un encadrement strict plutôt qu'une validation directe.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération du RCP/notice TFDA (mises en garde, contre-indications formelles) — écart bloquant DG001
- Données de mécanisme d'action officielles (DrugBank) — écart DG002
- Confirmation ou infirmation formelle du statut de contre-indication relative pour la migraine avec aura du tronc cérébral dans les référentiels actuels
- Données d'interactions médicamenteuses (actuellement non trouvées)
- Le cas échéant, conception d'une étude prospective ciblée avant toute utilisation hors AMM dans cette sous-population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

