---
layout: default
title: Difluprednate
parent: Prédiction du modèle uniquement (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Difluprednate
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

# Difluprednate : Évaluation de Repositionnement, de l'Anti-inflammatoire Corticoïde à l'Hypoplasie Surrénalienne Familiale (Prédiction)

## Résumé en Une Phrase

Le difluprednate est un corticoïde de synthèse anti-inflammatoire. L'indication d'origine n'est pas renseignée dans le dossier.
Le modèle TxGNN prédit en premier rang qu'il pourrait être efficace pour l'**hypoplasie surrénalienne familiale avec absence de LH hypophysaire**, mais **aucun essai clinique ni aucune publication** ne soutient cette prédiction.
Parmi les 10 prédictions, seule la maladie de l'iris (rang 10) dispose d'essais cliniques de phase 3 : il s'agit d'un usage proche de l'indication ophtalmique déjà commercialisée, et non d'un véritable repositionnement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Hypoplasie surrénalienne familiale avec absence de LH hypophysaire |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Le difluprednate est un glucocorticoïde de synthèse puissant, agoniste du récepteur des glucocorticoïdes. Son métabolite actif (butyrate de difluoroprednisolone) freine l'inflammation en inhibant les médiateurs inflammatoires.

Pour la première prédiction, **le lien mécanistique n'est pas convaincant**. L'hypoplasie surrénalienne familiale avec absence de LH est un défaut congénital du développement surrénalien et hypophysaire. Un corticoïde ne peut pas corriger un tel défaut. Le score élevé reflète probablement la proximité du médicament avec le récepteur des glucocorticoïdes et l'axe surrénalien dans le graphe de connaissances, et non une justification thérapeutique.

Il en va de même pour les autres prédictions sans preuve : kératose séborrhéique, syndrome PAGOD, kératose folliculaire inversée vulvaire et trouble du développement sexuel 46,XY. Deux cas relèvent d'une logique de classe (corticoïdes en remplacement ou en traitement standard) : l'insuffisance surrénalienne (rang 5) et le syndrome néphrotique (rang 9). Un produit topique ou ophtalmique n'a cependant aucun rôle de substitution plausible, et son exposition systémique est limitée.

Pour la dermatite séborrhéique (rang 6) et la nécrobiose lipoïdique (rang 8), il existe un rationnel de classe (corticoïdes topiques ou intralésionnels), sans donnée propre au difluprednate.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré pour la première prédiction (hypoplasie surrénalienne familiale).

Seule la prédiction de rang 10, **maladie de l'iris** (score 99,16 %), dispose d'essais :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00407056](https://clinicaltrials.gov/study/NCT00407056) | Phase 3 | Terminé | 20 | Étude ouverte du difluprednate 0,05 % dans l'uvéite antérieure sévère (y compris panuvéite). Directement pertinente, mais petite et non contrôlée |
| [NCT01124045](https://clinicaltrials.gov/study/NCT01124045) | Phase 3B | Terminé | 80 | Difluprednate (Durezol™) vs acétate de prednisolone 1 % (Pred Forte™), randomisée en double insu, chez l'enfant de 0 à 3 ans après chirurgie de la cataracte. Pertinence indirecte (inflammation postopératoire) |
| [NCT03693989](https://clinicaltrials.gov/study/NCT03693989) | Phase 3 | Terminé | 178 | Émulsion ophtalmique PRO-145 vs prednisolone 1 % contre l'inflammation et la douleur après phacoémulsification. Pertinence indirecte, à vérifier (titre tronqué) |
| [NCT05082415](https://clinicaltrials.gov/study/NCT05082415) | N/A | Terminé | 9456 | Étude en vie réelle du brolucizumab dans la DMLA néovasculaire (registre IRIS). **Non pertinente** : correspondance fortuite, sans lien avec le difluprednate |

## Preuves de la Littérature

Aucune publication n'est disponible pour la première prédiction. Pour la maladie de l'iris (rang 10) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/) | 2011 | Préclinique (PK chez le lapin) | J Ocul Pharmacol Ther | Caractéristiques pharmacocinétiques et pharmacodynamiques de l'émulsion ophtalmique de difluprednate, comparées à d'autres agents ophtalmiques. Rappelle son usage ancien comme anti-inflammatoire dermatologique |
| [27594198](https://pubmed.ncbi.nlm.nih.gov/27594198/) | 2016 | Rapport de cas | Ophthalmology | Prise en charge à long terme d'une panuvéite et d'une hétérochromie de l'iris chez un survivant d'Ebola. Lien indirect, sans résumé disponible |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63588061 | EPITOPIC 0,05 POUR CENT (ETHYX PHARMACEUTICALS) | Crème | Non renseignée dans le dossier |

Le produit commercialisé en France est une **crème** (voie cutanée). Les données de prédiction, elles, décrivent surtout une émulsion ophtalmique. Cette différence de forme et de voie est à clarifier avant toute extrapolation.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La première prédiction repose uniquement sur le score du modèle (L5), sans essai, sans publication, et avec un mécanisme non plausible.
- Le seul signal exploitable (maladie de l'iris, rang 10, marqué L1 et « Proceed with Guardrails » dans le dossier) correspond à l'usage ophtalmique existant. Son niveau L1 reste provisoire, car les essais NCT01124045 et NCT03693989 portent surtout sur l'inflammation postopératoire, et le seul essai directement pertinent (NCT00407056) est ouvert et de petite taille.

**Pour avancer, les éléments suivants sont nécessaires :**
- Lire la notice ANSM (mises en garde, contre-indications, indication de l'AMM 63588061) : c'est le point bloquant pour le criblage de sécurité.
- Renseigner l'indication d'origine et le mécanisme d'action (DrugBank).
- Confirmer la population et le design de NCT01124045 et NCT03693989, pour valider ou non le niveau L1 dans la maladie de l'iris.
- Si la voie ophtalmique est retenue : surveiller la pression intraoculaire et le risque de cataracte, et exclure les étiologies infectieuses.
- Clarifier la compatibilité de voie entre la crème commercialisée en France et l'émulsion ophtalmique étudiée.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

