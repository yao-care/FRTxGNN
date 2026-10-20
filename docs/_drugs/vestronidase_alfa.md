---
layout: default
title: Vestronidase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 811
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Vestronidase Alfa : nouvelle indication prédite, Syndrome de Scheie (niveau de preuve L5). Indication d'origine : Mucopolysaccharidose (type VII)"
monitor_inn: "VESTRONIDASE ALFA"
predicted_indications: ["Scheie syndrome", "lysosomal storage disease with skeletal involvement", "Hurler syndrome", "Sanfilippo syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "ptosis-vocal cord paralysis syndrome", "ptosis-strabismus-ectopic pupils syndrome", "ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome", "congenital Horner syndrome (disease)"]
---

# Vestronidase Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Vestronidase alfa : De la mucopolysaccharidose au syndrome de Scheie

## Resume en Une Phrase

Vestronidase alfa est une enzyme recombinante (beta-glucuronidase humaine) utilisee a l'origine dans le traitement de la mucopolysaccharidose (type VII).
Le modele TxGNN predit qu'elle pourrait etre efficace pour le **syndrome de Scheie**, mais **aucun essai clinique ni aucune publication** ne soutient directement cette indication a ce jour.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Mucopolysaccharidose (type VII) |
| Nouvelle Indication Predite | Syndrome de Scheie |
| Score de Prediction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | AMM annulee uniquement |
| Nombre d'AMM | 1 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les informations compilees. D'apres les connaissances generales, vestronidase alfa est une beta-glucuronidase humaine recombinante qui degrade les glycosaminoglycanes (GAG) tels que le dermatane sulfate, l'heparane sulfate et le chondroitine sulfate. Son efficacite est etablie dans la mucopolysaccharidose de type VII.

Le syndrome de Scheie (forme attenuee de MPS I) est du a un deficit en alpha-L-iduronidase (IDUA), entrainant l'accumulation de dermatane sulfate et d'heparane sulfate. Les substrats communs offrent un argument biologique plausible mais **indirect**.

Cette prediction doit toutefois etre interpretee avec prudence : les enzymes sont differentes, et la beta-glucuronidase ne remplace pas l'etape IDUA manquante. Le score eleve reflete probablement la proximite dans le reseau de connaissances au sein de la famille des MPS plutot qu'un mecanisme direct. Un traitement enzymatique substitutif specifique (laronidase) existe deja.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement pour le syndrome de Scheie.

*A titre indicatif, pour une autre indication predite (syndrome de Hurler, MPS IB) :*

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | En recrutement | 10 | Etude PEARL : traitement enzymatique substitutif prenatal (in utero) dans les maladies lysosomales ; objectif : securite et faisabilite pour la mere et le foetus. Role de vestronidase alfa non confirme ; aucun resultat d'efficacite. |

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement pour le syndrome de Scheie.

*A titre indicatif, publications retrouvees pour le syndrome de Sanfilippo (concernant uniquement la MPS VII, donc preuves indirectes) :*

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [32063397](https://pubmed.ncbi.nlm.nih.gov/32063397/) | 2020 | Cohorte (suivi a long terme) | Mol Genet Metab | Securite et efficacite a long terme de vestronidase alfa 4 mg/kg IV dans la MPS VII, apres une etude de phase 3 randomisee controlee contre placebo (12 sujets) |
| [30467742](https://pubmed.ncbi.nlm.nih.gov/30467742/) | 2019 | Modelisation PK/PD | Clin Pharmacokinet | Optimisation de la dose de vestronidase alfa dans la MPS VII a partir de trois essais |
| [29478819](https://pubmed.ncbi.nlm.nih.gov/29478819/) | 2018 | Methodologie d'etude | Mol Genet Metab | Conception d'etude « Blind Start » pour une maladie ultra-rare (MPS VII) |

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 61759695 (annulee) | MEPSEVII 2 mg/ml, solution a diluer pour perfusion | Solution a diluer pour perfusion | Non renseignee |

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

Aucune interaction medicamenteuse n'a ete retrouvee dans les donnees compilees.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prediction repose uniquement sur le modele (niveau L5) : aucun essai ni publication ne concerne le syndrome de Scheie, et les enzymes impliquees sont differentes. De plus, l'AMM francaise est annulee et une therapie specifique (laronidase) existe deja.
- Parmi les autres predictions, seul le syndrome de Hurler dispose d'un essai de phase 1 (niveau L3, « question de recherche »), sans lien confirme avec vestronidase alfa. Les predictions de maladies oculaires ou neuromusculaires (ptosis, syndrome de Horner congenital, etc.) n'ont aucune base mecanistique et semblent etre des artefacts du reseau.

**Pour avancer, les elements suivants sont necessaires :**
- Donnees detaillees sur le mecanisme d'action (MOA)
- Informations de securite issues de la notice (mises en garde et contre-indications), actuellement manquantes et bloquantes pour toute evaluation de securite
- Etudes precliniques demontrant une activite de la beta-glucuronidase sur les substrats accumules dans le syndrome de Scheie
- Clarification du statut commercial en France (AMM annulee) et de la compatibilite de voie d'administration
- Comparaison avec la laronidase, traitement de reference
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

