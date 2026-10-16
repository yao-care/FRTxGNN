---
layout: default
title: Tropicamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 793
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tropicamide : nouvelle indication prédite, Syndrome de la queue de cheval (niveau de preuve L5). Indication d'origine : Cycloplégie"
---

# Tropicamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Tropicamide : De la cycloplégie au syndrome de la queue de cheval

## Resume en Une Phrase

Le tropicamide est un antagoniste muscarinique à courte durée d'action, utilisé en ophtalmologie pour obtenir une mydriase et une cycloplégie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la queue de cheval**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Cycloplégie (selon le graphe de connaissances ; le texte des AMM ne précise aucune indication) |
| Nouvelle Indication Predite | Syndrome de la queue de cheval |
| Score de Prediction TxGNN | 99,53 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 4 (toutes annulées) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. Sur la base des informations connues, le tropicamide est un antagoniste des récepteurs muscariniques (les données pharmacologiques indiquent une liaison aux récepteurs M2, M3, M4 et M5). Il est utilisé en collyre pour dilater la pupille lors des examens du fond d'œil.

Le lien hypothétique serait une action antimuscarinique sur l'hyperactivité du détrusor, responsable des troubles vésicaux associés au syndrome de la queue de cheval. Ce raisonnement reste toutefois fragile. Le tropicamide n'existe qu'en formulation ophtalmique, avec une exposition systémique minimale, ce qui rend peu plausible un effet sur la vessie ou le tissu nerveux. De plus, le syndrome de la queue de cheval est avant tout une urgence chirurgicale (décompression) : un antimuscarinique ne pourrait au mieux traiter qu'un symptôme, pas la compression sous-jacente.

Les deux autres prédictions du modèle vont dans le même sens, avec les mêmes limites :
- **Vessie neurogène** (terme signalé comme obsolète dans l'ontologie, à reclasser vers un terme actuel) : score de 99,13 %. Des antimuscariniques établis (oxybutynine, toltérodine) existent déjà et sont bien plus plausibles que le tropicamide.
- **Syndrome de l'intestin irritable** : score de 99,12 %. Des antispasmodiques approuvés (dicyclomine, hyoscyamine) couvrent déjà ce besoin.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 62915154 | MYDRIATICUM 0,5 POUR CENT, collyre (THEA) | Collyre | Non renseignée (AMM annulée) |
| 64029712 | MYDRIATICUM 2 mg/0,4 ml, collyre en récipient unidose (THEA) | Collyre | Non renseignée (AMM annulée) |
| 67423452 | MYDRIASERT, insert ophtalmique (THEA) | Insert ophtalmique | Non renseignée (AMM annulée) |
| 65082408 | MYDRANE 0,2 mg/ml + 3,1 mg/ml + 10 mg/ml, solution injectable (THEA) | Solution injectable | Non renseignée (AMM annulée) |

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : hypertension artérielle, glaucome à angle ouvert, glaucome à angle fermé, hypertension oculaire, diabète et acidocétose diabétique, arrêt cardiaque soudain, maladie de la conduction cardiaque, hyperthyroïdie (dont maladie de Basedow et thyrotoxicose), ischémie myocardique et maladie coronarienne.
- **Interactions médicamenteuses** : 14 interactions recensées, dont 10 avec des médicaments (atropine, chlorure de potassium, vancomycine, simvastatine, prednisolone, famotidine, warfarine, lidocaïne, fluconazole, brimonidine), toutes de niveau de gravité non précisé. Les 4 autres correspondent à des données de liaison aux récepteurs muscariniques M2 à M5.

Les mises en garde et contre-indications officielles de la notice ANSM n'ont pas pu être récupérées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication. La formulation ophtalmique à faible exposition systémique, l'absence d'AMM valide et l'existence d'alternatives antimuscariniques approuvées rendent le repositionnement peu pertinent.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications), une lacune bloquante pour le criblage de sécurité
- Compléter les données sur le mécanisme d'action du tropicamide
- Reclasser la vessie neurogène vers un terme d'ontologie actuel
- Évaluer, en cas de poursuite, la faisabilité d'une formulation systémique et son profil de sécurité
- Comparer avec les antimuscariniques déjà approuvés pour les indications visées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

