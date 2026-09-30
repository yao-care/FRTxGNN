---
layout: default
title: Tildrakizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 310
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Tildrakizumab : Du Psoriasis en plaques à la Rétinopathie diabétique non proliférante sévère

## Résumé en Une Phrase

Tildrakizumab est un anticorps monoclonal anti-IL-23 p19, commercialisé pour le traitement du psoriasis en plaques.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **rétinopathie diabétique non proliférante sévère**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Psoriasis en plaques (d'après le rationnel du pack de preuves ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, tildrakizumab est un anticorps anti-IL-23 p19, son efficacité dans le psoriasis en plaques est reconnue, et sur le plan mécanistique il pourrait être applicable à la rétinopathie diabétique.

L'hypothèse est qu'une inflammation chronique de bas grade et la signalisation cytokinique, notamment l'axe IL-23/IL-17, contribueraient aux lésions vasculaires rétiniennes. Bloquer l'IL-23 pourrait donc moduler cette inflammation dans la rétine diabétique. Ce lien reste **spéculatif** et n'est pas établi pour ce médicament.

Plusieurs limites sont à noter. Un biologique administré par voie systémique pénètre peu dans l'œil. Le médicament ne cible pas non plus le VEGF ni les autres voies établies de la rétinopathie diabétique. Enfin, le score élevé repose uniquement sur le modèle, sans aucune étude réelle. Une première étape raisonnable serait une validation préclinique, par exemple l'expression rétinienne d'IL-23/IL-17 dans des modèles diabétiques.

### Autres indications prédites (pour information)

| Indication prédite | Score TxGNN | Niveau de preuve | Recommandation | Commentaire |
|------|------|------|------|------|
| Rétinopathie diabétique | 99,53 % | L5 | Research Question | Recouvre largement la prédiction principale ; ce n'est pas une preuve indépendante. |
| Cataracte diabétique | 99,21 % | L5 | Hold | Aucun mécanisme direct plausible (voie des polyols, stress oxydatif, glycation) ; le score reflète probablement la proximité dans le réseau. |
| Ostéoporose d'origine médicamenteuse | 99,20 % | L5 | Hold | Lien théorique faible via l'IL-23/IL-17 et l'ostéoclastogenèse, mais le sens de l'effet est incertain ; des traitements établis existent (bisphosphonates, dénosumab). |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65992266 | ILUMETRI 200 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée dans les données |
| 69596271 | ILUMETRI 100 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée dans les données |
| 69150269 | ILUMETRI 100 mg, solution injectable en stylo prérempli | Solution injectable | Non renseignée dans les données |

Titulaire : ALMIRALL (Espagne).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score TxGNN (niveau L5), sans essai clinique ni publication. Le lien mécanistique est spéculatif et la pénétration oculaire d'un anticorps systémique est limitée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour tout criblage de sécurité).
- Les données détaillées sur le mécanisme d'action (DrugBank).
- Les textes d'indication des trois AMM.
- Des données précliniques sur l'expression rétinienne d'IL-23/IL-17 dans des modèles de rétinopathie diabétique.
- Une recherche systématique d'essais et de publications, ainsi que d'études observationnelles chez des patients diabétiques traités pour un psoriasis.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

