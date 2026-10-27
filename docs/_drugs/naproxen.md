---
layout: default
title: Naproxen
parent: Prédiction du modèle uniquement (L5)
nav_order: 525
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Naproxen : nouvelle indication prédite, Syndrome de brachydactylie-syndactylie (niveau de preuve L5). Indication d'origine : Données non disponibles dans les AMM"
monitor_inn: "naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Naproxen
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Naproxène : Des Pathologies Inflammatoires et Douloureuses au Syndrome de Brachydactylie-Syndactylie
{: .text-alpha }

## Resume en Une Phrase

Le naproxène est un anti-inflammatoire non stéroïdien (AINS) initialement utilisé pour traiter les affections ostéo-articulaires inflammatoires (polyarthrite rhumatoïde, arthrose, spondylarthrite ankylosante), la goutte, les tendinites et les céphalées ou migraines.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **syndrome de brachydactylie-syndactylie**, une malformation congénitale rare des membres.
Aucun essai clinique et aucune publication ne soutiennent actuellement cette prédiction, qui repose uniquement sur le calcul du modèle.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Données non disponibles dans les AMM (le graphe de connaissances indique notamment bursite, polyarthrite rhumatoïde, spondylarthrite ankylosante, arthrose, goutte, migraine) |
| Nouvelle Indication Predite | Syndrome de brachydactylie-syndactylie |
| Score de Prediction TxGNN | 99,35 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 12 (0 valide, 12 annulées) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, le naproxène est un inhibiteur non sélectif des cyclooxygénases (COX), dont l'efficacité a été établie dans les douleurs et les maladies inflammatoires de l'appareil locomoteur. Ce point n'est toutefois pas documenté dans les données compilées pour ce rapport.

Le syndrome de brachydactylie-syndactylie est une malformation congénitale rare des membres, d'origine vraisemblablement développementale et génétique. Les effets anti-inflammatoires et antalgiques de l'inhibition des COX n'ont pas de pertinence évidente pour sa physiopathologie. Le seul lien concevable, le soulagement symptomatique de douleurs musculo-squelettiques, ne modifierait pas l'évolution de la maladie et n'est pas étayé ici.

Le score élevé du modèle (99,35 %) est donc une prédiction purement computationnelle. En l'état, aucun lien mécanistique n'est soutenu par les données disponibles.

D'autres candidats prédits présentent le même profil (niveau L5, sans essai ni publication) : le syndrome de microphtalmie colobomateuse-dysplasie rhizomélique (99,22 %), la dysplasie acromésomélique de type Hunter-Thompson (99,17 %) et le syndrome de brachyolmie-amélogenèse imparfaite (99,06 %).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Litterature

Aucune littérature associée disponible actuellement.

---

## Informations de Marche en France

Les 12 AMM du naproxène en France sont toutes annulées. Le texte des indications approuvées n'est pas renseigné. Les 5 premières sont listées ci-dessous.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 61990606 | Naproxène sodique Arrow 550 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 62237910 | Alevetabs 220 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 69378155 | Naprosyne 250 mg | Comprimé | Non renseignée (AMM annulée) |
| 67849644 | Apranax 275 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 63738842 | Apranax 550 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, insuffisance hépatique, maladie hépatique, maladie rénale, insuffisance cardiaque congestive, maladie coronarienne, infarctus du myocarde, accident vasculaire cérébral et infarctus cérébral, troubles de la coagulation, épilepsie, diabète et acidocétose diabétique, ostéoporose, obésité, anémie et hémoglobinopathies, maladie de la vésicule biliaire, hyperplasie bénigne de la prostate, abus ou dépendance aux substances.
- **Interactions médicamenteuses** : 309 interactions recensées, parmi lesquelles des interactions de niveau modéré avec l'acide acétylsalicylique, les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), la metformine, la chlorpropamide, les anti-H2 et inhibiteurs de la pompe à protons (famotidine, ranitidine, cimétidine, rabéprazole, dexlansoprazole), l'aprépitant, la mésalazine et le balsalazide.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle, sans essai clinique, sans publication ni lien mécanistique plausible avec une malformation congénitale rare. Le naproxène n'a par ailleurs plus d'AMM valide en France, et les données de sécurité issues de la notice manquent.

**Pour avancer, les elements suivants sont necessaires :**
- Les mises en garde et contre-indications de la notice de l'ANSM (point bloquant pour l'évaluation de la sécurité)
- Les données sur le mécanisme d'action issues de DrugBank
- Une justification biologique reliant l'inhibition des COX à la physiopathologie du syndrome ciblé
- Des données précliniques ou cliniques, ou une revue de la littérature, pour dépasser le niveau L5
- Une évaluation de la compatibilité des voies d'administration et de la situation réglementaire (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

