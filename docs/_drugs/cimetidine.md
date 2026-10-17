---
layout: default
title: Cimetidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 170
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Cimetidine : nouvelle indication prédite, Mastocytose systémique indolente (smouldering) (niveau de preuve L5). Indication d'origine : Ulcère gastrique, reflux gastro-œsophagien, ulcère duodénal…"
monitor_inn: "cimetidine"
predicted_indications: ["duodenal obstruction", "acne (disease)", "abnormality of glucagon secretion"]
---

# Cimetidine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Cimétidine : Des Ulcères Gastroduodénaux à la Mastocytose Systémique Indolente (Smouldering)

## Résumé en Une Phrase

La cimétidine est un antagoniste des récepteurs H2 de l'histamine, initialement utilisé pour traiter l'ulcère gastrique et duodénal, le reflux gastro-œsophagien et les états d'hypersécrétion gastrique (dont le syndrome de Zollinger-Ellison).
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **mastocytose systémique indolente (smouldering)**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette indication précise : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Ulcère gastrique, reflux gastro-œsophagien, ulcère duodénal, syndrome de Zollinger-Ellison, mastocytose systémique (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Mastocytose systémique indolente (smouldering) |
| Score de Prédiction TxGNN | 99,80 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances établies, la cimétidine est un antagoniste compétitif des récepteurs H2 de l'histamine qui réduit la sécrétion d'acide gastrique, basale comme stimulée.

Le graphe de connaissances associe déjà la cimétidine à la mastocytose systémique, où la libération de médiateurs mastocytaires (dont l'histamine) provoque une hypersécrétion gastrique. Le score élevé du modèle reflète probablement cette proximité avec une indication déjà reconnue. La forme indolente (smouldering) est un sous-type de cette maladie.

Le bénéfice attendu serait uniquement symptomatique (contrôle des symptômes gastriques liés aux médiateurs) et non modificateur de la maladie. Aucune donnée ne traite directement ce sous-type.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68053454 | CIMETIDINE ARROW 200 mg, comprimé effervescent (ARROW GENERIQUES) | Comprimé effervescent | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (non issues de la notice) : maladie hépatique, maladie de la vésicule biliaire, insuffisance rénale, cancer gastrique et néoplasmes gastriques (adénocarcinome gastrique diffus, linite plastique, carcinome gastrique).
- **Interactions médicamenteuses** : 551 interactions recensées. Parmi les principales de niveau modéré : paclitaxel, fentanyl, acalabrutinib, lidocaïne, acébutolol, dihydrocodéine, codéine, tramadol, nifédipine, alfentanil. Interactions mineures notables : dolutégravir, zidovudine, paracétamol, kétorolac, ibuprofène, éthinylestradiol, albendazole, éthanol, alendronate, cholécalciférol.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Autres Indications Prédites (Pour Information)

| Rang | Indication | Score TxGNN | Niveau de Preuve | Commentaire |
|---|---|---|---|---|
| 2 | Ulcère peptique actif | 99,79 % | L4 | Indication déjà reconnue, donc pas un repositionnement ; un ECR de 1981 (PMID 7034155) contre placebo ; cimétidine largement remplacée par les IPP |
| 3 | Ulcère gastro-jéjunal | 99,77 % | L4 | Preuves indirectes extrapolées de l'ulcère peptique |
| 4 | Perforation d'ulcère peptique | 99,77 % | L4 | Plusieurs cas de perforation sous cimétidine : signal défavorable |
| 5 | Mastocytose lymphadénopathique avec éosinophilie | 99,76 % | L5 | Aucune donnée ; non adapté |
| 6 | Reflux duodéno-gastrique | 99,49 % | L4 | Petites études physiologiques, sans bénéfice clinique démontré |
| 7 | Obstruction duodénale | 99,44 % | L4 | Un cas isolé de 1978 (PMID 361048) ; preuve anecdotique |
| 8 | Acné | 99,33 % | L4 | Activité antiandrogénique faible ; hypothèse à explorer (question de recherche) |
| 9 | Anomalie de la sécrétion de glucagon | 99,14 % | L5 | Correspondance de mots-clés faussement positive |

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction pour la mastocytose systémique indolente repose uniquement sur le modèle (L5), sans essai ni publication, avec un bénéfice au mieux symptomatique. De plus, la cimétidine n'a plus qu'une AMM annulée en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de sécurité issues de la notice (mises en garde et contre-indications), actuellement manquantes
- Données sur le mécanisme d'action (à compléter via DrugBank)
- Revue de la littérature ciblée sur la mastocytose systémique et les antagonistes H2
- Vérification du statut réglementaire et de la disponibilité d'une formulation commercialisée en France
- Comparaison avec les alternatives actuelles (autres anti-H2, IPP, anti-H1, stabilisateurs mastocytaires)
- Pour l'acné (hypothèse secondaire) : évaluation préclinique ou exploratoire de l'effet antiandrogénique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

