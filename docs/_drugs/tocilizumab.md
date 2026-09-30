---
layout: default
title: Tocilizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab : De la Polyarthrite Rhumatoïde à la Spondylarthrite Ankylosante

## Résumé en Une Phrase

Le tocilizumab est un anticorps monoclonal dirigé contre le récepteur de l'interleukine-6 (IL-6R). D'après la littérature fournie, il est utilisé principalement dans la polyarthrite rhumatoïde et les arthrites juvéniles idiopathiques.
Le modèle TxGNN prédit qu'il pourrait être efficace dans la **spondylarthrite ankylosante**.
Cette piste s'appuie sur **9 essais cliniques** et **19 publications**, mais seuls **2 essais randomisés de phase 3 directement pertinents** existent, et tous deux ont été **arrêtés prématurément, sans signal d'efficacité confirmé**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM françaises fournies (texte d'indication vide). La littérature cite la polyarthrite rhumatoïde et les arthrites juvéniles idiopathiques comme usages principaux |
| Nouvelle Indication Prédite | Spondylarthrite ankylosante |
| Score de Prédiction TxGNN | 99,99 % (rang 268) |
| Niveau de Preuve | L3 (voir la note ci-dessous) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 9 |
| Décision Recommandée | Hold |

**Note sur le niveau de preuve :** le dossier source indique L1. Or, selon les règles d'évaluation, L1 exige au moins 2 essais de phase 3 *complétés*. Ici, les deux essais directement pertinents (NCT01209689 et NCT01209702) sont au statut « Terminé prématurément » (*terminated*) et n'ont pas montré de résultat d'efficacité favorable. Nous retenons donc L3 : une revue systématique, des revues narratives et des cas cliniques existent, mais aucune démonstration randomisée d'efficacité.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, le tocilizumab bloque le récepteur de l'IL-6, une cytokine centrale de l'inflammation chronique. Son efficacité est établie dans la polyarthrite rhumatoïde, l'artérite à cellules géantes et les arthrites juvéniles, et il pourrait mécanistiquement s'appliquer à la spondylarthrite ankylosante.

L'IL-6 est impliquée dans l'inflammation axiale et le remodelage osseux. Bloquer son récepteur est donc biologiquement plausible, et c'est ce qui explique le score élevé du modèle.

Cependant, la plausibilité biologique ne suffit pas ici. Les deux essais randomisés contre placebo menés dans cette maladie ont été arrêtés, et le blocage de l'IL-6 n'est pas un traitement établi de la spondylarthrite ankylosante. Les traitements de référence restent les anti-TNF et les anti-IL-17. Le seul signal positif dans les données est un rapport de deux cas d'amylose AA secondaire à la spondylarthrite ankylosante, traités avec succès par tocilizumab. Cela reste anecdotique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminé prématurément | 113 | Tocilizumab (8 ou 4 mg/kg IV) vs placebo pendant 24 semaines, chez des patients en échec d'un anti-TNF. Pas de résultat d'efficacité favorable identifié |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminé prématurément | 306 | Tocilizumab 8 mg/kg vs placebo chez des patients en échec des AINS et naïfs d'anti-TNF. Pas de résultat d'efficacité favorable identifié |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Pas encore en recrutement | 52 | Sécukinumab dans l'artérite de Takayasu sévère. Indirect, sans résultat |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Pas encore en recrutement | 80 | Gestion périopératoire des immunosuppresseurs en rhumatologie. Non pertinent pour l'efficacité |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | En recrutement | 2 500 | Registre de profilage de biomarqueurs cytokiniques dans les maladies inflammatoires systémiques. Observationnel |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Terminé | 60 | Effet du tocilizumab sur les lymphocytes T folliculaires auxiliaires dans la polyarthrite rhumatoïde. Étude mécanistique |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | En recrutement | 10 000 | Registre coréen des biothérapies (polyarthrite rhumatoïde, spondylarthrite, rhumatisme psoriasique). Observationnel |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Terminé | 1 431 | Observatoire français d'utilisation d'Inflectra (biosimilaire de l'infliximab). Non spécifique au tocilizumab |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Statut inconnu | 750 000 | Risque de nouvelle maladie inflammatoire immuno-médiée sous biothérapie. Cohorte de sécurité |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | ECR (analyse des essais BUILDER-1 et BUILDER-2) | Ann Rheum Dis | Évaluation de l'efficacité symptomatique à court terme du tocilizumab dans la spondylarthrite ankylosante. Les résultats chiffrés ne figurent pas dans l'extrait disponible |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Revue systématique et méta-analyse en réseau | Medicine | Comparaison de l'efficacité des biothérapies dans la spondylarthrite ankylosante à partir d'essais randomisés |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Revue | Inflamm Allergy Drug Targets | Rôle de l'IL-6 dans la physiopathologie de la spondylarthrite ankylosante et intérêt de son blocage |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Revue | Curr Opin Rheumatol | Alternatives thérapeutiques chez les patients réfractaires aux anti-TNF |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Revue | Joint Bone Spine | Biothérapies au-delà des anti-TNF dans la spondylarthrite ankylosante |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Revue | Semin Arthritis Rheum | Choix de la biothérapie de deuxième ligne dans la polyarthrite rhumatoïde, le rhumatisme psoriasique et la spondylarthrite ankylosante |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Méta-analyse (risque infectieux) | Clin Rheumatol | Risque d'infections graves sous biothérapie dans la spondylarthrite ankylosante et la spondyloarthrite axiale non radiographique |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Revue systématique et méta-analyse (risque infectieux) | Expert Rev Clin Immunol | Comparaison du risque infectieux entre traitements non biologiques et biologiques dans les arthrites inflammatoires |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | Revue / recommandations | Front Immunol | Dépistage et prévention de la tuberculose sous biothérapies dans les arthrites auto-immunes chroniques |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Cas cliniques (2 cas) | Front Med | Traitement réussi d'une amylose AA secondaire à la spondylarthrite ankylosante par tocilizumab |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69107620 | ROACTEMRA 162 mg, seringue préremplie | Solution injectable | Non renseignée dans les données |
| 67121308 | ROACTEMRA 162 mg, stylo prérempli | Solution injectable | Non renseignée dans les données |
| 66297328 | TYENNE 162 mg, stylo prérempli | Solution injectable | Non renseignée dans les données |
| 69582503 | ROACTEMRA 20 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée dans les données |
| 65554606 | AVTOZMA 162 mg, seringue préremplie | Solution injectable | Non renseignée dans les données |

