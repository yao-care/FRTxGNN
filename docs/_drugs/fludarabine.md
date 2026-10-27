---
layout: default
title: Fludarabine
parent: Preuves élevées (L1-L2)
nav_order: 333
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Fludarabine : nouvelle indication prédite, Myélome multiple (plasmocytome) (niveau de preuve L2). Indication d'origine : Non précisée dans les données d'AMM compilées"
monitor_inn: "fludarabine"
predicted_indications: ["plasma cell myeloma", "hyperthyroidism", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "indolent plasma cell myeloma", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "brain small vessel disease 1 with or without ocular anomalies", "myelodysplastic syndrome", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "diabetic nephropathy"]
---

# Fludarabine
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **10** 
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

## Fludarabine : De la leucémie lymphoïde chronique au myélome multiple (plasmocytome)
{: .text-alpha }

## Résumé en Une Phrase

La fludarabine est un analogue nucléosidique de la purine, utilisé en oncohématologie. Les données compilées pour ce rapport ne précisent toutefois pas le texte de son indication d'origine.
Le modèle TxGNN prédit qu'elle pourrait être utile dans le **myélome multiple (plasmocytome)**, avec **29 essais cliniques** et **19 publications** associés à cette direction. Ces preuves concernent surtout l'usage de la fludarabine comme composante de schémas combinés (conditionnement de greffe, lymphodéplétion avant CAR-T), et non comme traitement antimyélome autonome.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Myélome multiple (plasmocytome) |
| Score de Prédiction TxGNN | 99,82 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 3 |
| Décision Recommandée | Proceed with Guardrails |

> Remarque : le titre mentionne la leucémie lymphoïde chronique à titre de contexte pharmacologique connu de la fludarabine. Cette indication n'apparaît pas dans les textes d'AMM compilés, qui sont vides.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, la fludarabine est un analogue nucléosidique de la purine : elle inhibe la synthèse de l'ADN et induit l'apoptose des cellules lymphoïdes.

Le myélome est une hémopathie maligne des plasmocytes, lignée B lymphoïde. Dans cette maladie, la fludarabine intervient surtout comme agent de lymphodéplétion (avec le cyclophosphamide) avant une thérapie CAR-T anti-BCMA, et comme composante des conditionnements à intensité réduite avant allogreffe. Des travaux précliniques (PMID 17976186) montrent aussi une activité antimyélome directe in vitro et in vivo.

Le signal est donc réel mais indirect : il repose sur le rôle de la fludarabine dans des schémas combinés, et non sur une efficacité démontrée en monothérapie dans le myélome.

## Preuves d'Essais Cliniques

