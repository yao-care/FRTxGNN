---
layout: default
title: Ipratropium
parent: Prédiction du modèle uniquement (L5)
nav_order: 411
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "IPRATROPIUM"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "respiratory malformation", "papillary conjunctivitis", "Rienhoff syndrome", "tracheal disease", "anaphylaxis", "food-dependent exercise-induced anaphylaxis"]
description: "Ipratropium : nouvelle indication prédite, Nasal cavity disease (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Ipratropium
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

## Ipratropium: Nasal cavity disease
{: .text-alpha }

## Résumé en Une Phrase

L'ipratropium est un anticholinergique inhalé (antagoniste muscarinique), initialement utilisé pour la bronchopneumopathie chronique obstructive (BPCO), la bronchite, l'emphysème et certaines rhinites.
Cette indication recoupe toutefois largement les usages d'origine : il ne s'agit pas d'un repositionnement au sens strict, mais plutôt d'une validation du classement du modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Nasal cavity disease |
| Score de Prédiction TxGNN | 0.9986 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base compilée. D'après les informations connues et la littérature citée, l'ipratropium est un dérivé quaternaire de l'atropine : il bloque de façon compétitive les récepteurs muscariniques du muscle lisse bronchique, s'oppose à l'acétylcholine et interrompt la bronchoconstriction d'origine vagale.

La « maladie pulmonaire obstructive » englobe la BPCO, la bronchite chronique et l'emphysème, qui figurent déjà parmi les indications d'origine du médicament. La prédiction est donc mécanistiquement cohérente, mais elle est en grande partie circulaire : elle confirme le modèle plus qu'elle ne révèle un usage nouveau.

Les autres pistes prédites (rhinite/cavité nasale, pharyngite, trachée, anaphylaxie, etc.) sont beaucoup moins étayées ; elles sont brièvement évoquées dans la conclusion.

---

## Preuves d'Essais Cliniques