Le dossier recense 9 AMM au total. Les 5 principales sont listées ci-dessus. Les titulaires sont Roche, Fresenius Kabi et Celltrion (biosimilaires).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Le dossier ne contient ni mises en garde, ni contre-indications, ni interactions médicamenteuses exploitables.

La littérature associée signale toutefois un risque infectieux accru sous biothérapie, dont la tuberculose. Il justifie un dépistage préalable.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les deux seuls essais randomisés de phase 3 directement pertinents ont été arrêtés prématurément, sans signal d'efficacité confirmé. Le blocage de l'IL-6 n'est pas un traitement établi de la spondylarthrite ankylosante.
- Les données de sécurité de la notice française sont absentes du dossier, ce qui bloque le passage à l'étape de criblage de sécurité (S1). La plausibilité mécanistique et le score TxGNN élevé ne compensent pas ces lacunes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérifier les résultats et les motifs d'arrêt de NCT01209689 et NCT01209702 dans le registre ClinicalTrials.gov, et retrouver les résultats chiffrés de BUILDER-1 et BUILDER-2 (PMID 23765873).
- Récupérer et analyser les notices de l'ANSM (mises en garde, contre-indications, interactions).
- Compléter les données sur le mécanisme d'action via DrugBank.
- Renseigner les indications approuvées des AMM françaises, vides dans le dossier.

**Autre constat :** dans le même dossier, l'arthrite juvénile idiopathique polyarticulaire et sa forme à facteur rhumatoïde positif sont classées « Proceed with Guardrails » (L1, phase 3 complétée). Il s'agit d'usages déjà établis, non de repositionnement. Leur statut réglementaire en France est à vérifier.

*Ces résultats sont fournis à titre de recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute utilisation.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

