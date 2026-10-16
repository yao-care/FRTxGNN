---
layout: default
title: Isavuconazonium
parent: Prédiction du modèle uniquement (L5)
nav_order: 413
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Isavuconazonium : nouvelle indication prédite, Pneumocystose (niveau de preuve L5). Indication d'origine : Aspergillose, piedra blanche, piedra noire, coccidioïdomycose…"
monitor_inn: "isavuconazonium"
predicted_indications: ["pneumocystosis", "mycetoma"]
---

# Isavuconazonium
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Isavuconazonium : Des mycoses systémiques à la pneumocystose

## Résumé en une phrase

L'isavuconazonium est un antifongique triazolé (promédicament de l'isavuconazole), initialement utilisé pour traiter l'aspergillose, la mucormycose (zygomycose), la coccidioïdomycose, l'histoplasmose et d'autres mycoses.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **pneumocystose** (score de 99,56 %), mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.
Une seconde prédiction, le **mycétome** (score de 99,34 %), repose sur une seule revue indirecte. Elle est présentée en complément.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Aspergillose, piedra blanche, piedra noire, coccidioïdomycose, sporotrichose, histoplasmose, zygomycose (le texte d'indication des AMM n'est pas renseigné ; ces indications proviennent du graphe de connaissances) |
| Nouvelle indication prédite | Pneumocystose |
| Score de prédiction TxGNN | 99,56 % |
| Niveau de preuve | L5 |
| Statut de marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision recommandée | Hold |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier compilé. D'après les connaissances générales, l'isavuconazonium est le promédicament de l'isavuconazole, un triazole qui inhibe la lanostérol 14-alpha-déméthylase (CYP51) et bloque ainsi la synthèse de l'ergostérol, composant essentiel de la membrane des champignons.

Le lien de la prédiction avec la pneumocystose est **biologiquement faible**. *Pneumocystis jirovecii* ne possède pas d'ergostérol et utilise le cholestérol et d'autres stérols dans sa membrane : la cible des azolés n'est donc pas clairement présente. De plus, les azolés ne sont pas un traitement établi de la pneumonie à *Pneumocystis* (le cotrimoxazole, associant triméthoprime et sulfaméthoxazole, reste la référence). La prédiction provient vraisemblablement d'associations de classe antifongique dans le graphe de connaissances et n'est pas étayée par un raisonnement mécanistique solide.

À titre de comparaison, la seconde prédiction (le mycétome) est plus plausible. L'eumycétome est causé par des champignons filamenteux (par ex. *Madurella mycetomatis*), cibles plausibles d'un triazole à large spectre. D'autres azolés (itraconazole, fosravuconazole dans un essai récent de phase 2) ont montré une activité clinique. L'actinomycétome, d'origine bactérienne, ne répondrait pas à un azolé.

---

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement, que ce soit pour la pneumocystose ou pour le mycétome.

---

## Preuves de la littérature

Aucune littérature associée disponible actuellement pour la pneumocystose.

Pour la prédiction secondaire (mycétome) :

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Revue | Parasites & Vectors | Revue du pipeline de médicaments pour les maladies tropicales négligées (anti-infectieux oraux et associations pour usage hors AMM) ; preuve indirecte |

---

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 69181040 | CRESEMBA 100 mg, gélule | Gélule | Non renseignée (AMM annulée) |
| 60184590 | CRESEMBA 200 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |

---

## Considérations de sécurité

- **Interactions médicamenteuses** : 177 interactions ont été recensées. Parmi les exemples figurant dans les données :
  - **Majeures** : clarithromycine, éliglustat, cisapride.
  - **Modérées** : hydrocortisone, metformine, pioglitazone, lopéramide, bupropion, aprépitant, triamcinolone, dexaméthasone, bétaméthasone, budésonide, cimétidine, saxagliptine, empagliflozine, linagliptine, clotrimazole.
  - **Mineure** : fidaxomicine.

Veuillez consulter la notice pour les mises en garde et contre-indications.

---

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la pneumocystose repose uniquement sur le score du modèle (L5), sans essai ni publication, et son fondement biologique est faible (absence d'ergostérol chez *Pneumocystis*, traitement de référence différent).
- En outre, les deux AMM françaises sont annulées et les données de sécurité de la notice sont absentes, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), point bloquant.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Pour la pneumocystose : données précliniques ou cliniques démontrant une activité de l'isavuconazole sur *Pneumocystis*.
- Pour le mycétome (piste secondaire plus plausible) : recherche ciblée de données in vitro ou cliniques sur l'eumycétome et clarification du statut réglementaire en France.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

