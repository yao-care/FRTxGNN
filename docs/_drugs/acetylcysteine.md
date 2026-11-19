---
layout: default
title: Acetylcysteine
parent: Preuves élevées (L1-L2)
nav_order: 21
evidence_level: L1
indication_count: 10
monitor_inn: "acetylcysteine"
predicted_indications: ["thrombotic disease", "closed-angle glaucoma", "nasal cavity disease", "dry eye syndrome", "pharyngitis", "acute laryngopharyngitis", "tracheal disease", "transient ischemic attack (disease)", "laryngotracheitis", "angle-closure glaucoma"]
last_modified_at: 2026-11-20
description: "Acetylcysteine : nouvelle indication prédite, Maladie thrombotique (thrombotic disease) (niveau de preuve L1). En France, AMM dans la BDPM : au moins 20"
---

# Acetylcysteine
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

## Acétylcystéine : agent mucolytique et antioxydant (thiol) → maladie thrombotique (thrombotic disease)
{: .text-alpha }

## Résumé en Une Phrase

L'acétylcystéine est un composé thiolé aux propriétés mucolytiques et antioxydantes, utilisé de longue date en pratique clinique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie thrombotique (thrombotic disease)**,
avec **6 essais cliniques** et **20 publications** actuellement associés à cette direction, dont un essai de Phase 3 terminé dans la microangiopathie thrombotique associée à la greffe.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Maladie thrombotique (thrombotic disease) |
| Score de Prédiction TxGNN | 0,9996 |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Acetylcysteine (traduction non officielle) : « Il a été démontré que l'acétylcystéine réduit l'étendue des lésions hépatiques consécutives à un surdosage en paracétamol. Des doses de paracétamol de 150 mg/kg ou plus ont été associées à une hépatotoxicité. L'acétylcystéine protège probablement le foie en maintenant ou en restaurant les taux de glutathion, ou en agissant comme substrat alternatif pour la conjugaison avec le métabolite réactif du paracétamol, et donc pour sa détoxification. » Texte original en anglais : "Acetylcysteine has been shown to reduce the extent of liver injury following acetaminophen overdose. Acetaminophen doses of 150 mg/kg or greater have been associated with hepatotoxicity. Acetylcysteine probably protects the liver by maintaining or restoring the glutathione levels, or by acting as an alternate substrate for conjugation with, and thus detoxification of, the reactive metabolite of acetaminophen." ([DailyMed: Acetadote (acetylcysteine) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=472f158a-5ab9-4308-8e49-1116e6ea3d39), version du 2025-04-30 ; consulté le 2026-11-19). D'après les informations connues, l'acétylcystéine est un composé thiolé capable de réduire les ponts disulfure. Dans les modèles précliniques de purpura thrombotique thrombocytopénique (souris et babouin), elle réduit la taille des multimères du facteur von Willebrand (VWF) et donc leur capacité à fixer les plaquettes.

Elle possède aussi une action antioxydante et reconstitue le glutathion, ce qui pourrait atténuer les lésions endothéliales et le phénotype pro-thrombotique observés dans la microangiopathie thrombotique associée à la greffe et dans l'insuffisance rénale.

Il faut toutefois rester prudent : les preuves cliniques sont hétérogènes. L'essai de Phase 3 porte sur la microangiopathie thrombotique post-greffe, les données dans le purpura thrombotique thrombocytopénique reposent sur un très petit essai pilote (3 patients) et des revues systématiques, et plusieurs essais concernent la thrombopénie immune, un mécanisme différent de la thrombose.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Terminé | 170 | Sécurité et efficacité de la N-acétylcystéine dans la microangiopathie thrombotique associée à la greffe ; résultats non résumés dans les données |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Actif, ne recrute plus | 44 | Essai à bras unique dans la même indication ; résultats non disponibles |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Terminé | 40 | ECR croisé contre placebo : réduction du phénotype thrombotique dans l'insuffisance rénale (critère de substitution) |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Phase 1 précoce | Terminé | 3 | Pilote dans le PTT suspecté, en complément des échanges plasmatiques ; trop petit pour conclure |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Inconnu | 44 | Dexaméthasone à haute dose + acétylcystéine dans la thrombopénie immune récente (relation indirecte) |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Phase 1 précoce | Terminé | 15 | Atorvastatine + N-acétylcystéine sur le taux de plaquettes dans la thrombopénie immune (relation indirecte) |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Inconnu | 200 | Atorvastatine, acétylcystéine et danazol dans la thrombopénie immune résistante ou en rechute (relation indirecte) |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Revue systématique | Journal of Clinical Medicine | Évaluation critique de la N-acétylcystéine dans le PTT |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Revue systématique | Cureus | Utilisation de la N-acétylcystéine comme traitement adjuvant dans le PTT réfractaire ou en rechute |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohorte rétrospective | Annals of Hematology | Association entre N-acétylcystéine et mortalité hospitalière dans le PTT acquis ; usage controversé |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Préclinique (souris/babouin) | Blood | Effet de la N-acétylcystéine dans des modèles animaux de PTT |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Revue | Expert Review of Hematology | Médicaments repositionnés dans le PTT, dont la N-acétylcystéine |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Revue | Blood | Physiopathologie et prise en charge du PTT |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revue | Journal of Clinical Medicine | PTT : physiopathologie, diagnostic et prise en charge |
| [32614622](https://pubmed.ncbi.nlm.nih.gov/32614622/) | 2021 | Revue | Platelets | Stratégies antiplaquettaires ciblant VWF et GPIb |

## Informations de Marché en France

Des autorisations de mise sur le marché (AMM) pour des spécialités à base d'acétylcystéine seule figurent dans les données locales (liste éventuellement partielle) ; le texte d'indication n'y est pas renseigné. L'acétylcystéine est commercialisée en France.

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour ces informations.

**Interactions médicamenteuses** : 247 interactions sont recensées. Parmi les principales : insuline humaine inhalée à action rapide (niveau modéré) et charbon activé (niveau mineur). De nombreuses autres interactions (par exemple morphine, metformine, oméprazole, pantoprazole, vancomycine, prednisone) ont un niveau de gravité non précisé.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Un essai de Phase 3 terminé (170 patients) et un essai de Phase 2/3 en cours portent sur la microangiopathie thrombotique associée à la greffe, et plusieurs revues systématiques traitent du PTT. Les résultats de ces essais ne sont toutefois pas résumés dans les données, et le bénéfice direct reste à confirmer.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats publiés de l'essai de Phase 3 NCT03252925 (critères principaux, sécurité) et de l'essai NCT07279610
- Données détaillées sur le mécanisme d'action
- Informations de sécurité issues de la notice (mises en garde, contre-indications)
- Précision de la définition de « maladie thrombotique » visée (microangiopathie thrombotique, PTT ou autre), car les preuves actuelles sont hétérogènes

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Acetadote (acetylcysteine) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=472f158a-5ab9-4308-8e49-1116e6ea3d39) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