Sélection parmi les essais les plus pertinents pour le myélome (classés par pertinence). La plupart incluent la fludarabine dans un schéma combiné.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | Terminé prématurément | 6 | Conditionnement busulfan + fludarabine + cyclophosphamide avant allogreffe dans le myélome ou la myélofibrose ; très faible effectif |
| [NCT06045806](https://clinicaltrials.gov/study/NCT06045806) | Phase 3 | Actif, non en recrutement | 79 | Ide-cel + lénalidomide vs lénalidomide seul (KarMMa-9) ; la fludarabine fait partie de la lymphodéplétion, elle n'est pas testée en elle-même |
| [NCT07764978](https://clinicaltrials.gov/study/NCT07764978) | Phase 3 | En recrutement | 750 | Consolidation par CAR-T BCMA/CD19 (AZD0120) dans le myélome nouvellement diagnostiqué ; preuve indirecte |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | Terminé | 20 | Fludarabine + méthoxyamine (TRC102) dans les hémopathies malignes en rechute ou réfractaires ; population mixte |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Terminé | 16 | Autogreffe suivie d'une allogreffe non myéloablative haplo-identique (lymphome, myélome, LLC) ; petit échantillon |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Terminé | 213 | Greffe de sang de cordon avec cyclophosphamide/fludarabine/irradiation corporelle totale dans des hémopathies mixtes ; données spécifiques au myélome limitées |
| [NCT00014508](https://clinicaltrials.gov/study/NCT00014508) | Phase 2 | Terminé | Non précisé | Autogreffe suivie d'une mini-allogreffe dans le myélome |
| [NCT05020444](https://clinicaltrials.gov/study/NCT05020444) | Phase 1 | Actif, non en recrutement | 16 | CAR-T TriPRIL dans le myélome en rechute ou réfractaire ; fludarabine + cyclophosphamide en lymphodéplétion |
| [NCT06413498](https://clinicaltrials.gov/study/NCT06413498) | Phase 3 | Actif, non en recrutement | 452 | Anitocabtagène autoleucel vs traitement standard dans le myélome en rechute ou réfractaire |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Terminé | 147 | Allogreffe non myéloablative avec busulfan, fludarabine et irradiation corporelle totale dans des hémopathies malignes |

Aucun de ces essais ne teste la fludarabine en monothérapie dans le myélome.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Préclinique | Eur J Haematol | Activité antitumorale de la fludarabine contre le myélome humain in vitro et in vivo (lignée RPMI8226), avec baisse de la phosphorylation d'Akt (cité dans l'entrée « myélome indolent ») |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Cohorte | Blood Cancer J | Bendamustine vs fludarabine/cyclophosphamide en lymphodéplétion avant CAR-T BCMA dans le myélome |
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | Cohorte (données réelles) | Transplant Cell Ther | L'exposition à la fludarabine en lymphodéplétion est associée aux toxicités après ide-cel dans le myélome en rechute ou réfractaire |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Essai de phase 1 | Am J Clin Oncol | Conditionnement bortézomib + fludarabine + melphalan, avec ou sans irradiation médullaire totale, avant allogreffe dans le myélome à haut risque |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Analyse rétrospective multicentrique | Bone Marrow Transplant | Conditionnement à toxicité réduite fludarabine + treosulfan avant allogreffe chez 34 patients atteints de myélome |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Essai de phase 2 | Leuk Res Rep | Allogreffe avec busulfan fractionné, fludarabine et cyclophosphamide (4 myélofibroses, 2 myélomes) : mortalité hors rechute de 33,3 % à 1 an, survie globale de 50 % |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | Cohorte | J Clin Oncol | Suivi à long terme des CAR-T BCMA + CD19 dans le myélome en rechute ou réfractaire |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | Cohorte | J Hematol Oncol | Suivi à 5 ans de LEGEND-2 (cilta-cel) : rémissions profondes et durables |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Non classé | Eur J Haematol | Fludarabine et leucémie à plasmocytes (pas de résumé disponible) |
| [38576761](https://pubmed.ncbi.nlm.nih.gov/38576761/) | 2024 | Revue | World J Transplant | Régimes de conditionnement de l'autogreffe et CAR-T dans diverses maladies |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62818883 | FLUDARABINE TEVA 25 mg/mL (annulée) | Solution à diluer injectable ou pour perfusion | Non renseignée |
| 64281631 | FLUDARABINE ACCORD 25 mg/ml (annulée) | Solution à diluer pour solution injectable ou pour perfusion | Non renseignée |
| 62751438 | FLUDARA 10 mg (annulée) | Comprimé pelliculé | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (analogue nucléosidique de la purine) |
| Risque de Myélosuppression | Élevé (myélosuppression significative décrite dans la littérature, PMID 23787174) |
| Classification d'Émétogénicité | Faible à moyenne (selon la classe du médicament) |
| Éléments de Surveillance | NFS avec formule, fonction rénale (ajustement posologique nécessaire), fonction hépatique, surveillance neurologique, lymphocytes CD4 |
| Protection de Manipulation | Appliquer les règles de manipulation des médicaments cytotoxiques |

Veuillez consulter les mises en garde et précautions de la notice pour les détails complets.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 369 interactions sont recensées. Parmi les principales : métronidazole, rosuvastatine, simvastatine et tinidazole (niveau modéré) ; lévofloxacine (niveau mineur). De nombreuses autres interactions, dont l'amphotéricine B, la cimétidine et la morphine, sont de niveau inconnu.
- **Autres éléments de la littérature** : risque de neurotoxicité sévère à fortes doses (PMID 7525188) et de syndrome myélodysplasique ou leucémie aiguë myéloïde secondaires après chimiothérapie combinée à base de fludarabine (PMID 20962860).

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- De nombreux essais et études soutiennent l'utilisation de la fludarabine dans le myélome, mais uniquement comme composante de schémas de conditionnement ou de lymphodéplétion, pas comme traitement antimyélome autonome. Les essais en cause sont principalement de petite taille ou de phase 1/2, ou testent un autre agent.
- Toutes les AMM françaises sont annulées et les informations de sécurité officielles ne sont pas disponibles, ce qui impose des garde-fous stricts.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice (mises en garde et contre-indications) auprès de l'ANSM, élément bloquant pour l'évaluation de sécurité
- Données détaillées sur le mécanisme d'action
- Clarification du statut réglementaire, puisque toutes les AMM sont annulées
- Essais comparatifs spécifiques au myélome pour isoler la contribution de la fludarabine
- Plan de surveillance de la toxicité (myélosuppression, neurotoxicité, fonction rénale)

**Autres indications prédites (pour information) :**
- Le myélome indolent et le syndrome myélodysplasique présentent aussi un niveau L2, avec la même réserve : la fludarabine y est une composante de conditionnement avant allogreffe. Le syndrome myélodysplasique non classé est au niveau L3 (question de recherche).
- Les autres prédictions (hyperthyroïdie, diabète néphropathique, maladies monogéniques rares, délétion 5q) sont au niveau L5, sans lien mécanistique plausible : décision **Hold**.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

