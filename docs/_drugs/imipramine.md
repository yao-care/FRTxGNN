---
layout: default
title: Imipramine
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 7
---

# Imipramine
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

# Imipramine : De la Dépression au Trouble Déficit de l'Attention/Hyperactivité (TDAH)

## Résumé en Une Phrase

Imipramine est un antidépresseur tricyclique (ATC) historiquement associé au traitement de la **dépression majeure**. Le modèle TxGNN prédit, avec un score de **99,90 %**, qu'il pourrait également être efficace dans le **Trouble Déficit de l'Attention/Hyperactivité (TDAH)**, une piste actuellement appuyée par **20 publications** (dont plusieurs études historiques testant directement l'imipramine chez des enfants TDAH) mais par **aucun essai clinique moderne** dédié à cette combinaison médicament-indication.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dépression (non documentée dans ce pack de preuves — information générale sur la classe thérapeutique de l'imipramine) |
| Nouvelle Indication Prédite | Trouble Déficit de l'Attention/Hyperactivité (TDAH) |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action (MOA) de l'imipramine ne sont pas disponibles dans ce pack de preuves (écart de données **DG002**, priorité Haute). Sur la base des connaissances pharmacologiques générales, l'imipramine est un antidépresseur tricyclique (ATC) de première génération qui inhibe de façon non sélective la recapture de la noradrénaline (NA) et, dans une moindre mesure, de la sérotonine (5-HT). Son efficacité dans le traitement de la dépression majeure est établie depuis les années 1950.

Le TDAH est caractérisé par un déficit fonctionnel des systèmes catécholaminergiques (noradrénaline et dopamine) au niveau préfrontal — un mécanisme partiellement chevauchant avec l'hypothèse monoaminergique de la dépression. L'atomoxétine, seul inhibiteur sélectif de la recapture de la noradrénaline (NRI) actuellement approuvé pour le TDAH, partage ce même mécanisme d'action de base que l'imipramine.

L'analyse TxGNN souligne que l'inhibition de la recapture de la noradrénaline par l'imipramine chevauche partiellement le mécanisme de l'atomoxétine, ce qui pourrait théoriquement améliorer les symptômes d'inattention liés à un déficit de signalisation noradrénergique/dopaminergique préfrontal. Cependant, la sélectivité de l'imipramine est nettement inférieure à celle de l'atomoxétine, et ses effets secondaires anticholinergiques et cardiotoxiques limitent fortement son utilisation, en particulier chez l'enfant — la population la plus touchée par le TDAH. Cette limite est d'ailleurs corroborée par la littérature historique : l'imipramine a été testée comme traitement de seconde ligne chez des enfants non-répondeurs aux psychostimulants, mais n'a jamais obtenu d'indication officielle pour le TDAH.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03220308](https://clinicaltrials.gov/study/NCT03220308) | N/A | Terminé | 103 | Évalue un programme de pleine conscience de 8 semaines pour enfants TDAH combiné à une formation parentale ; **ne teste pas l'imipramine** — essai retenu uniquement par appariement de mots-clés sur la maladie (pertinence Grade C, non lié au médicament). |

Aucun essai clinique testant directement l'imipramine dans le TDAH n'est actuellement enregistré.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6849467](https://pubmed.ncbi.nlm.nih.gov/6849467/) | 1983 | Non classifié | Am J Psychiatry | Résumé non disponible ; rapport clinique historique sur l'utilisation de l'imipramine dans le trouble du déficit de l'attention. |
| [9465283](https://pubmed.ncbi.nlm.nih.gov/9465283/) | 1996 | Non classifié | Clinical EEG | Chez 17 enfants TDAH non-répondeurs au pémoline traités par imipramine, une latence P300 prolongée prédit une mauvaise réponse au traitement. |
| [18304665](https://pubmed.ncbi.nlm.nih.gov/18304665/) | 2008 | Non classifié | Int J Psychophysiol | Étude des effets de l'imipramine sur l'EEG d'enfants TDAH non-répondeurs aux psychostimulants (dexamphétamine, méthylphénidate). |
| [2830919](https://pubmed.ncbi.nlm.nih.gov/2830919/) | 1988 | Non classifié | Biol Psychiatry | Liaison au [³H]imipramine sur plaquettes de 11 garçons ADDH avant/après méthylphénidate ; aucune différence des paramètres de liaison vs témoins. |
| [2258453](https://pubmed.ncbi.nlm.nih.gov/2258453/) | 1990 | Non classifié | J Clin Psychopharmacol | Étude rétrospective (36 enfants TDAH) : la carbamazépine associée à l'imipramine augmente la dose nécessaire, suggérant une interaction pharmacocinétique réduisant les concentrations plasmatiques. |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Non classifié | Expert Opin Drug Saf | Revue de la sécurité des traitements non stimulants du TDAH ; les ATC comme la désipramine ou l'imipramine peuvent être efficaces en alternative de 2ᵉ ligne à l'atomoxétine. |
| [31776871](https://pubmed.ncbi.nlm.nih.gov/31776871/) | 2019 | Revue | CNS Drugs | Revue des interactions médicamenteuses pharmacocinétiques cliniquement significatives pour les agents du TDAH, incluant les molécules en développement. |
| [17078784](https://pubmed.ncbi.nlm.nih.gov/17078784/) | 2006 | Étude de cohorte | Expert Rev Neurother | Les inhibiteurs non sélectifs (désipramine, imipramine) et sélectifs (atomoxétine) de la recapture de la noradrénaline peuvent être efficaces dans le TDAH, en complément des psychostimulants de première intention. |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Méta-revue | Front Psychiatry | Méta-revue de l'efficacité, la tolérance et le risque suicidaire des antidépresseurs en traitement aigu chez l'enfant/adolescent, incluant le TDAH. |
| [10790990](https://pubmed.ncbi.nlm.nih.gov/10790990/) | 1999 | Revue | Evid Rep Technol Assess | Rapport d'évaluation technologique sur l'efficacité et la sécurité des interventions pharmacologiques et non pharmacologiques du TDAH, et l'intérêt des traitements combinés. |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune donnée de sécurité structurée (mises en garde, contre-indications) n'est actuellement disponible — l'écart **DG001** (avertissements/contre-indications TFDA) est classé **bloquant** et empêche formellement le passage à l'évaluation de sécurité S1.
- Le médicament n'est pas commercialisé à Taïwan ni en France (0 AMM), et les seules preuves disponibles pour le TDAH sont des études anciennes (1983-2008), majoritairement non classifiées, sans essai clinique moderne testant directement l'imipramine dans cette indication.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice TFDA (mises en garde, contre-indications) — DG001, priorité bloquante
- Documenter le mécanisme d'action détaillé via DrugBank — DG002, priorité haute
- Confirmer auprès d'une source réglementaire les indications d'origine approuvées de l'imipramine
- Rechercher des essais cliniques et de la littérature récente (post-2010) testant spécifiquement l'imipramine dans le TDAH
- Évaluer le profil de risque cardiovasculaire/anticholinergique de l'imipramine chez la population pédiatrique TDAH avant toute étude clinique prospective
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

