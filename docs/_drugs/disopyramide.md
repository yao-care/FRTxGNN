---
layout: default
title: Disopyramide
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Disopyramide
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

# Disopyramide : De l'Arythmie Ventriculaire au Syndrome de Gilles de la Tourette

## Résumé en Une Phrase

Disopyramide est un antiarythmique de Classe Ia, utilisé pour le traitement des arythmies ventriculaires et supraventriculaires, avec des propriétés anticholinergiques marquées.
Le modèle TxGNN prédit, parmi **10 indications candidates**, que le **Syndrome de Gilles de la Tourette** présente le score de prédiction le plus élevé (99,86%) ; cependant, le lien mécanistique est contestable et la pertinence clinique reste à démontrer.
L'ensemble des 10 indications prédites ne dispose d'aucun essai clinique enregistré ; une seule publication est disponible — pour la **Tachycardie Auriculaire Multifocale** (rang 9) — et les indications **cardiovasculaires** (rangs 7 et 9) présentent la meilleure cohérence avec le profil antiarythmique connu du médicament.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Arythmies ventriculaires et supraventriculaires (médicament non commercialisé en France) |
| Nouvelle Indication Prédite | Syndrome de Gilles de la Tourette |
| Score de Prédiction TxGNN | 99,86% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Vue d'Ensemble : 10 Indications Prédites

Ce rapport couvre les 10 premières indications prédites par TxGNN pour la Disopyramide. Les deux indications cardiovasculaires (rangs 7 et 9) présentent la meilleure cohérence mécanistique avec le profil pharmacologique connu du médicament.

| Rang | Indication | Score TxGNN | Niveau de Preuve | Recommandation | Cohérence Mécanistique |
|---|---|---|---|---|---|
| 1 | Syndrome de Gilles de la Tourette | 99,86% | L5 | Hold | Faible — anticholinergique potentiellement contre-productif |
| 2 | TDAH (type global) | 99,82% | L5 | Hold | Faible — sans lien avec les voies NE/DA |
| 3 | Trichotillomanie | 99,81% | L5 | Hold | Très faible — mécanisme cardiaque sans pertinence |
| 4 | TDAH type inattentif | 99,74% | L5 | Hold | Faible — même profil que rang 2 |
| 5 | Syndrome Facio-Digito-Génital | 99,66% | En attente | En attente | Inconnue |
| 6 | Trouble du développement spécifique | 99,54% | L5 | Hold | Très faible — aucun lien neurodéveloppemental identifié |
| **7** | **Flutter auriculaire néonatal idiopathique** | **99,42%** | **L4** | **Research Question** | **Forte — mécanisme Classe Ia directement applicable** |
| 8 | Fibrome chondromyxoïde | 99,41% | L5 | Hold | Très faible — tumeur osseuse bénigne, traitement chirurgical |
| **9** | **Tachycardie auriculaire multifocale** | **99,21%** | **L4** | **Research Question** | **Modérée — suppression théorique des foyers ectopiques auriculaires** |
| 10 | Néoplasme du nerf trijumeau | 99,16% | L5 | Hold | Très faible — connexion non spécifique dans le graphe |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la source de données locale. Sur la base des informations déductibles des rationales de prédiction intégrées dans ce dossier, Disopyramide est un antiarythmique de **Classe Ia** : il bloque les canaux sodiques rapides, prolonge la période réfractaire du potentiel d'action auriculaire et ventriculaire, ralentit la conduction sino-auriculaire et possède des propriétés **anticholinergiques (antimuscariiniques)** significatives. Son efficacité dans les arythmies cardiaques est documentée, bien qu'aucune AMM française ne figure dans ce jeu de données.

