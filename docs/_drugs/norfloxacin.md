---
layout: default
title: Norfloxacin
parent: Prédiction du modèle uniquement (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Norfloxacin : nouvelle indication prédite, Hyperamylasémie (niveau de preuve L5). Indication d'origine : Infections bactériennes"
monitor_inn: "norfloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
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

# Norfloxacine : D'une antibiothérapie anti-infectieuse à l'Hyperamylasémie

## Résumé en Une Phrase

La norfloxacine est une fluoroquinolone antibactérienne, utilisée à l'origine pour traiter les infections urinaires, les infections digestives (dysenterie, maladies diarrhéiques, fièvre typhoïde) et d'autres infections bactériennes.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hyperamylasémie**, mais cette prédiction repose uniquement sur le graphe de connaissances.
**Aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections bactériennes (infection urinaire, fièvre typhoïde, dysenterie, maladies diarrhéiques, etc., d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hyperamylasémie |
| Score de Prédiction TxGNN | 99,70 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la norfloxacine appartient à la classe des fluoroquinolones, qui inhibent l'ADN gyrase et la topoisomérase IV bactériennes. Son efficacité est établie dans les infections bactériennes, notamment urinaires et digestives.

En revanche, il n'existe **aucun lien mécanistique identifiable** avec l'hyperamylasémie. La norfloxacine n'agit pas sur la régulation de l'amylase ni sur les pathologies pancréatiques ou salivaires. Le score élevé (99,70 %) apparaît comme un résultat purement calculé par le graphe, non étayé par des données cliniques ou bibliographiques.

Il convient donc d'interpréter cette prédiction avec une grande prudence : elle constitue au mieux une hypothèse computationnelle, sans fondement pharmacologique démontré.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hyperamylasémie.

## Informations de Marché en France

Toutes les AMM listées sont annulées ; le texte d'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65616470 | NORFLOXACINE CRISTERS 400 mg | Comprimé pelliculé | Annulée |
| 68557867 | NORFLOXACINE EG 400 mg | Comprimé pelliculé | Annulée |
| 69563150 | NORFLOXACINE ZENTIVA 400 mg | Comprimé pelliculé | Annulée |
| 61062600 | CHIBROXINE 0,3 POUR CENT | Collyre en solution | Annulée |
| 62866052 | NORFLOXACINE BIOGARAN 400 mg | Comprimé pelliculé | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : syndrome du QT long (y compris familial), torsades de pointes, insuffisance et maladies hépatiques, cirrhose, épilepsie, maladies rénales, thrombocytopénie, anémie, troubles psychiatriques (troubles anxieux, psychotiques, schizo-affectifs), hypokaliémie, tendinite et atteintes tendineuses, rhabdomyolyse, diabète et acidocétose diabétique, neuropathie périphérique, maladies de la vésicule biliaire.
- **Interactions médicamenteuses** : 299 interactions recensées. Parmi les interactions de niveau **majeur** figurent : hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone (corticoïdes, risque accru d'atteinte tendineuse), bupropion et chlorpropamide. Des interactions de niveau modéré concernent notamment les antidiabétiques (metformine, pioglitazone, acarbose, canagliflozine, alogliptine, albiglutide), l'acide acétylsalicylique, le lopéramide, la famotidine, le bisacodyl, le balsalazide et des sels de calcium ou de potassium.

Les mises en garde et contre-indications officielles de la notice ANSM n'ont pas pu être consultées : veuillez consulter la notice pour les informations de sécurité détaillées.

## Autres Indications Prédites (pour information)

Aucune des autres prédictions n'est étayée par des données directes sur la norfloxacine :

| Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|
| Syndrome d'hyperviscosité polyclonale | 99,70 % | L5 | Aucun mécanisme plausible |
| Analbuminémie congénitale | 99,67 % | L5 | Maladie génétique, aucun rationnel pharmacologique |
| Incompatibilité de groupe sanguin | 99,55 % | L5 | Processus immunologique, aucun lien |
| Kératoconjonctivite épithéliale ponctuée | 99,54 % | L4 | Deux publications indirectes (kératoconjonctivite microsporidienne), non spécifiques à la norfloxacine |
| Maladie hématologique prémaligne | 99,48 % | L5 | Aucun rationnel |
| Sclérodermie diffuse | 99,44 % | L5 | Aucun lien établi |
| Gammapathie monoclonale | 99,42 % | L5 | Une publication sur la résistance bactérienne, sans valeur thérapeutique |
| Maladie hématologique avec neuropathie périphérique acquise | 99,38 % | L5 | Les fluoroquinolones peuvent causer des neuropathies |
| Peste septicémique | 99,37 % | L4 | Plausible pour la classe des fluoroquinolones ; données précliniques indirectes ; d'autres molécules mieux soutenues |

La peste septicémique est la seule piste biologiquement plausible (Yersinia pestis est une bactérie à Gram négatif), classée « Question de recherche ». Toutefois, la faible exposition systémique de la norfloxacine limite son intérêt dans les septicémies.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction d'hyperamylasémie ne repose que sur le score du modèle (L5), sans essai, sans publication ni mécanisme plausible. De plus, toutes les AMM françaises de la norfloxacine sont annulées, et le profil de sécurité comporte de nombreuses contre-indications et interactions majeures.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice ANSM (lacune bloquante pour tout criblage de sécurité)
- Les données détaillées sur le mécanisme d'action
- Un rationnel biologique reliant la norfloxacine à l'hyperamylasémie, ainsi que des données précliniques ou cliniques directes
- Pour la peste septicémique, une comparaison avec les fluoroquinolones mieux documentées (ciprofloxacine, lévofloxacine) avant toute poursuite
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

