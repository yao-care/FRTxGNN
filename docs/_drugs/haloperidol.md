---
layout: default
title: Haloperidol
parent: Prédiction du modèle uniquement (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Halopéridol : De la schizophrénie et des troubles psychotiques au trouble congénital de la glycosylation avec défaut de fucosylation

## Résumé en Une Phrase

Le halopéridol est un antipsychotique, initialement utilisé pour traiter la schizophrénie, les troubles psychotiques, les troubles schizo-affectifs et le syndrome de Gilles de la Tourette.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble congénital de la glycosylation avec défaut de fucosylation**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Troubles psychotiques, schizophrénie, trouble schizophréniforme, trouble schizo-affectif, syndrome de Gilles de la Tourette (le texte d'indication des AMM françaises n'est pas renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Trouble congénital de la glycosylation avec défaut de fucosylation |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances générales, le halopéridol est un antipsychotique typique (butyrophénone) qui agit principalement par antagonisme des récepteurs dopaminergiques D2, avec une liaison aux récepteurs sigma. Son efficacité dans la schizophrénie et les troubles psychotiques est établie.

**Aucun lien mécanistique n'a pu être identifié** entre ce mécanisme et un défaut de fucosylation, c'est-à-dire un trouble métabolique rare de la glycosylation des protéines. Le score élevé (99,91 %) reflète la structure du graphe de connaissances, et non une raison biologique ou clinique démontrée. La similarité avec l'indication originale (maladie psychiatrique) n'est pas établie non plus.

Cette prédiction doit donc être considérée comme une simple hypothèse à tester, et non comme une piste thérapeutique étayée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les cinq AMM du halopéridol (laboratoire ESSENTIAL PHARMA (M), Malte) sont **annulées** ; aucune n'est actuellement en vigueur. Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 61490049 | HALDOL 1 mg, comprimé | Comprimé | Annulée |
| 61697400 | HALDOL 5 mg, comprimé | Comprimé | Annulée |
| 61505095 | HALDOL DECANOAS 50 mg/ml, solution injectable | Solution injectable | Annulée |
| 62237643 | HALDOL 2 mg/ml, solution buvable | Solution buvable | Annulée |
| 65374654 | HALDOL 5 mg/ml, solution injectable en ampoule | Solution injectable | Annulée |

## Considérations de Sécurité

Les mentions de la notice (mises en garde et contre-indications officielles) ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

- **Pathologies associées à une contre-indication ou à une précaution (graphe de connaissances, et non texte de la notice)** :
  - Cardiaques : syndrome du QT long (y compris familial), torsades de pointes.
  - Neurologiques : épilepsie, maladies des noyaux gris centraux, dystonie focale de la main, blépharospasme, syndrome malin des neuroleptiques.
  - Hématologiques : neutropénie (dont de nombreuses formes congénitales), agranulocytose, leucopénie.
  - Métaboliques et endocriniennes : hypothyroïdie, myxœdème, hypothyroïdie congénitale, carence en potassium.
  - Autres : maladie hépatique, maladie de la vésicule biliaire, hypotension, carcinome mammaire féminin.
- **Interactions médicamenteuses** : 303 interactions sont répertoriées. Les interactions de niveau **majeur** les plus notables concernent le bupropion, la morphine, la clarithromycine et le dolasétron. De nombreuses interactions de niveau modéré sont aussi signalées (par exemple famotidine, épinéphrine, hydrocortisone, amphotéricine B, atropine, lopéramide).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le trouble congénital de la glycosylation avec défaut de fucosylation repose uniquement sur le score du modèle (niveau L5). Il n'existe aucun essai, aucune publication ni lien mécanistique plausible.
- Le profil de sécurité du halopéridol est notable (risque cardiaque, hématologique, neurologique), et toutes ses AMM françaises sont annulées.

**Remarque sur les autres prédictions du modèle :**
- *Dystrophie rétinienne* (L4) : deux études précliniques chez le rat (modèle de rétinite pigmentaire) montrent une modulation des réponses visuelles des cellules ganglionnaires rétiniennes. Ce résultat est indirect et ne démontre aucun effet modificateur de la maladie.
- *Trouble bipolaire de type maniaque* (L1) : des essais de phase 3, dont un essai contrôlé par placebo et halopéridol (NCT00129220, olanzapine, n = 224), apportent des données randomisées directes. Le halopéridol y est toutefois un comparateur, et son usage dans la manie est déjà établi cliniquement. Ce n'est donc pas un véritable repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) et analyse d'un éventuel lien avec la voie de la fucosylation.
- Données précliniques (modèles cellulaires ou animaux) justifiant une hypothèse biologique pour cette maladie.
- Récupération et analyse de la notice officielle de l'ANSM (mises en garde, contre-indications) pour un examen de sécurité complet.
- Clarification de la situation réglementaire en France, puisque toutes les AMM sont annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

