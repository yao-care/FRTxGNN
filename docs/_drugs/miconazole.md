---
layout: default
title: Miconazole
parent: Preuves modérées (L3-L4)
nav_order: 498
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "MICONAZOLE"
predicted_indications: ["acne (disease)"]
description: "Miconazole : nouvelle indication prédite, Acné (acne (disease)) (acne (disease)) (niveau de preuve L3). Indication d'origine : Non renseignée dans les données locales"
---

# Miconazole
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **1** 
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

## Miconazole: Acné (acne (disease)) (acne (disease))
{: .text-alpha }

## Résumé en Une Phrase

Le miconazole est un antifongique de la classe des imidazolés, initialement utilisé pour traiter les mycoses cutanées (pied d'athlète, teigne du corps, pityriasis versicolor) et les candidoses (cutanées, vulvovaginales).
Le modèle TxGNN prédit qu'il pourrait être utile pour l'**acné**, mais cette direction ne repose pour l'instant que sur **4 publications** (une revue, une étude clinique de petite taille, une étude sur une affection voisine et une étude in vitro) et **aucun essai clinique** enregistré.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Acné (acne (disease)) (acne (disease)) |
| Score de Prédiction TxGNN | 0.9954 |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après la pharmacologie connue des azolés, le miconazole inhibe la CYP51 fongique (lanostérol 14-alpha-déméthylase), bloquant la synthèse de l'ergostérol, composant essentiel de la membrane des champignons.

Le lien avec l'acné peut passer par trois voies plausibles : (1) une activité in vitro contre *Cutibacterium (Propionibacterium) acnes*, observée lors de tests de sensibilité aux azolés ; (2) une activité contre *Malassezia* (*Pityrosporum*), responsable de la folliculite à Malassezia, qui ressemble cliniquement à l'acné ; (3) des effets anti-inflammatoires et antibactériens cutanés rapportés dans la littérature.

Il faut toutefois rester prudent : le score TxGNN élevé est une prédiction informatique et non une preuve clinique. Une partie des données concerne la folliculite à Malassezia, qui n'est pas de l'acné vulgaire. La seule donnée clinique directe est une petite étude en split-face sur l'acné inflammatoire cataméniale légère.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Étude clinique (split-face, évaluation bio-instrumentale ; probablement de petite taille) | Skin Research and Technology | Évaluation de la prise en charge de l'acné inflammatoire cataméniale légère chez la jeune femme ; seule donnée humaine directe sur l'acné, mais à petite échelle |
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Revue | Expert Opinion on Pharmacotherapy | Revue des effets multiples du miconazole sur les affections cutanées, dont des effets anti-inflammatoires et antibactériens |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Étude clinique / essai thérapeutique | Clinical and Experimental Dermatology | 62 patients atteints de folliculite à Pityrosporum (souvent confondue avec l'acné vulgaire) ; il ne s'agit pas d'acné vulgaire à proprement parler |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Étude in vitro | Biological & Pharmaceutical Bulletin | Activité in vitro des azolés antifongiques contre *P. acnes* isolé de patients atteints d'acné vulgaire |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69184289 | DAKTARIN 2 %, gel buccal (KENVUE FRANCE) | Gel | Non renseignée (AMM active) |
| 69980852 | LORAMYC 50 mg, comprimé buccogingival muco-adhésif (VECTANS PHARMA) | Comprimé muco-adhésif | Non renseignée (AMM active) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie du foie, maladie de la vésicule biliaire.
- **Interactions médicamenteuses** : 100 interactions répertoriées, dont les principales (niveau modéré) concernent :
  - les opioïdes : fentanyl, alfentanil, hydrocodone ;
  - les médicaments cardiovasculaires : amiodarone, nifédipine, amlodipine, alfuzosine, aliskirène ;
  - les anticancéreux : paclitaxel, acalabrutinib ;
  - les hormones : éthinylestradiol, estradiol ;
  - les psychotropes : alprazolam, amitriptyline ;
  - autres : alosétron.

  Des interactions de niveau mineur sont également signalées (dolutégravir, loratadine, amphotéricine B, ambrisentan).

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être compilées. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à une revue, une petite étude clinique, une étude in vitro et une étude sur une affection voisine ; aucun essai clinique n'est enregistré. Le score TxGNN élevé ne suffit pas, et les données de sécurité issues de la notice manquent (lacune bloquante pour le dépistage de sécurité).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Réaliser des essais cliniques contrôlés (idéalement randomisés) du miconazole dans l'acné vulgaire.
- Confirmer la compatibilité de la voie d'administration (topique) et clarifier la situation réglementaire des produits à base de miconazole.
- Évaluer le risque hépatique et les interactions médicamenteuses selon la formulation et le mode d'administration envisagés.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

