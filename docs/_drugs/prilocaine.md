---
layout: default
title: Prilocaine
parent: Prédiction du modèle uniquement (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Prilocaine : nouvelle indication prédite, Conjonctivite papillaire (niveau de preuve L5). Indication d'origine : Éjaculation précoce"
monitor_inn: "prilocaine"
predicted_indications: ["papillary conjunctivitis", "manic bipolar affective disorder", "bronchitis", "migraine disorder", "neuralgia", "migraine with brainstem aura", "atopic eczema", "allergic asthma", "rhinitis", "rosacea conjunctivitis"]
---

# Prilocaine
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

# Prilocaïne : De l'éjaculation précoce à la papillary conjunctivitis (conjonctivite papillaire)

## Résumé en Une Phrase

La prilocaïne est un anesthésique local de type amide, associé à l'origine, dans les données compilées pour ce rapport, à l'éjaculation précoce et à la dyspareunie psychologique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **conjonctivite papillaire** (rang 1), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction.
Parmi les autres indications prédites, la **névralgie** (notamment post-zostérienne) est la mieux documentée, avec **2 essais cliniques** et **13 publications**, essentiellement avec la combinaison lidocaïne/prilocaïne (EMLA).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Éjaculation précoce ; dyspareunie psychologique (le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Conjonctivite papillaire |
| Score de Prédiction TxGNN | 99,78 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Uniquement des AMM annulées |
| Nombre d'AMM | 12 (toutes annulées) |
| Décision Recommandée | Hold |

> **Remarque :** pour la conjonctivite papillaire, le niveau de preuve est L5 (prédiction du modèle uniquement). Parmi les 10 premières prédictions, la névralgie est la plus avancée (niveau L3, statut « question de recherche »). Elle est détaillée ci-dessous à titre de comparaison.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la prilocaïne est un anesthésique local de la famille des amides, utilisé seul ou en association avec la lidocaïne (EMLA, Fortacin). Elle bloque les canaux sodiques voltage-dépendants, ce qui réduit la transmission de la douleur et la sensibilité cutanée ou muqueuse. Cet effet est cohérent avec ses usages d'origine (anesthésie de surface, retard de l'éjaculation par réduction de la sensibilité).

Pour la conjonctivite papillaire, le lien est **spéculatif** : un blocage des canaux sodiques pourrait atténuer les symptômes de surface oculaire, mais la prilocaïne n'est pas un agent ophtalmique et rien ne soutient son effet sur la maladie inflammatoire sous-jacente.

La **névralgie** offre une hypothèse plus plausible : le blocage sodique réduit les décharges ectopiques des nerfs périphériques lésés. Les données restent toutefois petites, anciennes et surtout non contrôlées, et comme l'EMLA est une association, la contribution propre de la prilocaïne ne peut pas être isolée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré pour la conjonctivite papillaire. Les essais ci-dessous concernent la **névralgie** (rang 5) et la **migraine** (rang 4), à titre de contexte.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00916942](https://clinicaltrials.gov/study/NCT00916942) | Phase 2 | Terminé | 20 | Étude ouverte de la crème lidocaïne 2,5 %/prilocaïne 2,5 % en prétraitement avant NGX-4010 (capsaïcine) dans la névralgie post-zostérienne ; évalue la tolérance, pas le traitement de la névralgie |
| [NCT06899438](https://clinicaltrials.gov/study/NCT06899438) | N/A | Terminé | 38 | Toxine botulique A comparée à la prilocaïne dans le syndrome myofascial douloureux ; preuve indirecte |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Terminé | 300 | Étude observationnelle de 24 semaines sur des AINS topiques contre la douleur ; aucun test de la prilocaïne dans la migraine |

---

## Preuves de la Littérature

Aucune publication n'est disponible pour la conjonctivite papillaire. Les références les plus pertinentes concernent la **névralgie** (rang 5).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [10342425](https://pubmed.ncbi.nlm.nih.gov/10342425/) | 1999 | ECR | Pain | Le prétraitement par EMLA n'a pas réduit la douleur induite par la capsaïcine 1 % (9 sujets sains) |
| [2616182](https://pubmed.ncbi.nlm.nih.gov/2616182/) | 1989 | Cohorte | Pain | Crème EMLA 5 % dans la névralgie post-zostérienne réfractaire (12 patients) : amélioration significative de la douleur à 6 h |
| [2493878](https://pubmed.ncbi.nlm.nih.gov/2493878/) | 1989 | Cohorte | BMJ | Crème lidocaïne-prilocaïne dans la névralgie post-zostérienne |
| [22182397](https://pubmed.ncbi.nlm.nih.gov/22182397/) | 2011 | Étude de tolérance | BMC Anesthesiology | Tolérance du patch de capsaïcine 8 % après prétraitement par lidocaïne/prilocaïne 2,5 %/2,5 % |
| [41777672](https://pubmed.ncbi.nlm.nih.gov/41777672/) | 2026 | Cohorte rétrospective | Front Aging Neurosci | EMLA seul versus bloc paravertébral + EMLA pour la tolérance du patch de capsaïcine 8 % |
| [8695081](https://pubmed.ncbi.nlm.nih.gov/8695081/) | 1996 | Cas clinique | J Clin Anesth | Traitement réussi par EMLA d'une névralgie post-zostérienne résistante |
| [1430539](https://pubmed.ncbi.nlm.nih.gov/1430539/) | 1992 | Revue | J Dermatol Surg Oncol | EMLA : anesthésique topique efficace et sûr, avec usage possible dans la névralgie post-zostérienne |
| [23314014](https://pubmed.ncbi.nlm.nih.gov/23314014/) | 2013 | Revue | Curr Opin Support Palliat Care | Prise en charge de la douleur persistante liée aux plaies |
| [40519459](https://pubmed.ncbi.nlm.nih.gov/40519459/) | 2025 | Revue | Cureus | Risques systémiques des anesthésiques topiques sur peau à barrière altérée (atopie, psoriasis) |
| [27397059](https://pubmed.ncbi.nlm.nih.gov/27397059/) | 2016 | Cas clinique | Pediatr Dermatol | Convulsions et méthémoglobinémie après application d'EMLA chez un enfant de 3,5 ans atteint de dermatite atopique |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63794766 | ANESDERM 5 %, crème | Crème | Non renseignée (AMM annulée) |
| 63396602 | EMLA 5 POUR CENT, crème | Crème | Non renseignée (AMM annulée) |
| 67458460 | EMLAPATCH 5 POUR CENT, pansement adhésif cutané | Pansement adhésif | Non renseignée (AMM annulée) |
| 60355340 | ORAQIX, gel périodontal | Gel | Non renseignée (AMM annulée) |
| 67099299 | FORTACIN 150 mg/ml / 50 mg/ml, spray cutané, solution | Solution pour pulvérisation | Non renseignée (AMM annulée) |

> Au total, 12 AMM sont recensées, toutes annulées (génériques de lidocaïne/prilocaïne inclus). Aucune AMM valide n'est actuellement en vigueur.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : hypertension, épilepsie, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, diabète et acidocétose diabétique, maladies coronariennes et infarctus du myocarde, maladies cardiovasculaires, troubles de la conduction cardiaque et blocs auriculo-ventriculaires, arrêt cardiaque soudain, insuffisance respiratoire, glaucome à angle fermé, myasthénie et maladies de la jonction neuromusculaire, déficit en butyrylcholinestérase, hémoglobinopathie, hyperthyroïdie (maladie de Basedow, thyrotoxicose).
- **Interactions médicamenteuses** : 22 interactions recensées, dont la majorité de niveau **majeur**. Les principales concernent des agents favorisant la méthémoglobinémie : métoclopramide, sulfasalazine, nitrite d'amyle, acide nitreux, monoxyde d'azote, rasburicase, dapsone (oral et topique), chloroquine, primaquine, quinine, tafénoquine, nitrate d'argent et sulfadiazine argentique topiques. S'y ajoutent d'autres anesthésiques locaux (lidocaïne, lidocaïne topique, benzocaïne topique, cinchocaïne topique), également de niveau majeur. Les interactions modérées (morphine liposomale) et mineures (hyaluronidase) sont moins préoccupantes.
- **Signaux de sécurité dans la littérature** : risque de méthémoglobinémie et de convulsions après application sur peau altérée ou chez le jeune enfant, allergie de contact à la prilocaïne et purpura rapportés après EMLA.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être compilées. Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la conjonctivite papillaire repose uniquement sur le modèle (L5), sans essai ni publication. De plus, toutes les AMM françaises sont annulées et le profil de sécurité (méthémoglobinémie, nombreuses interactions majeures) appelle à la prudence. Parmi les autres prédictions, seule la névralgie atteint le niveau L3, avec des données anciennes, petites et surtout non contrôlées sur une association lidocaïne/prilocaïne.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), car cette absence bloque le passage à l'évaluation de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Pour la conjonctivite papillaire : une justification mécanistique et des données précliniques ou cliniques, en tenant compte de l'absence de formulation ophtalmique de la prilocaïne.
- Pour la névralgie : des essais contrôlés isolant la contribution de la prilocaïne par rapport à la lidocaïne seule.
- Un plan de surveillance de la méthémoglobinémie, notamment chez les enfants, les patients à barrière cutanée altérée et ceux recevant des médicaments interagissant.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

