---
layout: default
title: Clindamycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 179
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Clindamycin : nouvelle indication prédite, Kératoconjonctivite épithéliale ponctuée (niveau de preuve L5). Indication d'origine : Acné, infections à streptocoques et à staphylocoques…"
monitor_inn: "clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
---

# Clindamycin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Clindamycine : Des infections bactériennes et de l'acné à la kératoconjonctivite épithéliale ponctuée

## Résumé en Une Phrase

La clindamycine est un antibiotique de la famille des lincosamides, initialement utilisé contre l'acné, les infections à streptocoques et à staphylocoques, les infections à bactéries anaérobies et la vaginose bactérienne.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **kératoconjonctivite épithéliale ponctuée**, mais il s'agit d'une prédiction issue du graphe de connaissances uniquement : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Acné, infections à streptocoques et à staphylocoques, infections à bactéries anaérobies, vaginose bactérienne (le texte d'indication des AMM n'est pas renseigné ; ces indications proviennent du graphe de connaissances) |
| Nouvelle Indication Prédite | Kératoconjonctivite épithéliale ponctuée |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 8 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la clindamycine est un antibiotique lincosamide actif surtout contre les bactéries à Gram positif (dont *Staphylococcus aureus*) et les anaérobies. Son efficacité dans les infections bactériennes cutanées, respiratoires et gynécologiques est établie.

Le lien avec la nouvelle indication reste faible. La kératopathie épithéliale ponctuée est souvent non infectieuse (sécheresse oculaire, causes toxiques ou virales), et un antibactérien n'a alors pas de justification claire. Un bénéfice ne serait envisageable que pour une composante bactérienne, par exemple une blépharoconjonctivite staphylococcique, ce qui n'est pas établi ici.

Le score élevé du modèle (99,97 %) repose sur la structure du graphe et non sur des preuves expérimentales ou cliniques. Il doit être interprété avec prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour cette indication.

*Remarque : pour la deuxième indication prédite (kératite d'exposition), quatre publications ont été retrouvées (rapports de cas et cohortes rétrospectives sur les kératites bactériennes et les infections oculaires à *S. aureus*), mais aucune n'étudie la clindamycine. Elles ne constituent pas une preuve pour la présente évaluation.*

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68943331 | ZINDACLINE 1 %, gel | Gel | Non renseignée (AMM annulée) |
| 60978355 | DALACINE 900 mg, solution injectable | Solution injectable | Non renseignée (AMM annulée) |
| 68147829 | CLINDAMYCINE KALCEKS 600 mg/4 mL | Solution injectable ou pour perfusion | Non renseignée (AMM annulée) |
| 62286010 | DALACINE 75 mg | Gélule | Non renseignée (AMM annulée) |
| 63185288 | CLINDAMYCINE KABI 600 mg/4 ml | Solution injectable | Non renseignée (AMM annulée) |

Au total, 8 AMM sont recensées, toutes annulées ; aucune n'est actuellement valide. Seules les 5 premières sont listées ci-dessus.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, coup de soleil, maladie de Crohn, maladies inflammatoires chroniques de l'intestin, colite de Crohn, eczéma atopique, dermatite atopique, dermatite exfoliative, maladies diarrhéiques, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, dermatite, rectocolite hémorragique, candidose vulvovaginale.
- **Interactions médicamenteuses** : 320 interactions recensées. Parmi les principales, de niveau modéré : balsalazide, clarithromycine, acide picosulfurique, attapulgite et kaolin. D'autres, de niveau non précisé, concernent notamment l'amphotéricine B, l'acide acétylsalicylique, l'amoxicilline, le bupropion, le pantoprazole, la metformine, la morphine et la vancomycine.
- **Risque de colite à *C. difficile*** : la clindamycine est un facteur de risque connu de cette infection, ce qui est pertinent pour toute extension d'usage.

Les mises en garde et contre-indications issues de la notice officielle ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le rationnel mécanistique est faible, car la pathologie est souvent non infectieuse. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données sur le mécanisme d'action, afin d'analyser le lien mécanistique.
- Les mises en garde et contre-indications issues de la notice, qui bloquent l'étape de criblage de sécurité.
- Des données précliniques ou cliniques de la clindamycine dans la kératoconjonctivite épithéliale ponctuée, notamment dans une composante bactérienne à staphylocoques.
- Une évaluation de la compatibilité des voies d'administration (une formulation ophtalmique n'est pas disponible dans les AMM recensées).
- Une clarification du statut réglementaire, puisque aucune AMM n'est valide.
- Une analyse du risque de résistance (notamment SARM à résistance inductible à la clindamycine).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

