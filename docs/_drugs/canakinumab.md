---
layout: default
title: Canakinumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab : Des Syndromes Périodiques Associés à la Cryopyrine (CAPS) à l'Infarctus Hépatique

## Résumé en Une Phrase

Canakinumab (Ilaris) est un anticorps monoclonal anti-interleukine-1β, utilisé dans les syndromes auto-inflammatoires, notamment les syndromes périodiques associés à la cryopyrine (CAPS). Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infarctus hépatique**, avec un score très élevé. **Aucun essai clinique** et **aucune publication pertinente** ne soutiennent cette prédiction : elle repose uniquement sur le graphe de connaissances.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM. Les essais et publications du dossier portent sur les CAPS et les syndromes de fièvre périodique |
| Nouvelle Indication Prédite | Infarctus hépatique |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après la littérature, canakinumab neutralise l'IL-1β et supprime ainsi l'inflammation dans les maladies auto-inflammatoires. Son efficacité est établie dans les CAPS et les fièvres périodiques apparentées.

Le lien avec l'infarctus hépatique est **spéculatif**. Le blocage de l'IL-1β pourrait moduler l'inflammation ischémique, mais aucune donnée clinique ne le confirme. Le score élevé du graphe n'est pas étayé par des preuves, et l'indication d'origine (auto-inflammation monogénique) est mécanistiquement éloignée d'une atteinte ischémique du foie.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37354546](https://pubmed.ncbi.nlm.nih.gov/37354546/) | 2023 | ECR (sans rapport) | JAMA | Acide bempédoïque en prévention primaire cardiovasculaire chez des patients intolérants aux statines. Cette étude ne concerne ni le canakinumab ni l'infarctus hépatique. |

Aucune publication directement pertinente n'est disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69541570 | ILARIS 150 mg/ml, solution injectable (NOVARTIS EUROPHARM, Irlande) | Solution injectable | Non renseignée dans les données disponibles |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Autres Indications Prédites (Pour Information)

Le dossier contient 10 indications prédites. Les mieux étayées sont les suivantes :

| Indication | Score TxGNN | Niveau | Décision | Commentaire |
|------|------|------|------|------|
| Fièvre méditerranéenne familiale (autosomique dominante) | 99,41 % | L1 | Proceed with Guardrails | L'IL-1β est directement en cause. Des cohortes récentes, une méta-analyse (PMID [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/)) et des revues soutiennent l'usage en cas de résistance ou d'intolérance à la colchicine. Les essais de phase 3 listés ([NCT00465985](https://clinicaltrials.gov/study/NCT00465985), [NCT00685373](https://clinicaltrials.gov/study/NCT00685373), etc.) relèvent apparemment du programme CAPS. Le lien essai-indication est à vérifier. |
| Syndrome périodique de fièvre - entérocolite infantile - auto-inflammation | 99,57 % | L3 | Research Question | Preuves indirectes issues de revues, d'une revue systématique et d'une cohorte réelle dans les CAPS. |
| Syndrome de Blau | 99,34 % | L4 | Research Question | Cas cliniques de réponse au canakinumab et revue systématique sur l'uvéite. Le tocilizumab a aussi été efficace, donc l'avantage relatif du canakinumab est incertain. |
| Syndrome avec immunodéficience combinée | 99,71 % | L4 | Hold | Un seul cas pédiatrique de CAPS. Le risque infectieux est préoccupant chez un hôte immunodéficient. |
| Occlusion veineuse hépatique, péliose hépatique, mastocytome extracutané, monosomie X, angiosarcome hépatique | 99,30 à 99,82 % | L5 | Hold | Aucune preuve clinique. Pour la monosomie X, les publications liées sont sans rapport et la prédiction paraît fallacieuse. |

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'infarctus hépatique n'a ni essai clinique ni publication pertinente (L5), et le mécanisme reste hypothétique. Les données de sécurité de l'ANSM manquent (lacune bloquante), donc aucune évaluation de sécurité n'est possible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), une lacune bloquante
- Compléter les données de mécanisme d'action via DrugBank
- Renseigner les indications approuvées de l'AMM 69541570
- Pour un usage prioritaire, réorienter l'évaluation vers la fièvre méditerranéenne familiale (L1). Il faut d'abord vérifier le lien entre les essais listés et cette indication, puis retrouver l'essai de phase 3 spécifique (CLUSTER)
- Pour l'infarctus hépatique, rechercher des données précliniques ou de mécanisme avant toute étude

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

