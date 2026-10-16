---
layout: default
title: Eculizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eculizumab : nouvelle indication prédite, Hematopoiese cyclique (niveau de preuve L5). Indication d'origine : Hemoglobinurie paroxystique nocturne…"
monitor_inn: "eculizumab"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
---

# Eculizumab
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

# Eculizumab : De l'Hemoglobinurie Paroxystique Nocturne a l'Hematopoiese Cyclique

## Resume en Une Phrase

Eculizumab est un inhibiteur du complement (C5), initialement utilise pour le traitement de l'hemoglobinurie paroxystique nocturne et de la neuromyelite optique.
Le modele TxGNN predit qu'il pourrait etre efficace pour l'**hematopoiese cyclique** (neutropenie cyclique), avec un score eleve mais **aucun essai clinique** et **aucune publication** directement en faveur de cette indication.
Il s'agit d'une prediction purement computationnelle (niveau de preuve L5).

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Hemoglobinurie paroxystique nocturne, neuromyelite optique (les textes d'indication des AMM ne sont pas renseignes) |
| Nouvelle Indication Predite | Hematopoiese cyclique |
| Score de Prediction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulees |
| Nombre d'AMM | 3 (toutes annulees) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les donnees compilees pour ce rapport. Sur la base des informations connues, eculizumab est un anticorps monoclonal inhibiteur de la proteine C5 du complement. Son efficacite dans l'hemoglobinurie paroxystique nocturne, maladie ou l'activation incontrôlee du complement provoque une hemolyse, est etablie.

La relation avec la nouvelle indication est **faible**. L'hematopoiese cyclique (neutropenie cyclique, liee a ELANE) est un trouble de la production des neutrophiles, et non une maladie mediee par le complement. Aucun lien mecanistique n'est etabli dans les donnees disponibles : le score eleve du modele provient uniquement de la structure du graphe de connaissances.

Les autres predictions du meme classement (neutropenies congenitales severes, neutropenie idiopathique de l'adulte, deficit en p14, etc.) presentent la meme limite : aucun role connu du complement terminal dans ces pathologies.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement pour l'hematopoiese cyclique.

Remarque : des publications ont ete retrouvees pour d'autres predictions du modele (par exemple le syndrome neutropenie congenitale-myelofibrose-nephromegalie), mais elles portent surtout sur les indications deja etablies d'eculizumab (hemoglobinurie paroxystique nocturne, microangiopathies thrombotiques, syndrome hemolytique et uremique atypique, myasthenie, deficit en CD59) et ne documentent pas un traitement de ces maladies par eculizumab.

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee | Statut |
|---------|------|------|-----------|------|
| 61969188 | SOLIRIS 300 mg | Solution a diluer pour perfusion | Non renseignee | Annulee |
| 67665594 | EPYSQLI 300 mg | Solution a diluer pour perfusion | Non renseignee | Annulee |
| 63275561 | BEKEMV 300 mg | Solution a diluer pour perfusion | Non renseignee | Annulee |

---

## Considerations de Securite

- **Interactions Medicamenteuses** : 4 interactions de niveau mineur ont ete identifiees, toutes avec des immunoglobulines G humaines (voies intraveineuse, sous-cutanee, intramusculaire, et intraveineuse/sous-cutanee).

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prediction repose uniquement sur le modele (L5), sans essai ni publication, et sans lien mecanistique plausible avec une inhibition de C5. De plus, les trois AMM francaises sont annulees.

**Pour avancer, les elements suivants sont necessaires :**
- Donnees detaillees sur le mecanisme d'action (MOA)
- Informations de securite issues de la notice (mises en garde et contre-indications) : lacune bloquante pour tout depistage de securite
- Hypothese physiopathologique demontrant un role du complement dans l'hematopoiese cyclique
- Etudes precliniques ou series de cas soutenant l'usage d'eculizumab dans cette indication
- Clarification du statut reglementaire actuel en France et des textes d'indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

