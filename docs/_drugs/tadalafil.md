---
layout: default
title: Tadalafil
parent: Prédiction du modèle uniquement (L5)
nav_order: 729
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

# Tadalafil : De l'Hyperplasie Benigne de la Prostate a l'Hypertrichose Congenitale de type Ambras

## Resume en Une Phrase

Tadalafil est un inhibiteur de la phosphodiesterase de type 5 (PDE5), initialement utilise pour l'hyperplasie benigne de la prostate, l'hypertension pulmonaire et la dysfonction erectile.
Le modele TxGNN predit qu'il pourrait etre efficace pour l'**hypertrichose universelle congenitale de type Ambras**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Hyperplasie benigne de la prostate (le texte des indications des AMM n'est pas renseigne ; indications issues du graphe de connaissances) |
| Nouvelle Indication Predite | Hypertrichose universelle congenitale de type Ambras |
| Score de Prediction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Toutes les AMM sont annulees |
| Nombre d'AMM | 20 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles. Sur la base des informations connues, tadalafil est un inhibiteur de la PDE5 qui augmente le GMPc et favorise la vasodilatation. Son efficacite a ete etablie dans la dysfonction erectile, l'hyperplasie benigne de la prostate et l'hypertension pulmonaire.

La prediction pour le syndrome d'Ambras est en realite **peu convaincante**. Cette maladie genetique rare, liee a des remaniements du chromosome 8q affectant la regulation de TRPS1, provoque une pilosite excessive. La voie PDE5 n'a aucun role connu dans ce trouble du follicule pilleux. Le score eleve reflete probablement des associations dans le graphe de connaissances avec d'autres hypertrichoses, et non une justification biologique.

Les autres predictions du modele vont dans le meme sens : l'hypertrichose (rang 2), les syndromes malformatifs avec atteinte dentaire ou parodontale, les syndromes avec malformation de Dandy-Walker, les anomalies genetiques isolees de la tige pilaire et la trichomegalie familiale n'ont aucun lien mecanistique etabli. Pour l'hypertrichose, d'autres vasodilatateurs comme le minoxidil la provoquent : tadalafil pourrait donc plutot l'induire que la traiter. Une seule piste indirecte et faible existe, la cardiopathie cyphoscoliotique (rang 7), a cause de l'hypertension pulmonaire associee. Elle reste speculative, car les inhibiteurs de la PDE5 pourraient aggraver l'appariement ventilation-perfusion dans l'hypertension pulmonaire de groupe 3.

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

## Preuves de la Litterature

Aucune litterature associee disponible actuellement pour l'indication principale predite.

A titre d'information, pour une autre prediction (migraine avec aura du tronc cerebral, rang 8), une seule publication existe :

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Rapport de cas | Cephalalgia | Tadalafil associe a une aura migraineuse typique sans cephalee, suggerant un effet declencheur plutot que therapeutique |

## Informations de Marche en France

Les 20 AMM recensees sont toutes annulees. Le texte des indications approuvees n'est pas renseigne. Les cinq premieres sont listees ci-dessous.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 63324624 | TADALAFIL BIOGARAN 10 mg | Comprime pelllicule | Annulee |
| 65834394 | CIALIS 10 mg | Comprime pelllicule | Annulee |
| 64194023 | TADALAFIL ALMUS 20 mg | Comprime pelllicule | Annulee |
| 64615675 | TADALAFIL EG LABO 20 mg | Comprime pelllicule secable | Annulee |
| 65869623 | TADALAFIL ALMUS 5 mg | Comprime pelllicule | Annulee |

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (associations du graphe, et non texte de la notice) : insuffisance hepatique, epilepsie, stenose aortique et maladies de la valve aortique, troubles hypotensifs, troubles de la coagulation, syndrome coronarien aigu, drepanocytose et hemoglobinopathies, accident vasculaire cerebral et infarctus cerebral, infarctus du myocarde, myelome multiple, leucemie, priapisme, maladie de La Peyronie, perte auditive, cardiomyopathie hypertrophique.
- **Interactions medicamenteuses** (100 interactions recensees) : la plupart sont de niveau modere, par exemple aprepitant, dexamethasone, clarithromycine, cimetidine, miconazole, clotrimazole, lorcaserine et les inhibiteurs du SGLT2 (canagliflozine, dapagliflozine, empagliflozine, ertugliflozine). La papaverine est de niveau mineur.

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prediction repose uniquement sur le modele (L5), sans essai ni publication, et sans lien mecanistique plausible entre l'inhibition de la PDE5 et l'hypertrichose d'Ambras. Le statut reglementaire en France (toutes les AMM annulees) complique encore toute perspective de developpement.

**Pour avancer, les elements suivants sont necessaires :**
- Donnees sur le mecanisme d'action issues de DrugBank
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de securite)
- Donnees precliniques demontrant un role de la voie PDE5/GMPc dans le follicule pileux
- Reevaluation d'autres candidats plus plausibles, car la direction de la prediction pour l'hypertrichose est discutable
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

