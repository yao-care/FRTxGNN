---
layout: default
title: Primaquine
parent: Prédiction du modèle uniquement (L5)
nav_order: 630
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Primaquine : nouvelle indication prédite, Myiase (niveau de preuve L5). Indication d'origine : Paludisme à Plasmodium vivax"
monitor_inn: "primaquine"
predicted_indications: ["myiasis", "furuncular myiasis", "wound myiasis", "creeping myiasis", "toxoplasmosis", "nocardiosis", "pneumocystosis"]
---

# Primaquine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Primaquine : Du paludisme à *Plasmodium vivax* à la myiase
{: .text-alpha }

## Résumé en Une Phrase

La primaquine est un antipaludique de la famille des 8-aminoquinoléines, initialement utilisé dans le traitement du paludisme à *Plasmodium vivax*.
Le modèle TxGNN prédit qu'elle pourrait être efficace contre la **myiase** (infestation par des larves de mouches), avec un score très élevé.
Cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Paludisme à *Plasmodium vivax* |
| Nouvelle Indication Prédite | Myiase |
| Score de Prédiction TxGNN | 99,76 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM abrogées (aucune AMM valide) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, la primaquine appartient à la classe des 8-aminoquinoléines. Son efficacité est établie dans le paludisme à *P. vivax*, notamment contre les formes hépatiques dormantes (hypnozoïtes), et elle bloque aussi la transmission en agissant sur les gamétocytes. Rien dans les données disponibles n'indique qu'un mécanisme similaire s'applique à la myiase.

La myiase est une infestation par des larves de diptères, c'est-à-dire un ectoparasitisme. Elle est très éloignée du paludisme, qui est une infection à protozoaire. Aucune activité de la primaquine contre ces larves n'est étayée par les données compilées pour ce rapport.

Le score élevé du modèle (99,76 %) semble donc refléter la proximité dans le graphe de connaissances avec d'autres indications antiparasitaires, et non un signal biologique ou clinique indépendant. Les sous-types de myiase (furonculeuse, des plaies, rampante) ont des scores quasi identiques (99,73 %). Cela suggère une propagation par l'ontologie à partir du terme parent plutôt que des signaux distincts. Cette prédiction doit être considérée comme une hypothèse purement computationnelle.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62907143 | PRIMAQUINE SANOFI 15 mg, comprimé pelliculé (SANOFI WINTHROP INDUSTRIE) | Comprimé | Texte d'indication non renseigné ; AMM abrogée |

---

## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, et non du texte de la notice)** : neutropénie, agranulocytose, déficit en G6PD, anémie hémolytique, méthémoglobinémie par déficit en méthémoglobine réductase, galactosémie, cystinurie, glycogénose, déficit en pyruvate déshydrogénase E3. Le déficit en G6PD et le risque hémolytique sont les points les plus critiques pour cette molécule.
- **Interactions médicamenteuses** : 278 interactions sont recensées, ce qui représente une charge élevée.
  - Interaction **majeure** : dolasétron.
  - Interactions **modérées**, parmi les principales : clarithromycine, lévofloxacine, ondansétron, granisétron, palonosétron, alosétron, famotidine, lopéramide, ainsi que plusieurs laxatifs (bisacodyl, picosulfate, lactulose, lactitol, polyéthylène glycol, citrate de magnésium, sulfate de sodium, glycérine, huile de ricin).
  - Interaction **mineure** : métronidazole.

Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la myiase est de niveau L5 : aucun essai clinique, aucune publication, aucun mécanisme plausible, et un score vraisemblablement hérité de l'ontologie. De plus, la primaquine n'a actuellement plus d'AMM valide en France et présente un profil de sécurité exigeant (hémolyse, G6PD).

**Autres prédictions du modèle, à titre d'information :**
- **Pneumocystose** : l'association clindamycine/primaquine est une option de seconde ligne dans la pneumonie à *Pneumocystis jirovecii* légère à modérée. Elle s'appuie sur un essai de phase 3 (NCT00000640, 290 patients) et sur des revues et recommandations. Elle serait de niveau L1 avec la mention « Proceed with Guardrails » (dépistage G6PD obligatoire, usage en association, seconde ligne uniquement). Un essai de phase 4 (NCT07357103) n'a pas encore commencé à recruter.
- **Toxoplasmose** : niveau L4. Il existe une plausibilité biologique, mais seulement des revues générales et aucun essai.
- **Nocardiose** : niveau L5, sans fondement mécanistique.
- **Paludisme** : il s'agit de l'indication d'origine, confirmée par de nombreux essais, et non d'un repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice de l'ANSM (mises en garde et contre-indications), dont l'absence bloque le criblage de sécurité.
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank) pour analyser un éventuel lien mécanistique.
- Pour la myiase, disposer d'au moins des données précliniques ou de séries de cas avant d'envisager une évaluation. Il serait plus pertinent de prioriser la pneumocystose.
- Vérifier la disponibilité réelle du produit en France, l'AMM étant abrogée.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

