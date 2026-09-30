---
layout: default
title: Sotatercept
parent: Prédiction du modèle uniquement (L5)
nav_order: 288
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept : De l'hypertension artérielle pulmonaire à la leucémie lymphoblastique aiguë

## Résumé en Une Phrase

Sotatercept est commercialisé en France sous le nom WINREVAIR. Les données fournies ne précisent pas son indication d'origine ; selon les connaissances générales, il s'agit de l'hypertension artérielle pulmonaire (HTAP), à vérifier auprès de l'ANSM.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **leucémie lymphoblastique aiguë**, avec un score élevé (99,78 %).
Cette prédiction repose uniquement sur le modèle : **0 essai clinique** et **0 publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données (HTAP selon les connaissances générales, à vérifier) |
| Nouvelle Indication Prédite | Leucémie lymphoblastique aiguë |
| Score de Prédiction TxGNN | 99,78 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données. D'après l'analyse de l'Evidence Pack, le sotatercept est un piège à ligands de type protéine de fusion Fc du récepteur de l'activine de type IIA (ActRIIA-Fc). Il capte l'activine, les GDF8/11 et certaines BMP.

**Pour la leucémie lymphoblastique aiguë, il n'existe pas de lien mécanistique clair.** Aucun rôle établi de cet axe de signalisation dans la biologie de cette leucémie n'a été identifié. Le score élevé est une prédiction issue du graphe de connaissances, pas une preuve. De plus, le sotatercept augmente l'hémoglobine et les plaquettes, ce qui complique tout usage dans une hémopathie maligne.

Les autres prédictions du modèle sont de même nature (niveau L5, sans essai ni publication) :
- **Rétinopathie diabétique** (sévère non proliférante et forme générale) et **cataracte diabétique** : lien spéculatif ou absent. Le sotatercept a des effets vasculaires connus (télangiectasies, saignements), ce qui soulève des questions de sécurité oculaire.
- **Carcinomes urothéliaux et cancer du sein HER2 positif** : seul un lien générique et dépendant du contexte avec la signalisation activine/TGF-bêta existe. Les scores quasi identiques entre sous-types urothéliaux suggèrent des prédictions corrélées plutôt que des signaux indépendants.
- **Ostéoporose médicamenteuse** : c'est la prédiction la plus cohérente sur le plan biologique. La signalisation de l'activine régule le remodelage osseux, et des protéines de fusion activin receptor-Fc ont été explorées pour leurs effets sur la densité minérale osseuse. Elle est classée « Research Question ». Une revue ciblée de la littérature sur les données osseuses des ActRIIA-Fc serait la première étape.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61615894 | WINREVAIR 45 mg (MERCK SHARP & DOHME, Pays-Bas) | Poudre et solvant pour solution injectable | Non renseignée dans les données |
| 61402622 | WINREVAIR 60 mg (MERCK SHARP & DOHME, Pays-Bas) | Poudre et solvant pour solution injectable | Non renseignée dans les données |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la leucémie lymphoblastique aiguë repose uniquement sur le modèle (L5), sans essai, sans publication et sans lien mécanistique identifié. Les effets du sotatercept sur l'hémoglobine et les plaquettes compliquent en outre son usage dans une hémopathie maligne.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), étape bloquante pour le criblage de sécurité
- Confirmer l'indication d'origine et le mécanisme d'action détaillé (DrugBank)
- Mener une revue ciblée de la littérature, en priorité sur l'ostéoporose médicamenteuse (données osseuses des ActRIIA-Fc), seule piste mécanistiquement cohérente
- Rechercher d'éventuels essais ou données précliniques pour chaque indication prédite avant toute réévaluation

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

