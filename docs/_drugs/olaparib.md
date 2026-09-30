---
layout: default
title: Olaparib
parent: Preuves élevées (L1-L2)
nav_order: 222
evidence_level: L1
indication_count: 1
---

# Olaparib
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **1** 
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

# Olaparib : De l'Indication Originale (non renseignée) au Carcinome Mammaire Féminin

## Résumé en Une Phrase

L'olaparib est un inhibiteur de PARP commercialisé en France sous le nom Lynparza. Les données fournies ne précisent pas son indication d'origine.
Le modèle TxGNN le prédit comme potentiellement efficace dans le **carcinome mammaire féminin**, avec un score de 99,09 %.
**50 essais cliniques** (dont une minorité centrée sur le sein) et **20 publications** sont associés à cette direction. Il s'agit d'une **confirmation d'une indication déjà approuvée** (cancer du sein HER2-négatif avec mutation germinale BRCA) et non d'un repositionnement inédit.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données fournies |
| Nouvelle Indication Prédite | Carcinome mammaire féminin |
| Score de Prédiction TxGNN | 99,09 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées du mécanisme d'action ne sont pas disponibles dans la source DrugBank. Le mécanisme ci-dessous provient de l'analyse de repositionnement jointe au dossier. L'olaparib inhibe PARP1 et PARP2. Il bloque ainsi la réparation par excision de bases et piège PARP sur l'ADN.

Dans les tumeurs porteuses d'une mutation germinale BRCA1/2, ou d'une autre déficience de la recombinaison homologue (HRD), cette inhibition provoque une **létalité synthétique**. La cellule tumorale ne peut plus réparer ses cassures d'ADN et meurt. Le score TxGNN élevé (0,991) est cohérent avec ce mécanisme.

L'efficacité est **restreinte à un biomarqueur** (mutation gBRCA ou HRD). Elle est établie pour le cancer du sein HER2-négatif en situation métastatique (OlympiAD) et adjuvante (OlympiA). Elle ne s'étend pas au cancer du sein non sélectionné.

---

## Preuves d'Essais Cliniques

