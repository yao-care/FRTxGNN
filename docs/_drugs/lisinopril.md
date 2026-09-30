---
layout: default
title: Lisinopril
parent: Prédiction du modèle uniquement (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril : De l'Indication Originale (non renseignée) à l'Infarctus du Myocarde Postéro-inférieur

## Résumé en Une Phrase

Lisinopril est un médicament commercialisé en France (comprimé sécable de 20 mg), mais son indication d'origine n'est pas renseignée dans les données fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infarctus du myocarde postéro-inférieur**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction pour cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données (texte d'indication de l'AMM vide) |
| Nouvelle Indication Prédite | Infarctus du myocarde postéro-inférieur |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des connaissances pharmacologiques générales, le lisinopril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC). Il bloque le système rénine-angiotensine-aldostérone (SRAA), et ce blocage pourrait limiter le remodelage du cœur après un infarctus.

La relation avec l'indication d'origine ne peut pas être établie, car celle-ci n'est pas renseignée dans les données. Le mécanisme reste cependant plausible : le SRAA joue un rôle dans la remodelisation du muscle cardiaque après une nécrose.

**Point d'attention :** les IEC sont généralement utilisés dans l'infarctus aigu du myocarde. Cette prédiction pourrait donc correspondre à un usage déjà existant, et non à un véritable repositionnement. Il faut le vérifier dans le résumé des caractéristiques du produit (RCP) avant tout travail supplémentaire.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62606357 | LISINOPRIL ZENTIVA 20 mg, comprimé sécable (ZENTIVA FRANCE) | Comprimé sécable | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique ni aucune publication ne la soutient.
- Les données de sécurité de l'ANSM manquent, ce qui bloque l'étape de criblage de sécurité.
- L'indication pourrait déjà figurer dans l'usage autorisé des IEC.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice / le RCP de l'ANSM (mises en garde, contre-indications, indications autorisées), pour confirmer si l'infarctus du myocarde est déjà couvert.
- Compléter les données sur le mécanisme d'action (MOA), par exemple via l'API DrugBank.
- Effectuer une recherche bibliographique ciblée sur le lisinopril et l'infarctus du myocarde postéro-inférieur.
- Prioriser, parmi les autres candidats du pack, la **cardiopathie pulmonaire chronique** (niveau L3). Deux publications spécifiques au lisinopril existent pour cette indication (PMID 14524095 et PMID 17047621). Leur schéma d'étude n'est pas déterminable à partir des titres et elles sont anciennes, donc une confirmation par un essai contrôlé reste nécessaire.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

