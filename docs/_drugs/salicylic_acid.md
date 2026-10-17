---
layout: default
title: Salicylic Acid
parent: Prédiction du modèle uniquement (L5)
nav_order: 691
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Salicylic Acid : nouvelle indication prédite, Conjonctivite papillaire (niveau de preuve L5). Indication d'origine : Teigne du pied (tinea pedis), synovite, polyarthrite rhumatoide, acne…"
monitor_inn: "salicylic acid"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia", "spondyloarthropathy, susceptibility to"]
---

# Salicylic Acid
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

# Acide salicylique : Des affections inflammatoires et dermatologiques a la conjonctivite papillaire

## Resume en Une Phrase

L'acide salicylique est un agent keratolytique et anti-inflammatoire, initialement utilise dans des affections dermatologiques (acne, dermatite seborrheique, teignes) et inflammatoires articulaires (polyarthrite rhumatoide, synovite).
Le modele TxGNN predit qu'il pourrait etre efficace pour la **conjonctivite papillaire**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prediction purement computationnelle.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Teigne du pied (tinea pedis), synovite, polyarthrite rhumatoide, acne, dermatite seborrheique, rhinite allergique, rhume (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigne) |
| Nouvelle Indication Predite | Conjonctivite papillaire |
| Score de Prediction TxGNN | 99,88 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulees |
| Nombre d'AMM | 2 (toutes deux annulees) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'acide salicylique possede des proprietes keratolytiques et anti-inflammatoires, vraisemblablement via l'inhibition des enzymes COX, bien que les donnees de bioactivite publiques ne permettent pas de le confirmer.

La conjonctivite papillaire comporte une composante allergique et inflammatoire. L'acide salicylique est deja associe a des affections inflammatoires ou allergiques (rhinite allergique, rhinite vasomotrice, acne, dermatite seborrheique). Un lien mecanistique lache est donc concevable.

Ce lien reste toutefois non verifiable. L'application oculaire d'un agent irritant et keratolytique souleve en outre un reel probleme de securite. Le score eleve du modele refleterait surtout une proximite dans le graphe de connaissances plutot qu'une preuve therapeutique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 65711534 | SALICYLICUM ACIDUM BOIRON, degre de dilution compris entre 3CH et 30CH ou entre 6DH et 60DH (BOIRON) | Comprime, solution, granules, poudre et pommade | Non renseignee (AMM annulee) |
| 64614242 | BILLEROL, comprime a croquer (LEHNING) | Comprime a croquer | Non renseignee (AMM annulee) |

---

## Considerations de Securite

- **Interactions / pharmacologie** : une cible pharmacologique est repertoriee, ASIC3 (canal ionique sensible a l'acide), sans niveau de gravite associe. Aucune interaction medicamenteuse cliniquement caracterisee n'est disponible.
- **Risque specifique a la voie oculaire** : l'acide salicylique est un irritant et un agent keratolytique ; son application sur la surface oculaire est preoccupante.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prediction repose uniquement sur le modele (niveau L5), sans essai ni publication, et les deux AMM francaises sont annulees.
- Le risque d'irritation et de lesion keratolytique oculaire n'est pas evalue, et le mecanisme d'action n'est pas documente.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperation des mises en garde et contre-indications officielles (notice ANSM), indispensable avant tout depistage de securite
- Donnees detaillees sur le mecanisme d'action (DrugBank)
- Recherche systematique d'essais cliniques et de litterature sur la conjonctivite papillaire
- Evaluation de la faisabilite d'une formulation et d'une voie d'administration oculaires, ainsi que des etudes de tolerance oculaire precliniques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

