---
layout: default
title: Docusate
parent: Prédiction du modèle uniquement (L5)
nav_order: 252
evidence_level: L5
indication_count: 2
---

# Docusate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Docusate : De la Constipation au Syndrome de Plummer-Vinson

## Résumé en Une Phrase

Docusate est un tensioactif laxatif émollient des selles, dont les indications d'origine répertoriées concernent la constipation et plusieurs formes d'anémie (carence en fer, carence en folates, anémie hypochrome, microcytaire).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Plummer-Vinson**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Constipation (les données réglementaires françaises ne fournissent pas de texte d'indication ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Syndrome de Plummer-Vinson |
| Score de Prédiction TxGNN | 99,18 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulée (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le docusate est un tensioactif émollient des selles ; son usage dans la constipation est établi, et il figure aussi, dans le graphe de connaissances, associé à plusieurs anémies par carence (dont la carence en fer).

Le syndrome de Plummer-Vinson associe dysphagie, membranes œsophagiennes et anémie ferriprive. Le modèle a probablement établi le lien par la proximité avec les indications d'anémie ferriprive répertoriées pour le docusate. Cette proximité provient vraisemblablement d'annotations partagées entre maladies voisines dans le graphe, et non d'une relation pharmacologique démontrée.

Le docusate n'a aucun effet connu sur l'absorption du fer, les membranes œsophagiennes ou la dysphagie. Le traitement de ce syndrome repose sur la supplémentation en fer et, si nécessaire, la dilatation endoscopique des membranes. La plausibilité mécanistique est donc faible : la prédiction est à considérer comme un artefact probable du modèle.

Une seconde prédiction du modèle, l'anémie mégaloblastique constitutionnelle indépendante de la vitamine B12 et des folates (score de 99,15 %), présente la même limite : aucune preuve clinique ni mécanisme connu dans l'hématopoïèse ou la synthèse de l'ADN.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69281980 | NORGALAX, gel rectal en récipient unidose (ESSENTIAL PHARMA, Malte) | Gel (voie rectale/topique) | Non renseignée — AMM annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : ulcère gastroduodénal, carence en potassium, drépanocytose, persistance héréditaire de l'hémoglobine fœtale, hyperoxalurie primaire, hémochromatose héréditaire, hémosidérose, trouble du métabolisme du fer, maladie de Wilson, rectocolite ulcéro-hémorragique, maladie inflammatoire chronique de l'intestin, anémie hémolytique, appendicite, gastrite atrophique chronique, neuropathie optique héréditaire de Leber, gastroentérite.
- **Interactions médicamenteuses** (4 identifiées) :
  - Lactulose : modérée
  - Mineral oil (huile minérale) : modérée
  - Phénolphtaléine : modérée
  - Linaclotide : mineure

Les mises en garde et contre-indications de la notice officielle n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et le lien mécanistique est improbable. De plus, la seule AMM française est annulée, ce qui limite toute voie de développement pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de sécurité de la notice (mises en garde et contre-indications), indispensables avant tout examen de sécurité
- Les données détaillées sur le mécanisme d'action
- Toute preuve clinique ou publiée reliant le docusate au syndrome de Plummer-Vinson
- Une évaluation de la compatibilité des voies d'administration et de la similarité avec l'indication d'origine, non réalisées à ce stade
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

