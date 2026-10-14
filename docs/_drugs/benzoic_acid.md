---
layout: default
title: Benzoic Acid
parent: Prédiction du modèle uniquement (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Benzoic Acid
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

# Acide benzoïque : De la fibromatose et la sclérodermie à la bronchite

## Résumé en Une Phrase

L'acide benzoïque (présent ici sous forme de préparations homéopathiques) est associé, dans la base de connaissances utilisée par le modèle, à des maladies fibrosantes et auto-immunes de la peau et des tissus conjonctifs, comme la maladie de Lapeyronie, la sclérodermie et la dermatomyosite.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **bronchite**, avec un score très élevé.
**Aucun essai clinique** et **aucune publication réellement pertinente** ne soutiennent cette prédiction : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Aucune indication texte renseignée dans les AMM ; indications issues du graphe de connaissances : pemphigus, maladie de Lapeyronie, fibromatose pénienne, sclérodermie, sclérodermie systémique, dermatomyosite |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'acide benzoïque est un composé simple, utilisé notamment comme conservateur pour son effet antimicrobien faible. En France, il figure ici dans des préparations homéopathiques diluées. Aucun mécanisme documenté ne relie ce composé à l'inflammation bronchique.

Les indications originales issues du graphe de connaissances (maladie de Lapeyronie, fibromatose, sclérodermie, dermatomyosite) sont des maladies fibrosantes ou auto-immunes. Elles sont très éloignées de la bronchite, qui est le plus souvent une atteinte infectieuse ou inflammatoire des voies respiratoires. Le lien est donc faible.

Le score élevé du modèle reflète probablement une proximité dans le graphe de connaissances plutôt qu'un lien biologique démontré. Les deux publications retrouvées ne concernent pas l'acide benzoïque, ce qui confirme que la prédiction n'est pas étayée à ce jour.

À titre de comparaison, d'autres prédictions du même médicament paraissent biologiquement plus plausibles, notamment la **fibromatose palmaire** (maladie de Dupuytren) et la **maladie de Ledderhose**. Elles partagent une pathologie fibrosante avec la maladie de Lapeyronie et la fibromatose pénienne. Elles restent toutefois sans preuve directe et sont classées comme questions de recherche.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Revue | Drugs | Revue du répaglinide (dérivé de l'acide benzoïque) dans le diabète de type 2 ; sans rapport avec la bronchite ni l'acide benzoïque lui-même |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Préclinique | Am J Respir Cell Mol Biol | Inhibiteur de l'époxyde hydrolase soluble dans la BPCO induite par le tabac ; composé sans rapport avec l'acide benzoïque |

Ces deux publications ne soutiennent pas la prédiction. Elles proviennent vraisemblablement d'artefacts de recherche.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69376909 | BENZOICUM ACIDUM LEHNING, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH | Comprimé, solution(s), granules, poudre et pommade | Non renseignée (AMM annulée) |
| 67434502 | BENZOICUM ACIDUM BOIRON, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH | Comprimé, solution(s), granules, poudre et pommade | Non renseignée (AMM annulée) |
| 69736225 | RHUS TOXICODENDRON COMPOSE | Granules et solution | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du modèle, et non texte de notice) : hypertension, insuffisance hépatique, maladie rénale, maladie de la vésicule biliaire, gastrite, diabète et acidocétose diabétique, hyperplasie bénigne de la prostate, troubles de la coagulation et hémophilie, maladie coronarienne, anémies, arrêt cardiaque soudain et troubles de la conduction cardiaque, déficit en G6PD, glycogénose, cystinurie, galactosémie, myasthénie et maladies de la jonction neuromusculaire, anorexie mentale, maladies cardiovasculaires, achalasie et mégaœsophage.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans les données compilées.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être consultées. Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5). Aucun essai clinique n'existe, la littérature retrouvée n'est pas pertinente, aucun mécanisme n'est établi et les trois AMM françaises sont annulées.
- Parmi les autres prédictions, la fibromatose palmaire et la maladie de Ledderhose méritent d'être explorées comme questions de recherche, en raison de leur proximité avec les maladies fibrosantes d'origine.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (par exemple via DrugBank)
- Notice officielle de l'ANSM avec mises en garde et contre-indications, indispensable avant tout examen de sécurité
- Revue ciblée de la littérature sur l'acide benzoïque dans la bronchite, et sur les maladies fibrosantes pour les indications alternatives
- Données précliniques de plausibilité biologique avant toute étude clinique
- Clarification du statut réglementaire, puisque toutes les AMM sont annulées et que les produits sont homéopathiques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

