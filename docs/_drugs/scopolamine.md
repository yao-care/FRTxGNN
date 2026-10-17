---
layout: default
title: Scopolamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 693
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Scopolamine : nouvelle indication prédite, Syndrome de la queue de cheval (niveau de preuve L5). Indication d'origine : Maladie ulcéreuse gastroduodénale"
monitor_inn: "SCOPOLAMINE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "papillary conjunctivitis", "atopic conjunctivitis", "rosacea conjunctivitis", "vernal conjunctivitis"]
---

# Scopolamine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Scopolamine : De la maladie ulcéreuse gastroduodénale au syndrome de la queue de cheval

## Résumé en Une Phrase

La scopolamine est un anticholinergique (antagoniste muscarinique) utilisé à l'origine, entre autres, dans la maladie ulcéreuse gastroduodénale, le mal des transports et le syndrome de l'intestin irritable.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de la queue de cheval**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie ulcéreuse gastroduodénale (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la scopolamine est un antagoniste muscarinique aux effets antispasmodiques et anticholinergiques sur les muscles lisses. Son efficacité est reconnue dans plusieurs indications (mal des transports, troubles digestifs spastiques, uvéite, cycloplégie).

Le lien plausible avec le syndrome de la queue de cheval concerne uniquement la prise en charge du dysfonctionnement vésical secondaire, par réduction de l'hyperactivité du détrusor. La scopolamine ne traiterait en aucun cas la cause sous-jacente (la compression nerveuse), qui nécessite une décompression chirurgicale.

Le score TxGNN est très élevé (0,9999), mais il repose uniquement sur la proximité dans le graphe de connaissances. Aucune donnée clinique ou bibliographique ne le confirme.

### Autres indications prédites (à titre indicatif)

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|------|
| 2 | Vessie neurogène (entrée obsolète dans l'ontologie) | 99,98 % | L5 | Mécanisme plausible (antimuscarinique), mais effets centraux de la scopolamine ; des agents plus sélectifs existent |
| 3 | Conjonctivite papillaire | 99,98 % | L5 | Pas de mécanisme clair contre les facteurs allergiques ou mécaniques |
| 4 | Conjonctivite atopique | 99,80 % | L5 | Bénéfice probablement faible, risque d'aggravation de la sécheresse oculaire |
| 5 | Conjonctivite de la rosacée | 99,40 % | L5 | Lien faible, potentiellement contre-productif (réduction de la sécrétion lacrymale) |
| 6 | Conjonctivite vernale | 99,08 % | L5 | La seule utilité concevable serait un confort par cycloplégie |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63958849 | SCOPODERM TTS 1 mg/72 heures, dispositif transdermique (BAXTER) | Dispositif | Non renseignée (AMM annulée) |
| 68731823 | SCOPODERM TTS 1 mg/72 heures, dispositif transdermique (DIFARMED, Espagne) | Dispositif | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, insuffisance hépatique et maladie du foie, épilepsie, bronchopneumopathie chronique obstructive, ulcère gastrique, troubles anxieux et névrotiques, porphyries, maladie rénale, pancréatite, maladie de la vésicule biliaire, thrombocytopénie, glaucome à angle ouvert, troubles psychotiques et schizophréniformes, diabète et acidocétose diabétique, hypertrophie bénigne de la prostate, neutropénie et agranulocytose, coma hépatique.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales, de niveau modéré : toxine botulique de type A, fentanyl, phényléphrine, acébutolol, codéine, dihydrocodéine, tramadol, alfentanil, éthanol, amitriptyline, amantadine, hyoscyamine, lopéramide, chlorphéniramine, acrivastine, aclidinium, acétylcholine et phényltoloxamine. Deux interactions mineures : paracétamol et hydrochlorothiazide. Beaucoup relèvent d'effets anticholinergiques ou sédatifs additifs.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Le mécanisme ne couvrirait au mieux qu'un traitement symptomatique des troubles vésicaux, pas la maladie elle-même.
- Les AMM françaises sont toutes annulées, et les données de sécurité issues de la notice manquent, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice officielle (ANSM) pour les mises en garde et contre-indications
- Données détaillées sur le mécanisme d'action (DrugBank)
- Revue de la littérature sur les antimuscariniques dans la dysfonction vésicale neurogène, et comparaison avec des agents périphériquement sélectifs
- Évaluation de la compatibilité de la voie d'administration (seule la forme transdermique a été commercialisée en France)
- Évaluation du profil bénéfice/risque, notamment les effets centraux (sédation, confusion) chez les patients concernés
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

