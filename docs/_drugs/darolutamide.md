---
layout: default
title: Darolutamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 216
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Darolutamide : nouvelle indication prédite, Hypercholestérolémie familiale homozygote (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "DAROLUTAMIDE"
predicted_indications: ["homozygous familial hypercholesterolemia", "multiple endocrine neoplasia", "HIV infectious disease"]
---

# Darolutamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Darolutamide : Du Cancer de la Prostate à l'Hypercholestérolémie Familiale Homozygote
{: .text-alpha }

## Résumé en Une Phrase

Darolutamide est un antagoniste non stéroïdien du récepteur des androgènes. L'indication d'origine n'est pas renseignée dans les données compilées pour ce rapport pour l'AMM française.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypercholestérolémie familiale homozygote**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Hypercholestérolémie familiale homozygote |
| Score de Prédiction TxGNN | 0,9911 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, darolutamide est un antagoniste non stéroïdien du récepteur des androgènes, utilisé dans les cancers de la prostate hormonodépendants. Son indication d'origine n'a toutefois pas pu être confirmée à partir du texte d'AMM disponible.

Aucun lien mécanistique plausible n'apparaît entre l'antagonisme du récepteur des androgènes et le dysfonctionnement du récepteur du LDL, cause de l'hypercholestérolémie familiale homozygote. Le score élevé (0,9911) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

La similarité avec l'indication d'origine n'a pas encore été évaluée. En l'absence d'essai ou de publication, cette prédiction doit être considérée comme hautement spéculative.

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
| 62384935 | NUBEQA 300 mg, comprimé pelliculé (BAYER AG, Allemagne) | Comprimé pelliculé | Non renseignée (AMM active) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (hormonothérapie, antagoniste du récepteur des androgènes) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

**Interactions Médicamenteuses** : 100 interactions ont été recensées. Parmi les principales :
- **Majeures** : dexaméthasone, éluxadoline, rosuvastatine
- **Modérées** : clarithromycine, empagliflozine, glibenclamide, répaglinide, rifaximine, simvastatine, sulfasalazine, cobicistat, déférasirox, eltrombopag, lusutrombopag, phénylbutyrate de glycérol, métréleptine, troglitazone
- **Mineures** : aprépitant, cimétidine, miconazole

Pour les autres informations de sécurité (mises en garde, contre-indications), veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et aucun lien mécanistique plausible n'est identifié. De plus, la seule AMM française est annulée et les données de sécurité de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), actuellement bloquante pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Justification mécanistique plausible entre le récepteur des androgènes et le métabolisme du LDL, ou données précliniques
- Confirmation de l'indication d'origine et du statut réglementaire

---

## Autres Indications Prédites (pour information)

| Indication | Score TxGNN | Niveau de Preuve | Décision | Commentaire |
|------|------|------|------|------|
| Néoplasie endocrinienne multiple | 0,9906 | L5 | Hold | Deux essais retrouvés (NCT07795177, NCT03878524), en réalité centrés sur le cancer de la prostate et la médecine de précision en oncologie, associés par une terminologie large. Aucune donnée spécifique à cette indication. |
| Infection par le VIH | 0,9904 | L5 | Hold | Prédiction purement computationnelle, sans lien mécanistique direct. Les nombreuses interactions médicamenteuses (CYP3A4/P-gp) poseraient un problème pratique avec les antirétroviraux. |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

