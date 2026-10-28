---
layout: default
title: Vancomycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 804
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
description: "Vancomycin : nouvelle indication prédite, Sclérodermie diffuse (diffuse scleroderma) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Vancomycin
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

## Vancomycin: Sclérodermie diffuse (diffuse scleroderma)
{: .text-alpha }

## Résumé en Une Phrase

La vancomycine est un antibiotique de la famille des glycopeptides, initialement utilisé pour traiter des infections à bactéries Gram positif (colite à *Clostridium difficile*, infections à staphylocoques, endocardites, etc.).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **sclérodermie diffuse**, avec un score élevé, mais **aucun essai clinique** et **une seule publication** (un rapport de cas sans lien direct avec la sclérodermie) n'étayent cette prédiction.
Cette prédiction relève très probablement de similarités apprises par le modèle TxGNN (apprentissage profond) entre maladies apparentées, et non d'une piste thérapeutique réelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Sclérodermie diffuse (diffuse scleroderma) |
| Score de Prédiction TxGNN | 0.9992 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, la vancomycine est un antibiotique glycopeptidique qui inhibe la synthèse de la paroi cellulaire des bactéries Gram positif. Son efficacité est établie dans les infections à staphylocoques résistants, l'endocardite et la colite à *C. difficile* (par voie orale).

**La prédiction ne paraît pas plausible sur le plan mécanistique.** La sclérodermie diffuse est une maladie auto-immune et fibrosante, sans cause bactérienne connue qu'un antibiotique ciblant la paroi bactérienne pourrait traiter. Le score élevé (0,9992) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non un lien biologique réel.

La seule publication associée porte sur un cas d'érythrodermie avec sepsis et éosinophilie. Elle ne concerne pas la sclérodermie et n'apporte aucune preuve d'efficacité.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Rapport de cas | The American Journal of Case Reports | Cas d'un homme de 56 ans présentant une éruption exfoliative diffuse avec sepsis et éosinophilie (érythrodermie) ; sans rapport avec la sclérodermie |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64022454 | VANCOMYCINE SANDOZ 500 mg, poudre pour solution à diluer pour perfusion ou pour solution buvable (SANDOZ) – AMM active | Poudre pour solution à diluer pour perfusion ou buvable | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de la notice) : maladie rénale, pyourètre, neutropénie, agranulocytose, troubles de l'audition et maladies du système auditif.
- **Interactions médicamenteuses** : 454 interactions recensées. Parmi les exemples :
  - **Majeures** : immunoglobuline humaine G (intraveineuse), immunoglobuline humaine anti-neurotoxine botulique A/B, souche vivante de *Vibrio cholerae* CVD 103-HgR.
  - **Modérées** : kétorolac, ibuprofène, diclofénac, célécoxib, amphotéricine B, amikacine, capréomycine, carboplatine, bacitracine, métformine, mésalazine, cholestyramine, éthinylestradiol, estradiol, ibandronate, balsalazide.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication pertinente, et sans lien mécanistique plausible entre un antibiotique ciblant la paroi bactérienne et une maladie fibrosante auto-immune.
- L'AMM française est annulée, et les données de sécurité officielles (mises en garde, contre-indications) sont manquantes, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle auprès de l'ANSM (mises en garde, contre-indications) pour permettre l'évaluation de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Démontrer un lien biologique crédible avec la sclérodermie diffuse (études précliniques) avant toute étude clinique

**Remarque sur les autres indications prédites :** parmi les dix prédictions du modèle, la plupart n'ont aucun support (fièvres paratyphoïde et typhoïde, salmonellose : bactéries Gram négatif naturellement résistantes à la vancomycine ; analbuminémie congénitale, syndrome d'hyperviscosité polyclonale, hyperamylasémie, incompatibilité de groupe sanguin, maladie hématologique prémaligne). La seule piste biologiquement plausible est la **pneumonie à streptocoques** (niveau L4) : la vancomycine y est active sur les souches Gram positif et sert de recours pour les souches très résistantes à la pénicilline. Elle correspond toutefois à un usage déjà existant plutôt qu'à un véritable repositionnement, et les 20 publications associées sont des revues et des études d'épidémiologie de la résistance, sans données d'essai spécifiques à la vancomycine.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