Concernant l'indication de rang 1 — **Syndrome de Gilles de la Tourette** — la pertinence mécanistique est **contestable**. L'effet anticholinergique de la Disopyramide pourrait théoriquement moduler l'équilibre cholinergique-dopaminergique dans les ganglions de la base. Cependant, les médicaments anticholinergiques sont documentés cliniquement comme pouvant **aggraver les tics** chez les patients atteints du syndrome de Tourette, la maladie étant associée à une hyperactivité dopaminergique striatale. Le score TxGNN élevé (99,86%) reflète probablement une **similarité topologique** dans le graphe de connaissances — clustering de nœuds de maladies neuropsychiatriques (Tourette, TDAH, trichotillomanie aux rangs 1–4) — plutôt qu'un lien pharmacologique direct. Ce phénomène de clustering explique pourquoi quatre des dix premières prédictions appartiennent à ce même sous-groupe nosologique.

Les indications mécanistiquement les plus pertinentes sont les **indications cardiovasculaires** (rangs 7 et 9). Le mécanisme Classe Ia — ralentissement de la conduction auriculaire, prolongation de la période réfractaire, blocage des circuits de réentrée — correspond directement à la physiopathologie du flutter auriculaire et des tachycardies auriculaires ectopiques multifocales. Des cas cliniques et petites séries ont été rapportés dans la littérature externe pour l'utilisation de la Disopyramide dans les arythmies néonatales réfractaires, bien que ces données ne soient pas capturées dans le présent jeu de données. La principale préoccupation pour une utilisation néonatale reste la pharmacocinétique immature (liaison protéique réduite, élimination rénale incomplète) et la fenêtre thérapeutique étroite.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour l'ensemble des 10 indications prédites.

---

## Preuves de la Littérature

**Indication principale — Syndrome de Gilles de la Tourette :** Aucune littérature associée disponible actuellement.

**Tachycardie Auriculaire Multifocale (Rang 9) — 1 publication identifiée :**

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [7418495](https://pubmed.ncbi.nlm.nih.gov/7418495/) | 1980 | Série de cas / Rapport clinique précoce | Chest | Patient de 68 ans avec arythmies complexes résistantes (ESV multifocaux, bigéminisme, TV, flutter et fibrillation auriculaire) : la disopyramide — ainsi que quinidine, procaïnamide, propranolol et digoxine — s'est révélée **inefficace** ; la lorcaïnide (antiarythmique alors évalué) a contrôlé les arythmies. **⚠ Ce rapport constitue une preuve négative pour la disopyramide dans ce contexte.** |

**Toutes les autres indications :** Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Disopyramide ne dispose d'aucune autorisation de mise sur le marché (AMM) active en France. Le médicament n'est pas commercialisé sur le territoire français.

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité (mises en garde, contre-indications, interactions médicamenteuses).

> **Note :** Les données de sécurité (mises en garde, contre-indications) n'ont pas pu être récupérées lors de cette évaluation (lacune DG001 — bloquante). La récupération de la notice ANSM constitue un prérequis avant toute évaluation clinique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'ensemble des 10 indications prédites repose uniquement sur le modèle TxGNN (niveau de preuve L5 dominant), sans aucun essai clinique enregistré. Les prédictions les mieux classées — Tourette, TDAH, trichotillomanie — présentent une cohérence mécanistique faible à contre-productive, et le regroupement de ces indications neuropsychiatriques dans le top 6 s'explique par des artefacts de topologie du graphe de connaissances plutôt que par une pharmacologie partagée. La seule publication disponible (rang 9 — MAT) constitue une preuve **négative**. Les deux indications cardiovasculaires (rangs 7 et 9) justifient une investigation ciblée, mais restent insuffisamment documentées pour progresser sans lever les lacunes de données critiques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications officielles via la notice ANSM (lacune DG001 — **bloquante**)
- Compléter les données MOA complètes via DrugBank API (lacune DG002 — priorité haute)
- Conduire une recherche bibliographique ciblée sur les indications à fort potentiel mécanistique : **flutter auriculaire néonatal idiopathique** (rang 7) et **tachycardie auriculaire multifocale** (rang 9)
- Consulter un cardiologue pédiatrique pour évaluation de la faisabilité d'un usage néonatal
- Réévaluer les rangs 7 et 9 comme cibles prioritaires de repositionnement une fois les lacunes de données comblées, indépendamment des prédictions neuropsychiatriques de rang élevé
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

