---
layout: default
title: Itraconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 418
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Itraconazole : nouvelle indication prédite, Pneumocystose (niveau de preuve L5). Indication d'origine : Mycoses systémiques (candidose œsophagienne, candidémie…"
monitor_inn: "ITRACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Itraconazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Itraconazole : Des Mycoses Systémiques à la Pneumocystose

## Résumé en Une Phrase

L'itraconazole est un antifongique azolé, initialement utilisé pour traiter plusieurs mycoses (candidose œsophagienne, histoplasmose, aspergillose, blastomycose, sporotrichose, etc.).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **pneumocystose**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** n'est enregistré et la littérature disponible ne documente pas d'efficacité de l'itraconazole contre *Pneumocystis*.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mycoses systémiques (candidose œsophagienne, candidémie, histoplasmose, aspergillose, blastomycose, sporotrichose, etc.) |
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,34 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques générales, l'itraconazole inhibe l'enzyme fongique CYP51 (lanostérol 14-alpha-déméthylase), bloquant ainsi la synthèse de l'ergostérol, composant essentiel de la membrane des champignons.

Le score élevé du modèle reflète probablement la proximité, dans le graphe de connaissances, entre la pneumocystose et d'autres infections fongiques opportunistes déjà traitées par l'itraconazole (histoplasmose, aspergillose). Il s'agit d'une association de réseau, et non d'un lien mécanistique démontré.

Le lien mécanistique direct est en réalité peu plausible : *Pneumocystis jirovecii* ne contient que peu ou pas d'ergostérol et utilise principalement du cholestérol dans sa membrane. Une cible de type azole n'est donc pas un bon ajustement. Cette prédiction doit être considérée avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Les publications recensées sont majoritairement des revues et des rapports de cas, sans étude démontrant l'efficacité de l'itraconazole dans la pneumocystose. Sélection des plus pertinentes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Essai randomisé, double aveugle (phase III) | HIV Medicine | Prophylaxie par itraconazole contre les infections fongiques profondes chez des patients VIH ; l'extrait ne mentionne pas la pneumocystose |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revue | BMJ Clinical Evidence | Prophylaxie primaire et secondaire des infections opportunistes au cours du VIH |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revue | Drugs | Traitement et prophylaxie des infections protozoaires systémiques, dont *P. carinii* |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Revue | Clin Infect Dis | Prophylaxie antimicrobienne en neutropénie fébrile ; le cotrimoxazole est efficace contre *P. carinii* |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Revue | Curr Clin Top Infect Dis | Prophylaxie et traitement des infections chez les greffés de moelle osseuse |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revue | Semin Respir Infect | Infections après transplantation pulmonaire |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revue | Clin Pharmacokinet | Pénétration pulmonaire des antifongiques et autres anti-infectieux |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Rapport de cas | Front Immunol | Co-infection *T. marneffei* et *P. jirovecii* chez un enfant porteur d'une mutation STAT1 |

Remarque : plusieurs références (histoplasmose chez des patients atteints de SIDA, par exemple) concernent d'autres infections que la pneumocystose. Les revues citées indiquent que le traitement de référence est le cotrimoxazole, et non un azolé.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60738303 | ITRACONAZOLE VIATRIS 100 mg | Gélule | Annulée |
| 69662344 | ITRACONAZOLE TEVA 100 mg | Gélule | Annulée |
| 69998156 | SPORANOX 10 mg/mL | Solution buvable | Annulée |
| 62469613 | SPORANOX 100 mg | Gélule | Annulée |
| 66188581 | ITRACONAZOLE SANDOZ 100 mg | Gélule | Annulée |

Le texte des indications approuvées n'est pas disponible dans les données compilées.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de la notice) : syndrome du QT long (y compris familial), torsades de pointes, insuffisance cardiaque congestive, cardiomyopathies, cardiopathie ischémique et maladie coronarienne, valvulopathies, insuffisance rénale, maladie hépatique et atteinte hépatique d'origine médicamenteuse, BPCO, neuropathie périphérique, hypokaliémie, hypercalcémie, trouble de la vue et surdité.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Majeures : lopéramide, triamcinolone, budésonide.
  - Modérées : famotidine, ranitidine, cimétidine, rabéprazole, oméprazole (réduction possible de l'absorption), hydrocortisone, dexaméthasone, bétaméthasone, alosétron, aprépitant.
  - Mineures : metformine, pioglitazone, chlorpropamide, amphotéricine B.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, et le mécanisme d'action de l'itraconazole est peu compatible avec la biologie de *Pneumocystis*. Le traitement de référence reste le cotrimoxazole. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice de l'ANSM (lacune bloquante pour l'évaluation de sécurité).
- Les données curées sur le mécanisme d'action (DrugBank).
- Des données précliniques ou cliniques spécifiques montrant une activité de l'itraconazole contre *Pneumocystis*.
- Une clarification de la situation réglementaire en France (AMM toutes annulées) et de la disponibilité des voies d'administration.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

