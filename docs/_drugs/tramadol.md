---
layout: default
title: Tramadol
parent: Prédiction du modèle uniquement (L5)
nav_order: 777
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "TRAMADOL"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
description: "Tramadol : nouvelle indication prédite, Dysplasie acromésomélique de type Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (niveau de preuve L5). Indication d'origine : Non renseignée …"
---

# Tramadol
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

## Tramadol: Dysplasie acromésomélique de type Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Résumé en Une Phrase

Le tramadol est un analgésique opioïde, initialement associé à la prise en charge de l'arthrose et des arthropathies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dysplasie acromésomélique de type Hunter-Thompson**, une maladie génétique rare du squelette.
Aucun essai clinique et aucune publication ne soutiennent actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, le tramadol est un agoniste des récepteurs opioïdes mu, doté d'une inhibition de la recapture de la sérotonine et de la noradrénaline. Il agit comme analgésique et son usage dans les douleurs ostéo-articulaires est connu.

L'analyse de la plausibilité ne identifie **aucun lien mécanistique** entre le tramadol et cette pathologie. La dysplasie acromésomélique de type Hunter-Thompson est une maladie génétique rare (perte de fonction de CDMP1/GDF5) qui altère la croissance des membres. Le tramadol n'a aucun effet modificateur de la maladie. Le score élevé provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Tout au plus, un effet analgésique symptomatique pourrait être pertinent, ce qui ne constitue pas un repositionnement.

Les autres prédictions les mieux classées vont dans le même sens : dysplasies squelettiques rares (syndrome brachyolmie-amélogenèse imparfaite, brachyolmie, pseudoachondroplasie), myosclérose, spondylarthropathie (susceptibilité), formes d'arthrite juvénile et nodulose rhumatoïde. Aucune ne dispose de preuves, et le tramadol n'y offrirait qu'un soulagement symptomatique de la douleur.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'indication principale prédite.

Pour information, une publication a été retrouvée pour une prédiction de rang inférieur (arthrite juvénile idiopathique) : [20799760](https://pubmed.ncbi.nlm.nih.gov/20799760/) (2010, revue, *Paediatric Drugs*), consacrée à la pharmacocinétique, l'efficacité et la tolérance du kétoprofène chez l'enfant. Elle ne concerne pas le tramadol et ne constitue donc pas une preuve directe.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66750351 | TRAMADOL TEVA L.P. 100 mg (TEVA SANTE) | Comprimé pelliculé à libération prolongée | Non renseignée ; AMM active |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : hypertension, insuffisance hépatique, maladie hépatique et cirrhose, épilepsie, troubles anxieux, trouble névrotique, trouble dysthymique, maladie de la vésicule biliaire, diabète et acidocétose diabétique, abus ou dépendance aux substances, syndrome de sevrage (dont sevrage alcoolique), hyperlipidémie (dont familiale), insuffisance respiratoire, intoxication au paracétamol, syndrome sérotoninergique, pseudotumeur cérébrale et hypertension intracrânienne, syndrome de Wernicke-Korsakoff, infections du système nerveux central.
- **Interactions médicamenteuses** (100 interactions recensées ; principales sur les 20 premières) :
  - Majeures : alvimopan, bupropion, cisapride, dexfenfluramine, diéthylpropion, dolasétron, dronabinol, éphédrine, fenfluramine.
  - Modérées : atropine, bisacodyl, huile de ricin, cimétidine, clarithromycine, clidinium, dicyclomine, éliglustat, éluxadoline, famotidine, glycérine.
- **Population pédiatrique** : les restrictions d'usage (risque de dépression respiratoire, métabolisme ultra-rapide du CYP2D6) sont pertinentes pour les formes juvéniles prédites.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être obtenues.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication directe ni lien mécanistique plausible. Le profil de sécurité est par ailleurs chargé, et la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice de l'ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Des preuves précliniques ou cliniques directes pour la pathologie prédite, ou la réorientation vers une évaluation symptomatique de la douleur dans les arthropathies, hors repositionnement strict
- Une évaluation de la compatibilité des voies d'administration et de la similarité avec l'indication d'origine
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

