---
layout: default
title: Topiramate
parent: Prédiction du modèle uniquement (L5)
nav_order: 773
evidence_level: L5
indication_count: 9
---

# Topiramate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Topiramate : De l'épilepsie à la tumeur du nerf trijumeau (prédiction du modèle)

## Résumé en Une Phrase

Le topiramate est un médicament antiépileptique à large spectre, initialement utilisé pour traiter l'épilepsie généralisée tonico-clonique, l'épilepsie partielle et le syndrome de Lennox-Gastaut.
Le modèle TxGNN prédit en tête de classement le **néoplasme du nerf trijumeau** (score très élevé, mais fondé uniquement sur le graphe de connaissances), sans **aucun essai clinique** ni **aucune publication** à l'appui pour cette indication.
Les autres prédictions du classement sont surtout des **épilepsies réflexes** (épilepsie visuelle, audiogène, de lecture, etc.), proches de l'indication d'origine, avec des preuves indirectes ou précliniques.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Épilepsie avec crises généralisées tonico-cloniques, épilepsie partielle, syndrome de Lennox-Gastaut (données du graphe de connaissances ; le texte des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Néoplasme du nerf trijumeau |
| Score de Prédiction TxGNN | 99,70 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations uniquement annulées (aucune AMM valide) |
| Nombre d'AMM | 17 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le topiramate est un antiépileptique à large spectre dont les actions décrites comprennent le blocage des canaux sodiques, le renforcement de la transmission GABA-A, l'antagonisme des récepteurs AMPA/kaïnate et une inhibition faible de l'anhydrase carbonique.

Pour la prédiction principale (néoplasme du nerf trijumeau), **aucun fondement mécanistique établi** n'existe : le topiramate n'a pas d'activité antitumorale reconnue. Le score élevé (99,70 %) provient uniquement du graphe de connaissances. Tout lien éventuel resterait spéculatif et relèverait plutôt du contrôle symptomatique (douleur neuropathique ou crises associées à la tumeur) que d'un effet sur la tumeur elle-même.

Les autres prédictions (épilepsie visuelle, épilepsie de la lecture, crises audiogènes, etc.) sont mécanistiquement plus plausibles, car ce sont des épilepsies réflexes relevant du spectre des épilepsies déjà traitées. Elles chevauchent toutefois les indications existantes et ne représentent pas un véritable signal de repositionnement.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la prédiction principale (néoplasme du nerf trijumeau).

À titre de contexte, pour les prédictions suivantes du classement, la littérature récupérée est surtout générale (revues sur les antiépileptiques) ou préclinique. Exemples les plus pertinents, rattachés aux crises audiogènes (rang 4) et aux crises de pensée (rang 8) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24570033](https://pubmed.ncbi.nlm.nih.gov/24570033/) | 2014 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Topiramate en traitement additif de l'épilepsie partielle pharmacorésistante |
| [31642054](https://pubmed.ncbi.nlm.nih.gov/31642054/) | 2019 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Topiramate en traitement additif de l'épilepsie focale pharmacorésistante |
| [10666508](https://pubmed.ncbi.nlm.nih.gov/10666508/) | 2000 | Préclinique (animal) | Eur J Pharmacol | Le topiramate antagonise les crises audiogènes chez la souris DBA/2 et potentialise d'autres anticonvulsivants |
| [12581224](https://pubmed.ncbi.nlm.nih.gov/12581224/) | 2003 | Préclinique (animal) | Epilepsia | Effets du topiramate dans deux modèles génétiques d'épilepsie généralisée (GAERS, rat audiogène Wistar AS) |
| [39854828](https://pubmed.ncbi.nlm.nih.gov/39854828/) | 2025 | Revue | Epilepsy Behav | Revue des antiépileptiques dans le syndrome de Lennox-Gastaut, dont le topiramate |

Ces publications soutiennent l'efficacité générale du topiramate dans l'épilepsie, mais n'évaluent pas directement les épilepsies réflexes rares, ni a fortiori le néoplasme du nerf trijumeau.

---

## Informations de Marché en France

Les 17 AMM recensées sont toutes annulées ; le texte d'indication approuvée n'est pas renseigné. Principales AMM (5 sur 17) :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68906660 | TOPIRAMATE VIATRIS 200 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 64696702 | TOPIRAMATE ARROW LAB 100 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 61913385 | EPITOMAX 100 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 68987922 | EPITOMAX 25 mg | Gélule | Non renseignée (AMM annulée) |
| 63478939 | TOPIRAMATE BGR 50 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : trouble anxieux, trouble névrotique, trouble dysthymique, maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, maladie diarrhéique, hypertension oculaire, néphrolithiase (dont la susceptibilité liée à SLC26A1), néphropathie uratique aiguë, acidose (dont acidose métabolique), trouble amnésique, amnésie rétrograde.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Majeures : metformine, hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, mépenzolate, méthscopolamine, propanthéline, trospium (notamment les anticholinergiques).
  - Modérées : pioglitazone, morphine, dronabinol, phentermine, métoclopramide, acide phénylbutyrique, nabilone, glibenclamide, phénylbutyrate de glycérol.
- La littérature récupérée signale par ailleurs des effets indésirables psychiatriques et des complications en cas d'utilisation pendant la grossesse.

Les mises en garde officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de securité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (néoplasme du nerf trijumeau) repose uniquement sur un score de graphe, sans essai, sans publication ni logique mécanistique antitumorale ; le niveau de preuve est L5.
- Aucune AMM n'est actuellement valide en France, et les données de sécurité officielles manquent (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Pour le néoplasme du nerf trijumeau : définir une hypothèse biologique précise (effet antitumoral ou simple contrôle symptomatique) et rechercher des données précliniques ou cliniques.
- Les épilepsies réflexes (épilepsie visuelle, audiogène, de lecture, crises de pensée) pourraient être étudiées comme questions de recherche, mais elles recoupent les indications existantes ; clarifier le statut réglementaire du topiramate en France.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

