---
layout: default
title: Ibuprofen
parent: Prédiction du modèle uniquement (L5)
nav_order: 385
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Ibuprofen : nouvelle indication prédite, Dysplasie acromésomélique de type Hunter-Thompson (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, céphalées, arthrose, arthropathies…"
monitor_inn: "ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Ibuprofène : De l'arthrose et de la polyarthrite rhumatoïde à la dysplasie acromésomélique de type Hunter-Thompson

## Résumé en Une Phrase

L'ibuprofène est un anti-inflammatoire non stéroïdien (AINS), initialement utilisé pour traiter la polyarthrite rhumatoïde, l'arthrose, les céphalées et d'autres atteintes articulaires.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dysplasie acromésomélique de type Hunter-Thompson**, une maladie osseuse génétique rare.
**Aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, céphalées, arthrose, arthropathies, arthrite juvénile idiopathique, spondyloarthropathies, persistance du canal artériel (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson |
| Score de Prédiction TxGNN | 99,74 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'ibuprofène est un inhibiteur non sélectif des cyclooxygénases (COX) : il réduit la production de prostaglandines, ce qui explique ses effets anti-inflammatoire et antalgique dans les affections rhumatologiques.

Dans le cas présent, **aucun lien mécanistique n'est établi**. La dysplasie acromésomélique de type Hunter-Thompson est due à des variants entraînant une perte de fonction de *CDMP1/GDF5*, qui altèrent la signalisation de croissance du cartilage et de l'os. L'inhibition des COX n'a pas de rapport connu avec cette voie. Le score élevé (0,997) reflète vraisemblablement une proximité dans le réseau de connaissances avec des maladies musculo-squelettiques et articulaires, plutôt qu'une justification biologique.

Au mieux, l'ibuprofène pourrait apporter un soulagement symptomatique de la douleur, ce qui ne constitue pas une modification de la maladie.

Autres candidats prédits (tous de niveau L5, sans essai ni publication, décision Hold) :
- Syndrome brachyolmie-amélogenèse imparfaite (99,71 %)
- Myosclérose (99,68 %)
- Brachyolmie (99,67 %)
- Syndrome brachydactylie-syndactylie (99,66 %), pour lequel l'exposition prénatale aux AMNS est plutôt un problème de sécurité
- Pseudoachondroplasie (99,66 %), le candidat avec la justification symptomatique la plus plausible (douleurs articulaires précoces et arthrose), sans preuve directe
- Syndrome de microphtalmie colobomateuse-dysplasie rhizomélique (99,60 %)

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Les 5 premières sont listées ci-dessous (le texte d'indication n'est pas renseigné dans les données compilées).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65573720 | BRUFEN 400 mg | Comprimé pelliculé | Non renseignée |
| 61138457 | IBUPROFENE TEVA CONSEIL 400 mg | Comprimé pelliculé | Non renseignée |
| 60830246 | NUROFENTABS 200 mg | Comprimé orodispersible | Non renseignée |
| 60961886 | IBUPROFENE SANDOZ CONSEIL 200 mg | Comprimé enrobé | Non renseignée |
| 64019682 | IBUPROFENE ZENTIVA 400 mg | Comprimé pelliculé | Non renseignée |

Les autres AMM concernent notamment ANTARENE, ADVIL, SPIFEN, SPEDIFEN, ADVILCAPS ainsi que des génériques. Une présentation en solution pour application cutanée (IBUPROFENE CHEMINEAU 5 %) figure aussi parmi elles.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, insuffisance hépatique, hépatopathies, maladie rénale, épilepsie, BPCO, ulcère peptique, maladie inflammatoire chronique de l'intestin, thrombopénie, troubles de la coagulation, accident vasculaire cérébral, infarctus du myocarde et du cerveau, lupus érythémateux systémique, hypothyroïdie, diabète et acidocétose diabétique, hypertrophie bénigne de la prostate, hypotension, carence en potassium, maladie de la vésicule biliaire, pyo-uretère, abus de substances.
- **Interactions médicamenteuses** : 687 interactions recensées. Parmi les principales :
  - **Majeure** : acide acétylsalicylique.
  - **Modérée** : corticoïdes (bétaméthasone, budésonide, dexaméthasone, hydrocortisone), sulfamides hypoglycémiants (acétohexamide, chlorpropamide, glimépiride, glipizide, glibenclamide), exénatide, aprépitant, balsalazide, fenfluramine et dexfenfluramine, kanamycine, lévofloxacine.
  - **Mineure** : famotidine, ranitidine, cimétidine.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication ni lien mécanistique plausible. Le bénéfice potentiel se limiterait à un soulagement symptomatique de la douleur.
- Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice font défaut.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action, afin d'analyser un éventuel lien mécanistique
- Mises en garde et contre-indications de la notice (ANSM), préalable indispensable à l'évaluation de sécurité
- Éclaircissement du statut réglementaire (AMM annulées) et des textes d'indication
- Études précliniques ou observationnelles, en priorité pour la pseudoachondroplasie (soulagement symptomatique), avant toute évaluation clinique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

