---
layout: default
title: Propafenone
parent: Preuves modérées (L3-L4)
nav_order: 635
evidence_level: L3
indication_count: 8
last_modified_at: 2026-10-14
description: "Propafenone : nouvelle indication prédite, Tachycardie ventriculaire polymorphe catécholergique (niveau de preuve L3). Indication d'origine : Fibrillation auriculaire…"
monitor_inn: "propafenone"
predicted_indications: ["manic bipolar affective disorder", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
---

# Propafenone
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **8** 
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

# Propafénone : De la fibrillation auriculaire à la tachycardie ventriculaire polymorphe catécholergique

## Résumé en Une Phrase

La propafénone est un antiarythmique de classe IC, initialement utilisé pour le traitement de la fibrillation auriculaire et de la tachycardie ventriculaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **tachycardie ventriculaire polymorphe catécholergique (TVPC)**, avec **10 publications** (études précliniques, cohortes et rapports de cas) et **aucun essai clinique enregistré** à ce jour.

> Remarque : la prédiction au rang 1 du modèle est la « manie (trouble bipolaire) ». Elle n'est pas retenue comme indication principale, car la littérature disponible décrit la propafénone comme une cause possible de manie, et non comme un traitement. La TVPC (rang 2, score quasi identique) est la piste la mieux étayée et est présentée ici.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Fibrillation auriculaire, tachycardie ventriculaire (le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Tachycardie ventriculaire polymorphe catécholergique |
| Score de Prédiction TxGNN | 99,79 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la propafénone fait partie des antiarythmiques de classe IC (bloqueurs des canaux sodiques) et son efficacité dans les arythmies supraventriculaires et ventriculaires est établie. Elle possède aussi une activité bêtabloquante légère.

La TVPC est une canalopathie cardiaque héréditaire rare, liée le plus souvent à des mutations du récepteur de la ryanodine de type 2 (RyR2) ou de la calséquestrine, qui provoquent des fuites de calcium et des arythmies ventriculaires lors d'un stress adrénergique. Des études précliniques (PMID 21270101, 21798265, 26121139) montrent que la propafénone, comme la flécaïnide, inhibe les canaux RyR2 et supprime les ondes calciques arythmogènes. Cette inhibition de RyR2 contribuerait à l'efficacité des antiarythmiques de classe I dans la TVPC. Un rapport de cas décrit en outre 35 ans de traitement efficace par propafénone (PMID 30820400).

Le lien mécanistique est donc plausible, mais la flécaïnide reste le comparateur établi. Les preuves se limitent à des études mécanistiques, des rapports de cas et des cohortes observationnelles.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30820400](https://pubmed.ncbi.nlm.nih.gov/30820400/) | 2019 | Rapport de cas | HeartRhythm Case Reports | Traitement efficace de la TVPC par propafénone pendant 35 ans |
| [21270101](https://pubmed.ncbi.nlm.nih.gov/21270101/) | 2011 | Préclinique/mécanistique | Circ Arrhythm Electrophysiol | L'inhibition de RyR2 détermine l'efficacité des antiarythmiques de classe I dans la TVPC |
| [26121139](https://pubmed.ncbi.nlm.nih.gov/26121139/) | 2015 | Préclinique/mécanistique | PLoS One | L'activité de RyR2 détermine la puissance de la flécaïnide et de la R-propafénone contre les ondes calciques |
| [21798265](https://pubmed.ncbi.nlm.nih.gov/21798265/) | 2011 | Préclinique/mécanistique | J Mol Cell Cardiol | Criblage des antiarythmiques de classe I contre les ondes Ca2+ dans des myocytes sans calséquestrine |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Revue systématique (cohortes) | Life (Basel) | Caractéristiques cliniques, génétiques et évolution des patients chinois atteints de TVPC |
| [39564160](https://pubmed.ncbi.nlm.nih.gov/39564160/) | 2024 | Cohorte | Ann Pediatr Cardiol | Évolution à long terme (plus de 10 ans) des patients atteints de TVPC |
| [23965883](https://pubmed.ncbi.nlm.nih.gov/23965883/) | 2013 | Cohorte | Zhongguo Dang Dai Er Ke Za Zhi | Facteurs prédictifs d'arythmie ventriculaire, effet des médicaments et pronostic à long terme dans la TVPC |
| [36082968](https://pubmed.ncbi.nlm.nih.gov/36082968/) | 2023 | Préclinique/mécanistique | Clin Exp Pharmacol Physiol | Mutation R1760W-RyR2 à gain de fonction dans la TVPC |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Rapport de cas | Medicine | Diagnostic tardif de TVPC avec mutation RYR2 chez un enfant |
| [42558477](https://pubmed.ncbi.nlm.nih.gov/42558477/) | 2026 | Rapport de cas | Front Pediatr | Chevauchement syndrome du QT long/TVPC dans la calmodulinopathie CALM2 |

Seules quelques-unes de ces publications portent directement sur la propafénone ; les autres décrivent la maladie ou le contexte mécanistique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66843923 (annulée) | RYTHMOL 300 mg, comprimé pelliculé sécable (VIATRIS MEDICAL) | Comprimé pelliculé sécable | Non renseignée |

## Considérations de Sécurité

Les données de la notice (mises en garde, contre-indications) ne sont pas disponibles. Les éléments ci-dessous proviennent du graphe de connaissances et ne reflètent pas le texte officiel de la notice.

- **Contre-indications issues du graphe de connaissances** :
  - Cardiaques : syndrome du QT long (y compris familial), torsades de pointes, infarctus du myocarde, maladie coronarienne, athérosclérose, hypotension.
  - Hématologiques : agranulocytose, neutropénies (dont formes congénitales), hémoglobinopathie.
  - Métaboliques, hépatiques et rénaux : insuffisance rénale, atteinte hépatique, maladie de la vésicule biliaire, déficit en potassium.
  - Neuromusculaires : myasthénie grave.
- **Interactions médicamenteuses** : 190 interactions recensées. Parmi celles listées :
  - **Majeures** : dolasétron, éliglustat.
  - **Modérées** : famotidine, cimétidine, clarithromycine, lévofloxacine, ondansétron, palonosétron, bupropion, aprépitant, alosétron, lopéramide, lorcasérine, lactulose, lactitol, bisacodyl, picosulfate, macrogol et sulfate de sodium.
  - **Mineure** : métronidazole.
- **Signaux de sécurité dans la littérature** : élargissement du QRS et tachycardie ventriculaire incessante induits par la propafénone en cas de cardiomyopathie arythmogène du ventricule droit (PMID 33194879, 8316922). Cas de manie et d'interactions psychiatriques (PMID 2579063, 11949740).

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- La TVPC est la prédiction la mieux soutenue : mécanisme plausible via l'inhibition de RyR2, études précliniques concordantes et un cas de traitement prolongé efficace. Le niveau de preuve reste toutefois L3, sans essai enregistré, et la flécaïnide demeure la référence.
- La propafénone n'est plus commercialisée en France (AMM annulée), et les données de sécurité officielles sont absentes. Cela justifie de n'avancer que dans un cadre strictement encadré, au stade de question de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM, car l'étape de criblage de sécurité ne peut être franchie sans elle.
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank).
- Comparer à la flécaïnide (efficacité et tolérance) et rechercher ou concevoir des études cliniques prospectives dans la TVPC.
- Évaluer le risque proarythmique et les contre-indications cardiaques (QT long, cardiopathie structurelle, cardiopathie ischémique), ainsi que la faisabilité d'un accès au médicament malgré l'AMM annulée.

## Autres prédictions du modèle (non retenues)

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Recommandation |
|------|------|------|------|------|
| 1 | Manie (trouble bipolaire) | 99,80 % | L5 | Hold : la littérature décrit la propafénone comme cause de manie, donc un risque et non un bénéfice |
| 3 | Paralysie périodique avec syndrome compartimental transitoire | 99,67 % | L5 | Hold : aucune donnée |
| 4 | Angor de Prinzmetal | 99,45 % | L5 | Hold : aucun bénéfice établi, prudence en cardiopathie ischémique |
| 5 | Tachycardie ventriculaire incessante du nourrisson | 99,44 % | L3 | Question de recherche : données anciennes, de petite taille, observationnelles ; évaluation de sécurité préalable |
| 6 | Cardiomyopathie arythmogène du ventricule droit | 99,42 % | L4 | Hold : signaux de sécurité (proarythmie) |
| 7 | Syndrome néphrogénique d'antidiurèse inappropriée | 99,23 % | L5 | Hold : aucune donnée |
| 8 | Trichotillomanie | 99,17 % | L5 | Hold : aucune donnée |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

