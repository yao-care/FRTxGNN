---
layout: default
title: Filgrastim
parent: Prédiction du modèle uniquement (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim : De la neutropénie congénitale sévère au trouble hémorragique de type plaquettaire

## Résumé en Une Phrase

Filgrastim (G-CSF) est un facteur de croissance de la lignée myéloïde, initialement utilisé dans les neutropénies constitutionnelles, dont la neutropénie congénitale sévère.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble hémorragique de type plaquettaire** (rang 10 des prédictions), mais **aucune publication** n'étaye cette piste et **7 essais cliniques** seulement, tous indirects (greffe de cellules souches où le filgrastim est probablement un traitement de soutien), y sont associés.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Neutropénie constitutionnelle / neutropénie congénitale sévère (source : graphe de connaissances ; aucun texte d'indication n'est disponible dans les AMM) |
| Nouvelle Indication Prédite | Primary release disorder of platelets (trouble primaire de la sécrétion plaquettaire), prédiction de rang 1 ; la prédiction de rang 10 (trouble hémorragique de type plaquettaire) est la seule à disposer d'essais associés |
| Score de Prédiction TxGNN | 99,9976 % (rang rapporté : 107) |
| Niveau de Preuve | L5 (rang 1) ; L4 pour le rang 10 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 16 (toutes annulées ; aucune valide) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, le filgrastim est un facteur de stimulation des colonies de granulocytes (G-CSF) qui favorise la prolifération et la différenciation des progéniteurs de neutrophiles. Son efficacité est établie dans les neutropénies, mais il n'agit pas directement sur la fonction ou la production des plaquettes.

Pour les prédictions classées en tête, aucun lien mécanistique plausible n'est identifié :
- **Trouble primaire de la sécrétion plaquettaire** : G-CSF n'a pas d'effet connu sur la sécrétion des granules ni sur la signalisation plaquettaire.
- **Pseudo-maladie de von Willebrand** : trouble par gain de fonction de la GPIb-alpha ; G-CSF ne cible pas l'axe GPIb-IX-V/VWF.
- **Thrombasthénie de Glanzmann** : défaut de l'intégrine αIIbβ3, non corrigé par G-CSF. Il peut seulement servir de soutien (mobilisation ou prise de greffe) lors d'une greffe de cellules souches, ce qui n'est pas un effet thérapeutique.
- **Autres prédictions** (syndrome de Scott, défaut du récepteur du collagène, déficit en inhibiteur de C1, serpinopathies, thrombopénie néonatale alloimmune) : aucune relation pharmacologique identifiée ; les scores élevés reflètent probablement une proximité dans le graphe et non un lien biologique.

Le score élevé du modèle est donc une prédiction purement computationnelle, sans appui expérimental ou clinique.

## Preuves d'Essais Cliniques

Aucun essai n'est enregistré pour la prédiction de rang 1. Pour la prédiction de rang 10 (trouble hémorragique de type plaquettaire), les essais suivants sont associés. Ils portent tous sur des greffes de cellules souches dans des hémopathies, où le filgrastim est vraisemblablement un traitement de soutien ; ils ne démontrent pas d'effet sur un trouble plaquettaire.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Terminé | 25 | Greffe allogénique de cellules souches périphériques à faible dose dans des hémopathies malignes de bas grade à haut risque |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Terminé | Non renseignée | Augmentation de la moelle par cellules CD34 enrichies pour greffe allogénique dans les hémopathies malignes |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Terminé | 55 | Greffe de plusieurs unités de sang de cordon après conditionnement non myéloablatif (hémopathies, aplasie médullaire sévère) |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Retiré | 0 | Busulfan/fludarabine avant greffe de donneur non apparenté ; aucune donnée exploitable |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Inconnu | 35 | Greffe allogénique non myéloablative (donneurs non apparentés) dans hémopathies malignes, cancer du rein et aplasie médullaire |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Terminé | 20 | Greffe haplo-identique déplétée en lymphocytes T à intensité réduite |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Terminé | Non renseignée | Greffe de donneur partiellement compatible déplétée en lymphocytes T avec cellules « veto » CD34 |

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Toutes les AMM sont annulées. Le texte d'indication approuvée n'est pas disponible dans les données compilées. Les 5 premières AMM sont listées ci-dessous (sur 16).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60670037 | ZARZIO 30 MU/0,5 mL, seringue préremplie | Solution injectable ou pour perfusion | Sandoz (Autriche) |
| 66749096 | NEUPOGEN 48 MU/0,5 mL, seringue préremplie | Solution injectable | Amgen Europe |
| 69287684 | NIVESTIM 30 MU/0,5 mL | Solution injectable ou pour perfusion | Pfizer Europe MA EEIG (Belgique) |
| 69225686 | NEUPOGEN 30 MU (0,3 mg/mL) | Solution injectable | Amgen Europe |
| 65313021 | TEVAGRASTIM 48 MUI/0,8 mL | Solution injectable ou pour perfusion | Teva (Allemagne) |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions ont été recensées, dont les premières de niveau modéré (source DDInter) : iobenguane (I-131), fludésoxyglucose (18F), ibritumomab tiuxétan, tositumomab (avec ou sans I-131), lévamisole, triméetrexate, mercaptopurine, abémaciclib, paclitaxel, acalabrutinib, aldesleukine, alemtuzumab, altrétamine, trioxyde d'arsenic, asparaginase, avapritinib, azacitidine, belantamab mafodotin, bendamustine. Il s'agit surtout d'agents antinéoplasiques et de radiopharmaceutiques.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les prédictions reposent uniquement sur le graphe (niveau L5 pour la plupart ; L4 pour le rang 10) : aucun lien mécanistique plausible, aucune publication, et des essais seulement indirects où le filgrastim est un soutien de greffe. De plus, les 16 AMM françaises sont annulées et les données de sécurité de la notice sont absentes (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (site de l'ANSM) pour permettre le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Réaliser une revue de la littérature ciblée sur les troubles plaquettaires et le G-CSF
- Établir un rationnel biologique ou des données précliniques avant tout essai clinique
- Vérifier la disponibilité actuelle du filgrastim en France (statut des AMM annulées, voies d'administration)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

