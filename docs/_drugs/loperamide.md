---
layout: default
title: Loperamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Loperamide : nouvelle indication prédite, Conjonctivite contagieuse aiguë (niveau de preuve L5). Indication d'origine : Maladies diarrhéiques, dysenterie"
monitor_inn: "loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "Angelucci syndrome"]
---

# Loperamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Lopéramide : De la diarrhée et la dysenterie à la conjonctivite contagieuse aiguë

## Resume en Une Phrase

Le lopéramide est un antidiarrhéique, initialement utilisé pour traiter les maladies diarrhéiques et la dysenterie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **conjonctivite contagieuse aiguë**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Maladies diarrhéiques, dysenterie (d'après le graphe de connaissances, les textes d'indication des AMM n'étant pas renseignés) |
| Nouvelle Indication Predite | Conjonctivite contagieuse aiguë |
| Score de Prediction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques générales, le lopéramide est un agoniste périphérique des récepteurs opioïdes mu, agissant sur les neurones du plexus myentérique de l'intestin pour ralentir le transit et réduire les sécrétions.

Il n'existe **aucun lien mécanistique clair** avec la conjonctivite. Aucune activité oculaire ni anti-infectieuse n'est établie pour le lopéramide. Le score élevé (99,97 %) provient vraisemblablement de la proximité du médicament avec des nœuds de maladies infectieuses dans le graphe de connaissances, et non d'une preuve biologique ou clinique.

Les autres prédictions du modèle vont dans le même sens : plusieurs entités conjonctivales (conjonctivite, conjonctivite pseudomembraneuse, conjonctivite folliculaire chronique, folliculose conjonctivale, conjonctivite parasitaire, syndrome d'Angelucci) présentent des scores identiques ou très proches, signe d'un signal partagé par le graphe plutôt que d'une preuve propre à chaque maladie. La seule piste proche de l'indication d'origine est la dysenterie amibienne, mais elle soulève surtout un problème de sécurité (voir ci-dessous).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement pour la conjonctivite contagieuse aiguë.

À titre d'information, deux publications concernent la deuxième prédiction (dysenterie amibienne) :

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Rapport de cas | Journal of Travel Medicine | Colite amibienne fulminante chez un patient ayant largement utilisé du lopéramide ; l'évolution a pu être aggravée par le ralentissement du transit |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Revue | The American Journal of Medicine | Traitements non liquidiens de la diarrhée aiguë ; la réhydratation orale reste la base, les agents symptomatiques peuvent réduire les symptômes |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 69522794 | IMODIUM 0,2 mg/ml ENFANTS | Solution buvable | Non renseignée |
| 61203061 | IMODIUMCAPS 2 mg | Gélule | Non renseignée |

Les deux AMM sont annulées : aucune présentation n'est actuellement commercialisée sous ces autorisations.

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : maladie hépatique, maladie de la vésicule biliaire, iléus paralytique, occlusion intestinale, myopathie viscérale familiale, dysenterie, maladies diarrhéiques, diarrhées infectieuses, maladies infectieuses intestinales.
- **Interactions médicamenteuses** : 591 interactions répertoriées. Parmi les interactions majeures figurent l'abiratérone, la ranitidine, le fosamprénavir et le gemfibrozil. Les interactions modérées incluent notamment les opioïdes (codéine, dihydrocodéine, tramadol), des antihistaminiques (chlorphéniramine, cétirizine, acrivastine), l'éthanol et le salbutamol.
- **Point d'attention (dysenterie amibienne)** : le ralentissement du transit en cas d'infection invasive peut favoriser une colite fulminante et un mégacôlon toxique.

Les mises en garde détaillées de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Etapes

**Décision : Hold**

**Justification :**
La prédiction pour la conjonctivite contagieuse aiguë repose uniquement sur le score du modèle (niveau L5), sans mécanisme plausible, essai ni publication. Les autres indications prédites sont également non étayées, et la piste la plus proche (dysenterie amibienne) soulève plutôt une alerte de sécurité. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), actuellement bloquante pour le criblage de sécurité
- Compléter les données sur le mécanisme d'action (via DrugBank)
- Démontrer une activité oculaire ou anti-infectieuse par des études précliniques avant toute évaluation clinique
- Évaluer la compatibilité de la voie d'administration (les formes existantes sont orales ; une voie ophtalmique serait nécessaire)
- Clarifier le statut réglementaire du produit en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

