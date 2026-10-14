---
layout: default
title: Riluzole
parent: Prédiction du modèle uniquement (L5)
nav_order: 669
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole : De la sclérose latérale amyotrophique à la polymicrogyrie parasagittale pariéto-occipitale bilatérale

## Résumé en Une Phrase

Le riluzole est un médicament initialement utilisé pour le traitement de la sclérose latérale amyotrophique (SLA).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **polymicrogyrie parasagittale pariéto-occipitale bilatérale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Sclérose latérale amyotrophique (d'après le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Polymicrogyrie parasagittale pariéto-occipitale bilatérale |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 10 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après la littérature générale sur la SLA, le riluzole est associé à la modulation de la transmission glutamatergique et à la limitation de l'excitotoxicité. Il s'agit ici d'un contexte général, non d'une donnée propre à ce dossier.

Le lien avec la nouvelle indication est très spéculatif. La polymicrogyrie est une malformation corticale pouvant s'accompagner de composantes épileptogènes ou neurodéveloppementales, où la signalisation glutamatergique pourrait jouer un rôle. Aucune donnée directe ne soutient cette hypothèse, et le score élevé du modèle reflète une prédiction par graphe, non une démonstration biologique.

Il convient de noter que d'autres prédictions du même médicament sont mécanistiquement plus plausibles, notamment les maladies du motoneurone (syndrome du motoneurone inférieur de l'adulte tardif, amyotrophie monomélique, syndrome de Mills, sous-types génétiques de SLA). Elles ne sont toutefois pas davantage étayées par des essais ou des publications spécifiques.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Toutes les AMM sont annulées ; le texte d'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69481874 | EMYLIF 50 mg | Film orodispersible | Annulée |
| 68413596 | TEGLUTIK 5 mg/ml | Suspension buvable | Annulée |
| 63943758 | RILUZOLE EG 50 mg | Comprimé pelliculé | Annulée |
| 66292199 | RILUTEK 50 mg | Comprimé pelliculé | Annulée |
| 69597074 | RILUZOLE BIOGARAN 50 mg | Comprimé pelliculé | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : neutropénie, agranulocytose, abus/dépendance aux substances, hyperbilirubinémie (y compris héréditaire), syndrome de Gilbert, pneumopathie interstitielle, atteinte hépatique d'origine médicamenteuse.
- **Interactions médicamenteuses** : 44 interactions recensées. Parmi celles listées, les niveaux **modérés** concernent l'acide obéticholique, la naltrexone, le déférasirox, l'osilodrostat, l'anagrélide, l'asparaginase, le brentuximab védotin, la clofarabine, le méthotrexate et l'épirubicine. Des interactions mineures sont décrites avec l'oméprazole, la caféine, la théophylline et l'aminophylline. Certaines (metformine, simvastatine, ranitidine, etc.) sont de niveau inconnu.

Les mises en garde et contre-indications issues de la notice ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le mécanisme n'est pas documenté, et le profil de risque hépatique et hématologique appelle la prudence.
- Les AMM françaises sont toutes annulées, ce qui limite la faisabilité d'un repositionnement local.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Compléter les données sur le mécanisme d'action (via DrugBank).
- Réaliser une revue de la littérature précliniques et cliniques ciblée sur la polymicrogyrie et la signalisation glutamatergique.
- Envisager de prioriser les prédictions voisines de la SLA (maladies du motoneurone), mécanistiquement plus plausibles.
- Clarifier la situation réglementaire (raisons des annulations d'AMM) et la disponibilité de la voie d'administration.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

