---
layout: default
title: Ketorolac
parent: Preuves élevées (L1-L2)
nav_order: 425
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-14
description: "Ketorolac : nouvelle indication prédite, Trouble céphalalgique (céphalées) (niveau de preuve L1). Indication d'origine : Conjonctivite atopique, papillaire et printanière"
monitor_inn: "ketorolac"
predicted_indications: ["headache disorder", "rosacea conjunctivitis", "trigeminal autonomic cephalalgia"]
---

# Ketorolac
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **3** 
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

## Kétorolac : De la conjonctivite atopique au trouble céphalalgique (céphalées)
{: .text-alpha }

## Résumé en Une Phrase

Le kétorolac est un anti-inflammatoire non stéroïdien (AINS), utilisé à l'origine sous forme de collyre pour traiter les conjonctivites atopique, papillaire et printanière.
Le modèle TxGNN prédit qu'il pourrait être efficace pour les **céphalées (trouble céphalalgique)**,
avec **17 essais cliniques** et **19 publications** soutenant actuellement cette direction, dont plusieurs revues systématiques et méta-analyses.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Conjonctivite atopique, papillaire et printanière (source : graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Trouble céphalalgique (céphalées) |
| Score de Prédiction TxGNN | 99,43 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | AMM annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques établies, le kétorolac fait partie de la classe des AINS : c'est un inhibiteur non sélectif des cyclooxygénases COX-1 et COX-2, qui réduit la synthèse des prostaglandines.

Dans l'indication d'origine (conjonctivites allergiques), cette inhibition limite l'inflammation de la surface oculaire. Dans la migraine et les céphalées de tension, les prostaglandines participent à la sensibilisation périphérique et centrale, à l'inflammation neurogène et à la transmission de la douleur. Le même mécanisme anti-prostaglandine peut donc expliquer un effet analgésique dans les céphalées aiguës.

Il faut noter que les données cliniques portent sur les formes systémiques (intraveineuse, intramusculaire, nasale), et non sur le collyre commercialisé à l'origine. La voie d'administration est donc un point d'attention majeur.

## Preuves d'Essais Cliniques

Parmi les 17 essais recensés, les plus pertinents sont listés ci-dessous.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | Terminé | 72 | Spray nasal de kétorolac vs spray nasal de sumatriptan vs placebo dans la migraine aiguë |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | Terminé | 173 | Kétorolac intranasal vs placebo (double aveugle) : sécurité et efficacité analgésique dans la migraine aiguë |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | Terminé | 123 | Métoclopramide/diphenhydramine vs kétorolac seul dans la céphalée de tension |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | Terminé | 330 | Valproate IV vs métoclopramide IV vs kétorolac IV dans la migraine aiguë |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | Terminé | 59 | Kétorolac intranasal vs intraveineux chez l'enfant migraineux (non-infériorité) |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | Terminé | 56 | Association kétorolac IV + métoclopramide dans la migraine pédiatrique aux urgences |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Inconnu | 60 | Kétamine vs kétorolac dans la céphalée de tension |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Phase 2 | Arrêté | 41 | « Cocktail » nasal contenant du kétorolac vs kétorolac IV chez l'enfant migraineux ; arrêt anticipé |
| [NCT03066544](https://clinicaltrials.gov/study/NCT03066544) | Phase 1/2 | Inconnu | 50 | État de mal migraineux : profil des répondeurs et non-répondeurs |
| [NCT02681211](https://clinicaltrials.gov/study/NCT02681211) | Non applicable | Inconnu | 80 | Acupuncture auriculaire vs médicaments IV dans l'état de mal migraineux pédiatrique |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Revue systématique / méta-analyse | Acad Emerg Med | Efficacité du kétorolac parentéral dans la crise migraineuse aiguë |
| [23298250](https://pubmed.ncbi.nlm.nih.gov/23298250/) | 2013 | Revue systématique | Headache | Efficacité du kétorolac parentéral dans la migraine aiguë ; données conflictuelles selon les études |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Méta-analyse | Adv Clin Exp Med | Comparaison du kétorolac IV et du métoclopramide chez l'adulte migraineux |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Recommandations | Headache | Mise à jour 2025 des recommandations de l'American Headache Society sur les traitements parentéraux de la migraine aux urgences |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Recommandations | Headache | Évaluation des preuves de l'AHS sur les traitements de la migraine aiguë |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | ECR | Headache | Ajout de kétorolac IV au métoclopramide chez l'enfant migraineux aux urgences |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | ECR | Neurol Sci | Comparaison IV de dexaméthasone, métoclopramide, kétorolac et chlorpromazine : douleur et récidive |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | ECR | Ann Emerg Med | Kétorolac IM vs péthidine et hydroxyzine dans la migraine aiguë |
| [41100185](https://pubmed.ncbi.nlm.nih.gov/41100185/) | 2025 | ECR | Cephalalgia | Bloc du nerf occipital associé à une trithérapie dans la migraine aiguë aux urgences |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | Revue systématique | Headache | Traitements parentéraux de la céphalée de tension épisodique |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63866361 | ACULAR 0,5 %, collyre en solution (ABBVIE) | Collyre en solution | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications évoquées par le graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, ulcère gastrique ou duodénal (y compris actif), maladie hépatique, maladie de la vésicule biliaire, polyarthrite rhumatoïde, maladie inflammatoire chronique de l'intestin, asthme (intrinsèque et allergique), diabète et acidocétose diabétique, troubles de la coagulation et hémophilie, accident vasculaire cérébral et maladies cérébrovasculaires, infarctus du myocarde, maladies cardiovasculaires, insuffisance rénale, hémoglobinopathies et anémies, syndrome de l'œil sec.
- **Interactions médicamenteuses** : 222 interactions recensées. Parmi les plus notables :
  - **Majeure** : acide acétylsalicylique.
  - **Modérée** : corticoïdes (bétaméthasone, budésonide, dexaméthasone, hydrocortisone), sulfamides hypoglycémiants (acétohexamide, chlorpropamide, glimépiride, glipizide, glibenclamide), balsalazide, exénatide, fenfluramine et dexfenfluramine, kanamycine, lévofloxacine.
  - **Mineure** : famotidine, ranitidine, cimétidine, linaclotide.
- **Signal de sécurité issu de la littérature** : un cas de toxicité neurologique du lithium induite par le kétorolac a été rapporté (PMID 7928331).
- Les risques classiques des AINS systémiques (hémorragie digestive, atteinte rénale, risque cardiovasculaire), ainsi qu'une durée de traitement courte, sont à surveiller. Veuillez consulter la notice pour les mises en garde officielles, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 2 à 4 et des revues systématiques/méta-analyses soutiennent l'usage du kétorolac dans la migraine aiguë et la céphalée de tension, avec des recommandations de sociétés savantes. Cependant, les effectifs des essais sont modestes, certains sont arrêtés, retirés ou de statut inconnu, et le profil de risque des AINS systémiques impose un encadrement strict.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice officielle (mises en garde et contre-indications) : ces données sont manquantes et bloquent l'évaluation de sécurité.
- Données détaillées sur le mécanisme d'action issues de DrugBank.
- Clarification de la voie d'administration : les preuves concernent les formes IV, IM et nasale, alors que la seule AMM française recensée est un collyre annulé.
- Plan de surveillance pour les populations à risque (sujets âgés, insuffisants rénaux, patients sous lithium, anticoagulants ou autres AINS) et limitation de la durée de traitement.

**Note sur les autres prédictions :** la conjonctivite rosacée (score 99,40 %) ne dispose d'aucun essai ni publication (niveau L5, décision Hold). La céphalalgie autonomique trigéminale (score 99,39 %) n'a qu'un essai retiré sans inclusion et une littérature indirecte (niveau L4, question de recherche).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

