---
layout: default
title: Voxelotor
parent: Prédiction du modèle uniquement (L5)
nav_order: 822
evidence_level: L5
indication_count: 7
---

# Voxelotor
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

# Voxelotor : De l'Anémie Falciforme à la Thrombopénie Héréditaire avec Plaquettes Normales

## Résumé en Une Phrase

Voxelotor est un inhibiteur de la polymérisation de l'hémoglobine S, initialement utilisé pour le traitement de l'anémie falciforme.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **thrombopénie héréditaire avec plaquettes normales**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Anémie falciforme ; persistance héréditaire de l'hémoglobine fœtale (source : graphe de connaissances, et non texte d'AMM) |
| Nouvelle Indication Prédite | Thrombopénie héréditaire avec plaquettes normales |
| Score de Prédiction TxGNN | 99,58 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, voxelotor est un inhibiteur de la polymérisation de l'hémoglobine S qui augmente l'affinité de l'hémoglobine pour l'oxygène. Son intérêt a été établi dans l'anémie falciforme, mais aucun lien mécanistique n'a pu être établi avec les troubles héréditaires du nombre de plaquettes.

Les maladies prédites (thrombopénies héréditaires, déficit en granules denses, troubles de la sécrétion plaquettaire) relèvent de défauts des mégacaryocytes ou des plaquettes, sans rapport évident avec la polymérisation de l'hémoglobine. Le score élevé du modèle (0,996) reflète vraisemblablement la proximité entre nœuds de maladies hématologiques dans le graphe de connaissances, plutôt qu'une justification biologique.

Les autres prédictions du modèle présentent la même faiblesse : thrombopénie macrocytaire avec insuffisance mitrale, maladie des granules denses, thrombopénie néonatale transitoire, thrombopénie (score 99,51 %), syndrome de Fanconi associé à une chaîne légère monoclonale acquise et trouble primaire de la libération plaquettaire. Pour aucune d'elles, un mécanisme plausible n'a été identifié.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Voxelotor n'est actuellement pas commercialisé en France et aucune AMM n'est enregistrée dans les données compilées pour ce rapport.

## Considérations de Sécurité

**Interactions Médicamenteuses** : 130 interactions ont été répertoriées (source : DDInter). Parmi celles affichées, les plus importantes sont :

- **Majeures** : dexaméthasone, clarithromycine, éliglustat, naloxégol
- **Modérées** : hydrocortisone, aprépitant, triamcinolone, bétaméthasone, budésonide, saxagliptine, naldémédine, nitisinone, prednisone, répaglinide, simvastatine, tinidazole (ainsi que des formes ophtalmiques ou nasales de corticoïdes)

Ce profil évoque surtout des interactions métaboliques, notamment avec des inducteurs ou inhibiteurs enzymatiques. Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible. Le médicament n'est en outre pas commercialisé en France, et les données de sécurité issues de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (point bloquant pour le criblage de sécurité)
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Démontrer un lien biologique plausible entre l'affinité de l'hémoglobine pour l'oxygène et les troubles plaquettaires, par des données précliniques
- Clarifier la disponibilité du médicament en France et son statut réglementaire
- Envisager de prioriser des indications plus proches de l'indication d'origine (maladies de l'hémoglobine ou hémolytiques)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