Parmi les 50 essais enregistrés, plusieurs concernent l'ovaire ou des tumeurs solides variées. Les 10 essais les plus pertinents pour le sein sont listés ci-dessous.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Terminé | 99 | Olaparib (AZD2281) dans le cancer du sein ou tubo-ovarien avec mutation BRCA, ou cancer du sein triple négatif. Évalue le taux de réponse objective et des marqueurs de réponse. Preuve directe de concept. |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Actif, ne recrute plus | 50 | Olaparib seul ou avec durvalumab en néoadjuvant, dans le cancer du sein précoce HER2-négatif avec mutation BRCA |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 (suivie d'une phase 2 randomisée) | Terminé | 25 | Carboplatine-olaparib puis olaparib seul vs capécitabine dans le cancer du sein avancé HER2-négatif avec mutation BRCA1/2, en première ligne. Le résumé ne mentionne que la dose recommandée de phase 2. |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Terminé | 103 | Olaparib + carboplatine dans les cancers du sein et de l'ovaire avec mutation BRCA1/2, et dans le cancer du sein triple négatif sporadique |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Phase 1/2 | Actif, ne recrute plus | 155 | Cédiranib + olaparib vs olaparib seul dans le cancer de l'ovaire ou le cancer du sein triple négatif récidivant |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Terminé | 24 | Olaparib avec radiothérapie dans le cancer du sein triple négatif (inflammatoire, localement avancé, métastatique ou avec maladie résiduelle) |
| [NCT02208375](https://clinicaltrials.gov/study/NCT02208375) | Phase 1 | Actif, ne recrute plus | 159 | Olaparib + vistusertib ou capivasertib dans les cancers de l'endomètre, du sein triple négatif et de l'ovaire |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Phase 1 | Terminé | 118 | Inhibiteur de PI3K (BKM120 ou BYL719) + olaparib dans le cancer du sein triple négatif ou de l'ovaire séreux de haut grade |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Terminé | 202 | Étude indienne sur l'olaparib dans le cancer de l'ovaire sensible au platine et le cancer du sein métastatique avec mutation gBRCA1/2 |
| [NCT07187674](https://clinicaltrials.gov/study/NCT07187674) | Non applicable | Pas encore en recrutement | 20 | QL1706 + olaparib + paclitaxel en néoadjuvant dans le cancer du sein triple négatif précoce à haut risque, HRD positif |

**Point d'attention :** l'essai [NCT02282020](https://clinicaltrials.gov/study/NCT02282020), de phase 3, correspond apparemment à SOLO3 dans le cancer de l'ovaire. Il n'apporte donc qu'un soutien indirect pour le sein et son rattachement à cette prédiction est à vérifier.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | ECR (OlympiA) | N Engl J Med | Olaparib adjuvant chez des patientes avec mutation germinale BRCA1/2 et cancer du sein précoce |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | ECR (OlympiA, survie globale) | Ann Oncol | Olaparib 1 an vs placebo en adjuvant, cancer du sein précoce HER2-négatif à haut risque avec mutation gBRCA1/2. Le résumé rappelle une amélioration significative de la survie sans maladie invasive à la première analyse intermédiaire. |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | ECR (OlympiAD) | N Engl J Med | Olaparib dans le cancer du sein métastatique avec mutation germinale BRCA. Le résumé indique une activité antitumorale prometteuse. |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | ECR (OlympiAD, survie globale finale) | Ann Oncol | Olaparib vs chimiothérapie au choix du médecin dans le cancer du sein métastatique HER2-négatif avec mutation gBRCA. Résultats finaux de survie globale et de tolérance. |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | ECR (OlympiAD, suivi prolongé) | Eur J Cancer | Survie globale médiane de 19,3 mois avec l'olaparib vs 17,1 mois avec la chimiothérapie (P = 0,513) dans l'analyse finale. Le suivi prolongé confirme le profil de sécurité. |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Essai de phase 2 (TBCRC 048) | J Clin Oncol | Olaparib dans le cancer du sein métastatique avec mutations BRCA1/2 somatiques ou mutations d'autres gènes de la recombinaison homologue |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Essai de phase 2 (I-SPY2) | Cancer Cell | Durvalumab + olaparib + paclitaxel en néoadjuvant : le taux de réponse complète pathologique augmente dans le cancer du sein HER2-négatif (de 20 % à 37 %) |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Essai de phase 2 (NOBROLA) | Breast | Olaparib seul dans le cancer du sein triple négatif avancé avec HRD et sans mutation germinale BRCA1/2 |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Vie réelle (LUCY, phase IIIb) | Breast Cancer Res Treat | Survie sans progression médiane de 8,11 mois à l'analyse intermédiaire, proche de celle d'OlympiAD (7,03 mois). Analyse finale de la survie globale et de la sécurité. |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Revue | Target Oncol | L'olaparib et le talazoparib sont approuvés en monothérapie dans le cancer du sein HER2-négatif avec mutation germinale BRCA |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 64748533 | LYNPARZA 100 mg, comprimé pelliculé | Comprimé pelliculé | ASTRAZENECA AB |
| 65789903 | LYNPARZA 50 mg, gélule | Gélule | ASTRAZENECA AB |
| 60058620 | LYNPARZA 150 mg, comprimé pelliculé | Comprimé pelliculé | ASTRAZENECA AB |

Les textes d'indication approuvée ne figurent pas dans les données fournies.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de PARP) |

Pour le risque de myélosuppression, l'émétogénicité, les paramètres de surveillance et la protection de manipulation, aucune donnée n'est disponible dans le dossier. Veuillez consulter les mises en garde et précautions de la notice.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Deux essais de phase 3 publiés (OlympiAD en métastatique, OlympiA en adjuvant) soutiennent l'efficacité de l'olaparib dans le cancer du sein avec mutation germinale BRCA. Le niveau de preuve est donc L1, et le médicament est déjà commercialisé en France.
- L'efficacité étant limitée aux patientes porteuses de la mutation gBRCA ou d'une HRD, il faut encadrer l'usage par ce biomarqueur. Les résultats ne se généralisent pas au cancer du sein non sélectionné.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les contre-indications et mises en garde de la notice ANSM. Ce manque bloque l'étape de criblage de sécurité.
- Récupérer le mécanisme d'action détaillé depuis DrugBank.
- Renseigner en amont l'indication originale, aujourd'hui vide.
- Confirmer que les textes d'indication des trois AMM françaises couvrent bien le cancer du sein avec mutation gBRCA.
- Vérifier le rattachement de NCT02282020 (probablement ovarien) et terminer l'évaluation de la pertinence des essais et publications encore en attente.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

