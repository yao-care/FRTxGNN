---
layout: default
title: Clioquinol
parent: Preuves modérées (L3-L4)
nav_order: 80
evidence_level: L4
indication_count: 7
---

# Clioquinol
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
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

# Clioquinol : Vers la Candidose Cutanée (indication d'origine non renseignée)

## Résumé en Une Phrase

Le clioquinol (DrugBank DB04815) est présent en France dans un seul produit autorisé, un patch pour test épicutané. Les données fournies n'indiquent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **candidose cutanée**.
Aucun essai clinique n'est enregistré, et **6 publications** sont associées. Seules 3 concernent des produits contenant du clioquinol, toutes en association, avec un plan d'étude non vérifié.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Candidose cutanée |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après des connaissances générales, qui ne proviennent pas des données fournies, le clioquinol est décrit comme un chélateur et ionophore de métaux (zinc, cuivre, fer) doté d'une activité antifongique et antibactérienne. Cela rend son activité contre *Candida* plausible sur le plan mécanistique.

Le lien avec l'indication d'origine ne peut pas être analysé, car aucune indication approuvée n'est renseignée dans les données. Le score TxGNN est très élevé (0,998), mais il reste une simple prédiction du modèle.

La littérature apporte un signal indirect et nuancé. Dans l'étude PMID 155507 (1979), le comparateur contenait de l'iodochlorhydroxyquine (clioquinol) associée à l'hydrocortisone. Il a donné une réponse excellente chez 43 % des patients atteints de candidose cutanée, contre 95 % avec l'association halcinonide-néomycine-amphotéricine. L'association à base de clioquinol s'est donc montrée nettement moins efficace que le produit de référence de cette étude.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Tous les plans d'étude sont non vérifiés. Aucune étude ne porte sur le clioquinol seul.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [155507](https://pubmed.ncbi.nlm.nih.gov/155507/) | 1979 | Étude clinique (comparative) | Current Medical Research and Opinion | Crème halcinonide-néomycine-amphotéricine : réponse excellente chez 38 patients sur 40 (95 %), contre 17 sur 40 (43 %) avec l'association iodochlorhydroxyquine-hydrocortisone |
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | Étude comparative randomisée | J Int Med Res | 154 patients (dont 67 avec candidose cutanée) : deux crèmes corticoïde-antimicrobien, dont une contenant du clioquinol, donnent des réponses thérapeutiques équivalentes |
| [128475](https://pubmed.ncbi.nlm.nih.gov/128475/) | 1975 | Étude clinique (double aveugle) | Dermatologica | 430 patients : la crème Locacorten-Vioform (avec clioquinol) est très efficace dans les dermatoses surinfectées par des bactéries. Il s'agit d'infections bactériennes, pas de candidose |
| [136333](https://pubmed.ncbi.nlm.nih.gov/136333/) | 1976 | Évaluation clinique | Curr Ther Res | Association halcinonide-antifongique ; pas de résumé disponible |
| [4220930](https://pubmed.ncbi.nlm.nih.gov/4220930/) | 1965 | Autre (indirect) | Z Haut Geschlechtskr | Article en allemand sur le rôle des levures dans l'acrodermatite entéropathique ; pas de résumé disponible |
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Autre (indirect, in vitro) | Przegl Dermatol | Additifs de savons de toilette testés in vitro sur *Candida albicans* ; lien indirect avec le clioquinol |

### Autres indications prédites (sans essai clinique)

| Maladie prédite | Score TxGNN | Niveau | Preuves disponibles |
|------|------|------|------|
| Mycose superficielle | 99,18 % | L3 | Étude préclinique de 2021 sur l'association clioquinol + ciclopirox + terbinafine (activité et toxicité, [PMID 33772895](https://pubmed.ncbi.nlm.nih.gov/33772895/)) ; rapport clinique de 1958 sur une crème clioquinol-hydrocortisone, plan non vérifié ([PMID 13521766](https://pubmed.ncbi.nlm.nih.gov/13521766/)) |
| Maladie infectieuse ectothrix | 99,26 % | L5 | Aucune |
| Granulome de Majocchi | 99,26 % | L5 | Aucune |
| Maladie infectieuse endothrix | 99,19 % | L5 | Aucune |
| Dermatophytie du cuir chevelu ou de la barbe | 99,17 % | L5 | 10 références examinées, toutes hors sujet (faux positifs sur le mot « beard ») |
| Tinea profunda | 99,13 % | L5 | Aucune |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 64835493 | TRUE TEST 36, patch pour test épicutané | Patch | SmartPractice Denmark (Danemark) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucun essai clinique n'existe pour la candidose cutanée. Les publications disponibles portent sur des associations à base de clioquinol, avec des plans d'étude non vérifiés, et l'une d'elles montre une efficacité inférieure au comparateur. Les données de sécurité ANSM manquent, ce qui bloque le passage à l'étape de dépistage de sécurité (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante)
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Confirmer l'indication d'origine et la voie d'administration compatible : le seul produit français est un patch de test épicutané, et non une forme thérapeutique
- Vérifier le plan et les résultats des études de 1975 à 1981 (PMID 155507, 6459255, 128475)
- Examiner de manière approfondie le lien entre le clioquinol et les mycoses superficielles (PMID 33772895)

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

