---
layout: default
title: Trastuzumab Emtansine
parent: Prédiction du modèle uniquement (L5)
nav_order: 324
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Trastuzumab emtansine : Du Cancer du Sein HER2-positif au Cancer du Sein à Récepteurs de Progestérone Positifs

## Résumé en Une Phrase

Le trastuzumab emtansine (T-DM1, commercialisé sous le nom de Kadcyla) est un conjugué anticorps-médicament ciblant HER2, déjà utilisé dans le cancer du sein HER2-positif.
Le modèle TxGNN le prédit comme potentiellement efficace dans le **cancer du sein à récepteurs de progestérone positifs (RP+)**, avec **4 essais cliniques** et **15 publications** associés.
Cette prédiction correspond à un sous-type qui recoupe l'indication déjà autorisée. Il ne s'agit donc pas d'un véritable repositionnement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du sein HER2-positif (déduit de l'analyse du pack ; le texte d'indication des AMM est vide) |
| Nouvelle Indication Prédite | Cancer du sein à récepteurs de progestérone positifs |
| Score de Prédiction TxGNN | 99,82 % |
| Niveau de Preuve | L2 (niveau attribué dans le pack ; preuve directe limitée, voir ci-dessous) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées de mécanisme d'action ne sont pas renseignées dans la fiche DrugBank. Le pack d'évidence décrit toutefois le T-DM1 comme un anticorps-médicament composé de trastuzumab (anticorps anti-HER2) lié à la DM1, un inhibiteur des microtubules. Son activité dépend de l'expression de HER2 et non du statut des récepteurs de progestérone.

Le cancer du sein RP+ est un sous-groupe défini par les récepteurs hormonaux. Il chevauche largement le cancer du sein HER2-positif, qui est déjà le cadre d'utilisation approuvé. Le score TxGNN très élevé reflète donc surtout ce recoupement d'étiquettes de sous-types, et non un signal nouveau de repositionnement.

Le mécanisme n'est applicable que si la tumeur est confirmée HER2-positive. Pour les tumeurs RP+ mais HER2-négatives, il n'y a pas de justification mécanistique. Les autres indications prédites (par exemple le cancer du sein RP-négatif) suivent la même logique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Actif, ne recrute plus | 164 | T-DM1 + pertuzumab en préopératoire dans le cancer du sein précoce HER2-positif ; étude de l'impact de l'hétérogénéité de HER2. Aucun résultat dans le pack. |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | Non applicable | Terminé | 1151 | Étude rétrospective non interventionnelle sur la prévalence de HER2-low et les schémas de traitement. Contexte épidémiologique uniquement, pas de preuve d'efficacité du T-DM1. |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Terminé | 454 | IMpassion050 : atezolizumab vs placebo avec chimiothérapie néoadjuvante puis paclitaxel + trastuzumab + pertuzumab dans le cancer du sein précoce HER2-positif. Le rôle du T-DM1 n'est pas confirmé. |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Arrêté prématurément | 139 | DECRESCENDO : désescalade de la chimiothérapie adjuvante dans le cancer du sein précoce HER2-positif, RE-négatif, sans atteinte ganglionnaire. Applicabilité limitée aux tumeurs RP+. |

Aucun de ces essais ne confirme directement l'efficacité du T-DM1 dans une population RP+.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Lignes directrices (ASCO) | J Clin Oncol | Mise à jour des recommandations sur le traitement systémique du cancer du sein avancé HER2-positif |
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Lignes directrices (ASCO) | J Clin Oncol | Mise à jour 2018 des recommandations, fondée sur une revue systématique ciblée de 622 articles |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Lignes directrices (ASCO) | J Clin Oncol | Recommandations initiales pour le cancer du sein avancé HER2-positif |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Lignes directrices (biomarqueurs, EGTM) | Eur J Cancer | Les RE et RP guident l'hormonothérapie. La détermination de HER2 est obligatoire pour toutes les thérapies anti-HER2, dont le T-DM1. |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Revue | Pharmacol Res | Inhibiteurs ciblés et cytotoxiques dans le cancer du sein ; la prise en charge dépend du statut HER2, RH, RE et RP |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revue | Future Oncol | Tendances dans le traitement HR+/HER2+ ; citation du T-DM1 et du neratinib parmi les nouvelles thérapies anti-HER2 |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Revue | Clin Adv Hematol Oncol | Nouveautés dans le cancer du sein métastatique, classé selon RE, RP et HER2 |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Cohorte en vie réelle | Sci Rep | Valeur pronostique du gain de positivité HER2 dans le cancer du sein métastatique (essai ChangeHER), patients traités par pertuzumab et/ou T-DM1 |
| [35140078](https://pubmed.ncbi.nlm.nih.gov/35140078/) | 2022 | Rapport de cas | BMJ Case Rep | Conversion des récepteurs (jusqu'à 32 % des patientes) pouvant rendre le traitement inefficace sans biomarqueur adapté |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Rapport de cas | Case Rep Oncol | T-DM1 à dose réduite, actif et bien toléré en cas de dysfonction hépatique aiguë |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 62170212 | KADCYLA 100 mg | Poudre pour solution à diluer pour perfusion | Roche Registration (Allemagne) |
| 64565603 | KADCYLA 160 mg | Poudre pour solution à diluer pour perfusion | Roche Registration (Allemagne) |

Le texte des indications approuvées n'est pas renseigné pour ces deux AMM.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée : conjugué anticorps-médicament (trastuzumab + inhibiteur des microtubules DM1) |
| Risque de Myélosuppression, Émétogénicité, Éléments de Surveillance, Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le T-DM1 agit sur HER2 quel que soit le statut RP. Le cancer du sein RP+ HER2-positif relève déjà du champ d'utilisation approuvé, et la littérature (lignes directrices ASCO) soutient cet usage.
- Le score élevé traduit un recoupement de sous-types plutôt qu'une preuve directe. Les quatre essais liés n'établissent pas d'efficacité du T-DM1 spécifique aux tumeurs RP+.

**Garde-fou principal :** limiter l'usage aux tumeurs dont la positivité HER2 est confirmée, et refaire le test à la progression en raison de la conversion des récepteurs.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées de mécanisme d'action depuis DrugBank
- La vérification de la présence du T-DM1 dans les essais NCT02326974 et NCT03726879
- Des analyses stratifiées selon le statut RP dans les essais T-DM1 existants
- Le texte des indications approuvées des deux AMM françaises

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

