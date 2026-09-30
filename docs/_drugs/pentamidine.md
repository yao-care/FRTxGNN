---
layout: default
title: Pentamidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 234
evidence_level: L5
indication_count: 5
---

# Pentamidine
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

# Pentamidine : De l'Anti-infectieux à la Kératoconjonctivite Épithéliale Ponctuée

## Résumé en Une Phrase

La pentamidine est un anti-infectieux (activité antiprotozoaire et antifongique) commercialisé en France sous forme de poudre pour aérosol et pour usage parentéral (Pentacarinat 300 mg).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **kératoconjonctivite épithéliale ponctuée**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Kératoconjonctivite épithéliale ponctuée |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la pentamidine est un anti-infectieux de la famille des diamidines aromatiques. Son activité antiprotozoaire et antifongique est connue, et son usage ophtalmologique n'a pas été démontré.

Le seul lien indirect est le suivant : des diamidines aromatiques apparentées (par exemple la propamidine) s'utilisent en collyre contre la kératite à *Acanthamoeba*. Cela suggère une possible activité antimicrobienne oculaire. Ce raisonnement reste une hypothèse. Aucun mécanisme direct n'est établi pour la kératoconjonctivite épithéliale ponctuée.

Le score élevé (0,997) provient uniquement du graphe de connaissances. De plus, la pentamidine par voie générale est notablement toxique (néphrotoxicité, dysglycémie, allongement de l'intervalle QT). Il n'existe ni formulation oculaire ni donnée de sécurité oculaire.

Les autres prédictions du modèle ne sont pas mieux étayées, toutes au niveau L5 avec la recommandation Hold :
- **Kératopathie neurotrophique** : aucun rationnel mécanistique plausible.
- **Kératite d'exposition** : probable artéfact de proximité dans le graphe.
- **Maladie animale non humaine** : catégorie d'ontologie non spécifique, à exclure de la priorisation.
- **Analbuminémie congénitale** : aucun mécanisme connu pour restaurer la synthèse d'albumine.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61423246 | PENTACARINAT 300 mg, poudre pour aérosol et pour usage parentéral | Poudre pour aérosol et pour usage parentéral | TAMRISA ACCESS (FRANCE) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (L5), sans essai clinique, sans publication et sans mécanisme établi. Le profil de toxicité systémique de la pentamidine et l'absence de formulation oculaire s'ajoutent à ces lacunes. Le dossier ne peut pas passer au criblage de sécurité tant que les données de la notice ANSM manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (télécharger et analyser le PDF de la notice)
- Données sur le mécanisme d'action (interroger l'API DrugBank)
- Texte de l'indication approuvée de l'AMM 61423246
- Revue de la littérature sur les diamidines en ophtalmologie (propamidine, kératite à *Acanthamoeba*)
- Évaluation de la faisabilité d'une voie d'administration oculaire et de sa sécurité locale
- Données précliniques sur l'activité de la pentamidine dans les atteintes de la surface oculaire
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

