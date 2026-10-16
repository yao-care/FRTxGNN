---
layout: default
title: Estazolam
parent: Prédiction du modèle uniquement (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Estazolam : nouvelle indication prédite, Insomnie (niveau de preuve L5). Indication d'origine : Non renseignée (le texte d'indication de l'AMM est vide)"
---

# Estazolam
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

# Estazolam : De l'indication d'origine non renseignée à l'insomnie

## Résumé en Une Phrase

L'estazolam est une benzodiazépine hypnotique. Les données compilées pour ce rapport ne précisent pas son indication d'origine en France.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**insomnie**, avec **7 essais cliniques** et **19 publications** associés.
Il faut toutefois noter que l'insomnie est vraisemblablement l'usage habituel (hors repositionnement) de ce médicament : cette prédiction correspond donc plutôt à une confirmation de l'indication classique qu'à un véritable repositionnement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (le texte d'indication de l'AMM est vide) |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,48 % |
| Niveau de Preuve | L1 (selon la grille d'évaluation des données compilées ; voir la réserve ci-dessous) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne figurent pas dans le dossier d'origine. D'après les connaissances pharmacologiques générales, l'estazolam est une benzodiazépine qui agit comme modulateur allostérique positif des récepteurs GABA-A. Il renforce la neurotransmission inhibitrice et produit un effet sédatif et hypnotique.

Ce mécanisme correspond directement au traitement de l'insomnie. Comme indiqué, l'insomnie est probablement l'usage historique du médicament, et non une extension vers une nouvelle maladie. Plusieurs essais récents utilisent d'ailleurs l'estazolam comme comparateur actif ou comme traitement de fond.

Il faut aussi souligner que le niveau L1 provient de l'application de la grille de preuve. Il repose sur un seul essai de Phase 3 terminé (NCT00347295), où le rôle exact de l'estazolam (médicament testé ou comparateur) n'est pas clair. Ce niveau doit donc être interprété avec prudence.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00347295](https://clinicaltrials.gov/study/NCT00347295) | Phase 3 | Terminé | 253 | Essai randomisé en double aveugle comparant le brotizolam à l'estazolam chez des patients ambulatoires insomniaques ; pas de résultats détaillés disponibles |
| [NCT00956319](https://clinicaltrials.gov/study/NCT00956319) | Phase 4 | Terminé | 42 | Zolpidem à libération modifiée comparé à l'estazolam dans l'insomnie primaire (étude ouverte, de petite taille) |
| [NCT06859190](https://clinicaltrials.gov/study/NCT06859190) | Phase 3 | En recrutement | 60 | Acupression auriculaire + électroacupuncture + estazolam dans l'insomnie liée au cancer ; pas de résultats |
| [NCT06258226](https://clinicaltrials.gov/study/NCT06258226) | Non applicable | Inconnu | 108 | Acupression auriculaire pour réduire l'usage d'estazolam chez des insomniaques (sevrage, non efficacité) |
| [NCT03997058](https://clinicaltrials.gov/study/NCT03997058) | Phase 4 | Inconnu | 120 | Acupression auriculaire comparée à l'estazolam oral chez des patients hémodialysés insomniaques |
| [NCT07306494](https://clinicaltrials.gov/study/NCT07306494) | Phase 4 | Pas encore en recrutement | 1200 | Granulés composés de Ciwujia, avec estazolam probablement comme comparateur ; pas de résultats |
| [NCT05452577](https://clinicaltrials.gov/study/NCT05452577) | Non applicable | Terminé | 187 | Évaluation de la médecine chinoise traditionnelle dans l'insomnie chronique ; rôle de l'estazolam peu clair |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1968721](https://pubmed.ncbi.nlm.nih.gov/1968721/) | 1990 | Revue | Am J Med | Efficacité hypnotique établie de l'estazolam (1 à 2 mg) sur la latence d'endormissement, la durée totale de sommeil et les réveils nocturnes, maintenue pendant au moins 6 semaines |
| [42455420](https://pubmed.ncbi.nlm.nih.gov/42455420/) | 2026 | ECR | Chin J Integr Med | Acupuncture associée à l'estazolam chez des hémodialysés insomniaques |
| [36571227](https://pubmed.ncbi.nlm.nih.gov/36571227/) | 2022 | ECR | Zhen Ci Yan Jiu | Aiguilles superficielles associées à l'estazolam dans l'insomnie de type « stagnation du foie se transformant en feu » |
| [31013432](https://pubmed.ncbi.nlm.nih.gov/31013432/) | 2019 | Revue systématique | J Altern Complement Med | Acupuncture dans l'insomnie primaire : mise à jour des essais randomisés |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Revue | Med Lett Drugs Ther | Synthèse des médicaments de l'insomnie chronique |
| [30625124](https://pubmed.ncbi.nlm.nih.gov/30625124/) | 2018 | Revue | Med Lett Drugs Ther | Tableau détaillé de certains hypnotiques oraux |
| [40896345](https://pubmed.ncbi.nlm.nih.gov/40896345/) | 2025 | Revue exploratoire | Integr Med Res | Phytothérapie chinoise et acupuncture dans l'insomnie associée à une douleur chronique |
| [33798303](https://pubmed.ncbi.nlm.nih.gov/33798303/) | 2021 | Observation clinique | Zhongguo Zhen Jiu | Baduanjin et points auriculaires comparés à l'estazolam oral dans l'insomnie liée à la COVID-19 |
| [42343684](https://pubmed.ncbi.nlm.nih.gov/42343684/) | 2026 | Non classé | Zhen Ci Yan Jiu | Acupuncture associée à l'estazolam dans l'insomnie chronique |
| [37697875](https://pubmed.ncbi.nlm.nih.gov/37697875/) | 2023 | Non classé | Zhongguo Zhen Jiu | Acupuncture selon la différenciation des syndromes comparée à l'estazolam dans l'insomnie chronique et ses effets cognitifs |

La plupart des publications sont des études associant l'estazolam à l'acupuncture, où il sert de traitement de référence ou de fond. Seule la revue de 1990 évalue directement son efficacité hypnotique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69888457 (annulée) | NUCTALON 2 mg, comprimé | Comprimé | Non renseignée |

Le titulaire est CHEPLAPHARM ARZNEIMITTEL (Allemagne). Aucune AMM valide n'est actuellement enregistrée.

## Considérations de Sécurité

**Contre-indications issues du graphe de connaissances (pas du texte de la notice) :** le graphe de connaissances signale notamment les maladies suivantes :
- Troubles psychiatriques : trouble anxieux, trouble névrotique, trouble dysthymique, trouble psychotique, trouble schizophréniforme, trouble schizo-affectif, trouble mental
- Insuffisance d'organe : maladie rénale, maladie hépatique, maladie de la vésicule biliaire
- Troubles respiratoires du sommeil : syndrome d'apnées du sommeil (dont obstructif), syndrome d'hypoventilation centrale congénitale
- Troubles neuromusculaires : myasthénie (dont forme de l'adulte), maladie de la jonction neuromusculaire
- Addictions : troubles liés aux substances, abus ou dépendance

**Interactions médicamenteuses :** 100 interactions ont été recensées. Parmi celles listées :
- **Majeures** : morphine et morphine liposomale (risque de dépression respiratoire et de sédation)
- **Modérées** : bupropion, aprépitant, oméprazole, cimétidine, clarithromycine, dronabinol, nabilone, métoclopramide, opium, sibutramine, tédaglutide
- **Mineures** : antiacides (hydroxyde d'aluminium, carbonate de calcium, oxyde de magnésium, etc.)

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- L'insomnie correspond à l'usage hypnotique classique de l'estazolam, soutenu par des essais cliniques et une revue ancienne. Il ne s'agit donc pas d'un repositionnement au sens strict.
- Les preuves récentes sont surtout indirectes (estazolam comme comparateur ou traitement de fond), et le produit n'a plus d'AMM valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Les données détaillées sur le mécanisme d'action (à compléter via DrugBank)
- La clarification du rôle de l'estazolam dans l'essai de Phase 3 NCT00347295 (médicament testé ou comparateur)
- Un plan de surveillance pour les risques de dépendance, de sédation et de dépression respiratoire, notamment en cas d'association avec des opioïdes

**Autres indications prédites (à titre d'information) :** les autres prédictions reposent surtout sur le modèle seul. L'épilepsie visuelle et les crises audiogéniques (niveau L4) ne s'appuient que sur des études animales indirectes, et sont à considérer comme des questions de recherche. Le delirium de sevrage alcoolique, le syndrome des jambes sans repos, le syndrome myofascial et les épilepsies réflexes rares (niveau L5) sont en attente (Hold), sans preuve spécifique à l'estazolam.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

