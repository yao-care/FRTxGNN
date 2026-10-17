---
layout: default
title: Budesonide
parent: Prédiction du modèle uniquement (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Budesonide : nouvelle indication prédite, Eczéma atopique (niveau de preuve L5). Indication d'origine : Maladie de Crohn, maladies inflammatoires de l'intestin, asthme…"
monitor_inn: "budesonide"
predicted_indications: ["atopic eczema", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
---

# Budesonide
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

# Budésonide : Des Maladies Inflammatoires (Asthme, Maladie de Crohn) à l'Eczéma Atopique

## Résumé en Une Phrase

Le budésonide est un corticoïde (glucocorticoïde) initialement utilisé dans l'asthme, la rhinite allergique et les maladies inflammatoires de l'intestin, dont la maladie de Crohn.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**eczéma atopique**, avec un score très élevé, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette indication précise dans les données compilées pour ce rapport.
Il s'agit donc d'une prédiction purement théorique à ce stade.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Crohn, maladies inflammatoires de l'intestin, asthme, rhinite allergique (d'après le graphe de connaissances ; le texte des indications d'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Eczéma atopique |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (0 valide, 20 annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le budésonide est un glucocorticoïde à large activité anti-inflammatoire et immunosuppressive. Son efficacité dans l'asthme et la rhinite allergique, des maladies inflammatoires de type allergique, est établie.

L'eczéma atopique est une inflammation cutanée largement dirigée par la voie Th2, proche de l'asthme allergique et de la rhinite allergique, déjà couverts par les indications d'origine. Un corticoïde pourrait donc, sur le plan mécanistique, être pertinent. Le score très élevé du modèle (99,96 %) reste cependant une prédiction et non une preuve.

Il faut aussi noter que la littérature retrouvée sur la dermatite atopique porte surtout sur l'allergie de contact aux corticoïdes et les tests épicutanés (le budésonide est un sensibilisant fréquent), et non sur un bénéfice thérapeutique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour l'eczéma atopique.

---

## Preuves de la Littérature

Pour l'eczéma atopique (« atopic eczema »), aucune littérature associée n'est disponible actuellement.

Pour la même maladie sous l'appellation voisine « dermatite atopique », les publications retrouvées sont indirectes. Aucune ne démontre un bénéfice thérapeutique chez l'humain :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Étude préclinique de formulation | Gels (Basel) | Nanoparticules de budésonide en hydrogels pour une thérapie locale de la dermatite atopique ; étape préclinique |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Revue | Neuroimmunomodulation | Corticoïdes intranasaux et suppression surrénalienne, dans le contexte de la rhinite allergique associée à l'asthme et à la dermatite atopique |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Étude de tests épicutanés | Contact Dermatitis | Allergie au budésonide en baisse sur deux décennies (série de base italienne) |
| [35184304](https://pubmed.ncbi.nlm.nih.gov/35184304/) | 2022 | Rapport de cas | Contact Dermatitis | Dermatite allergique systémique due à un test épicutané au budésonide |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | Étude in vitro | Int Immunopharmacol | Le budésonide, contrairement au tacrolimus, modifie les fonctions immunitaires des kératinocytes humains normaux |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | ECR (vétérinaire, chien) | J Vet Pharmacol Ther | Après-shampooing au budésonide (Barazone) : réduction des lésions et du prurit chez des chiens atopiques ; non transposable à l'humain |

---

## Informations de Marché en France

Toutes les AMM suivantes sont annulées. Le texte des indications approuvées n'est pas renseigné. Liste des 5 premières :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65648500 | Budesonide Teva 1 mg/2 mL | Suspension pour inhalation par nébuliseur | Non renseignée (AMM annulée) |
| 60468092 | Novopulmon Novolizer 200 µg/dose | Poudre pour inhalation | Non renseignée (AMM annulée) |
| 69152302 | Acorspray 200 µg par inhalation | Solution pour inhalation | Non renseignée (AMM annulée) |
| 66664532 | Pulmicort 1 mg/2 mL | Suspension pour inhalation par nébuliseur | Non renseignée (AMM annulée) |
| 65036357 | Pulmicort Turbuhaler 200 µg/dose | Poudre pour inhalation | Non renseignée (AMM annulée) |

Le budésonide a également existé sous forme nasale (Rhinocort), orale (Entocort, Cortiment, Jorveza) et en gélule inhalée (Miflonil). Aucune formulation cutanée n'figure parmi les AMM recensées.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : hypertension, épilepsie, maladie hépatique, maladie de la vésicule biliaire, hyperglycémie, insuffisance cardiaque congestive, kératite herpétique, rougeole, déficits en hormones hypophysaires (dont hypopituitarisme et syndrome de Sheehan), ainsi que certains troubles du cycle de l'urée.
- **Interactions médicamenteuses** : 599 interactions recensées. Parmi les principales :
  - Majeures : adalimumab, fosamprénavir
  - Modérées : zidovudine, isotrétinoïne, acébutolol, kétorolac, nifédipine, ibuprofène, éthinylestradiol, fluvoxamine, aldesleukine, alemtuzumab
  - Mineures : formotérol, salbutamol
- **Signal lié à l'indication prédite** : la littérature décrit des cas d'allergie de contact au budésonide chez des patients atteints de dermatite atopique, à prendre en compte pour toute voie cutanée.

Les mises en garde principales de la notice ne sont pas disponibles ; veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'eczéma atopique n'est soutenu que par une prédiction du modèle (niveau L5), sans essai clinique ni publication thérapeutique directe. De plus, aucune AMM n'est actuellement valide en France et les données de sécurité de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les notices de l'ANSM (mises en garde et contre-indications), qui constituent un point bloquant avant tout examen de sécurité
- Obtenir les données de mécanisme d'action depuis DrugBank
- Rechercher des essais cliniques et des études humaines sur le budésonide dans l'eczéma/dermatite atopique, et évaluer la compatibilité de voie d'administration (forme cutanée à définir)
- Évaluer le risque d'allergie de contact et d'effets systémiques des corticoïdes

**Autres pistes prédites à noter :**
- **Bronchite** (L2, 10 essais, score 99,81 %) : piste de recherche la plus étayée, mais les essais portent surtout sur la bronchiolite oblitérante post-greffe (NCT00624754, NCT01560689, tous deux de phase 2, n=32), la BPCO et la bronchite éosinophilique (NCT02002715, phase 4, n=106). Les résultats ne sont pas fournis et le terme « bronchite » recouvre probablement des pathologies distinctes.
- **Polype du sinus frontal** (L4) : plausibilité biologique relativement forte (le budésonide est utilisé dans la polypose nasale), mais les preuves retrouvées sont anciennes et indirectes.
- Les autres prédictions (polypes des cordes vocales, de l'oreille moyenne, du conduit auditif externe, fibroépithéliaux, utérins, épulis) reposent essentiellement sur le modèle et sont peu étayées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

