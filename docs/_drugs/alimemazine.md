---
layout: default
title: Alimemazine
parent: Preuves modérées (L3-L4)
nav_order: 38
evidence_level: L4
indication_count: 6
---

# Alimemazine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **6** 
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

# Alimémazine : De l'urticaire et des affections allergiques à l'urticaire allergique

## Résumé en Une Phrase

L'alimémazine (trimeprazine) est un antihistaminique H1 de première génération de la classe des phénothiazines, initialement utilisé dans l'urticaire, la rhinite allergique, l'angio-œdème et d'autres affections allergiques.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**urticaire allergique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction dans les données compilées pour ce rapport.
Il s'agit davantage d'une extension d'une indication déjà établie que d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Angio-œdème (indications d'origine issues du graphe de connaissances : angio-œdème, rhinite allergique, urticaire, conjonctivite atopique, etc.) |
| Nouvelle Indication Prédite | Urticaire allergique |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Autorisations uniquement annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

*Remarque : le texte d'indication approuvée n'est renseigné dans aucune des AMM ; l'indication originale provient donc du graphe de connaissances TxGNN.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'alimémazine fait partie de la classe des phénothiazines et agit comme antihistaminique H1 de première génération. Son efficacité dans l'urticaire est établie, et mécanistiquement elle pourrait être applicable à l'urticaire allergique.

Le blocage des récepteurs H1 réduit les papules et le prurit médiés par l'histamine. L'urticaire figure déjà parmi les indications d'origine de l'alimémazine : l'urticaire allergique en est essentiellement un sous-type. Le score élevé du modèle est donc cohérent avec cette logique pharmacologique.

Ce soutien reste cependant indirect : il repose sur la connaissance de la classe pharmacologique et non sur des données retrouvées pour ce médicament. L'urticaire allergique relève plutôt d'une extension d'usage établi que d'un repositionnement.

---

## Autres Indications Prédites (pour information)

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Recommandation |
|------|------|------|------|------|
| 2 | Urticaire au froid | 99,96 % | L4 | Question de recherche |
| 3 | Réactivité IgE atopique | 99,60 % | L5 | Hold |
| 4 | Maladie de la cavité nasale | 99,60 % | L4 | Question de recherche |
| 5 | Dermatite atopique récalcitrante | 99,59 % | L4 | Question de recherche |
| 6 | Laryngopharyngite aiguë | 99,54 % | L4 | Hold |

Aucune de ces indications ne dispose d'essais cliniques ou de publications dans les données compilées. Les antihistaminiques non sédatifs de nouvelle génération sont les options privilégiées par les recommandations dans l'urticaire au froid. La dermatite atopique n'est pas principalement pilotée par l'histamine, et le bénéfice serait surtout sédatif. Pour la laryngopharyngite aiguë, le rapport bénéfice-risque d'une phénothiazine sédative est défavorable.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 66801066 | THERALENE 5 mg, comprimé pelliculé sécable | Comprimé pelliculé sécable | Non renseignée | Annulée |
| 67410412 | THERALENE 4 POUR CENT, solution buvable | Solution buvable | Non renseignée | Annulée |

Les deux AMM sont détenues par le laboratoire XO et sont annulées. Aucune autorisation valide n'est actuellement recensée, ce qui réduit la faisabilité pratique.

---

## Considérations de Sécurité

**Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) :

- **Cardiovasculaires** : syndrome du QT long (y compris familial), torsades de pointes, arrêt cardiaque soudain, maladie de la conduction cardiaque, infarctus du myocarde, thrombose coronaire, hypotension orthostatique, syndrome de tachycardie orthostatique posturale
- **Neurologiques** : épilepsie, atrophie multisystématisée, maladie des noyaux gris centraux, dystonie focale de la main, blépharospasme
- **Hématologiques** : neutropénie, agranulocytose, leucopénie, thrombocytopénie, anémie (y compris macrocytaire), hémoglobinopathie
- **Hépatobiliaires** : maladie du foie, maladie de la vésicule biliaire
- **Métaboliques** : hyperglycémie, obésité (y compris monogénique)
- **Autres** : hyperplasie bénigne de la prostate, dépendance ou abus de substances, carcinome mammaire féminin

**Interactions Médicamenteuses** : 563 interactions recensées. Parmi les principales :
- **Majeures** : bupropion, citrate de potassium
- **Modérées** : acarbose, famotidine, épinéphrine, albiglutide, alogliptine, hyoscyamine, lopéramide, morphine, atropine, lorcasérine, bisacodyl, glycopyrronium, canagliflozine, chlorpropamide, clarithromycine, acide picosulfurique, polyéthylène glycol, dapagliflozine

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,98 %), mais il repose sur une indication déjà établie (urticaire) et aucun essai ni publication n'a été retrouvé (niveau L4). Le profil de sécurité est préoccupant (QT long, atteintes hématologiques, effets sédatifs) et les AMM françaises sont toutes annulées ; les antihistaminiques non sédatifs sont préférés.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications), car l'absence de ces données bloque le dépistage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank
- Réaliser une recherche bibliographique ciblée sur l'alimémazine dans l'urticaire allergique
- Comparer avec les antihistaminiques de seconde génération pour juger de l'intérêt clinique réel
- Clarifier la situation réglementaire (AMM annulées) et la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

