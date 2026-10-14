---
layout: default
title: Oxytetracycline
parent: Prédiction du modèle uniquement (L5)
nav_order: 569
evidence_level: L5
indication_count: 10
---

# Oxytetracycline
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

# Oxytétracycline : Des infections bactériennes à la rhinosinusite chronique

## Résumé en Une Phrase

L'oxytétracycline est un antibiotique de la famille des tétracyclines. D'après le graphe de connaissances utilisé par le modèle, il traitait à l'origine diverses infections bactériennes (infections urinaires, bronchite, pharyngite, conjonctivite, pneumonie, etc.).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **rhinosinusite chronique**,
mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections bactériennes diverses (infections urinaires, bronchite, pharyngite, conjonctivite, pneumonie, etc., selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Rhinosinusite chronique |
| Score de Prédiction TxGNN | 99,61 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'oxytétracycline fait partie de la classe des tétracyclines. Son efficacité antibactérienne est établie dans de nombreuses infections, et elle pourrait mécanistiquement être applicable à la rhinosinusite chronique.

Les tétracyclines sont connues pour leur activité antibactérienne et, selon la littérature générale sur la classe, pour des propriétés anti-inflammatoires (inhibition des métalloprotéinases matricielles, MMP). Ces propriétés pourraient avoir un lien avec l'inflammation sinusienne chronique, et la doxycycline, une autre tétracycline, a été explorée dans ce contexte. Ce raisonnement reste toutefois une hypothèse : le score élevé reflète une proximité dans le graphe de connaissances, pas une démonstration clinique.

Aucun essai ni aucune publication n'ont été fournis pour l'oxytétracycline dans cette indication. Le lien est donc plausible mais non étayé.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

> **Note complémentaire.** Parmi les autres indications prédites, l'**otite externe** (rang 10, score 99,27 %) dispose de publications : des comparaisons cliniques d'associations topiques contenant de l'oxytétracycline (avec polymyxine B et hydrocortisone), notamment un essai randomisé de 1985 (55 patients, 78 % de guérison, sans différence significative avec la framycétine/gramicidine) et une comparaison avec la ciprofloxacine (1993, 30 patients). Ces données sont anciennes, portent sur des associations et laissent la contribution propre de l'oxytétracycline incertaine. Cette piste, classée L3 (niveau conservateur), pourrait mériter une évaluation distincte.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69497177 | STERDEX, pommade ophtalmique en récipient unidose (THEA) | Pommade | Non renseignée (AMM annulée) |
| 66592652 | AURICULARUM, poudre et solvant pour suspension pour instillation auriculaire (GRIMBERG) | Poudre et solvant pour suspension pour instillation | Non renseignée (AMM annulée) |

Les deux AMM sont annulées, et les formes disponibles sont à usage ophtalmique et auriculaire. Aucune n'est conçue pour une administration nasale ou sinusienne, ce qui soulève une question de voie d'administration pour la nouvelle indication.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (ne provenant pas du texte de la notice) : maladie rénale, insuffisance rénale, urémie, glomérulonéphrite, maladie hépatique, maladie de la vésicule biliaire, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, déficit en G6PD, fibrillation auriculaire, bloc auriculo-ventriculaire, syndrome d'Adams-Stokes, syndrome de Wolff-Parkinson-White, insuffisance respiratoire, déficit en potassium, glycogénose, cystinurie, galactosémie, pyo-uretère.
- **Interactions médicamenteuses** : 144 interactions recensées. Parmi celles listées :
  - **Majeure** : vitamine A.
  - **Modérées** : sels de calcium, de magnésium et de zinc, citrate de potassium (chélation, absorption réduite), insulines, amoxicilline, balsalazide.
  - **Mineure** : mannitol.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique ni aucune publication ne la soutiennent, le mécanisme d'action n'est pas documenté et le médicament n'a plus d'AMM valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données sur le mécanisme d'action (DrugBank) pour analyser le lien mécanistique.
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Une revue de la littérature ciblée sur l'oxytétracycline ou les tétracyclines dans la rhinosinusite chronique.
- Une évaluation de la compatibilité de la voie d'administration (aucune forme nasale ou sinusienne disponible).
- Éventuellement, une évaluation séparée de l'otite externe, seule indication prédite disposant de publications cliniques.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