Parmi les 25 essais recensés, les plus pertinents sont présentés ci-dessous (certains sont retirés, terminés prématurément ou ne portent pas directement sur l'efficacité de l'ipratropium).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | Terminé | 1118 | Association ipratropium/salbutamol (Respimat) vs Combivent, ipratropium seul et placebo sur 12 semaines dans la BPCO : efficacité bronchodilatatrice et sécurité |
| [NCT01136421](https://clinicaltrials.gov/study/NCT01136421) | Phase 3 | Terminé | 124 | Sulfate de magnésium vs ipratropium (avec bêta-2 agoniste) dans l'exacerbation aiguë de BPCO |
| [NCT02172469](https://clinicaltrials.gov/study/NCT02172469) | Phase 3 | Terminé | 215 | Tiotropium vs Atrovent MDI chez des patients BPCO philippins |
| [NCT00239434](https://clinicaltrials.gov/study/NCT00239434) | Phase 3 | Terminé | 200 | Tiotropium une fois par jour vs Atrovent MDI quatre fois par jour dans la BPCO |
| [NCT02172404](https://clinicaltrials.gov/study/NCT02172404) | Phase 3 | Terminé | 160 | HandiHaler vs MDI : technique d'administration et facilité d'utilisation dans la BPCO (appui indirect) |
| [NCT01415518](https://clinicaltrials.gov/study/NCT01415518) | Phase 4 | Terminé | 581 | Symbicort ajouté à Atrovent + théophylline dans la BPCO sévère |
| [NCT00371527](https://clinicaltrials.gov/study/NCT00371527) | Non applicable | Terminé | 200 | Ipratropium vs placebo dans la bronchite aiguë sans maladie pulmonaire sous-jacente |
| [NCT02686086](https://clinicaltrials.gov/study/NCT02686086) | Non applicable | Terminé | 60 | Volumes pulmonaires et scores de symptômes après bronchodilatateur selon le type de nébuliseur dans la BPCO |
| [NCT02260011](https://clinicaltrials.gov/study/NCT02260011) | Phase 2 | Terminé | 41 | Ipratropium HFA-134a vs Atrovent CFC en dose unique dans la BPCO |
| [NCT04446637](https://clinicaltrials.gov/study/NCT04446637) | Phase 3 | Retiré | 0 | Association ipratropium/lévosalbutamol vs association libre dans la BPCO : aucune donnée d'efficacité |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Revue systématique | Cochrane Database Syst Rev | Comparaison tiotropium vs ipratropium dans la BPCO stable |
| [24043433](https://pubmed.ncbi.nlm.nih.gov/24043433/) | 2013 | Revue systématique | Cochrane Database Syst Rev | Version antérieure de la même comparaison tiotropium vs ipratropium |
| [35616126](https://pubmed.ncbi.nlm.nih.gov/35616126/) | 2022 | Revue systématique | Cochrane Database Syst Rev | Sulfate de magnésium dans les exacerbations aiguës de BPCO |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Revue | Ann Pharmacother | Utilisation concomitante d'ipratropium et de tiotropium dans la BPCO |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Revue | Expert Opin Drug Metab Toxicol | Albutérol/salbutamol, ipratropium et leur association dans la BPCO |
| [10565879](https://pubmed.ncbi.nlm.nih.gov/10565879/) | 1999 | Revue | Respir Care Clin N Am | Bronchodilatateurs anticholinergiques ; efficacité spirométrique de l'ipratropium seul ou avec l'albutérol |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Revue | Clin Pharm | Pharmacologie, efficacité et effets indésirables de l'ipratropium dans la maladie pulmonaire obstructive |
| [15987237](https://pubmed.ncbi.nlm.nih.gov/15987237/) | 2005 | Revue | Treat Respir Med | Ipratropium en formulation HFA (propulseur sans CFC) |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Recommandations | Basic Clin Pharmacol Toxicol | Recommandations finlandaises de diagnostic et de traitement de la BPCO stable |
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | Étude rétrospective | Medicine | Probiotiques associés au budésonide et à l'ipratropium dans la BPCO |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66698997 | ATROVENT 20 microgrammes/dose (Boehringer Ingelheim France) | Solution pour inhalation en flacon pressurisé | Non renseignée (AMM active) |
| 61260984 | IPRATROPIUM VIATRIS 0,25 mg/ml ENFANTS | Solution pour inhalation par nébuliseur | Non renseignée (AMM active) |
| 69293057 | IPRATROPIUM VIATRIS 0,5 mg/2 ml ADULTES | Solution pour inhalation par nébuliseur | Non renseignée (AMM active) |
| 60175716 | IPRATROPIUM AGUETTANT ADULTES 0,5 mg/2 ml | Solution pour inhalation par nébuliseur | Non renseignée (AMM active) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, syndrome du QT long (y compris familial), arrêt cardiaque soudain, maladie de la conduction cardiaque, ischémie myocardique, coronaropathie, épilepsie, carence en potassium, diabète et acidocétose diabétique, acidose (dont acidose métabolique), hyperplasie bénigne de la prostate, obstruction du col vésical, hypertension oculaire, glaucome à angle fermé, hyperthyroïdie (maladie de Basedow, thyrotoxicose).
- **Interactions médicamenteuses** : 100 interactions recensées ; les 20 présentées sont toutes de niveau modéré, principalement avec d'autres anticholinergiques (hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, scopolamine, trospium, aclidinium, etc.), ainsi qu'avec la prométhazine, la chlorphéniramine, l'élukadoline, la prucalopride et l'insuline humaine inhalée.
- **Signaux de sécurité rapportés dans la littérature** : cas d'anaphylaxie sévère après inhalation d'ipratropium (Chest, 1993) et cas de mydriasis unilatérale chez un nourrisson après inhalation (2025).

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de Phase 3 terminés, dont un grand essai de 1118 patients, soutiennent l'efficacité bronchodilatatrice de l'ipratropium dans l'obstruction bronchique, mais l'indication recoupe celle d'origine : il ne s'agit pas d'un véritable repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (mises en garde et contre-indications) auprès de l'ANSM ; cette lacune est bloquante pour le criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Clarifier les raisons de l'annulation des AMM et le statut de commercialisation actuel en France.
- Mettre en place une surveillance particulière pour les patients présentant les contre-indications relevées (glaucome à angle fermé, rétention urinaire/hyperplasie prostatique, troubles du rythme cardiaque).

**Autres pistes prédites (non recommandées à ce stade) :**
- Maladie de la cavité nasale : niveau de preuve L4, question de recherche seulement ; l'ipratropium nasal est mécanistiquement plausible pour la rhinorrhée, mais la littérature retrouvée est tangentielle.
- Pharyngite, laryngopharyngite aiguë, malformation respiratoire, conjonctivite papillaire, syndrome de Rienhoff, maladie trachéale, anaphylaxie et anaphylaxie induite par l'effort dépendante de l'alimentation : **Hold**. Les preuves sont absentes, précliniques ou indirectes ; pour l'anaphylaxie, un signal de sécurité défavorable existe.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

