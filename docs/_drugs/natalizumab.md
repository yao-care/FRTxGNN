---
layout: default
title: Natalizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 211
evidence_level: L5
indication_count: 5
---

# Natalizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Natalizumab : De la Sclérose en Plaques à la Bronchite

## Résumé en Une Phrase

Natalizumab est un anticorps monoclonal dont l'usage documenté dans la littérature est le traitement de la sclérose en plaques récurrente-rémittente. Le texte d'indication de ses AMM françaises n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **bronchite**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Sclérose en plaques (déduite de la littérature ; texte d'indication des AMM non renseigné) |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,46 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, natalizumab bloque l'intégrine alpha4, qui permet aux leucocytes de migrer vers les tissus enflammés. Son efficacité est reconnue dans une maladie inflammatoire auto-immune, la sclérose en plaques.

Sur le plan théorique, freiner la migration des leucocytes pourrait moduler l'inflammation des voies respiratoires. C'est le seul lien mécanistique avancé pour la bronchite. La similarité entre l'indication d'origine (maladie auto-immune du système nerveux central) et la bronchite (le plus souvent une inflammation d'origine infectieuse) n'a pas été évaluée.

Cette prédiction repose uniquement sur le score du modèle. Aucune étude ne l'appuie, et elle doit être considérée comme une hypothèse à explorer.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60779570 | TYRUKO 300 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | SANDOZ (Autriche) |
| 61863110 | TYSABRI 150 mg, solution injectable en seringue préremplie | Solution injectable | BIOGEN NETHERLANDS (Pays-Bas) |
| 68722564 | TYSABRI 300 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | BIOGEN NETHERLANDS (Pays-Bas) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Le dossier ne contient ni mises en garde, ni contre-indications, ni interactions médicamenteuses issues de la notice ANSM. La littérature jointe à d'autres indications prédites signale toutefois un risque de leucoencéphalopathie multifocale progressive (LEMP) sous natalizumab. Ce risque est difficile à justifier pour une pathologie bénigne comme la bronchite.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction pour la bronchite repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Les données de sécurité de la notice ANSM sont absentes, ce qui bloque toute évaluation du rapport bénéfice/risque.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications), une lacune bloquante
- Obtenir les données de mécanisme d'action depuis DrugBank
- Rechercher des études précliniques ou observationnelles sur natalizumab dans les maladies inflammatoires des voies respiratoires
- Comparer le profil de risque (notamment la LEMP) à la gravité de la bronchite avant toute poursuite

**Remarque :** parmi les 5 indications prédites, seul le psoriasis (rang 3, niveau L3) dispose d'une littérature substantielle. Elle est contradictoire : une cohorte rétrospective décrit une amélioration, tandis que plusieurs cas rapportent une induction ou une aggravation. Cette piste mérite une évaluation distincte, avec la question de sécurité à trancher en premier.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

