---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Risankizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Utilisation du contenu de l'Evidence Pack tel que fourni — synthèse rédigée directement, sans skill dédiée (tâche de rédaction ponctuelle, pas de recherche multi-étapes nécessaire).

# Risankizumab : Du Psoriasis à la Dermatite

## Résumé en Une Phrase

Risankizumab est un anticorps monoclonal IgG humanisé ciblant la sous-unité p19 de l'IL-23, initialement approuvé pour le traitement du psoriasis (psoriasis vulgaire, arthrite psoriasique, psoriasis pustuleux généralisé et érythrodermique) selon la littérature disponible.
Le modele TxGNN predit qu'il pourrait etre efficace pour la **Dermatite**,
avec **7 essais cliniques** et **17 publications** soutenant actuellement cette direction, dont un essai de Phase 2 complete specifiquement sur la dermatite atopique.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Psoriasis (d'apres la litterature disponible dans l'Evidence Pack ; aucune donnee DrugBank/AMM directe) |
| Nouvelle Indication Predite | Dermatite |
| Score de Prediction TxGNN | 99.98% |
| Niveau de Preuve | L2 (1 ECR de Phase 2 complete sur la dermatite atopique) |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

D'apres la litterature fournie (PMID 31098898), le risankizumab est un anticorps monoclonal humanise qui cible specifiquement la sous-unite p19 de l'interleukine-23 (IL-23). Il a obtenu sa premiere approbation mondiale au Japon en 2019 pour le psoriasis vulgaire, l'arthrite psoriasique, le psoriasis pustuleux generalise et le psoriasis erythrodermique, puis a ete approuve aux Etats-Unis, au Canada et en Europe.

Le psoriasis et la dermatite (notamment la dermatite atopique) sont deux maladies inflammatoires cutanees chroniques partageant des voies immunitaires communes. Selon la publication PMID 36588137, la dermatite atopique implique les voies Th2, Th22 et potentiellement Th17, ce qui justifie mecanistiquement le blocage de l'IL-23 et de l'IL-22 dans cette indication. Un essai de Phase 2 controle contre placebo (NCT03706040) a d'ailleurs deja teste cette hypothese chez des patients atteints de dermatite atopique moderee a severe.

Cette proximite mecanistique et clinique entre le psoriasis (indication d'origine) et la dermatite (nouvelle indication predite) rend la prediction TxGNN plausible, d'autant que plusieurs publications rapportent des cas d'utilisation croisee du risankizumab dans des tableaux dermatologiques mixtes (psoriasis + dermatite concomitants, eczema paradoxal).

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Termine | 172 | Evaluation de l'efficacite et de la securite du risankizumab dans la dermatite atopique moderee a severe (adultes et adolescents) |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Termine | 352 | Risankizumab vs apremilast dans le psoriasis en plaques modere |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Termine | 214 | Risankizumab dans le psoriasis genital ou du cuir chevelu modere a severe |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | En cours de recrutement | 840 | Etude observationnelle de biomarqueurs sur les maladies inflammatoires cutanees chroniques, incluant la dermatite atopique |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Termine | 1000 | Etude pharmacogenetique sur la survie a 10 ans des biotherapies dans le psoriasis cutane |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A | Termine | 240 | Cohorte observationnelle a Taiwan sur la durabilite de reponse du risankizumab dans le psoriasis en plaques modere a severe |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Pas encore recrutant | 10 | Test d'un microdispositif cutane delivrant plusieurs medicaments approuves (dont risankizumab) pour la dermatite atopique et le psoriasis |

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | ECR | Dermatology and Therapy | Etude de Phase 2 randomisee en double aveugle contre placebo montrant l'interet du blocage IL-23/IL-22 dans la dermatite atopique moderee a severe |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Revue Systematique | American Journal of Clinical Dermatology | Revue systematique des therapies systemiques (dont IL-23) dans le psoriasis erythrodermique |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Revue Systematique | Inflammopharmacology | Role des inhibiteurs d'interleukines, dont l'IL-23, dans le lichen plan : effets therapeutiques et paradoxaux |
| [41822639](https://pubmed.ncbi.nlm.nih.gov/41822639/) | 2026 | Revue Systematique | Cureus | Impact cardiovasculaire des biotherapies dans les dermatoses inflammatoires |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Revue | Drugs | Premiere approbation mondiale du risankizumab : mecanisme d'action anti-IL-23p19 et indications initiales en psoriasis |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Revue | Children (Basel) | Revue narrative des biotherapies et petites molecules dans le psoriasis et la dermatite atopique pediatriques |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Revue | Expert Opinion on Biological Therapy | Biotherapies actuelles et emergentes pour la dermatite atopique pediatrique |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Revue | Military Medicine | Reevaluation des immunomodulateurs systemiques pour le psoriasis et l'eczema en contexte militaire |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Serie de Cas | International Journal of Dermatology | Efficacite et securite de l'association dupilumab + risankizumab dans la dermatite atopique et le psoriasis concomitants |
| [37014149](https://pubmed.ncbi.nlm.nih.gov/37014149/) | 2023 | Rapport de Cas | Journal of Cutaneous Medicine and Surgery | Gestion de reactions eczemateuses induites par le brodalumab via un switch vers le risankizumab |

---

## Informations de Marche en France

Risankizumab n'est associe a aucune AMM dans les donnees disponibles (0 licence recensee, statut « Non commercialise »). Aucun tableau d'AMM ne peut donc etre presente.

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Le lien mecanistique est plausible et soutenu par un essai de Phase 2 complete sur la dermatite atopique (niveau de preuve L2), mais un gap de donnees bloquant empeche toute evaluation de securite initiale (S1) : les mises en garde et contre-indications TFDA ne sont pas disponibles, et le medicament n'a aucune AMM en France. La decision ne peut donc pas depasser le statut Hold en l'etat.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperation de la notice/des mises en garde TFDA (donnee bloquante S1)
- Confirmation du mecanisme d'action et des indications d'origine via l'API DrugBank
- Clarification si la « dermatite » predite vise specifiquement la dermatite atopique (mieux documentee) plutot qu'une categorie generique
- Evaluation du statut d'autorisation de mise sur le marche en France ou en Europe
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

