---
layout: default
title: Pretomanid
parent: Prédiction du modèle uniquement (L5)
nav_order: 628
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pretomanid : nouvelle indication prédite, Candidose (niveau de preuve L5). Indication d'origine : Non renseignée dans l'AMM française (tuberculose pharmacorésistante d…"
---

# Pretomanid
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Prétomanide : De l'indication d'origine non précisée à la candidose

## Résumé en Une Phrase

La prétomanide est un antibactérien de la famille des nitroimidazooxazines. Les publications compilées la décrivent comme utilisée dans le schéma BPaL/BPaLM (avec bédaquiline et linézolide) contre la tuberculose pharmacorésistante. L'indication d'origine n'est pas renseignée dans l'AMM française.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **candidose**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction purement informatique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM française (tuberculose pharmacorésistante d'après la littérature) |
| Nouvelle Indication Prédite | Candidose |
| Score de Prédiction TxGNN | 99,69 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la prétomanide est une prodrogue activée chez les mycobactéries par la nitroréductase dépendante de la déazaflavine (Ddn), qui requiert le cofacteur F420.

**Cette prédiction est en réalité peu plausible sur le plan biologique.** Les champignons comme *Candida* ne possèdent pas cette voie d'activation. Aucun lien mécanistique n'est étayé par les données disponibles, et le score élevé du modèle (0,997) reflète une proximité dans le graphe de connaissances, pas une preuve pharmacologique.

À titre de comparaison, d'autres prédictions du modèle sont examinées ci-dessous :

- **Lèpre** (score 99,27 %) : *Mycobacterium leprae* est proche de *M. tuberculosis*, donc un rationnel existe en principe. Toutefois, son génome très réduit pourrait ne plus contenir la voie F420/Ddn, ce qui reste à vérifier. Les huit publications récupérées concernent toutes la tuberculose pharmacorésistante et aucune ne traite de la lèpre.
- **Maladie coronarienne, ischémie myocardique, naissance anormale de l'artère coronaire gauche depuis l'artère pulmonaire** (scores 99,2 % à 99,1 %) : aucun lien pharmacologique, probablement des associations artéfactuelles du modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la candidose.

Pour information, les publications récupérées pour la lèpre (deuxième prédiction) portent uniquement sur la tuberculose pharmacorésistante et ne constituent pas une preuve pour la lèpre ni pour la candidose.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 63915869 | DOVPRELA 200 mg, comprimé | Comprimé | Non renseignée | Annulée |

Titulaire : Mylan Ireland Healthcare (Irlande). L'unique AMM est annulée : le médicament n'est actuellement pas commercialisé en France sous cette AMM.

## Considérations de Sécurité

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

**Interactions médicamenteuses** (14 interactions recensées) :

- **Majeures** : dexaméthasone, lumacaftor, apalutamide, dabrafénib, mitotane, lorlatinib, enzalutamide
- **Modérées** : empagliflozine, sitagliptine, somatropine, somatrem, baricitinib, clofarabine, méthotrexate

Plusieurs interactions majeures concernent des inducteurs enzymatiques ou des médicaments à métabolisme complexe. Toute utilisation exploratoire nécessiterait une revue pharmacologique approfondie.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le mécanisme d'action de la prétomanide, spécifique des mycobactéries, rend une activité antifongique biologiquement improbable.
- Les données de sécurité de la notice manquent (lacune bloquante) et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank)
- Réaliser des tests précliniques *in vitro* d'activité antifongique contre *Candida* avant tout autre investissement
- Si l'on souhaite explorer une piste plus plausible, vérifier la présence de la voie F420/Ddn chez *M. leprae* avant d'envisager la lèpre
- Clarifier la situation réglementaire (AMM annulée) et l'indication d'origine
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

