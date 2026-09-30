---
layout: default
title: Bendamustine
parent: Preuves élevées (L1-L2)
nav_order: 53
evidence_level: L1
indication_count: 10
---

# Bendamustine
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Bendamustine : De l'Indication d'Origine (Non Renseignée) au Lymphome à Cellules du Manteau

## Résumé en Une Phrase

La bendamustine est un agent alkylant cytotoxique commercialisé en France sous forme de poudre pour perfusion. Le texte d'indication des deux AMM françaises n'est pas renseigné dans les données reçues, donc l'indication d'origine ne peut pas être citée.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **lymphome à cellules du manteau (LCM)**, avec **50 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Cette utilisation correspond déjà à la pratique de référence (association bendamustine-rituximab, BR). Elle relève donc plus d'un usage établi que d'un repositionnement nouveau.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (texte d'indication vide pour les 2 AMM) |
| Nouvelle Indication Prédite | Lymphome à cellules du manteau |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après la littérature, la bendamustine est un agent alkylant bifonctionnel aux propriétés proches d'un analogue des purines. Elle crée des ponts intra-ADN et altère la réparation de l'ADN, ce qui lui donne une activité contre les hémopathies malignes B indolentes et le lymphome du manteau.

L'indication d'origine n'étant pas renseignée, la relation entre indication d'origine et nouvelle indication ne peut pas être établie à partir du dossier. En revanche, la bendamustine associée au rituximab est le socle ou le comparateur de plusieurs essais de phase 3 dans le LCM (BRIGHT, StiL, SHINE, ECHO, MANGROVE). Les recommandations européennes EHA-EU MCL (2025) figurent parmi les publications retrouvées.

Ce lien mécanistique (atteinte de l'ADN des cellules B malignes) est donc cohérent avec la pratique clinique. Un point de prudence : dans la plupart de ces essais, la bendamustine est évaluée en association, comme socle ou comparateur, et non seule. Il faut aussi vérifier le statut « dans l'AMM » ou « hors AMM » de cette indication sur les notices françaises.

## Preuves d'Essais Cliniques

Dix essais parmi les 50 identifiés sont listés. Les résumés décrivent l'objectif de chaque essai, car le dossier ne fournit pas de résultats chiffrés.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00877006](https://clinicaltrials.gov/study/NCT00877006) | Phase 3 | Terminé | 447 | BRIGHT : BR comparé à R-CHOP/R-CVP en première ligne (LNH indolent ou LCM). Comparaison directe, critère principal : taux de réponse complète |
| [NCT01456351](https://clinicaltrials.gov/study/NCT01456351) | Phase 3 | Terminé | 230 | StiL : BR comparé à fludarabine + rituximab (non-infériorité) dans les LNH de bas grade et LCM en rechute |
| [NCT01776840](https://clinicaltrials.gov/study/NCT01776840) | Phase 3 | Terminé | 523 | SHINE : ibrutinib ou placebo + BR chez les patients de 65 ans et plus avec LCM nouvellement diagnostiqué |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Phase 3 | Actif, ne recrute plus | 635 | ECHO : acalabrutinib ou placebo + BR dans le LCM non traité |
| [NCT04002297](https://clinicaltrials.gov/study/NCT04002297) | Phase 3 | Actif, ne recrute plus | 510 | Zanubrutinib + rituximab comparé à BR (comparateur actif) dans le LCM non éligible à la greffe |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | Recrutement en cours | 476 | Orélabrutinib + BR comparé à BR dans le LCM non traité |
| [NCT03567876](https://clinicaltrials.gov/study/NCT03567876) | Phase 2 | Terminé | 141 | R-BAC (rituximab, bendamustine, cytarabine) suivi de vénétoclax chez les patients âgés à haut risque |
| [NCT01415752](https://clinicaltrials.gov/study/NCT01415752) | Phase 2 | Actif, ne recrute plus | 373 | Quatre bras (BR ± bortézomib, consolidation par rituximab ± lénalidomide), patients de 60 ans et plus non traités |
| [NCT01662050](https://clinicaltrials.gov/study/NCT01662050) | Phase 2 | Terminé | 57 | R-BAC adapté à l'âge en induction chez les sujets âgés. Toxicité hématologique notable rapportée dans l'analyse intermédiaire |
| [NCT00076349](https://clinicaltrials.gov/study/NCT00076349) | Phase 2 | Terminé | 66 | Bendamustine + rituximab dans les LNH indolents ou LCM en rechute |

Trois essais de phase 3 sont terminés (BRIGHT, StiL, SHINE), ce qui correspond au niveau L1. Seuls BRIGHT et StiL comparent la bendamustine elle-même à un autre schéma.

## Preuves de la Littérature

Dix publications parmi les 20 identifiées sont listées, en privilégiant les essais randomisés.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | ECR | N Engl J Med | Ibrutinib + BR suivi d'une maintenance par rituximab chez les patients âgés atteints de LCM non traité (SHINE) |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | ECR | J Clin Oncol | Acalabrutinib + BR dans le LCM non traité. L'ibrutinib + BR avait allongé la survie sans progression sans gain de survie globale, probablement en raison de la toxicité |
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | ECR | Lancet | Essai de phase 3 de non-infériorité : BR comparé à R-CHOP en première ligne dans les lymphomes indolents et du manteau |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | ECR phase 2/3 | Lancet | ENRICH : ibrutinib + rituximab comparé à l'immunochimiothérapie (R-CHOP ou BR) chez les patients de 60 ans et plus |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | ECR (protocole) | Future Oncol | Conception de l'essai de phase 3 zanubrutinib + rituximab comparé à BR |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | Suivi d'essai de phase 3 | J Clin Oncol | BRIGHT : suivi à 5 ans de BR comparé à R-CHOP/R-CVP en première ligne |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Essais de phase 2 (analyse groupée) | Blood Adv | Induction rituximab/bendamustine puis rituximab/cytarabine avant autogreffe chez les patients éligibles |
| [36919283](https://pubmed.ncbi.nlm.nih.gov/36919283/) | 2023 | Méta-analyse en réseau | Eur J Haematol | Trois ECR (1 459 sujets) : supériorité d'ibrutinib + BR dans le LCM non éligible à un traitement intensif |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | Recommandations | HemaSphere | Recommandations EHA-EU MCL network pour le diagnostic et le traitement du LCM |
| [36456154](https://pubmed.ncbi.nlm.nih.gov/36456154/) | 2022 | Analyse rétrospective | Anticancer Res | BR dans le LCM en pratique réelle en Corée, chez les patients non traités et en rechute ou réfractaires |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64457346 | BENDAMUSTINE MEDAC 2,5 mg/mL | Poudre pour solution à diluer pour perfusion | Non renseignée |
| 61826343 | BENDAMUSTINE ARROW 2,5 mg/mL | Poudre pour solution à diluer pour perfusion | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant bifonctionnel) |
| Risque de Myélosuppression | Moyen à élevé (lymphopénie T documentée dans la littérature ; toxicité hématologique notable dans les associations avec la cytarabine, notamment chez les sujets âgés) |
| Classification d'Émétogénicité | Moyenne |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale, surveillance des infections |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune mise en garde, contre-indication ni interaction médicamenteuse n'est disponible dans le dossier.

La littérature signale par ailleurs un risque d'infection et de second cancer primitif après BR de première ligne (PMID 36792059), lié à l'effet immunosuppresseur de la bendamustine (lymphopénie T).

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Trois essais de phase 3 terminés (BRIGHT, StiL, SHINE) et des recommandations européennes de 2025 soutiennent BR dans le LCM, ce qui justifie le niveau L1. La bendamustine est toutefois évaluée surtout en association, et les données de sécurité des notices françaises manquent (lacune bloquante), d'où les garde-fous.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser les notices ANSM des deux AMM (mises en garde, contre-indications) : lacune bloquante pour le criblage de sécurité
- Vérifier les indications autorisées des deux AMM pour établir si le LCM est dans l'AMM ou hors AMM
- Obtenir les données sur le mécanisme d'action via DrugBank
- Prévoir un plan de surveillance des infections et de la myélosuppression, en particulier chez les patients âgés et en association avec un inhibiteur de BTK
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

