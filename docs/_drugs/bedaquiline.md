---
layout: default
title: Bedaquiline
parent: Prédiction du modèle uniquement (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bedaquiline : nouvelle indication prédite, Tuberculose inactive (rang 2 (niveau de preuve L5). Indication d'origine : Tuberculose pulmonaire, tuberculose multirésistante"
---

# Bedaquiline
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

# Bédaquiline : De la tuberculose pulmonaire et multirésistante à la tuberculose inactive (latente)

## Résumé en Une Phrase

La bédaquiline est un antituberculeux initialement utilisé pour traiter la tuberculose pulmonaire et la tuberculose multirésistante.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **tuberculose inactive (infection tuberculeuse latente)**,
avec **3 essais cliniques** (dont 2 essais de Phase 2/3) et **19 publications** associés à cette direction, mais aucun résultat d'essai de prévention n'est encore disponible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tuberculose pulmonaire, tuberculose multirésistante (source : graphe de connaissances TxGNN ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Tuberculose inactive (rang 2 ; le rang 1, la tuberculose bovine, est fondé uniquement sur une étude in vitro) |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L2 (essai de Phase 2/3 en cours, sans résultats publiés) |
| Statut de Marché en France | Uniquement annulée |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

> Remarque : l'indication la mieux classée par le modèle (tuberculose bovine) ne dispose d'aucun essai clinique et d'une seule étude in vitro (L4, Hold). La présente évaluation porte sur la tuberculose inactive, première indication disposant d'essais cliniques pertinents.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances publiées, la bédaquiline inhibe l'ATP synthase mycobactérienne (sous-unité c). Cette cible est essentielle à la production d'énergie de *Mycobacterium tuberculosis*, y compris sous forme dormante ou non réplicative.

L'indication originale (tuberculose active, y compris résistante) et la tuberculose inactive relèvent du même agent pathogène. Une molécule active sur les bacilles non réplicatifs est donc plausible pour prévenir la progression de l'infection latente vers la maladie, notamment chez les contacts de cas de tuberculose multirésistante et chez les personnes vivant avec le VIH. L'essai de Phase 2/3 BREACH-TB teste directement cette hypothèse, mais son efficacité reste non confirmée. Une littérature de modélisation suggère par ailleurs que des formulations à action prolongée pourraient être envisageables.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Phase 2/3 | En recrutement | 2530 | BREACH-TB : 4 semaines de bédaquiline vs schéma standard pour prévenir la tuberculose chez les personnes vivant avec le VIH et les contacts à haut risque ; pas encore de résultats |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Phase 2/3 | Actif, ne recrute plus | 288 | CRUSH-TB : schémas courts de 17 semaines (bédaquiline, moxifloxacine, pyrazinamide + rifabutine ou délamanide) vs schéma standard de 6 mois dans la tuberculose pulmonaire (indication originale) |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Phase 1 | Pas encore en recrutement | 60 | Étude pharmacocinétique : exposition plasmatique et dans le lait maternel chez les femmes allaitantes ; sans portée d'efficacité |

---

## Preuves de la Littérature

Aucune publication n'est un essai randomisé contrôlé. Il s'agit principalement de revues narratives et d'articles de synthèse (sélection ci-dessous).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Revue | Antibiotics | Inhibiteurs et cibles de l'ATP synthase de *M. tuberculosis*, y compris dans la phase dormante |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | Revue | Infectious Disorders Drug Targets | Systèmes d'administration innovants de bédaquiline ; activité sur les formes persistantes ou latentes |
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Revue | Recent Patents on Anti-Infective Drug Discovery | La bédaquiline comme espoir pour des schémas antituberculeux plus courts |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Revue | Respirology | Mise à jour clinique : la tuberculose comme spectre, rôle de la forme subclinique |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Revue | Clin Pharmacol Ther | Traitement de la tuberculose latente et active |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Revue | Zhejiang Da Xue Xue Bao Yi Xue Ban | Progrès du diagnostic et du traitement de l'infection tuberculeuse latente |
| [29991405](https://pubmed.ncbi.nlm.nih.gov/29991405/) | 2018 | Modélisation PBPK | Int J Tuberc Lung Dis | Preuve de concept de formulations antituberculeuses injectables à action prolongée |
| [28776518](https://pubmed.ncbi.nlm.nih.gov/28776518/) | 2017 | Revue | Int J Mycobacteriology | Médicaments ciblant les bacilles non réplicatifs |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65690588 | SIRTURO 100 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 226 interactions recensées. Parmi les exemples signalés comme majeures : dexaméthasone, clarithromycine, dolasétron, palonosétron, acide picosulfurique, polyéthylène glycol (3350 avec électrolytes) et sulfate de sodium. Des interactions de niveau modéré sont notamment rapportées avec la doxycycline, la minocycline, la tétracycline, la famotidine, la pioglitazone, le bupropion et la naltrexone.
- **Points de vigilance cliniques** (selon l'analyse de la prédiction) : allongement de l'intervalle QT, hépatotoxicité, et interactions importantes avec les rifamycines et les antirétroviraux, à gérer particulièrement dans une population préventive, sinon en bonne santé ou vivant avec le VIH.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Un essai de Phase 2/3 de grande taille (BREACH-TB) teste directement la prévention de la tuberculose par la bédaquiline, et le mécanisme est plausible. Toutefois, aucun résultat n'est disponible, l'AMM française est annulée et la charge d'interactions est élevée : la poursuite doit rester encadrée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats de l'essai BREACH-TB (NCT06568484) sur l'efficacité et la sécurité en prévention
- Mises en garde et contre-indications issues de la notice (non disponibles dans les données compilées, ce qui bloque le criblage de sécurité)
- Données détaillées sur le mécanisme d'action
- Plan de surveillance de l'ECG (QT), de la fonction hépatique et des interactions (rifamycines, antirétroviraux)
- Clarification du statut réglementaire en France (AMM annulée) et du texte d'indication

**Autres prédictions à ne pas retenir en l'état :** tuberculose bovine, aviaire, ascite tuberculeuse et tuberculose cutanée (preuves absentes ou indirectes, Hold) ; tuberculome (cas cliniques seulement, question de recherche, pénétration cérébrale limitée) ; candidose vulvovaginale et œsophagienne, fasciolose et trouble du cycle de l'urée (aucun lien mécanistique plausible, probables artefacts du modèle).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

