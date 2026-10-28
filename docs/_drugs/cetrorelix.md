---
layout: default
title: Cetrorelix
parent: Prédiction du modèle uniquement (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Cetrorelix : nouvelle indication prédite, Hypertrichose (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM (selon les données pharmacologi…"
monitor_inn: "cetrorelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
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

## Cétrorélix : De l'inhibition des pics prématurés de LH à l'hypertrichose
{: .text-alpha }

## Resume en Une Phrase

Le cétrorélix est un antagoniste du récepteur de la GnRH, utilisé dans la stimulation ovarienne contrôlée pour empêcher les pics prématurés de LH lors des traitements de fertilité.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertrichose**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.
La prédiction repose uniquement sur le modèle (niveau de preuve L5).

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (selon les données pharmacologiques : prévention des pics prématurés de LH lors de la stimulation ovarienne contrôlée) |
| Nouvelle Indication Predite | Hypertrichose |
| Score de Prediction TxGNN | 0,9998 |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base consultée. D'après les informations pharmacologiques connues, le cétrorélix est un peptide qui bloque le récepteur de la GnRH (gène GNRHR) au niveau hypophysaire. Il réduit ainsi la sécrétion de LH et de FSH, et par conséquent la production gonadique d'androgènes et d'œstrogènes.

Le lien avec l'hypertrichose reste spéculatif. Une baisse de la signalisation androgénique pourrait théoriquement influencer la pousse des poils sensibles aux androgènes. Or, la plupart des formes d'hypertrichose (congénitale, médicamenteuse, génétique) ne dépendent pas des androgènes. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Les autres prédictions du modèle appellent le même constat, car la plupart n'ont pas de justification mécanistique plausible :
- **Hypertrichose universelle congénitale de type Ambras**, **syndromes malformatifs dentaires/parodontaux**, **syndrome avec malformation de Dandy-Walker**, **anomalie génétique isolée de la tige pilaire**, **syndrome de circulation fœtale persistante**, **trichomégalie familiale isolée** : ces affections sont génétiques ou développementales, sans lien plausible avec l'antagonisme de la GnRH.
- **Syndrome d'excès d'aromatase** : le défaut primaire est l'aromatisation périphérique, pour laquelle les inhibiteurs de l'aromatase constituent le traitement mécanistiquement direct.
- **Puberté précoce centrale** et **puberté précoce familiale limitée au sexe masculin** : ce sont les prédictions les plus plausibles biologiquement (niveau L4, « question de recherche »). Pour la puberté précoce centrale, le blocage du récepteur de la GnRH est cohérent, mais le traitement de référence repose sur les agonistes. Pour la forme familiale masculine (mutations activatrices de LHCGR), un antagoniste de la GnRH ne bloquerait pas l'activité constitutive du récepteur. Dans les deux cas, la demi-vie courte, les administrations fréquentes, le manque de données pédiatriques et l'annulation des AMM limitent l'intérêt pratique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Litterature

Aucune littérature associée disponible actuellement.

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee | Statut |
|---------|------|------|-----------|------|
| 65669398 | CEZIBOE 0,25 mg, solution injectable en seringue pré-remplie | Solution injectable | Non renseignée | Active |
| 60650426 | CETROTIDE 0,25 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée | Active |

---

## Considerations de Securite

**Interactions Medicamenteuses :** la requête d'interactions est terminée. Elle ne signale aucune interaction médicamenteuse cliniquement documentée. Elle retourne uniquement l'information pharmacologique de la cible, le récepteur de la GnRH₁ (GNRHR), sans niveau de gravité.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations de sécurité.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Toutes les prédictions reposent uniquement sur le modèle (L5), ou sur un raisonnement mécanistique indirect (L4 pour les deux formes de puberté précoce), sans essai ni publication. Le mécanisme est faible ou absent pour l'hypertrichose, et les AMM françaises sont toutes annulées.
- Les données de sécurité issues de la notice manquent, ce qui bloque le passage au criblage de sécurité.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer et analyser la notice (mises en garde, contre-indications) sur le site de l'ANSM.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Réaliser une revue de la littérature et des registres d'essais pour l'hypertrichose, et surtout pour la puberté précoce centrale, seule piste à étudier comme question de recherche.
- Évaluer la faisabilité pratique (demi-vie courte, voie injectable, population pédiatrique, statut commercial) avant tout développement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

