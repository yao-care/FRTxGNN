---
layout: default
title: Clofazimine
parent: Prédiction du modèle uniquement (L5)
nav_order: 184
evidence_level: L5
indication_count: 3
---

# Clofazimine
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

# Clofazimine : De la lèpre à la pneumocystose

## Résumé en Une Phrase

La clofazimine est un antibactérien de la famille des riminophénazines, initialement utilisé dans le traitement de la lèpre (dont la lèpre multibacillaire) et pour le pyoderma gangrenosum.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **pneumocystose**, mais **aucun essai clinique** n'est enregistré et la littérature retrouvée (**3 publications**) ne porte pas réellement sur cette indication.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Lèpre, lèpre multibacillaire, pyoderma gangrenosum (indications issues du graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, la clofazimine est une riminophénazine dotée d'une activité antimycobactérienne et anti-inflammatoire. Son efficacité est reconnue dans la lèpre, et elle est également utilisée dans les schémas contre la tuberculose résistante à la rifampicine.

Le lien avec la pneumocystose est en revanche **faible**. *Pneumocystis* est un organisme fongique : l'activité antimycobactérienne ne se transpose pas à ce type d'agent. Le score élevé de TxGNN (99,9 %) reste une prédiction informatique, sans soutien clinique dans les données compilées pour ce rapport.

Les publications retrouvées concernent la prophylaxie de l'infection à *Mycobacterium avium complex* (MAC) chez des patients atteints du sida, ou des co-infections opportunistes. Ces patients avaient souvent un antécédent de pneumocystose, ce qui explique probablement l'association statistique, mais ces travaux n'évaluent pas la clofazimine comme traitement de la pneumocystose.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Essai randomisé ouvert (prophylaxie MAC, non *Pneumocystis*) | J Infect Dis | Évaluation de la clofazimine en prophylaxie de l'infection disséminée à MAC chez 110 patients VIH, dont certains avec antécédent de pneumonie à *P. carinii* ; ne concerne pas le traitement de la pneumocystose |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Rapport de cas | Infection | Patient sidéen avec infection à *M. kansasii* compliquée d'une pneumonie à *P. carinii* ; guérison sous association incluant la clofazimine, puis le triméthoprime-sulfaméthoxazole après l'apparition de la pneumocystose |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Revue | PI Perspective | Mise à jour générale sur les infections opportunistes |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62768220 | LAMPRENE 50 mg, capsule molle (Novartis Pharma) | Capsule molle | Non renseignée (AMM annulée) |
| 67132888 | LAMPRENE 100 mg, capsule molle (Novartis Pharma) | Capsule molle | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, maladie diarrhéique, ulcère gastroduodénal actif, maladie du système digestif, maladie intestinale, infarctus splénique, maladie splénique, hypersplénisme.
- **Interactions médicamenteuses** (100 interactions recensées ; principales ci-dessous) :
  - **Majeures** : cisapride, dolasétron.
  - **Modérées** : famotidine, lopéramide, clarithromycine, lévofloxacine, ondansétron, granisétron, palonosétron, ainsi que de nombreux laxatifs (bisacodyl, picosulfate, macrogol, huile de ricin, lactulose, lactitol, citrate et hydroxyde de magnésium, glycérine, huile minérale).
  - **Mineure** : métronidazole.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L5 : aucun essai clinique, et la littérature retrouvée ne porte pas sur le traitement de la pneumocystose. Le mécanisme n'offre pas de lien plausible, et les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données sur le mécanisme d'action (DrugBank).
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour l'évaluation de sécurité).
- Des données précliniques *in vitro* ou *in vivo* de la clofazimine contre *Pneumocystis*.

**Autres pistes prédites par TxGNN (à titre informatif) :**
- **Paludisme** (score 99,60 %, niveau L4, « question de recherche ») : une étude *in vitro* sur des analogues de la clofazimine suggère une activité antiplasmodiale. Les autres références retrouvées concernent surtout la tuberculose résistante ou d'autres composés, et ne constituent pas une preuve directe. Aucun essai clinique n'est enregistré.
- **Anomalie de la sécrétion de gastrine** (score 99,57 %, niveau L5, Hold) : aucune preuve ni justification mécanistique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

