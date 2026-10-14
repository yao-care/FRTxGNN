---
layout: default
title: Pravastatin
parent: Prédiction du modèle uniquement (L5)
nav_order: 623
evidence_level: L5
indication_count: 9
---

# Pravastatin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Pravastatine : De l'hypertriglycéridémie et de l'athérosclérose à l'hypercholestérolémie familiale homozygote

## Résumé en Une Phrase

La pravastatine est une statine (inhibiteur de l'HMG-CoA réductase), initialement utilisée pour traiter les dyslipidémies (hypertriglycéridémie, hyperlipoprotéinémie) et prévenir les maladies athéroscléreuses et cérébrovasculaires.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypercholestérolémie familiale homozygote**, mais cette prédiction repose sur des preuves indirectes : **1 essai clinique** et **12 publications** associés, dont aucun ne teste directement la pravastatine dans cette maladie.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertriglycéridémie, athérosclérose, accident vasculaire cérébral (texte d'indication de l'AMM non disponible ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Hypercholestérolémie familiale homozygote |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L4 (preuves indirectes, aucune étude directe sur la pravastatine) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la pravastatine inhibe l'HMG-CoA réductase, enzyme clé de la synthèse hépatique du cholestérol, et augmente l'expression des récepteurs hépatiques du LDL, ce qui abaisse le LDL-cholestérol.

L'indication originale (dyslipidémies et prévention de l'athérosclérose) et la nouvelle indication (hypercholestérolémie familiale homozygote, HFHo) partagent la même cible physiopathologique : l'excès de cholestérol LDL circulant. Le lien est donc plausible sur le plan thématique.

Il faut toutefois être prudent. Dans la HFHo, l'activité fonctionnelle des récepteurs du LDL est généralement très faible, voire nulle ; or l'effet des statines passe en grande partie par ces récepteurs. La réponse attendue est donc limitée. Une des publications disponibles précise d'ailleurs que les statines sont peu efficaces dans l'hypercholestérolémie familiale homozygote. Le seul essai associé teste l'alirocumab (un inhibiteur de PCSK9), pas la pravastatine.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Terminé | 18 | Alirocumab en ouvert chez des enfants et adolescents (8-17 ans) atteints de HFHo, critère principal : LDL-C à la semaine 12. Ne teste pas la pravastatine ; un traitement de fond peut inclure des statines. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Revue (Cochrane) | Cochrane Database Syst Rev | Statines chez les enfants atteints d'hypercholestérolémie familiale |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Revue (Cochrane) | Cochrane Database Syst Rev | Statines chez les enfants atteints d'hypercholestérolémie familiale |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Recommandations | Endocr Pract | Recommandations AACE/ACE sur la prise en charge de la dyslipidémie et la prévention cardiovasculaire |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | Essai randomisé (phase 4) | Lancet HIV | Pitavastatine versus pravastatine chez des adultes infectés par le VIH-1 avec dyslipidémie (population non HFHo) |
| [15532136](https://pubmed.ncbi.nlm.nih.gov/15532136/) | 2004 | Commentaire | Prescrire Int | Simvastatine et pravastatine sont les statines de référence dans l'hypercholestérolémie familiale hétérozygote ; les statines sont peu efficaces dans la forme homozygote |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Revue | Clin Ther | Rosuvastatine dans la prise en charge de l'hyperlipidémie, y compris la HFHo |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Revue | Am J Cardiovasc Drugs | Ézétimibe, inhibiteur de l'absorption du cholestérol |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Revue | Cardiovasc Drug Rev | Ézétimibe, inhibiteur de l'absorption du cholestérol de première classe |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Revue | Drugs | Rosuvastatine, supérieure à l'atorvastatine, la simvastatine et la pravastatine sur le profil lipidique |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Revue | Ann Pharmacother | Atorvastatine dans l'hypercholestérolémie primaire et les dyslipidémies mixtes |

La littérature porte surtout sur d'autres agents hypolipémiants (ézétimibe, rosuvastatine, atorvastatine) ou sur les statines en général : les preuves sont donc indirectes.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60097203 | PRAVASTATINE ARROW 10 mg | Comprimé sécable | Non disponible (AMM annulée) |
| 60270452 | PRAVASTATINE ZENTIVA 40 mg | Comprimé | Non disponible (AMM annulée) |
| 63964916 | PRAVASTATINE ZENTIVA 20 mg | Comprimé sécable | Non disponible (AMM annulée) |
| 61624936 | PRAVASTATINE CRISTERS PHARMA 20 mg | Comprimé sécable | Non disponible (AMM annulée) |
| 69922952 | PRAVASTATINE CRISTERS PHARMA 40 mg | Comprimé sécable | Non disponible (AMM annulée) |

Au total, 20 AMM sont recensées, toutes annulées ; aucune n'est actuellement valide.

---

## Considérations de Sécurité

- **Contre-indications (relations du graphe de connaissances, hors texte de la notice)** : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, ulcère gastroduodénal, myopathie et maladies musculaires, rhabdomyolyse, goutte, hémophilie, anémie, entre autres. Ces éléments sont à confirmer avec la notice officielle.
- **Interactions médicamenteuses** : 239 interactions recensées. Parmi les principales, de niveau modéré : métronidazole, clarithromycine, éluxadoline, naltrexone, pectine, rosuvastatine, simvastatine, tinidazole. D'autres interactions, de niveau non précisé, concernent notamment le calcitriol, l'acarbose, le sucralfate et la prednisone.

Les mises en garde issues de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune étude ne teste directement la pravastatine dans la HFHo, et la physiopathologie de cette maladie (récepteurs du LDL peu ou pas fonctionnels) laisse prévoir une efficacité limitée. Les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action détaillées (DrugBank)
- Mises en garde et contre-indications officielles de la notice (ANSM)
- Études cliniques évaluant directement la pravastatine chez des patients atteints de HFHo
- Clarification du statut réglementaire en France (AMM annulées)

**Remarque complémentaire :** parmi les autres prédictions, l'**hypercholestérolémie familiale** (forme hétérozygote, niveau L3) présente des preuves plus solides, notamment des données pédiatriques sur la pravastatine, mais il s'agit d'un usage cliniquement établi plutôt que d'un véritable repositionnement. L'infection par le VIH (niveau L2) soutient surtout la prise en charge des dyslipidémies associées, pas le traitement de l'infection elle-même.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

