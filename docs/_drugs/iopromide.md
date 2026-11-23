---
layout: default
title: Iopromide
parent: Prédiction du modèle uniquement (L5)
nav_order: 408
evidence_level: L5
indication_count: 9
monitor_inn: "IOPROMIDE"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-11-24
description: "Iopromide : nouvelle indication prédite, Arthrose (osteoarthritis) (niveau de preuve L5). En France, AMM dans la BDPM : 4 (valides : 3)"
---

# Iopromide
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

## Iopromide: Arthrose (osteoarthritis)
{: .text-alpha }

## Résumé en Une Phrase

Iopromide est un produit de contraste iodé non ionique, utilisé en imagerie diagnostique (spécialité Ultravist).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**arthrose**, mais il s'agit d'une prédiction purement informatique :
**aucun essai clinique** et **aucune publication** ne la soutiennent actuellement dans les données compilées pour ce rapport.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Arthrose (osteoarthritis) |
| Score de Prédiction TxGNN | 0.9953 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 4) |
| Nombre d'AMM | 4 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Iopromide (traduction non officielle) : « L'injection intravasculaire d'iopromide opacifie les vaisseaux dans lesquels le produit de contraste est présent, permettant la visualisation radiographique des structures internes par atténuation des photons. Lors de l'imagerie du corps, les produits de contraste iodés diffusent des vaisseaux vers l'espace extravasculaire. » Texte original en anglais : "Intravascular injection of iopromide opacifies those vessels where the contrast agent is present, permitting radiographic visualization of the internal structures through attenuation of photons. In imaging of the body, iodinated contrast agents diffuse from the vessels into the extravascular space." ([DailyMed: Ultravist (iopromide) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df917c3a-59a2-4ed1-8470-8a5394c73325), version du 2026-03-02 ; consulté le 2026-11-19). Iopromide est un agent de contraste iodé non ionique : il sert à rendre visibles les structures anatomiques à l'imagerie et n'a pas d'activité pharmacologique connue sur les maladies articulaires.

Le score élevé du modèle TxGNN (deep learning) (0,9953) provient du modèle et peut refléter des similarités apprises par le modèle entre maladies apparentées (maladies articulaires ou squelettiques), et non une justification biologique. L'usage du produit en arthrographie est un acte diagnostique, pas un effet thérapeutique.

Il n'est donc pas possible, en l'état, d'établir un lien mécanistique entre l'usage d'origine et l'arthrose. Les autres prédictions du modèle présentent la même limite : polyarthrite rhumatoïde (0.9937), brachyolmie (0.9919), dysplasie acromésomélique de type Hunter-Thompson (0.9914), syndrome brachyolmie-amélogenèse imparfaite (0.9912), alopécie (0.9911), myosclérose (0.9909), hémoglobinopathie (0.9908) et pseudoachondroplasie (0.9906). Aucune n'a de mécanisme plausible ni de preuve clinique ou bibliographique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68373358 | Ultravist 300 (300 mg d'iode/mL) | Solution injectable | Non renseignée |
| 62729413 | Ultravist 370 (370 mg d'iode/mL) | Solution injectable | Non renseignée |
| 65027575 | Ultravist 370 (370 mg d'iode/mL), seringue préremplie pour injecteur automatique | Solution injectable | Non renseignée |
| 60385522 | Ultravist 300 (300 mg d'iode/mL), seringue préremplie pour injecteur automatique | Solution injectable | Non renseignée |

Les quatre AMM, détenues par Bayer Healthcare, sont valides et concernent le médicament seul.

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées. Parmi les premières, les interactions de niveau majeur concernent notamment :
  - metformine ;
  - amphotéricine B (y compris formes lipidique, sulfate de cholestéryle et liposomale) ;
  - mésalazine, balsalazide, olsalazine et sulfasalazine ;
  - vancomycine ;
  - aminosides (kanamycine, néomycine, streptomycine) ;
  - polymyxine B.

  Le mannitol présente une interaction de niveau modéré. Plusieurs autres (clotrimazole, acide acétylsalicylique, bupropion, dexaméthasone, pantoprazole) sont de niveau non précisé.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai, aucune publication, aucun mécanisme plausible pour l'arthrose ni pour les autres maladies prédites.
- Les données de sécurité de la notice sont absentes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, indications autorisées).
- Obtenir les données sur le mécanisme d'action (DrugBank).
- Identifier des études précliniques ou cliniques portant directement sur l'arthrose, avant toute réévaluation.
- Évaluer la compatibilité de la voie d'administration (actuellement en attente) avec un usage thérapeutique.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Ultravist (iopromide) prescribing information, Bayer HealthCare Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df917c3a-59a2-4ed1-8470-8a5394c73325) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

