---
layout: default
title: Methionine
parent: Prédiction du modèle uniquement (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
monitor_inn: "methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "craniostenosis cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "tetanic cataract", "immature cataract", "diabetic cataract"]
last_modified_at: 2026-10-28
description: "Methionine : nouvelle indication prédite, Acné (niveau de preuve L5). Indication d'origine : Non renseignée dans les textes d'AMM compilés"
---

# Methionine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Méthionine : D'un usage en nutrition parentérale à l'acné (prédiction du modèle)
{: .text-alpha }

## Résumé en Une Phrase

La méthionine est un acide aminé essentiel, présent comme composant de nombreuses solutions de nutrition parentérale commercialisées en France.
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**acné**, mais **aucun essai clinique** et seulement **2 publications indirectes** existent, dont aucune ne teste la méthionine comme traitement de cette maladie.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les textes d'AMM compilés |
| Nouvelle Indication Prédite | Acné |
| Score de Prédiction TxGNN | 1,0000 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | Au moins 20 (la liste peut être partielle) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La méthionine est un acide aminé soufré, précurseur de l'homocystéine via le cycle de la méthionine. Elle entre dans la composition de nombreuses solutions d'acides aminés pour perfusion.

Le lien avec l'acné reste très indirect. Une étude de cohorte (2001) a observé des taux plasmatiques d'homocystéine élevés chez des patients traités par isotrétinoïne pour une acné kystique. Cela relie l'acné au métabolisme de la méthionine, mais ne montre pas que la méthionine traite l'acné. La seconde publication (mutation de MTHFR avec encéphalopathie néonatale) mentionne une acné néonatale parmi de nombreux signes et n'apporte pas de preuve pertinente.

Le score très élevé du modèle est une prédiction statistique et ne remplace pas des données cliniques. Comme aucune étude citée ne porte directement sur l'effet de la méthionine dans l'acné, le niveau de preuve est plafonné à L5.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohorte | Int J Dermatol | Élévation de l'homocystéine plasmatique chez des patients sous isotrétinoïne pour acné kystique ; association indirecte |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Cas clinique | BMJ Case Reports | Nouvelle mutation de MTHFR chez un nouveau-né (encéphalopathie, chute de cheveux, aspect marfanoïde, acné néonatale) ; sans lien démontré avec un traitement par méthionine |

## Informations de Marché en France

La liste ci-dessous présente 5 des AMM compilées (au moins 20 au total ; la liste peut être partielle). Les textes d'indication ne sont pas renseignés dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61960303 | AMINOVEN 10 POUR CENT | Solution pour perfusion | Non renseignée |
| 69667989 | AMINOVEN 5 POUR CENT | Solution pour perfusion | Non renseignée |
| 62947013 | AMINOPLASMAL 25 | Solution pour perfusion | Non renseignée |
| 63183821 | AMINOPLASMAL 8 | Solution pour perfusion | Non renseignée |
| 67972077 | AMINOPLASMAL 12 | Solution pour perfusion | Non renseignée |

Ces produits sont des solutions d'acides aminés ; leur statut ne permet pas de déduire une approbation dans l'acné.

## Considérations de Sécurité

- **Relations de contre-indication enregistrées dans le graphe de connaissances** (elles ne proviennent pas du texte de la notice) : hypertension, maladie rénale (dont insuffisance rénale chronique et terminale), diabète et acidocétose diabétique, hypercalcémie, néphrocalcinose, lithiase rénale, maladies cardiaques et cardiovasculaires, hyperlipidémie, phénylcétonurie et troubles du métabolisme de la phénylalanine, intoxication digitalique, fibrillation ventriculaire, sarcoïdose, néphropathie urique aiguë.
- **Interactions médicamenteuses** (5 recensées) : charbon actif (modérée) ; éphédrine, pseudoéphédrine, méxilétine et flécaïnide (mineures).
- Un autre point d'attention : l'homocystéine élevée est un facteur de risque vasculaire possible, ce qui appelle à la prudence en cas de supplémentation en méthionine.

Les mises en garde et contre-indications officielles de la notice ANSM n'ont pas pu être compilées ; veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle, sans essai clinique ni étude testant la méthionine dans l'acné. Les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), préalable au criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Réaliser des études précliniques ou observationnelles reliant directement la méthionine à la physiopathologie de l'acné
- Clarifier le sens de l'effet (bénéfice ou nuisance) compte tenu du rôle de l'homocystéine
- Évaluer la compatibilité des voies d'administration (les produits actuels sont des perfusions)

*Remarque : parmi les autres indications prédites, la cataracte diabétique est la piste la plus étayée indirectement (L4, statut « question de recherche » : biologie rédox de la méthionine, homocystéine), mais sans essai clinique ni étude testant la méthionine comme traitement.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

