---
layout: default
title: Tropicamide
parent: 僅模型預測 (L5)
nav_order: 323
evidence_level: L5
indication_count: 3
---

# Tropicamide
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

Using le format demandé pour générer le rapport à partir de l'Evidence Pack fourni.

# Tropicamide : De la Mydriase Pupillaire au Syndrome de la Queue de Cheval

## Résumé en Une Phrase

Tropicamide est un antagoniste muscarinique utilisé en ophtalmologie pour induire une **mydriase et une cycloplégie** (dilatation pupillaire) lors des examens oculaires, sans indication officiellement enregistrée en France (produit non commercialisé). Le modèle TxGNN prédit une association possible avec le **Syndrome de la Queue de Cheval**, mais cette direction n'est actuellement soutenue par **aucun essai clinique** ni **aucune publication**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mydriase/cycloplégie ophtalmique (usage établi) — aucune indication officiellement approuvée disponible dans les données regulatoires (produit non commercialisé en France) |
| Nouvelle Indication Prédite | Syndrome de la Queue de Cheval |
| Score de Prédiction TxGNN | 99.53% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de tropicamide ne sont pas disponibles dans ce dossier (lacune identifiée, sévérité élevée). Sur la base des informations disponibles dans le dossier de preuves, tropicamide agirait comme un antagoniste des récepteurs muscariniques M1/M4 à courte durée d'action (anticholinergique), administré par voie topique (collyre) pour bloquer transitoirement l'accommodation et la constriction pupillaire.

Le syndrome de la queue de cheval est une urgence neurochirurgicale causée par une **compression mécanique** des racines nerveuses lombo-sacrées, dont le traitement de première intention est la décompression chirurgicale — un processus pathologique qu'aucun agent pharmacologique ne peut inverser. Le lien mécanistique proposé ne concerne, au mieux, que la prise en charge symptomatique de la vessie neurogène secondaire à ce syndrome (par blocage des récepteurs M3 du détrusor), et non la maladie elle-même.

Ce lien est jugé faible et indirect : il n'existe aucune preuve clinique ou publiée le soutenant, et l'hypothèse la plus probable est que cette prédiction résulte d'un artefact du modèle TxGNN, généré par une association indirecte via la comorbidité « vessie neurogène » plutôt que par une relation causale directe entre tropicamide et le syndrome de la queue de cheval.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve est L5 (prédiction du modèle uniquement, aucun essai clinique ni publication) et le lien mécanistique proposé est jugé faible, probablement un artefact de comorbidité. De plus, l'absence de données sur les mises en garde/contre-indications (lacune bloquante) empêche toute évaluation de sécurité initiale (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice/mises en garde et contre-indications officielles (TFDA/ANSM) — lacune bloquante
- Données détaillées sur le mécanisme d'action (DrugBank)
- Clarification de la cible réelle : confirmer si l'association pertinente est « vessie neurogène » plutôt que « syndrome de la queue de cheval »
- Recherche d'études précliniques ou mécanistiques reliant spécifiquement tropicamide aux troubles neurologiques vésicaux avant toute progression vers S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

