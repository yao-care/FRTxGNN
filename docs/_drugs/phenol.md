---
layout: default
title: Phenol
parent: Prédiction du modèle uniquement (L5)
nav_order: 596
evidence_level: L5
indication_count: 8
---

# Phenol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

# Phénol : De la dermatite à la Acrodermatite chronique atrophiante

## Résumé en Une Phrase

Le phénol est une substance chimique dont l'indication d'origine, selon le graphe de connaissances, est la dermatite.
Le modèle TxGNN prédit qu'il pourrait être utile pour l'**acrodermatite chronique atrophiante**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.
Il s'agit d'une prédiction purement algorithmique (niveau de preuve L5).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dermatite (selon le graphe de connaissances ; aucun texte d'indication n'est renseigné dans les AMM françaises) |
| Nouvelle Indication Prédite | Acrodermatite chronique atrophiante |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le phénol est un agent chimique connu pour ses propriétés irritantes, protéino-dénaturantes et antiseptiques locales, mais les données compilées pour ce rapport ne permettent pas d'établir un lien mécanistique avec la nouvelle indication.

L'acrodermatite chronique atrophiante est le stade cutané tardif de la borréliose de Lyme et se traite par antibiotiques. Le phénol n'a pas de rôle antimicrobien connu dans ce contexte. Le score très élevé du modèle reflète vraisemblablement la proximité du phénol avec des nœuds « dermatite » et « peau » dans le graphe de connaissances, plutôt qu'un véritable mécanisme.

La prédiction doit donc être considérée comme une hypothèse de travail non étayée, et non comme une piste thérapeutique crédible en l'état.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'acrodermatite chronique atrophiante.

*Pour information, d'autres indications prédites ont été examinées :*
- **Chéloïde de l'acné (acne keloid)** : une seule publication (PMID [17204096](https://pubmed.ncbi.nlm.nih.gov/17204096/), 2007, *The Journal of Dermatology*) porte sur un peeling au phénol modifié (Exoderm) pour les rides, cicatrices d'acné et autres problèmes cutanés chez des patients asiatiques. Elle ne traite pas spécifiquement l'acné chéloïdienne ; le risque d'aggravation des lésions chéloïdiennes par agression tissulaire n'est pas à exclure.
- **Syndrome de l'œil sec** : les publications retrouvées portent sur la physiopathologie de la maladie et sur d'autres agents (berbérine, évodiamine, chrysine, etc.). Aucune n'évalue le phénol ; la recherche semble être une simple correspondance de mots-clés.
- Les autres prédictions (pneumopathie interstitielle de l'enfant, dermatomyosite néonatale et amyopathique, hydroa vacciniforme, rétinopathie diabétique non proliférante sévère) n'ont ni essai ni publication.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65026434 | DILUANT H.S.A. 0,03 POUR CENT DES STALLERGENES, solution injectable (annulée) | Solution injectable | Non renseignée |
| 63599951 | OTYLOL, solution pour instillation auriculaire (annulée) | Solution pour instillation | Non renseignée |
| 67066573 | BRULEX, pommade (annulée) | Pommade | Non renseignée |

## Considérations de Sécurité

- **Contre-indications (selon le graphe de connaissances, non issues d'une notice)** : épilepsie, maladie hépatique, maladie de la vésicule biliaire, diabète et acidocétose diabétique, neutropénie, agranulocytose, arrêt cardiaque soudain, maladies de la conduction cardiaque et blocs auriculo-ventriculaires, insuffisance respiratoire, maladie vasculaire périphérique (dont claudication intermittente et artériopathie), appendicite, ulcère gastroduodénal actif, infections virales (herpès simplex, zona, cytomégalovirus, papillomavirus anogénital, verrue commune), leucoencéphalopathie multifocale progressive, cancer, lymphomes (dont lymphome primitif du système nerveux central et lymphosarcome), embryome et dermatite.
- **Points d'attention liés aux prédictions** : le phénol est toxique par absorption systémique et par inhalation, et irritant pour les tissus oculaires ; l'usage néonatal ou intraoculaire soulève des préoccupations de sécurité importantes. Les peelings au phénol ont été associés à des arythmies, une hypopigmentation et des cicatrices hypertrophiques.
- Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

Veuillez consulter la notice pour les mises en garde officielles, qui n'ont pas pu être obtenues.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, sans mécanisme plausible, et avec des signaux de sécurité notables. Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des mises en garde et contre-indications officielles (notice ANSM), lacune bloquante pour tout examen de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Recherche bibliographique ciblée sur le phénol et l'acrodermatite chronique atrophiante
- Évaluation de la compatibilité des voies d'administration et de la similarité avec l'indication d'origine
- Si une piste dermatologique est poursuivie, la prédiction « chéloïde de l'acné » (niveau L4) pourrait être étudiée en priorité, avec une vigilance particulière sur le risque cicatriciel
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

