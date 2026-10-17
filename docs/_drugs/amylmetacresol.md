---
layout: default
title: Amylmetacresol
parent: Prédiction du modèle uniquement (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amylmetacresol : nouvelle indication prédite, Syndrome de la queue de cheval (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées (antiseptique local pour la g…"
monitor_inn: "amylmetacresol"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
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

# Amylmétacrésol : Des affections de la gorge au syndrome de la queue de cheval

## Résumé en Une Phrase

L'amylmétacrésol est un antiseptique local utilisé dans des pastilles et sprays pour la gorge (gamme Strepsils, Humex Mal de Gorge, génériques).
Le modèle TxGNN le prédit comme potentiellement efficace pour le **syndrome de la queue de cheval**, avec un score très élevé, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées (antiseptique local pour la gorge, d'après les produits commercialisés) |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 16 (0 valide, 16 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. L'amylmétacrésol est un antiseptique local présent dans des pastilles contre le mal de gorge, seul ou associé à l'alcool dichlorobenzylique et/ou à la lidocaïne.

**La prédiction ne repose sur aucun lien mécanistique démontré.** Le syndrome de la queue de cheval est une urgence chirurgicale due à la compression des racines nerveuses. Un antiseptique de pastille n'a aucune pertinence pharmacologique plausible pour cette affection. Le score élevé (0,9999) est une sortie purement computationnelle du modèle, probablement liée à des proximités dans le graphe de connaissances.

Les autres prédictions du modèle vont dans le même sens : syndrome de l'intestin irritable, vessie neurogène (terme obsolète), puis une série d'affections oculaires (uvéite, panuvéite, maladies de l'iris et du corps ciliaire, tumeurs du corps ciliaire). Aucune n'est étayée par un essai ou une publication. L'uvéite antérieure infectieuse est la plus plausible conceptuellement (propriété antimicrobienne), mais reste sans aucune donnée de formulation ophtalmique, de sécurité ou de pénétration intraoculaire. Pour le syndrome de l'intestin irritable, un effet de type anesthésique local est parfois évoqué pour des ingrédients voisins, mais cela reste spéculatif, sans exposition systémique ou digestive établie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 16 AMM recensées sont toutes annulées. Les 5 principales sont listées ci-dessous (le texte d'indication n'est pas renseigné dans les données compilées).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69742210 | Strepsils Miel Citron, pastille à sucer (BB Farma) | Pastille à sucer | Non renseignée |
| 65179483 | Amylmétacrésol/Alcool dichlorobenzylique Viatris Conseil 0,6 mg/1,2 mg Miel Citron | Pastille à sucer | Non renseignée |
| 68466734 | Strepsils Citron sans sucre | Pastille | Non renseignée |
| 65431016 | Strepsils Miel Citron, pastille à sucer (Difarmed) | Pastille à sucer | Non renseignée |
| 67591507 | Strepsils Menthe glaciale | Pastille à sucer | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune donnée d'interaction médicamenteuse n'a été trouvée, et les mises en garde et contre-indications issues des notices n'ont pas pu être compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai, aucune publication, aucun mécanisme plausible. Le produit est utilisé par voie locale oropharyngée et toutes ses AMM françaises sont annulées.
- Les données de sécurité des notices manquent, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse des notices ANSM (mises en garde, contre-indications)
- Données sur le mécanisme d'action (par exemple via DrugBank)
- Évaluation de la pertinence de voies d'administration autres que la voie oropharyngée
- Réexamen d'indications alternatives mieux étayées, car aucune des 10 prédictions actuelles ne dispose de preuves cliniques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

