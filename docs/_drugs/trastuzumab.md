---
layout: default
title: Trastuzumab
parent: Preuves élevées (L1-L2)
nav_order: 323
evidence_level: L1
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab : Vers le Cancer du Sein à Récepteurs de la Progestérone Positifs

## Résumé en Une Phrase

Le dossier ne précise pas l'indication d'origine du trastuzumab : aucun texte d'indication n'est renseigné dans les AMM françaises. Le trastuzumab est un anticorps monoclonal dirigé contre le récepteur HER2.
Le modèle TxGNN prédit qu'il pourrait être efficace dans le **cancer du sein à récepteurs de la progestérone positifs**, avec **36 essais cliniques** et **20 publications** associés à cette prédiction. Cette prédiction correspond très probablement à un usage déjà établi (voir plus bas).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Cancer du sein à récepteurs de la progestérone positifs |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 16 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action (MOA) ne sont pas disponibles dans le dossier. D'après l'analyse mécanistique jointe, le trastuzumab se fixe sur le domaine extracellulaire de HER2. Il provoque une cytotoxicité cellulaire dépendante des anticorps (ADCC) et inhibe la signalisation de HER2.

Les tumeurs à récepteurs de la progestérone positifs (RP+) qui présentent aussi une amplification de HER2 constituent déjà une population standard pour le trastuzumab. Le bénéfice attendu ne concerne donc que le sous-groupe HER2-positif, et non l'ensemble des cancers du sein RP+. Le score TxGNN très élevé reflète probablement l'axe bien connu « cancer du sein / HER2 ».

**Point d'attention :** cette prédiction est plus proche d'un usage déjà établi que d'un véritable repositionnement. Le champ des indications d'origine est vide dans le dossier, ce qui empêche de comparer précisément l'ancienne et la nouvelle indication.

---

## Preuves d'Essais Cliniques

