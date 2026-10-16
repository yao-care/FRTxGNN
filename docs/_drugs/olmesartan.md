---
layout: default
title: Olmesartan
parent: Prédiction du modèle uniquement (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Olmesartan : nouvelle indication prédite, Angor de Prinzmetal (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées (le texte d'indication des AM…"
---

# Olmesartan
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

# Olmésartan : De l'hypertension artérielle à l'angor de Prinzmetal

## Résumé en Une Phrase

L'olmésartan est un antagoniste des récepteurs de l'angiotensine II (type AT1), commercialisé en France sous plusieurs noms (Alteis, Olmetec, Coolmetec, Axeler, Sevikar). Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**angor de Prinzmetal**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction. Parmi les autres pistes prédites, la **migraine** est la mieux documentée (3 publications, dont une revue systématique).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées (le texte d'indication des AMM est vide) |
| Nouvelle Indication Prédite | Angor de Prinzmetal |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'olmésartan est un antagoniste des récepteurs AT1 de l'angiotensine II, classe utilisée dans le traitement de l'hypertension. Il pourrait être mécanistiquement applicable à des maladies où le tonus vasculaire joue un rôle.

Pour l'angor de Prinzmetal, l'angiotensine II contribue à la vasoconstriction et pourrait influencer le vasospasme coronarien. Ce raisonnement reste toutefois **spéculatif** : les inhibiteurs calciques et les dérivés nitrés restent la référence, et aucune donnée clinique n'a été fournie.

Plusieurs autres prédictions à score élevé (hypotrichose, alopécie, alopécie areata) n'ont aucun lien mécanistique identifié avec le blocage AT1. Leur score élevé reflète probablement la proximité dans le graphe de connaissances plutôt qu'une justification biologique.

### Autres pistes prédites

| Maladie | Score TxGNN | Niveau de preuve | Données disponibles |
|------|------|------|------|
| Migraine | 99,64 % | L3 | 3 publications (2 études de 2006 chez des patients hypertendus, 1 revue systématique de 2019 sur IEC/ARA II) |
| Hypertension pulmonaire | 99,61 % | L4 | 3 études précliniques chez le rongeur ; 1 essai COVID-19 non pertinent |
| Glaucome à angle ouvert | 99,40 % | L4 | 1 revue générale, soutien indirect uniquement |
| Alopécie, hypotrichose, alopécie areata, hypotrichose congénitale avec milia, migraine avec aura du tronc cérébral, cardiopathie cyphoscoliotique | 99,47 % à 99,57 % | L5 | Aucune |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est actuellement enregistré pour l'angor de Prinzmetal.

*(Pour information : le seul essai identifié dans l'ensemble des prédictions, NCT04330300, est un essai de phase 4 sur les IEC/ARA II dans la COVID-19, suspendu et sans rapport avec l'angor de Prinzmetal.)*

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour l'angor de Prinzmetal.

Pour la piste la plus documentée (migraine) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31515634](https://pubmed.ncbi.nlm.nih.gov/31515634/) | 2019 | Revue systématique | Current Pain and Headache Reports | Efficacité des IEC et ARA II dans la prévention de la migraine épisodique chez l'adulte ; vise à identifier les lacunes de recherche |
| [16618270](https://pubmed.ncbi.nlm.nih.gov/16618270/) | 2006 | Étude clinique | Headache | Effets de l'olmésartan sur la fréquence et la sévérité des migraines chez des patients hypertendus ou préhypertendus (plan d'étude non confirmé) |
| [16942482](https://pubmed.ncbi.nlm.nih.gov/16942482/) | 2006 | Commentaire | Headache | Commentaire sur l'olmésartan, la migraine et la pression artérielle |

---

## Informations de Marché en France

Les 20 AMM sont **annulées** ; aucune n'est valide. Le texte d'indication n'est pas renseigné. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62597926 | ALTEIS 10 mg | Comprimé pelliculé | Non renseignée |
| 67258011 | OLMETEC 20 mg | Comprimé pelliculé | Non renseignée |
| 64220863 | ALTEIS 40 mg | Comprimé pelliculé | Non renseignée |
| 66152197 | OLMETEC 40 mg | Comprimé pelliculé | Non renseignée |
| 68573412 | OLMETEC 10 mg | Comprimé pelliculé | Non renseignée |

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 94 interactions recensées. Les plus importantes :
  - **Majeures** : chlorure de potassium, bicarbonate de potassium (risque d'hyperkaliémie).
  - **Modérées** : hydrocortisone, éluxadoline, exénatide, polyéthylène glycol avec électrolytes, et de nombreuses formes d'insuline (humaine, asparte, dégludec, détémir, glargine, glulisine, lispro, etc.).

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'angor de Prinzmetal repose uniquement sur le modèle (L5), sans essai ni publication, et les traitements actuels (inhibiteurs calciques, dérivés nitrés) restent la référence.
- Toutes les AMM françaises sont annulées, et les mises en garde et contre-indications ne sont pas disponibles, ce qui empêche l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, indications) : lacune bloquante.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Rechercher des données précliniques ou cliniques sur l'olmésartan dans le vasospasme coronarien.
- Piste alternative à approfondir : la **migraine** (L3). Analyser en détail les études de 2006 et la revue de 2019, en tenant compte du biais lié à la baisse de la pression artérielle. Le candésartan dispose d'un meilleur soutien par essais randomisés dans cette classe.
- Clarifier le statut réglementaire actuel (raisons de l'annulation des AMM et disponibilité éventuelle de génériques).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

