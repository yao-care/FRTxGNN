---
layout: default
title: Lomitapide
parent: Prédiction du modèle uniquement (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lomitapide : nouvelle indication prédite, Macrothrombocytopénie avec insuffisance mitrale (niveau de preuve L5). Indication d'origine : Hypercholestérolémie familiale homozygote"
monitor_inn: "lomitapide"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "dense granule disease", "transient neonatal thrombocytopenia", "thrombocytopenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "hyperlipoproteinemia", "platelet storage pool deficiency"]
---

# Lomitapide
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

## Lomitapide : De l'hypercholestérolémie familiale homozygote à la macrothrombocytopénie avec insuffisance mitrale
{: .text-alpha }

## Résumé en Une Phrase

Le lomitapide est un inhibiteur de la protéine de transfert des triglycérides microsomiaux (MTP), initialement utilisé pour traiter l'hypercholestérolémie familiale homozygote.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **macrothrombocytopénie avec insuffisance mitrale**, avec un score très élevé (99,92 %).
Cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypercholestérolémie familiale homozygote (les textes d'indication des AMM ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Macrothrombocytopénie avec insuffisance mitrale |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le lomitapide inhibe la MTP. Il réduit ainsi l'assemblage et la sécrétion des lipoprotéines contenant l'apoB (VLDL, chylomicrons), ce qui abaisse le LDL-cholestérol. Son efficacité est établie dans l'hypercholestérolémie familiale homozygote.

**Aucun lien mécanistique plausible** n'a pu être établi entre l'inhibition de la MTP et la physiopathologie plaquettaire ou valvulaire de la maladie prédite. Les autres prédictions de haut rang pour ce médicament appartiennent au même groupe de troubles plaquettaires : thrombopénie héréditaire, maladie des granules denses, thrombasthénie de Glanzmann, déficit du pool de stockage plaquettaire, etc. Ce regroupement ressemble davantage à un artefact de l'embedding du graphe qu'à un signal biologiquement fondé.

La similarité avec l'indication originale n'a pas pu être évaluée. La prédiction doit donc être considérée comme une hypothèse purement computationnelle.

**Note sur une autre prédiction du même médicament :** l'**hyperlipoprotéinémie** (rang 9, score 99,74 %) est soutenue par plusieurs essais de phase 3 et des revues. Il s'agit toutefois essentiellement de l'indication d'origine (hypercholestérolémie familiale homozygote), et non d'un véritable repositionnement. Les essais de phase 3 y concernent des populations atteintes d'hypercholestérolémie sévère, et non l'hyperlipoprotéinémie au sens large.

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
| 69243759 | LOJUXTA 10 mg, gélule (CHIESI FARMACEUTICI) | Gélule | Non précisée (AMM annulée) |
| 69565055 | LOJUXTA 20 mg, gélule (CHIESI FARMACEUTICI) | Gélule | Non précisée (AMM annulée) |
| 69851117 | LOJUXTA 5 mg, gélule (CHIESI FARMACEUTICI) | Gélule | Non précisée (AMM annulée) |

Les trois autorisations sont annulées et aucune n'est valide. La disponibilité réelle du produit en France doit donc être vérifiée.

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 206 interactions sont recensées, ce qui représente une charge d'interactions élevée. Parmi les principales :
  - **Majeures** : acarbose, doxycycline, minocycline, tétracycline, pioglitazone, bupropion, aprépitant, clarithromycine, acide chénodésoxycholique, naltrexone, oxandrolone, oxymétholone.
  - **Modérées** : ranitidine, cimétidine, lopéramide, budésonide (y compris nasal), saxagliptine, linagliptine, éliglustat.
- **Points d'attention connus pour la classe** : toxicité hépatique (accumulation de graisse hépatique, élévation des transaminases), effets indésirables digestifs et interactions avec les inhibiteurs du CYP3A4. Ces éléments sont à confirmer dans la notice.

Les mises en garde et contre-indications détaillées de l'ANSM ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 : elle repose uniquement sur le score du modèle, sans essai clinique, sans publication et sans lien mécanistique plausible. Le score élevé ne suffit pas à justifier une poursuite.
- Le profil de sécurité est contraignant (toxicité hépatique, nombreuses interactions) et les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de mécanisme d'action (MOA) du médicament, pour analyser un éventuel lien avec la pathologie plaquettaire ou valvulaire.
- Les mises en garde et contre-indications de la notice ANSM, nécessaires pour tout dépistage de sécurité.
- Des preuves précliniques ou cliniques reliant l'inhibition de la MTP à la macrothrombocytopénie, ou le choix d'une autre indication prédite mieux étayée.
- La confirmation de la disponibilité réelle du produit en France, compte tenu de l'annulation des AMM.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

