---
layout: default
title: Baricitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 52
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Baricitinib : De l'indication d'origine (non renseignée) au syndrome de microphtalmie colobomateuse-dysplasie rhizomélique

## Résumé en Une Phrase

Baricitinib est un inhibiteur de JAK1/JAK2 commercialisé en France sous le nom OLUMIANT. Le texte de ses indications approuvées n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de microphtalmie colobomateuse-dysplasie rhizomélique**, une maladie congénitale rare.
Cette prédiction repose sur le seul score du modèle : **0 essai clinique** et **0 publication** la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM fournies |
| Nouvelle Indication Prédite | Syndrome de microphtalmie colobomateuse-dysplasie rhizomélique |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après l'analyse du modèle, baricitinib est un inhibiteur de JAK1/JAK2, une voie de signalisation impliquée dans l'inflammation et l'immunité. Les indications d'origine ne figurant pas dans les données, le lien avec la nouvelle indication ne peut pas être établi à partir de celles-ci.

**Le lien mécanistique n'est pas démontré.** Le syndrome prédit associe un colobome oculaire, une microphtalmie et une dysplasie squelettique. C'est un trouble malformatif du développement, sans pathologie connue dépendante de la voie JAK-STAT. Un inhibiteur de kinase immunomodulateur a peu de chances de corriger une malformation structurelle congénitale.

Le score très élevé (99,94 %) est une prédiction informatique. Il reflète probablement une proximité dans le graphe de connaissances et ne constitue pas une preuve clinique. Toute utilisation soulèverait aussi des questions de sécurité liées au développement.

**Deuxième prédiction (rang 2) :** le syndrome de brachydactylie-syndactylie (score 99,94 %). Il s'agit également d'une malformation congénitale des membres, sans composante inflammatoire médiée par JAK-STAT connue, sans essai ni publication associés. Le niveau de preuve est L5 et la recommandation est Hold. Pour l'explorer, il faudrait d'abord identifier une voie commune entre le gène causal et la signalisation JAK/STAT.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61751780 | OLUMIANT 4 mg, comprimé pelliculé | Comprimé pelliculé | Texte non renseigné dans les données |
| 63788717 | OLUMIANT 2 mg, comprimé pelliculé | Comprimé pelliculé | Texte non renseigné dans les données |

Titulaire des deux AMM : ELI LILLY NEDERLAND BV (Pays-Bas).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été trouvée dans la base interrogée. Cela ne prouve pas l'absence d'interactions. Par ailleurs, l'utilisation d'un inhibiteur de JAK dans une maladie congénitale du développement soulèverait des préoccupations de sécurité développementale, à évaluer avant toute exploration.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique établi avec la voie JAK-STAT.
- La nature congénitale et structurelle de la maladie rend un effet thérapeutique peu plausible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de sécurité de la notice ANSM (mises en garde et contre-indications), actuellement manquantes et bloquantes pour le criblage de sécurité
- Les données du mécanisme d'action (MOA), à obtenir via DrugBank
- Le texte des indications approuvées des deux AMM OLUMIANT
- L'identification d'une voie biologique commune entre le gène causal du syndrome et la signalisation JAK/STAT
- Des données précliniques ou de la littérature étayant l'hypothèse, avant toute étude clinique

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

