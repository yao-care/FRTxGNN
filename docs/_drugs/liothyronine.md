---
layout: default
title: Liothyronine
parent: Prédiction du modèle uniquement (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Liothyronine : nouvelle indication prédite, Hypoplasie/aplasie rénale (niveau de preuve L5). Indication d'origine : Hypothyroïdie"
monitor_inn: "LIOTHYRONINE"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "nodular goiter (disease)", "Carney complex", "peripheral dysostosis", "Potter sequence", "acrodysostosis with or without hormone resistance", "angiomyxoma", "myxoma", "hypotrichosis simplex of the scalp"]
---

# Liothyronine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Liothyronine : De l'Hypothyroïdie à l'Hypoplasie/Aplasie Rénale

## Résumé en Une Phrase

La liothyronine (triiodothyronine, T3) est une hormone thyroïdienne de synthèse, utilisée à l'origine dans le traitement de l'hypothyroïdie et des maladies thyroïdiennes apparentées (goitre, myxœdème, cancers thyroïdiens différenciés).
Le modèle TxGNN la prédit comme potentiellement efficace pour l'**hypoplasie/aplasie rénale**, mais il s'agit d'une prédiction du modèle uniquement : **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypothyroïdie (le texte d'indication de l'AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Hypoplasie/aplasie rénale |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la liothyronine est la forme active de l'hormone thyroïdienne (T3). Son efficacité dans l'hypothyroïdie est établie, et les hormones thyroïdiennes jouent un rôle général dans le développement et la maturation de nombreux organes, dont le rein.

Cependant, le lien avec l'hypoplasie/aplasie rénale reste très faible. Il s'agit d'une malformation congénitale structurelle, et un médicament administré après la naissance a peu de chances d'en inverser les effets. Aucun lien mécanistique direct n'est établi. Le score élevé du modèle reflète probablement une proximité dans le graphe de connaissances avec d'autres troubles du développement rénal, et non une preuve pharmacologique.

**Autres prédictions du modèle (toutes sans essai clinique) :**

| Rang | Maladie prédite | Score | Niveau de preuve | Commentaire |
|---|---|---|---|---|
| 2 | Agénésie rénale bilatérale | 99,94 % | L5 | Aucune justification pharmacologique plausible |
| 3 | Goitre nodulaire | 99,94 % | L4 | Déjà dans les indications d'origine ; la seule publication concerne l'hyperthyroïdie du chat, non pertinente |
| 4 | Complexe de Carney | 99,93 % | L5 | Axe AMPc/PKA commun, mais aucune preuve clinique |
| 5 | Dysostose périphérique | 99,91 % | L5 | Aucune preuve de correction de la dysostose |
| 6 | Séquence de Potter | 99,91 % | L5 | Aucune justification pratique |
| 7 | Acrodysostose (avec ou sans résistance hormonale) | 99,89 % | L4 | Lien biologique plausible via l'AMPc, preuves indirectes uniquement (question de recherche) |
| 8 | Angiomyxome | 99,89 % | L5 | Proximité avec le complexe de Carney |
| 9 | Myxome | 99,89 % | L5 | Prise en charge chirurgicale ; aucune preuve |
| 10 | Hypotrichose simple du cuir chevelu | 99,87 % | L5 | Trouble génétique non lié à un déficit thyroïdien |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée à l'hypoplasie/aplasie rénale n'est disponible actuellement.

À titre indicatif, pour la prédiction de rang 7 (acrodysostose), vingt publications ont été retrouvées, mais elles portent sur la liothyronine en général et non sur cette maladie :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Revue systématique / méta-analyse en réseau | J Affect Disord | Stratégies d'augmentation dans la dépression résistante |
| [36421864](https://pubmed.ncbi.nlm.nih.gov/36421864/) | 2022 | Revue systématique | Brain Sci | Supplémentation en hormones thyroïdiennes dans le trouble bipolaire (8 études) |
| [41838451](https://pubmed.ncbi.nlm.nih.gov/41838451/) | 2026 | Méta-analyse en réseau | Endocr Connect | Traitements additionnels de l'hypothyroïdie en complément de la lévothyroxine |
| [31588494](https://pubmed.ncbi.nlm.nih.gov/31588494/) | 2020 | Étude clinique interventionnelle de petite taille | J Clin Endocrinol Metab | Effets des hormones thyroïdiennes sur l'utilisation du glucose en cas de mutations du récepteur de l'insuline |
| [7477166](https://pubmed.ncbi.nlm.nih.gov/7477166/) | 1995 | ECR (chirurgie cardiaque) | N Engl J Med | T3 périopératoire après pontage coronarien chez des patients à haut risque |
| [32614450](https://pubmed.ncbi.nlm.nih.gov/32614450/) | 2020 | Revue | J Clin Endocrinol Metab | Traitement individualisé de l'hypothyroïdie : place de l'association T4 + T3 |
| [40598574](https://pubmed.ncbi.nlm.nih.gov/40598574/) | 2025 | Protocole d'ECR | Trials | Lévothyroxine associée à la liothyronine à libération prolongée dans l'hypothyroïdie |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69081937 | EUTHYRAL 100 microgrammes/20 microgrammes, comprimé sécable (MERCK SANTE) | Comprimé sécable | Non renseignée ; AMM annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, hypopituitarisme et déficits hypophysaires (dont syndrome de Sheehan), hypogonadisme hypogonadotrope (dont syndrome de Kallmann), déficit en hormone de croissance, maladie du thymus, ostéoporose (dont postménopausique), diabète et acidocétose diabétique, maladie coronarienne, infarctus du myocarde.
- **Interactions médicamenteuses** : 100 interactions recensées, les 20 premières étant de niveau modéré. Principales classes concernées :
  - antidiabétiques (acarbose, metformine, pioglitazone, alogliptine, linagliptine, canagliflozine, dapagliflozine, empagliflozine, chlorpropamide, albiglutide, dulaglutide) ;
  - inhibiteurs de la pompe à protons (oméprazole, rabéprazole, dexlansoprazole) ;
  - sels de calcium et de magnésium (phosphate et acétate de calcium, oxyde de magnésium) ;
  - sympathomimétiques (épinéphrine, isométheptène, diéthylpropion).

Les mises en garde et contre-indications de la notice n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun mécanisme plausible ne permet de corriger une malformation rénale congénitale par la liothyronine.
- Le seul produit français lié est annulé, et le dépistage de sécurité ne peut pas avancer faute de données de notice.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice (ANSM)
- Les données sur le mécanisme d'action (DrugBank)
- Des études précliniques ou mécanistiques sur le rôle des hormones thyroïdiennes dans le développement rénal
- Parmi les autres prédictions, seule l'acrodysostose mérite d'être étudiée comme question de recherche, sur la base du lien AMPc/PKA, avec une revue ciblée de la littérature
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

