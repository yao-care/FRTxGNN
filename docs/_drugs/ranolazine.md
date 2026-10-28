---
layout: default
title: Ranolazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 652
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Ranolazine : nouvelle indication prédite, Syndrome néphrogénique d'antidiurèse inappropriée (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées"
monitor_inn: "RANOLAZINE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ranolazine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Ranolazine : De l'Indication Originale Non Renseignée au Syndrome Néphrogénique d'Antidiurèse Inappropriée
{: .text-alpha }

## Résumé en Une Phrase

Ranolazine est un inhibiteur du courant sodique tardif, commercialisé en France sous le nom RANEXA (comprimés à libération prolongée). Les données compilées pour ce rapport n'indiquent pas son indication originale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée (NSIAD)**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée |
| Score de Prédiction TxGNN | 0,9965 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, la ranolazine inhibe le courant sodique tardif (INaL) et peut aussi agir sur d'autres canaux ioniques, notamment hERG et, dans une moindre mesure, le courant sodique de pointe.

Le NSIAD est causé par des mutations avec gain de fonction du récepteur V2 de la vasopressine (AVPR2, par exemple R137C/R137L) ou, dans certains cas, par une anomalie de signalisation liée à GNAS. Le récepteur est alors activé en permanence, ce qui provoque une rétention d'eau indépendante de la vasopressine.

**Aucun lien mécanistique établi n'a été identifié.** La ranolazine n'a pas d'action connue sur le récepteur V2, sur la signalisation AMPc/aquaporine-2 ni sur la gestion rénale de l'eau. Le score très élevé (0.9965) provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. La similarité avec l'indication originale reste à évaluer.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63170891 | RANEXA 375 mg, comprimé à libération prolongée (statut : active) | Comprimé à libération prolongée | Non renseignée |
| 64679592 | RANEXA 500 mg, comprimé à libération prolongée (statut : active) | Comprimé à libération prolongée | Non renseignée |

Les deux autorisations sont détenues par MENARINI INTERNATIONAL OPERATIONS LUXEMBOURG et sont valides (2 AMM valides sur 2) ; le médicament est commercialisé.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie de TxGNN/PrimeKG, et non texte de la notice) : syndrome du QT long, syndrome du QT long familial, torsades de pointes, maladie rénale, pyo-uretère, cirrhose du foie.
- **Interactions médicamenteuses** : 100 interactions recensées ; les principales sont listées ci-dessous (extrait des 20 premières).
  - **Majeures** : aprépitant, dexaméthasone, clarithromycine, dolasétron, éliglustat.
  - **Modérées** : famotidine, metformine, lopéramide, bisacodyl, budésonide (y compris nasal), canagliflozine, dapagliflozine, empagliflozine, acide picosulfurique, polyéthylène glycol (3350 avec électrolytes), sulfate de sodium.
  - **Mineures** : bupropion, lorcasérine, cimétidine.

Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu être exploitées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique plausible n'a été identifié entre la ranolazine et le NSIAD.
- Les contre-indications liées au graphe de connaissances (QT long, atteinte rénale, cirrhose) et l'absence d'AMM valide en France renforcent la prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (par exemple via l'API DrugBank) afin de vérifier la plausibilité mécanistique.
- Mises en garde et contre-indications de la notice ANSM (téléchargement et analyse du PDF) ; cette lacune bloque le passage à l'étape de criblage de sécurité.
- Indication originale de l'AMM, actuellement non renseignée.
- Données précliniques ou études de mécanisme sur les voies V2/AMPc/aquaporine-2.
- Compatibilité des voies d'administration, à évaluer.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