Sur les 36 essais associés, voici les 10 plus pertinents. Beaucoup portent sur des schémas combinés et n'ont pas encore d'évaluation de pertinence finalisée.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Terminé | 3436 | AC puis paclitaxel hebdomadaire, avec ou sans trastuzumab, en adjuvant (HER2+ ganglions positifs ou haut risque) |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Terminé | 3270 | Chimiothérapie seule versus chimiothérapie + trastuzumab en adjuvant. Le titre mentionne « HER2-low » : le rôle exact du trastuzumab est à confirmer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Terminé | 652 | Chimiothérapie à base de taxane + lapatinib ou trastuzumab en première ligne (cancer du sein métastatique HER2+) |
| [NCT01785420](https://clinicaltrials.gov/study/NCT01785420) | Phase 3 | En recrutement | 1100 | Trastuzumab versus placebo en traitement préopératoire de courte durée (HER2+ opérable) |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Terminé | 200 | Paclitaxel + Herceptin en adjuvant dans le cancer du sein de stade précoce |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Terminé | 33 | Létrozole + trastuzumab dans le cancer du sein métastatique ErbB2+ et RE et/ou RP+ |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | En recrutement | 30 | Neratinib + hormonothérapie + trastuzumab en préopératoire (RE+/HER2+) |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | Inconnu | 34 | Palbociclib + trastuzumab + pyrotinib + fulvestrant dans les métastases cérébrales RE/RP+ et HER2+ |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Inconnu | 7 | Inhibiteur de l'aromatase + pertuzumab/trastuzumab sans chimiothérapie (RH+/HER2+ localisé) |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | Retiré | 0 | Trastuzumab avec ou sans tamoxifène (stade IV, RE ou RP+ et HER2+) : aucune donnée |

---

## Preuves de la Littérature

Sur les 20 publications associées, voici les 10 plus pertinentes, classées par niveau de preuve.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | ECR | Lancet Oncol | NeoSphere : analyse à 5 ans du pertuzumab + trastuzumab néoadjuvants (survie sans progression, survie sans maladie, tolérance) |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | ECR | Lancet Oncol | monarcHER : abémaciclib + trastuzumab ± fulvestrant versus trastuzumab + chimiothérapie dans le cancer avancé RH+/HER2+ |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | ECR | Lancet Oncol | ExteNET : nératinib après traitement adjuvant à base de trastuzumab (HER2+) |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | ECR (d'après le titre) | JAMA Oncol | WSG-TP-II : hormonothérapie + double blocage HER2 versus chimiothérapie désescaladée dans le cancer précoce RH+/HER2+ |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Méta-analyse | Lancet | Effets des chimiothérapies et hormonothérapies adjuvantes sur la récidive et la survie à 15 ans |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Cohorte | Theranostics | Profil moléculaire et réponse au trastuzumab des cancers RE+/RP+/HER2+ (triple positifs) |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Étude rétrospective | BMC Cancer | Trastuzumab + fulvestrant dans le cancer avancé RH+/HER2+ (étude monocentrique) |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Recommandations | J Clin Oncol | Mise à jour ASCO du traitement systémique du cancer du sein avancé HER2+ |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Revue | Pharmacol Res | Inhibiteurs ciblés et cytotoxiques dans le cancer du sein selon les statuts HER2, RH, RE et RP |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Revue | Nat Rev Clin Oncol | Cancers HER2+ et RH+ : ciblage du bon récepteur |

---

## Informations de Marché en France

Le dossier recense 16 AMM ; les 5 principales sont listées ci-dessous. Le texte de l'indication approuvée n'est renseigné pour aucune d'entre elles.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 68153262 | HERZUMA 420 mg | Poudre pour solution à diluer pour perfusion | CELLTRION HEALTHCARE HUNGARY (Hongrie) |
| 60990496 | OGIVRI 150 mg | Poudre pour solution à diluer pour perfusion | BIOSIMILAR COLLABORATIONS IRELAND (Irlande) |
| 61276045 | HERCEPTIN 150 mg | Poudre pour solution à diluer pour perfusion | ROCHE REGISTRATION (Allemagne) |
| 62425937 | HERZUMA 150 mg | Poudre pour solution à diluer pour perfusion | CELLTRION HEALTHCARE HUNGARY (Hongrie) |
| 64346029 | ONTRUZANT 420 mg | Poudre pour solution à diluer pour perfusion | SAMSUNG BIOEPIS NL (Pays-Bas) |

---

## Cytotoxicité

Les données de toxicité DrugBank ne figurent pas dans le dossier. Les éléments ci-dessous relèvent de connaissances générales sur cette classe et doivent être vérifiés dans le RCP.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-HER2) |
| Risque de Myélosuppression | Faible en monothérapie ; le risque dépend surtout de la chimiothérapie associée (données de toxicité non fournies) |
| Classification d'Émétogénicité | Faible (connaissance générale) |
| Éléments de Surveillance | Fonction cardiaque (FEVG), et NFS ainsi que fonctions hépatique et rénale en cas d'association à une chimiothérapie. Un essai du dossier (NCT00446030) évalue justement la sécurité cardiaque de schémas associés |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'est enregistrée dans le dossier.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de Phase 3 terminés et des ECR publiés soutiennent le trastuzumab dans le cancer du sein HER2-positif, y compris RH+/HER2+ (niveau L1).
- Ces preuves valent uniquement pour les tumeurs HER2-positives. Le bénéfice n'est pas démontré pour tous les cancers du sein RP+, et la prédiction est proche d'un usage déjà établi.

**Pour avancer, les éléments suivants sont nécessaires :**
- **Bloquant :** la notice ANSM (mises en garde et contre-indications) n'est pas disponible. Elle est indispensable avant toute étape de dépistage de sécurité.
- Les données détaillées sur le mécanisme d'action (MOA), par exemple via l'API DrugBank.
- Les indications d'origine et les textes d'indication des AMM, pour confirmer si l'usage est déjà couvert.
- La restriction explicite aux tumeurs HER2-positives confirmées.
- La confirmation du rôle du trastuzumab dans les essais aux titres tronqués ou ambigus (par exemple NCT01275677) et la finalisation des évaluations de pertinence encore en attente.

**Note :** parmi les autres prédictions du dossier, le cancer du sein RP-négatif (rang 3) et le cancer du sein luminal A ou B (rang 4) reposent sur la même logique HER2. Les tumeurs rares (rangs 5 à 10) n'ont pratiquement aucune preuve (Hold).

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

