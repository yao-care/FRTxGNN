---
layout: default
title: Sotatercept
parent: Prédiction du modèle uniquement (L5)
nav_order: 712
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Sotatercept : nouvelle indication prédite, Leucémie lymphoblastique aiguë (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "SOTATERCEPT"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
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

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Sotatercept : D'une indication originale non documentée à la Leucémie lymphoblastique aiguë
{: .text-alpha }

## Résumé en Une Phrase

Sotatercept est une protéine de fusion du récepteur de l'activine de type IIA (Fc), qui piège les ligands de la famille de l'activine et des GDF/BMP. Les données compilées pour ce rapport ne mentionnent aucune indication originale exploitable.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **leucémie lymphoblastique aiguë**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Leucémie lymphoblastique aiguë |
| Score de Prédiction TxGNN | 0,9978 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le sotatercept est un piège à ligands (activine, GDF/BMP) fondé sur le récepteur de l'activine de type IIA. L'indication originale n'est pas renseignée dans les données d'AMM compilées, ce qui empêche de comparer l'indication d'origine et la nouvelle indication.

La signalisation de la famille activine/TGF-bêta a été évoquée dans la régulation de l'hématopoïèse. Toutefois, aucun lien direct et étayé avec la physiopathologie de la leucémie lymphoblastique aiguë n'est établi dans les données disponibles.

Le score élevé (0,9978) est donc une sortie purement computationnelle. Il doit être considéré comme une hypothèse à vérifier, et non comme une preuve d'efficacité.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61615894 | WINREVAIR 45 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM active) |
| 61402622 | WINREVAIR 60 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM active) |

Titulaire : Merck Sharp & Dohme (Pays-Bas). Les deux autorisations sont au statut « annulée ».

---

## Autres Indications Prédites (pour information)

Toutes les prédictions suivantes sont au niveau L5, sans essai clinique ni publication, avec une décision Hold.

| Rang | Indication Prédite | Score TxGNN | Remarque |
|------|------|------|------|
| 2 | Rétinopathie diabétique non proliférante sévère | 0,9977 | Hypothèse sur le remodelage vasculaire rétinien, non étayée |
| 3 | Rétinopathie diabétique | 0,9972 | Catégorie parente du rang 2, prédictions corrélées |
| 4 | Ostéoporose d'origine médicamenteuse | 0,9965 | Piste la plus plausible : l'activine intervient dans le remodelage osseux, mais aucune donnée humaine fournie |
| 5 | Cataracte diabétique | 0,9949 | Aucun lien mécanistique identifié ; le score provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique |
| 6 | Carcinome mammaire HER2 positif | 0,9943 | Rôle contextuel du TGF-bêta, sans lien spécifique démontré |
| 7 à 10 | Carcinomes urothéliaux (cellules transitionnelles, urètre prostatique, bassinet du rein sarcomatoïde, vessie sarcomatoïde) | 0,9934 à 0,9939 | Groupe de termes voisins dans l'ontologie, non indépendants |

---

## Considérations de Sécurité

Aucune donnée de sécurité exploitable n'est disponible (mises en garde et contre-indications non renseignées, aucune interaction médicamenteuse trouvée).

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle TxGNN (niveau L5), sans essai clinique, sans publication et sans mécanisme d'action documenté.
- Les données de sécurité sont absentes et les deux AMM françaises sont annulées, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice officielle sur le site de l'ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action via DrugBank
- Clarifier l'indication originale et les raisons de l'annulation des AMM
- Rechercher des études précliniques ou cliniques reliant la signalisation activine/GDF/BMP à la leucémie lymphoblastique aiguë
- Évaluer en priorité l'ostéoporose d'origine médicamenteuse, mécanistiquement plus plausible, avant d'engager des ressources sur d'autres indications
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

