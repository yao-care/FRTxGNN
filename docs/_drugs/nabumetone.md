---
layout: default
title: Nabumetone
parent: Prédiction du modèle uniquement (L5)
nav_order: 520
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "nabumetone"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis"]
description: "Nabumetone : nouvelle indication prédite, Dysplasie acromésomélique de type Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (niveau de preuve L5). Indication d'origine : Non renseigné…"
---

# Nabumetone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Nabumetone: Dysplasie acromésomélique de type Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Résumé en Une Phrase

La nabumétone est un anti-inflammatoire non stéroïdien (AINS), initialement utilisé pour traiter la polyarthrite rhumatoïde, l'arthrose et les arthropathies.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **dysplasie acromésomélique de type Hunter-Thompson**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.
Cette prédiction repose uniquement sur le modèle TxGNN (apprentissage profond) (niveau de preuve L5) ; son score peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base. D'après les connaissances pharmacologiques générales, la nabumétone est un AINS à préférence pour la COX-2, dont l'effet passe par son métabolite actif, la 6-MNA. Son efficacité est établie dans les affections articulaires inflammatoires et dégénératives (polyarthrite rhumatoïde, arthrose).

La dysplasie acromésomélique de type Hunter-Thompson est une maladie squelettique rare, due à des mutations avec perte de fonction de *CDMP1/GDF5* qui perturbent la formation du cartilage. L'inhibition des COX ne corrige pas ce défaut génétique. **Aucun lien mécanistique établi n'a été identifié.**

Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Cette prédiction doit donc être considérée avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 64224915 | NABUCOX 500 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée | Active |
| 60774655 | NABUCOX 1 g, comprimé dispersible | Comprimé dispersible | Non renseignée | Active |

Les deux AMM, détenues par EXPANSCIENCE, sont annulées : il n'existe actuellement aucune présentation commercialisée en France.

## Considérations de Sécurité

Les textes de mises en garde et de contre-indications de la notice n'ont pas pu être récupérés. Veuillez consulter la notice pour les informations de sécurité officielles.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, ulcère gastroduodénal (dont actif), troubles de la coagulation, infarctus du myocarde, thrombose coronaire, maladie cardiovasculaire et cardiopathie, hémoglobinopathie, abus de substances/dépendance.
- **Interactions médicamenteuses** : 217 interactions recensées. Parmi les exemples :
  - Niveau modéré : acide acétylsalicylique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), metformine, glimépiride, chlorpropamide, mésalazine, balsalazide, vancomycine, citrate et bicarbonate de potassium, laxatifs osmotiques ou préparations coliques (picosulfate, sulfate de sodium, macrogol avec électrolytes).
  - Niveau mineur : ranitidine, cimétidine, linaclotide.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune preuve clinique ou publiée ne soutient cette prédiction, et aucun lien mécanistique plausible n'existe : la COX n'intervient pas dans le défaut génétique de *GDF5*.
- Le médicament n'a plus d'AMM valide en France, et le profil de sécurité (risques cardiovasculaires, rénaux, hépatiques et gastro-intestinaux) est peu favorable pour une maladie génétique rare du développement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (DrugBank).
- Mises en garde et contre-indications officielles de la notice ANSM.
- Données précliniques montrant un effet sur la voie GDF5/chondrogenèse.

**Autres prédictions du modèle (pour information) :**
Parmi les dix premières prédictions, deux relèvent du niveau L4 (« question de recherche ») : la **susceptibilité aux spondylarthropathies** (les AINS sont un traitement de première ligne, mais l'argument ne repose que sur l'effet de classe) et la **nodulose rhumatoïde** (proximité avec l'indication approuvée dans la polyarthrite rhumatoïde, sans preuve spécifique). Parmi les prédictions squelettiques, la **pseudoachondroplasie** est la plus plausible sur le plan biologique, mais uniquement pour un soulagement symptomatique de la douleur articulaire secondaire. Les autres prédictions (brachyolmie, syndrome brachydactylie-syndactylie, myosclérose, syndrome de WHIM, etc.) n'ont aucun fondement mécanistique identifié.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

