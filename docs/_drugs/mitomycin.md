---
layout: default
title: Mitomycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
---

# Mitomycin
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

# Mitomycine : De l'adénocarcinome pancréatique à la tumeur pseudopapillaire solide du pancréas

## Résumé en Une Phrase

La mitomycine est un agent cytotoxique alkylant, initialement utilisé dans le traitement de l'adénocarcinome pancréatique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **carcinome pseudopapillaire solide du pancréas**.
Aucun essai clinique et aucune publication ne soutiennent actuellement cette prédiction précise : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Adénocarcinome pancréatique (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Carcinome pseudopapillaire solide du pancréas |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la mitomycine est un agent alkylant qui crée des pontages dans l'ADN et bloque ainsi la division des cellules tumorales. Son usage dans l'adénocarcinome pancréatique est documenté.

La tumeur pseudopapillaire solide est une tumeur pancréatique rare. Le raisonnement du modèle est une extrapolation à partir d'un cancer du même organe. Cette extrapolation est limitée : cette tumeur est généralement d'évolution lente et se traite le plus souvent par chirurgie, ce qui réduit l'intérêt présumé d'une chimiothérapie cytotoxique.

Les autres prédictions du modèle concernent d'autres tumeurs pancréatiques rares ou des sous-types histologiques : ostéoclastique à cellules géantes, carcinome mixte, adénocarcinome à cellules en bague à chaton, carcinome indifférencié, néoplasme exocrine malin, néoplasmes intracanalaires papillaires et mucineux, cystadénocarcinome à cellules acineuses. Elles ont toutes un score proche (99,82 % à 99,86 %) et reposent sur la même logique d'extrapolation.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune publication n'est associée à la nouvelle indication principale (carcinome pseudopapillaire solide). Pour les autres indications prédites, seules des publications indirectes existent :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Rapport de cas | Pancreatology | Pseudomyxome péritonéal associé à un néoplasme intracanalaire papillaire et mucineux du pancréas, pris en charge par chimioperfusion intrapéritonéale hyperthermique ; ne porte pas sur l'efficacité de la mitomycine |
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Revue | Strahlentherapie und Onkologie | Radiochimiothérapie adjuvante et néoadjuvante dans le carcinome pancréatique canalaire ; non spécifique à la mitomycine |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | Étude clinique (traitement adjuvant, détails non vérifiés) | Nihon Geka Gakkai Zasshi | Tamoxifène ajouté à une immuno-chimiothérapie (tégafur, mitomycine, Krestin, OK-432) après résection d'un carcinome pancréatique ; le rôle propre de la mitomycine n'est pas établi |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Revue | Bulletin du Cancer | Diagnostic et traitement des tumeurs d'origine inconnue ; ancienne et non spécifique |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65355771 | Mitomycine Accord 20 mg (Accord Healthcare France) | Poudre pour solution injectable pour perfusion ou voie intravésicale | Non renseignée (AMM annulée) |
| 68956396 | Mitomycine Accord 10 mg (Accord Healthcare France) | Poudre pour solution injectable pour perfusion ou voie intravésicale | Non renseignée (AMM annulée) |
| 69855350 | Mitomycine Medac 40 mg (Medac, Allemagne) | Poudre pour solution intravésicale | Non renseignée (AMM annulée) |
| 63017696 | Mitomycine Substipharm 20 mg (Substipharm) | Poudre pour solution injectable pour perfusion ou voie intravésicale | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant, antibiotique antitumoral) |
| Risque de Myélosuppression | Élevé (les maladies sanguines figurent parmi les contre-indications du graphe de connaissances : thrombocytopénie, leucopénie, anémie, troubles de la coagulation) |
| Classification d'Émétogénicité | Moyenne (selon la catégorie du médicament) |
| Éléments de Surveillance | NFS avec plaquettes, fonction rénale (risque de syndrome hémolytique et urémique), fonction cardiaque, muqueuses buccales |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, pyo-uretère, thrombocytopénie, troubles de la coagulation, anémie (dont macrocytaire), leucopénie, syndrome hémolytique et urémique (dont forme typique), insuffisance cardiaque (dont congestive), stomatite.
- **Interactions médicamenteuses** : 193 interactions répertoriées. Parmi celles analysées, les plus notables sont de niveau majeur (déférilone, lexidronam de samarium-153) ou modéré (palifermine, chlorure de strontium-89, fostamatinib). La majorité des autres sont de niveau inconnu, et une seule (lévofloxacine) est mineure.

Les mises en garde et contre-indications officielles de la notice n'étant pas disponibles, veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication directe, et toutes les AMM françaises sont annulées. Cette tumeur rare se traite en outre généralement par chirurgie.
- Les données de sécurité officielles et le mécanisme d'action sont manquants, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données de mécanisme d'action via DrugBank
- Rechercher des séries de cas ou des données précliniques sur la mitomycine dans les tumeurs pancréatiques rares
- Clarifier le statut réglementaire actuel (AMM annulées) et la disponibilité réelle du produit en France
- Évaluer la place d'une chimiothérapie par rapport à la chirurgie pour cette tumeur
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

