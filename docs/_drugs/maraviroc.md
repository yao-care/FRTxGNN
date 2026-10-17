---
layout: default
title: Maraviroc
parent: Prédiction du modèle uniquement (L5)
nav_order: 474
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Maraviroc : nouvelle indication prédite, Néoplasie endocrinienne multiple (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "MARAVIROC"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
---

# Maraviroc
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

# Maraviroc : De l'infection par le VIH à l'Néoplasie Endocrinienne Multiple

## Resume en Une Phrase

Maraviroc est un antagoniste du récepteur CCR5. Les données compilées pour ce rapport ne mentionnent aucune indication originale approuvée en France (les textes d'indication sont vides dans les AMM).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **néoplasie endocrinienne multiple**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Predite | Néoplasie endocrinienne multiple |
| Score de Prediction TxGNN | 99,82 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Toutes les AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 7 (dont 7 annulées) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, maraviroc est un antagoniste du récepteur de chimiokines CCR5. Son indication originale n'est pas renseignée dans les données compilées.

Aucun lien mécanistique n'est étayé par les données fournies entre le blocage de CCR5 et les syndromes de néoplasie endocrinienne multiple. Le score élevé de TxGNN (0,998) correspond uniquement à une prédiction computationnelle.

À titre d'information, les autres candidats prédits sont présentés ci-dessous. Tous restent au niveau L5 et en décision Hold :

| Rang | Maladie prédite | Score TxGNN | Remarque |
|------|------|------|------|
| 2 | Acné | 99,76 % | Aucune preuve ; lien spéculatif via le recrutement de cellules inflammatoires |
| 3 | Lymphome cutané primitif à cellules T | 99,72 % | Une seule revue sur ACKR1, un autre récepteur ; pas de preuve directe |
| 4 | Lupus érythémateux systémique pédiatrique | 99,71 % | Aucune preuve ; lien spéculatif |
| 5 | Lymphome cutané primitif non hodgkinien à cellules T | 99,50 % | Même famille que le rang 3, même limite |
| 6 | Lymphome cutané primitif à cellules B | 99,38 % | Aucune preuve |
| 7 | Candidose | 99,28 % | Revue sur les effets indésirables des antirétroviraux ; plutôt un contexte d'infection opportuniste liée au VIH |
| 8 | Déficit en composant 4a du complément | 99,24 % | Aucune preuve ni mécanisme plausible |
| 9 | Infection à cytomégalovirus | 99,23 % | Cohorte VIH sans démonstration d'efficacité |
| 10 | Carcinome mammaire HER2 positif | 99,22 % | Étude préclinique plausible (axe CCL5-CCR5), la plus étayée sur le plan mécanistique |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Litterature

Aucune littérature associée disponible actuellement pour la néoplasie endocrinienne multiple.

Pour information, des publications existent pour d'autres candidats, sans preuve directe pour maraviroc :

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) | 2020 | Préclinique | Mol Cancer Ther | L'effet autocrine de CCL5 médie la résistance au trastuzumab via l'activation de la voie ERK dans le cancer du sein HER2 positif (candidat n° 10) |
| [37006247](https://pubmed.ncbi.nlm.nih.gov/37006247/) | 2023 | Revue | Front Immunol | Perspectives du ciblage d'ACKR1 dans le cancer et d'autres maladies (lymphomes cutanés, candidats n° 3 et 5) |
| [25397464](https://pubmed.ncbi.nlm.nih.gov/25397464/) | 2014 | Cohorte | J Int AIDS Soc | Immunité innée et paramètres métaboliques chez des patients VIH+ sous traitement antirétroviral (candidat n° 9) |
| [21671545](https://pubmed.ncbi.nlm.nih.gov/21671545/) | 2011 | Revue | Am Fam Physician | Effets indésirables courants des traitements antirétroviraux (candidat n° 7) |

---

## Informations de Marche en France

Toutes les AMM sont annulées ; aucune n'est actuellement valide. Les textes d'indication ne sont pas disponibles.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 61182724 | CELSENTRI 300 mg | Comprimé pelliculé | Non renseignée |
| 60992262 | CELSENTRI 25 mg | Comprimé pelliculé | Non renseignée |
| 64830457 | MARAVIROC WAYMADE 300 mg | Comprimé pelliculé | Non renseignée |
| 64813486 | MARAVIROC WAYMADE 150 mg | Comprimé pelliculé | Non renseignée |
| 65936214 | CELSENTRI 20 mg/ml | Solution buvable | Non renseignée |

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe PrimeKG, et non le texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, maladie rénale (dont insuffisance rénale chronique et terminale), maladie hépatique (dont atteinte hépatique d'origine médicamenteuse), maladie de la vésicule biliaire, hépatite B chronique, hépatite C, maladie coronarienne, infarctus du myocarde, thrombose coronarienne, ischémie myocardique, hémoglobinopathie, pyo-uretère et maladies infectieuses.
- **Interactions Medicamenteuses** : 93 interactions recensées. Interaction majeure : **clarithromycine**. Interactions modérées (exemples) : aprépitant, dexaméthasone, cimétidine, cobicistat, clotrimazole, miconazole, naltrexone, rolapitant, deferasirox, diazoxide, phentolamine, prométhazine, époprosténol, fostamatinib.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, sans mécanisme étayé, et aucune AMM n'est actuellement valide en France.
- Le signal préclinique CCL5-CCR5 dans le cancer du sein HER2 positif est la piste la plus plausible, mais elle relève d'une question de recherche et non d'une recommandation clinique.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) pour permettre le criblage de sécurité
- Obtenir les données sur le mécanisme d'action et sur l'indication originale
- Mener des études précliniques ou cliniques testant directement maraviroc, en priorité dans le cancer du sein HER2 positif
- Clarifier la situation réglementaire (AMM annulées) et la disponibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

