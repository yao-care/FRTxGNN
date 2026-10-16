---
layout: default
title: Amoxicillin
parent: Prédiction du modèle uniquement (L5)
nav_order: 61
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Amoxicillin : nouvelle indication prédite, Hyperamylasémie (niveau de preuve L5). Indication d'origine : Infection des voies urinaires, otite moyenne infectieuse…"
monitor_inn: "amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
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

# Amoxicilline : Des infections bactériennes à l'hyperamylasémie

## Résumé en Une Phrase

L'amoxicilline est un antibiotique de la famille des bêta-lactamines, initialement utilisé pour traiter des infections bactériennes (infections urinaires, otite moyenne, pneumonie, pharyngite, infections à streptocoques et à staphylocoques, entre autres).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hyperamylasémie**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection des voies urinaires, otite moyenne infectieuse, pneumonie bactérienne, pharyngite et autres infections bactériennes (les textes d'indication des AMM ne sont pas renseignés) |
| Nouvelle Indication Prédite | Hyperamylasémie |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 15 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, l'amoxicilline est une bêta-lactamine bactéricide qui inhibe la synthèse de la paroi cellulaire bactérienne. Son efficacité dans de nombreuses infections bactériennes est établie.

En revanche, **aucun lien mécanistique plausible** n'a été identifié avec l'hyperamylasémie. Il s'agit d'une anomalie biochimique (d'origine pancréatique, salivaire ou rénale) et non d'une maladie infectieuse : l'amoxicilline n'a donc pas de cible évidente. Le score élevé de 99,63 % est une prédiction issue du graphe de connaissances, sans confirmation clinique ni bibliographique, et doit être interprété avec prudence.

À titre d'information, les autres indications prédites par le modèle (syndrome d'hyperviscosité polyclonale, analbuminémie congénitale, incompatibilité de groupe sanguin, gammapathie monoclonale, etc.) ne montrent pas non plus de justification mécanistique solide. La seule piste biologiquement plausible, mais faible, est la **peste septicémique** : les données sont indirectes et suggèrent que les bêta-lactamines sont moins efficaces que les traitements de référence (aminosides, tétracyclines, fluoroquinolones).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour l'hyperamylasémie.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour l'hyperamylasémie.

---

## Informations de Marché en France

Les 15 AMM recensées sont toutes annulées. Les textes d'indication approuvée ne sont pas renseignés. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 66918105 | AMOXICILLINE PANPHARMA 1 g | Poudre pour solution injectable | Annulée |
| 69915160 | AMOXICILLINE PANPHARMA 1 g/5 ml (IM) | Poudre et solution pour solution injectable | Annulée |
| 69416855 | AMOXICILLINE PANPHARMA 2 g | Poudre pour solution injectable | Annulée |
| 61645058 | XYLLOMAC 500 mg (IM-IV) | Poudre pour solution injectable ou pour perfusion | Annulée |
| 60271045 | XYLLOMAC 2 g (IV) | Poudre pour solution injectable ou pour perfusion | Annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe, et non texte de la notice) : syndrome du QT long, torsades de pointes, insuffisance hépatique, maladies hépatiques, cholestase, porphyries, maladies rénales, colite à *Clostridium difficile*, myasthénie grave, tachycardie ventriculaire, ostéoporose, fracture osseuse, mononucléose infectieuse, maladie de la vésicule biliaire, entérocolite nécrosante périnatale, entre autres.
- **Interactions médicamenteuses** : 271 interactions recensées. Parmi les principales :
  - **Majeures** : méthotrexate ; vaccin vivant anticholérique (*Vibrio cholerae* CVD 103-HgR).
  - **Modérées** : doxycycline, minocycline, déméclocycline, éthinylestradiol, estradiol, anisindione, dicoumarol, mycophénolate mofétil, entécavir, balsalazide, probiotiques (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*), indium In-111 oxyquinoléine.
  - **Mineures** : allopurinol, amiloride, azithromycine, clarithromycine, érythromycine.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'hyperamylasémie n'est soutenue par aucune étude (niveau L5) et aucun mécanisme plausible n'a été identifié ; de plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (DrugBank)
- Mises en garde et contre-indications officielles issues de la notice (site de l'ANSM)
- Justification biologique de l'association avec l'hyperamylasémie, ou examen d'artefact du graphe de connaissances
- Si une piste est poursuivie, privilégier la peste septicémique comme question de recherche (preuves indirectes seulement, absence d'essai chez l'humain, agents de référence plus efficaces)
- Clarification du statut réglementaire, toutes les AMM étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

