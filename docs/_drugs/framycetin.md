---
layout: default
title: Framycetin
parent: Prédiction du modèle uniquement (L5)
nav_order: 350
evidence_level: L5
indication_count: 7
---

# Framycetin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Framycétine : D'un antibiotique topique à la cholangite sclérosante

## Résumé en Une Phrase

La framycétine est un antibiotique de la famille des aminosides, commercialisé en France sous forme de pâte dentaire, de pommade et collyre ophtalmiques et de solution auriculaire (toutes ces autorisations sont aujourd'hui annulées).
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **cholangite sclérosante**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette hypothèse : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Cholangite sclérosante |
| Score de Prédiction TxGNN | 99,66 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la framycétine fait partie des aminosides, antibiotiques qui inhibent la synthèse protéique bactérienne (sous-unité ribosomale 30S) et sont actifs surtout contre les bactéries à Gram négatif. Elle est faiblement absorbée par voie orale et agit principalement dans la lumière intestinale ou localement.

Le lien hypothétique avec la cholangite sclérosante passe par l'axe intestin-foie : moduler le microbiote intestinal pourrait influencer la maladie, comme cela a été exploré avec la vancomycine orale. Cependant, la classe des aminosides n'a pas de rôle établi dans cette maladie, et le score élevé (0,997) reste une simple prédiction du modèle.

### Autres indications prédites (à titre d'information)

| Indication prédite | Score TxGNN | Commentaire |
|------|------|------|
| Infection urinaire | 99,42 % | Plausible biologiquement (activité sur Gram négatif), mais exposition systémique limitée et alternatives mieux établies |
| Déficit congénital en prothrombine | 99,41 % | Aucun lien mécanistique plausible ; probable faux positif |
| Urétrite à Ureaplasma | 99,28 % | Adéquation faible : ces germes sont traités par tétracyclines, macrolides ou fluoroquinolones |
| Urétrite gonococcique | 99,28 % | Plausibilité au niveau de la classe seulement ; molécules de référence disponibles (ex. ceftriaxone) |
| Maladie inflammatoire de l'utérus | 99,18 % | Plausible au niveau de la classe uniquement ; non utilisée par voie systémique |
| Pyélonéphrite xanthogranulomateuse | 99,18 % | Antibiotiques seuls peu probablement suffisants (prise en charge souvent chirurgicale) |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67644148 | SEPTOMIXINE, pâte pour usage dentaire | Pâte pour usage dentaire | Non renseignée (AMM annulée) |
| 65164218 | FRAKIDEX, pommade ophtalmique | Pommade | Non renseignée (AMM annulée) |
| 60814943 | FRAKIDEX, collyre en solution | Collyre en solution | Non renseignée (AMM annulée) |
| 66586731 | FRAMYXONE, solution pour instillation auriculaire | Solution pour instillation | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme est hypothétique, les formes commercialisées étaient locales (dentaire, ophtalmique, auriculaire) et toutes les AMM sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de la framycétine
- Mises en garde et contre-indications issues de la notice officielle (ANSM), indispensables pour toute évaluation de sécurité
- Évaluation de la compatibilité des voies d'administration avec l'indication visée
- Études précliniques ou observationnelles étayant le lien intestin-foie dans la cholangite sclérosante
- Revue de la littérature ciblée sur les aminosides et les maladies hépatobiliaires
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

