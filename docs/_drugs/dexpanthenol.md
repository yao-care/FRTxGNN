---
layout: default
title: Dexpanthenol
parent: Prédiction du modèle uniquement (L5)
nav_order: 232
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "dexpanthenol"
predicted_indications: ["anorectal stricture", "imperforate anus", "anal polyp", "vulvar inverted follicular keratosis", "proctitis", "exanthem (disease)", "punctate epithelial keratoconjunctivitis"]
description: "Dexpanthenol : nouvelle indication prédite, Anorectal stricture (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Dexpanthenol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Dexpanthenol: Anorectal stricture
{: .text-alpha }

## Résumé en Une Phrase

Le dexpanthénol est un précurseur de l'acide pantothénique (vitamine B5), utilisé à l'origine dans des affections cutanées (dermatite, eczéma atopique) et des troubles de la motilité digestive (iléus paralytique, gastroparésie).
Le modèle TxGNN prédit qu'il pourrait être utile pour l'**exanthème**, l'indication la mieux documentée parmi les sept candidates, avec **1 essai clinique** de phase 3 indirect et **aucune publication** à ce jour.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Anorectal stricture |
| Score de Prédiction TxGNN | 0.9972 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 13 sur 14) |
| Nombre d'AMM | 14 (valides : 13) |
| Décision Recommandée | Hold |

> Remarque : l'exanthème est la candidate au 6e rang du classement TxGNN, mais c'est la seule qui dispose d'une preuve clinique ; elle a donc été retenue comme indication principale de ce rapport. Les six autres candidates sont présentées plus bas.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le dexpanthénol est converti dans l'organisme en acide pantothénique, précurseur du coenzyme A. Il est utilisé pour soutenir la réparation épithéliale, l'hydratation et la fonction de barrière cutanée.

Ce mécanisme est cohérent avec les indications dermatologiques d'origine (dermatite, eczéma atopique, maladie de la peau). Un exanthème, éruption cutanée inflammatoire, relève du même champ : la restauration de la barrière cutanée pourrait en atténuer l'expression.

Cette plausibilité reste toutefois théorique. Le seul essai identifié porte sur la prévention d'une éruption cutanée induite par des traitements anticancéreux, et non sur l'exanthème au sens strict. Il s'agit donc d'une preuve indirecte.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Terminé | 160 | Essai randomisé en double aveugle comparant la crème Bepanthen® à une crème de cétomacrogol pour prévenir l'éruption papulopustuleuse chez les patients traités par inhibiteurs du récepteur de l'EGF. Résultats non fournis. Preuve indirecte. |

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 14 AMM recensées sont **annulées**. Aucun texte d'indication approuvée n'est disponible. Les cinq premières sont listées :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 63272113 | DEXPANTHENOL CRISTERS 5 %, pommade | Pommade | Active |
| 66172278 | DEXPANTHENOL ZENTIVA CONSEIL 5 %, pommade | Pommade | Active |
| 66261549 | BEPANTHENE 250 mg/ml, solution injectable I.M. | Solution injectable | Active |
| 61662513 | DEXPANTHENOL EG LABO CONSEIL 5 %, pommade | Pommade | Active |
| 68370337 | DEXPANTHENOL VIATRIS 5 %, pommade | Pommade | Active |

---

## Autres Indications Prédites

| Rang | Indication | Score TxGNN | Preuves | Niveau |
|---|---|---|---|---|
| 1 | Sténose anorectale | 0,9972 | Aucune | L5 |
| 2 | Anus imperforé | 0,9971 | Aucune | L5 |
| 3 | Polype anal | 0,9962 | Aucune | L5 |
| 4 | Kératose folliculaire inversée de la vulve | 0,9960 | Aucune | L5 |
| 5 | Proctite | 0,9960 | Aucune | L5 |
| 7 | Kératoconjonctivite épithéliale ponctuée | 0,9934 | Aucune | L5 |

Pour la sténose anorectale et la proctite, un rôle dans la cicatrisation muqueuse est envisageable mais purement spéculatif. Pour l'anus imperforé (malformation congénitale chirurgicale) et le polype anal, aucun mécanisme plausible n'est identifié.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** : hémophilie (donnée issue des relations médicament-maladie du graphe, et non du texte de la notice).

Veuillez consulter la notice pour les autres informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à un essai de phase 3 indirect, sans résultats, et à aucune publication ; la prédiction repose donc essentiellement sur le modèle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action via DrugBank
- Obtenir les résultats de l'essai NCT01136005 et vérifier précisément la condition étudiée
- Rechercher de la littérature directement liée à l'exanthème
- Clarifier la compatibilité des voies d'administration (topique, injectable, orale)
- Examiner la signification des 14 AMM annulées (raisons commerciales ou réglementaires)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

