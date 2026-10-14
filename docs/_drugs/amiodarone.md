---
layout: default
title: Amiodarone
parent: Prédiction du modèle uniquement (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarone : De la fibrillation ventriculaire à la tachycardie ventriculaire polymorphe catécholaminergique

## Résumé en Une Phrase

Amiodarone est un antiarythmique initialement utilisé pour le traitement de la fibrillation ventriculaire.
Le modèle TxGNN prédit en première position qu'il pourrait être efficace pour la **tachycardie ventriculaire polymorphe catécholaminergique (TVPC)**, mais cette prédiction n'est soutenue par **aucun essai clinique** et par **9 publications** de faible niveau de preuve (une revue systématique, deux cohortes, une revue narrative et cinq cas cliniques), qui ne démontrent pas d'efficacité.
Les données compilées pour ce rapport montrent que la tachycardie ventriculaire (**17 essais cliniques**, **20 publications**) et la tachycardie ventriculaire incessante du nourrisson (**20 publications**, dont un essai randomisé) sont des pistes nettement mieux documentées.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Fibrillation ventriculaire (le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Tachycardie ventriculaire polymorphe catécholaminergique |
| Score de Prédiction TxGNN | 99,78 % |
| Niveau de Preuve | L4 (pour cette indication) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold (pour la TVPC) |

**Autres indications prédites, à titre de comparaison :**

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Décision |
|------|------|------|------|------|
| 2 | Tachycardie ventriculaire incessante du nourrisson | 99,65 % | L2 | Question de recherche |
| 3 | Tachycardie ventriculaire | 99,64 % | L1 | Proceed with Guardrails |
| 4 | Bloc de branche (libellé obsolète) | 99,58 % | L5 | Hold |
| 5 | Polyarthrite rhumatoïde | 99,40 % | L5 | Hold |
| 6 à 10 | Syndrome brachydactylie-syndactylie, déficit en cofacteur II de l'héparine, trichotillomanie, syndrome de microphtalmie colobomateuse avec dysplasie rhizomélique, goutte | 99,19 % à 99,38 % | L5 | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les informations connues, l'amiodarone est un antiarythmique de classe III qui bloque les canaux potassiques cardiaques et prolonge la repolarisation. Elle agit aussi sur les canaux sodiques et calciques et exerce un effet antagoniste bêta-adrénergique. Son efficacité dans la fibrillation ventriculaire est établie.

Pour la TVPC, un lien mécanistique est plausible : les effets bêta-bloquants et sur la gestion du calcium touchent une arythmie déclenchée par les catécholamines et liée aux mutations de RYR2. Toutefois, la littérature décrit l'amiodarone surtout comme peu efficace ou comme traitement d'appoint dans les cas réfractaires. Les traitements de référence sont les bêta-bloquants et la flécaïnide. **Le score TxGNN très élevé n'est donc pas corroboré par des données d'efficacité clinique.**

La prédiction est bien plus solide pour la tachycardie ventriculaire, très proche de l'indication d'origine. Il s'agit là d'une pratique clinique établie, plus proche d'une indication voisine de l'indication d'origine que d'un véritable repositionnement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la TVPC.

À titre de référence, voici les principaux essais disponibles pour la **tachycardie ventriculaire** (indication de rang 3, sur 17 essais recensés, les plus pertinents sont présentés) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00000531](https://clinicaltrials.gov/study/NCT00000531) | Phase 3 | Terminé | Non renseigné | AVID : défibrillateur implantable vs traitement antiarythmique (principalement amiodarone) après mort subite récupérée |
| [NCT01401647](https://clinicaltrials.gov/study/NCT01401647) | Phase 3 | Terminé | 3024 | ALPS : amiodarone vs lidocaïne vs placebo dans l'arrêt cardiaque extrahospitalier par FV/TV sans pouls |
| [NCT00383799](https://clinicaltrials.gov/study/NCT00383799) | Phase 4 | Arrêté | 302 | PROCAMIO : amiodarone IV vs procaïnamide IV dans la tachycardie à QRS larges bien tolérée |
| [NCT03299517](https://clinicaltrials.gov/study/NCT03299517) | Phase 4 | Inconnu | 80 | Amiodarone vs lidocaïne dans la TV stable aux urgences |
| [NCT00257959](https://clinicaltrials.gov/study/NCT00257959) | Phase 4 | Terminé | 400 | OPTIC : amiodarone + bêta-bloquant vs bêta-bloquant seul vs sotalol pour prévenir les chocs du défibrillateur |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Phase 4 | Terminé | 416 | VANISH2 : ablation par cathéter vs traitement antiarythmique après infarctus avec TV monomorphe soutenue |
| [NCT01722942](https://clinicaltrials.gov/study/NCT01722942) | Non applicable | Inconnu | 1100 | CHAGASICS : amiodarone vs défibrillateur implantable dans la cardiomyopathie de Chagas |
| [NCT03855826](https://clinicaltrials.gov/study/NCT03855826) | Phase 4 | Inconnu | 756 | Nifékalant (amiodarone probablement en comparateur) dans la TV et la FV |

## Preuves de la Littérature

**Pour la TVPC (indication de rang 1) :**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Revue systématique | Life (Basel) | Caractéristiques cliniques, génétiques et évolution rythmique de patients chinois atteints de TVPC ; ne porte pas sur l'efficacité de l'amiodarone |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohorte | Rev Cardiovasc Med | Caractéristiques cliniques, génétiques et coûts de santé de la TVPC dans une ville chinoise |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Revue | Expert Opin Pharmacother | Avancées du traitement pharmacologique des arythmies ventriculaires |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Cas clinique | PACE | La flécaïnide supprime l'orage rythmique induit par le défibrillateur dans la TVPC |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Cas clinique | Front Cardiovasc Med | Résolution de la TVPC par dénervation sympathique cardiaque droite après dénervation gauche |

**Pour la tachycardie ventriculaire incessante du nourrisson (rang 2), les plus pertinentes :**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [16316969](https://pubmed.ncbi.nlm.nih.gov/16316969/) | 2005 | ECR | Circulation | Amiodarone IV dans les tachyarythmies incessantes de l'enfant, essai randomisé en double aveugle |
| [14508682](https://pubmed.ncbi.nlm.nih.gov/14508682/) | 2003 | Cohorte | Eur J Pediatr | Efficacité et sécurité de l'amiodarone IV chez 23 nourrissons avec tachycardies incessantes |
| [2114081](https://pubmed.ncbi.nlm.nih.gov/2114081/) | 1990 | Série de cas | Arch Mal Coeur Vaiss | Tachycardie ventriculaire idiopathique incessante du nourrisson : réduction de l'arythmie sous amiodarone orale dans 5 cas |

**Pour la tachycardie ventriculaire (rang 3), les plus pertinentes :**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27354046](https://pubmed.ncbi.nlm.nih.gov/27354046/) | 2017 | ECR | Eur Heart J | PROCAMIO : procaïnamide IV vs amiodarone IV dans la tachycardie à QRS larges tolérée |
| [30084131](https://pubmed.ncbi.nlm.nih.gov/30084131/) | 2018 | Cohorte | Emerg Med Australas | Amiodarone administrée par les paramédicaux dans la TV stable en préhospitalier |
| [20730062](https://pubmed.ncbi.nlm.nih.gov/20730062/) | 2010 | Revue | Vasc Health Risk Manag | L'amiodarone, traitement antiarythmique de référence pour la FV et la TV |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62305927 | CORDARONE 150 mg/3 ml, solution injectable en ampoule (IV) | Solution injectable | Non renseignée (AMM annulée) |
| 64408662 | CORDARONE 200 mg, comprimé sécable | Comprimé sécable | Non renseignée (AMM annulée) |
| 68973926 | CORDARONE 200 mg, comprimé sécable (BB FARMA, Italie) | Comprimé sécable | Non renseignée (AMM annulée) |
| 60662396 | CORDARONE 200 mg, comprimé sécable (DIFARMED, Espagne) | Comprimé sécable | Non renseignée (AMM annulée) |

Les quatre AMM recensées sont annulées : aucune AMM valide n'apparaît dans les données compilées.

## Cytotoxicité

Non applicable : l'amiodarone n'est pas un médicament antinéoplasique.

## Considérations de Sécurité

**Contre-indications et pathologies à risque (issues du graphe de connaissances, et non du texte de la notice) :**
- **Cardiaques** : syndrome du QT long (y compris familial), torsades de pointes, bloc auriculo-ventriculaire, maladie du sinus
- **Thyroïdiennes** : hypothyroïdie (dont myxœdème et hypothyroïdie congénitale), hyperthyroïdie, maladie de Basedow, thyrotoxicose
- **Pulmonaires** : pneumopathie interstitielle, pneumonie à éosinophiles, éosinophilie pulmonaire, alvéolite allergique extrinsèque, pneumopathie d'hypersensibilité, poumon du fermier
- **Hépatiques et biliaires** : maladie du foie, lésion hépatique d'origine médicamenteuse, maladie de la vésicule biliaire
- **Neurologiques et oculaires** : maladie du système nerveux périphérique, neuropathie périphérique, névrite optique, maladie du nerf optique, maladie des voies visuelles, dépôts cornéens
- **Métaboliques** : carence en potassium

**Interactions médicamenteuses :** 100 interactions sont recensées. Parmi les exemples retrouvés :
- **Majeures** : amphotéricine B (et ses formes lipidiques, liposomale et au sulfate de cholestéryle), cisapride, clarithromycine, clotrimazole, dexaméthasone, hydrocortisone, dolasétron, éliglustat, agalsidase bêta
- **Modérées** : famotidine, cimétidine, aprépitant, bisacodyl, budésonide, huile de ricin
- **Mineure** : fidaxomicine

Le texte officiel des mises en garde de la notice n'a pas pu être exploité. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold (pour la TVPC)**

**Justification :**
- Aucun essai clinique ni donnée d'efficacité ne soutient l'amiodarone dans la TVPC, où les bêta-bloquants et la flécaïnide restent les traitements établis. Le score TxGNN élevé n'est pas confirmé par la clinique. Parmi les autres prédictions, la tachycardie ventriculaire (L1, Proceed with Guardrails) est la mieux étayée, mais elle relève d'une pratique établie proche de l'indication d'origine. La tachycardie ventriculaire incessante du nourrisson (L2) reste une question de recherche. Les prédictions de rang 4 à 10 sont purement algorithmiques (L5), certaines avec un risque de nocivité (bloc de branche, polyarthrite rhumatoïde avec toxicité pulmonaire).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (consultation de DrugBank)
- Mises en garde et contre-indications issues de la notice officielle (ANSM), indispensables avant tout dépistage de sécurité
- Pour la tachycardie ventriculaire : surveillance pulmonaire, thyroïdienne, hépatique et de l'intervalle QT, ainsi qu'une gestion rigoureuse des interactions médicamenteuses
- Pour la forme pédiatrique : évaluation de la sécurité (thyroïde, poumon, effets hémodynamiques) et données portant spécifiquement sur la tachycardie ventriculaire, la population de l'essai randomisé étant mixte (essentiellement supraventriculaire et jonctionnelle)
- Clarification du statut réglementaire : toutes les AMM françaises recensées sont annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

