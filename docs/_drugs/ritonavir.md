---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir : De l'Infection par le VIH à l'Infection par le Virus de l'Immunodéficience Simienne (VIS)

## Résumé en Une Phrase

Le ritonavir est un inhibiteur de protéase utilisé dans le traitement de l'infection par le VIH-1, le plus souvent en association pour potentialiser d'autres antirétroviraux. Le modèle TxGNN prédit une efficacité potentielle contre l'**infection par le virus de l'immunodéficience simienne (VIS)**, mais cette direction n'est soutenue par **aucun essai clinique** et seulement **12 publications**, très majoritairement précliniques — dont l'analyse montre qu'il s'agit en réalité de données validant l'activité déjà connue du ritonavir contre le VIH dans des modèles animaux, plutôt que d'une véritable nouvelle indication thérapeutique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH-1 (déduite des descriptions de mécanisme d'action figurant dans les données ; aucune fiche d'AMM française disponible) |
| Nouvelle Indication Prédite | Infection par le virus de l'immunodéficience simienne (VIS) |
| Score de Prédiction TxGNN | 99.92% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier (écart de données identifié : mécanisme d'action manquant, sévérité élevée). Sur la base des informations rapportées dans la littérature associée, le ritonavir agit comme **inhibiteur de la protéase du VIH-1**, une classe pharmacologique dont l'efficacité contre l'infection par le VIH est bien établie.

Le VIS (virus de l'immunodéficience simienne) est un lentivirus apparenté au VIH, dont la protéase partage une forte homologie structurale avec celle du VIH-1. Plusieurs études in vitro incluses dans les preuves montrent que le ritonavir inhibe effectivement la réplication du VIS avec une puissance comparable à celle observée contre le VIH-1 (CE50 de l'ordre de 13 nM contre le VIS versus 25 nM contre le VIH-1), ce qui soutient mécanistiquement la prédiction du modèle.

Toutefois, une réserve importante s'impose : le VIS est un modèle d'infection expérimentale chez le macaque, et non une pathologie humaine. L'essentiel de la littérature retrouvée documente donc la pharmacologie déjà connue du ritonavir dans des modèles animaux de recherche sur le VIH (dynamique virale, réservoirs, essais de nouvelles associations), plutôt qu'une piste de repositionnement vers une maladie humaine distincte. Cette prédiction doit être interprétée comme une confirmation mécanistique de l'indication existante plutôt que comme une nouvelle indication clinique exploitable.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | Préclinique / in vitro | Antimicrobial Agents and Chemotherapy | Le ritonavir inhibe le VIS avec une CE50 d'environ 13 nM, comparable à son activité contre le VIH-1 (25 nM) — sensibilité croisée des inhibiteurs de protéase |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Préclinique / in vitro | Antiviral Therapy | Évaluation de 16 antirétroviraux approuvés (dont le ritonavir) contre le VIH-2, le VIS et des souches SHIV, dans une optique de prophylaxie post-exposition |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Préclinique (modèle macaque) | Journal of Virology | Décroissance virale rapide chez des macaques infectés par le VIS sous quadrithérapie antirétrovirale |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Préclinique (modèle macaque) | PLoS One | Trithérapie antirétrovirale associée à un inhibiteur d'histone désacétylase (SAHA) chez des macaques infectés par le VIS, étude des réservoirs viraux |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Préclinique (modèle macaque) | PLoS Pathogens | Un protocole antirétroviral intensifié induit une suppression virale durable et restreint le réservoir viral dans un modèle simien de SIDA |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Préclinique (modèle macaque) | Journal of Virological Methods | Impact d'une trithérapie orale (AZT + 3TC + Lopinavir/Ritonavir) sur le sous-groupe lymphocytaire CD8 chez des macaques infectés chroniquement par le SHIV |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Préclinique (persistance SNC) | mBio | Persistance de l'infection lentivirale dans le cerveau malgré un traitement antirétroviral efficace |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Construction de modèle préclinique | Microbes and Infection | Construction d'un SHIV chimérique portant le gène de la protéase du VIH-1, outil pour tester in vivo les inhibiteurs de protéase chez le macaque |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | Mécanistique / in vitro | Journal of Virology | Étude du clivage de la protéine Vif du VIH-1 par la protéase virale — pertinence mécanistique indirecte |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | Composé non apparenté, pertinence faible | Antiviral Chemistry & Chemotherapy | Dérivé de fluoroquinolone actif contre des souches de VIH-1 résistantes au ritonavir, le VIH-2 et le VIS — mention indirecte du ritonavir |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucun essai clinique ne soutient cette piste, et les 10 publications retenues sont quasi-exclusivement précliniques (modèles macaque, tests in vitro) — elles confirment l'activité déjà connue du ritonavir sur le VIH plutôt que d'apporter une preuve de repositionnement vers une nouvelle indication humaine. De plus, la cible prédite (infection par le VIS) est un modèle animal expérimental et non une pathologie humaine, ce qui limite fortement l'applicabilité clinique directe de cette prédiction.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résolution de l'écart de données bloquant : mises en garde/contre-indications de la notice TFDA (nécessaire avant toute évaluation de sécurité initiale S1)
- Données de mécanisme d'action structurées (DrugBank), actuellement absentes du dossier
- Clarification de la pertinence clinique de la cible prédite — vérifier si le modèle TxGNN dispose d'une cartographie vers une indication humaine apparentée (ex. infection VIH réfractaire) plutôt que le seul modèle animal VIS
- Données de tarification/réglementation françaises, le produit n'étant actuellement pas commercialisé (0 AMM)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

