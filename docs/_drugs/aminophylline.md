---
layout: default
title: Aminophylline
parent: Preuves modérées (L3-L4)
nav_order: 34
evidence_level: L4
indication_count: 10
---

# Aminophylline
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Aminophylline : D'une indication non renseignée à la migraine

## Résumé en Une Phrase

L'aminophylline (théophylline associée à l'éthylènediamine) est commercialisée en France sous forme de solution pour perfusion, mais son indication autorisée n'est pas renseignée dans les données ANSM disponibles.
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **migraine**, avec **0 essai clinique** et **6 publications** seulement. Une seule est une revue récente (2023) ; les autres sont des cas cliniques, des travaux précliniques ou des articles anciens.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (texte d'indication vide) |
| Nouvelle Indication Prédite | Migraine (*migraine disorder*) |
| Score de Prédiction TxGNN | 99,88 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank. D'après la pharmacologie générale, l'aminophylline est un inhibiteur non sélectif des phosphodiestérases et un antagoniste des récepteurs de l'adénosine. Le résumé de l'essai NCT07011134 mentionne son usage établi comme bronchodilatateur et dans l'apnée du prématuré. L'indication originale n'a cependant pas pu être confirmée par les données réglementaires.

L'hypothèse sous-jacente est que la migraine pourrait être liée à un métabolisme énergétique cérébral altéré, avec des taux d'adénosine anormalement élevés. Or l'adénosine dilate les artères cérébrales et participe à la transmission de la douleur. Bloquer ses récepteurs pourrait donc soulager la douleur. Ce raisonnement s'appuie sur une revue de 2023 qui rapporte un bénéfice thérapeutique dans la douleur, notamment les céphalées post-ponction durale, et sur une série de cas observationnelle déjà publiée.

Deux éléments appuient indirectement cette piste. Un cas de migraine hémiplégique a été déclenché par le régadénoson, un agoniste de l'adénosine. Des données *in vitro* montrent que l'adénosine et les composés adéniniques dilatent les artères piales. Ces éléments restent des indices mécanistiques et non des preuves d'efficacité chez l'humain.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Revue | Pain Management | L'aminophylline, antagoniste de l'adénosine, pourrait soulager fortement la douleur, en particulier les céphalées post-ponction durale. Une série de cas observationnelle antérieure suggère un effet thérapeutique dans la migraine. |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Cas clinique | J Nucl Cardiol | Épisode de migraine hémiplégique déclenché par le régadénoson (agoniste de l'adénosine). L'aminophylline est citée parmi les moyens d'inverser ses effets indésirables. |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Cas clinique | Can J Cardiol | Patiente avec syndrome X attribué à un excès d'effet de l'adénosine (« migraine myocardique » sans ischémie). |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | Préclinique (*in vitro*) | Stroke | L'adénosine et les composés adéniniques dilatent nettement les artères piales du chat et de l'humain, mais pas les artères extracrâniennes testées. Implication possible dans la migraine. |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Revue / autre | Aggiornamenti Clinicoterapeutici | Article ancien sur les céphalées, sans résumé disponible. Contenu non vérifiable. |
| [5540199](https://pubmed.ncbi.nlm.nih.gov/5540199/) | 1971 | Autre | The Practitioner | Article de 1971 intitulé « Suppositories », sans résumé. Pertinence incertaine. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69586398 | AMINOPHYLLINE RENAUDIN 250 mg/10 ml | Solution pour perfusion | Non renseignée |

Le titulaire est le Laboratoire Renaudin.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais aucun essai clinique n'est enregistré. Les preuves humaines se limitent à une revue narrative récente, à des cas cliniques et à des articles anciens dont le contenu n'est pas vérifiable. Le niveau de preuve reste L4.
- L'indication originale et la sécurité ne sont pas documentées. L'analyse d'une autre indication prédite (hypertension pulmonaire) signale en outre une marge thérapeutique étroite et un potentiel d'interactions. Il est donc trop tôt pour recommander une progression.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le RCP/la notice ANSM (mises en garde, contre-indications, indication autorisée), lacune bloquante pour le dépistage de sécurité.
- Compléter le mécanisme d'action via DrugBank.
- Analyser la série de cas observationnelle citée dans la revue de 2023 et évaluer la faisabilité d'un essai contrôlé. La voie d'administration (perfusion) doit aussi être confrontée à l'usage attendu dans la migraine, la compatibilité de voie n'étant pas encore évaluée.
- Les prédictions de sous-types (migraine avec aura du tronc cérébral, susceptibilité génétique) n'ont aucune preuve propre. Elles dépendent de la validation de l'hypothèse migraine.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

