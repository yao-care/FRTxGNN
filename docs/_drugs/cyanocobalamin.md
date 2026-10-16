---
layout: default
title: Cyanocobalamin
parent: Prédiction du modèle uniquement (L5)
nav_order: 201
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Cyanocobalamin : nouvelle indication prédite, Maladie métabolique de la biotine (niveau de preuve L5). Indication d'origine : Carence en vitamine B12 et anémies carentielles (anémie pernicieuse…"
---

# Cyanocobalamin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Cyanocobalamine : De la carence en vitamine B12 à la maladie métabolique de la biotine

## Résumé en Une Phrase

La cyanocobalamine (vitamine B12) est initialement utilisée pour traiter les carences en vitamine B12 et les anémies carentielles (dont l'anémie pernicieuse).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie métabolique de la biotine**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **1 publication** de portée générale (revue sur la production biotechnologique des vitamines) la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carence en vitamine B12 et anémies carentielles (anémie pernicieuse, anémie par carence en folates, anémie ferriprive, etc.) |
| Nouvelle Indication Prédite | Maladie métabolique de la biotine |
| Score de Prédiction TxGNN | 99,60 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 10 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la cyanocobalamine est la forme de vitamine B12 utilisée en supplémentation. Elle sert de cofacteur à la méthionine synthase et à la méthylmalonyl-CoA mutase, et son efficacité dans la carence en B12 est établie.

Un lien biochimique est envisageable : la biotine est le cofacteur de carboxylases, dont la propionyl-CoA carboxylase, qui agit en amont du méthylmalonyl-CoA dans le métabolisme du propionate. Les deux vitamines interviennent donc dans des voies voisines (acides organiques, propionate).

Ce lien reste toutefois **spéculatif** et aucune donnée fournie ne le confirme. Le score élevé peut refléter la proximité générale des vitamines et cofacteurs dans le graphe de connaissances plutôt qu'une relation thérapeutique réelle. Les maladies métaboliques de la biotine (déficit en biotinidase ou en holocarboxylase synthétase) sont traitées par supplémentation en biotine, et non par la vitamine B12.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Revue | Journal of Chemical Technology and Biotechnology | Revue sur la production biotechnologique de vitamines, coenzymes et biofacteurs apparentés. Elle ne traite pas de l'efficacité clinique de la B12 dans les maladies métaboliques de la biotine. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65647512 | VITAMINE B12 GERDA 1000 µg/4 ml, solution injectable (IM) et buvable | Solution injectable et buvable | Non précisée (AMM annulée) |
| 61247741 | VITAMINE B12 GERDA 250 microgrammes, comprimé sécable | Comprimé sécable | Non précisée (AMM annulée) |
| 60941894 | VITAMINE B12 LAVOISIER 1000 microgrammes/1 ml, solution injectable (I.M.) | Solution injectable | Non précisée (AMM annulée) |
| 66166745 | VITAMINE B12 CHAUVIN 0,2 mg/0,4 ml, collyre en solution en récipient unidose | Collyre en solution | Non précisée (AMM annulée) |
| 64452203 | VITAMINE B12 HORUS PHARMA 0,2 mg/0,4 ml, collyre en solution en récipient unidose | Collyre en solution | Non précisée (AMM annulée) |

Seules 5 des 10 AMM sont listées. Les 10 AMM sont annulées, et aucune AMM valide n'est actuellement recensée.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 313 interactions sont recensées dans les données compilées pour ce rapport. Parmi les premières entrées :
  - Gravité mineure : anti-H2 (famotidine, ranitidine, cimétidine, nizatidine) et inhibiteurs de la pompe à protons (oméprazole, ésoméprazole, lansoprazole, pantoprazole, rabéprazole, dexlansoprazole), ainsi que le chlorure de potassium.
  - Gravité non précisée : metformine, glimépiride, acarbose, rosiglitazone, mésalazine, doxycycline, morphine, sucralfate.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5). Aucun essai clinique ni publication pertinente ne la soutient, et le lien mécanistique reste spéculatif.
- Le traitement de référence des maladies métaboliques de la biotine est la biotine. De plus, toutes les AMM françaises de la cyanocobalamine sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) de la cyanocobalamine
- Données de sécurité issues de la notice (mises en garde et contre-indications) auprès de l'ANSM
- Études précliniques ou de mécanisme démontrant un lien entre la B12 et la voie de la biotine
- Revue de la littérature ciblée sur la B12 dans les déficits en biotinidase ou en holocarboxylase synthétase
- Clarification du statut réglementaire actuel des présentations de B12 en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

