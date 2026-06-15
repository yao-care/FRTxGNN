---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 3
---

# Emtricitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Emtricitabine : De l'Infection à VIH-1 au Syndrome d'Immunodéficience Acquise Féline

## Résumé en Une Phrase

L'emtricitabine (FTC) est un inhibiteur nucléosidique de la transcriptase inverse (INTI), pilier du traitement de l'infection à VIH-1 chez l'adulte en association antivirale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Syndrome d'Immunodéficience Acquise Féline (FIV)** et l'**Infection à Virus de l'Immunodéficience Simienne (SIV)**,
avec **1 étude clinique vétérinaire directe** et **plus de 20 publications en modèles primates non-humains** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection à VIH-1 (adultes) |
| Nouvelle Indication Prédite | Syndrome d'Immunodéficience Acquise Féline (FIV) |
| Score de Prédiction TxGNN | 99,92% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non commercialisé (données non disponibles) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold (FIV) / Proceed with Guardrails (SIV) |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans cet Evidence Pack. Sur la base des connaissances pharmacologiques établies, l'emtricitabine est un analogue nucléosidique de la cytidine qui, après phosphorylation intracellulaire en FTC-TP (triphosphate), inhibe compétitivement la transcriptase inverse (RT) virale et provoque la terminaison prématurée de la chaîne d'ADN viral en cours de synthèse — mécanisme dit de « terminaison de chaîne ».

Le **Virus de l'Immunodéficience Féline (FIV)** appartient au genre *Lentivirus*, tout comme le VIH-1. Sa transcriptase inverse présente une homologie structurale avec celle du VIH-1 : l'emtricitabine, une fois phosphorylée en FTC-TP, se fixe au site actif de la RT du FIV et bloque la réplication virale RNA→DNA. La sensibilité *in vitro* du FIV à l'emtricitabine a été documentée, bien que la distribution des mutations de résistance (notamment K65R) dans le contexte félin nécessite encore des données cliniques vétérinaires contrôlées.

Cette prédiction est renforcée par un solide corpus de preuves issu de modèles **primates non-humains (NHP)** avec le **Virus de l'Immunodéficience Simienne (SIV/SHIV)** — également un lentivirus, dont la transcriptase inverse présente une homologie d'acides aminés supérieure à 60 % avec celle du VIH-1. Dans plus de 15 études NHP, l'emtricitabine en association avec le ténofovir (FTC/TDF ou FTC/TAF) a démontré une efficacité prophylactique (PrEP) et thérapeutique dans des modèles de challenge mucosal rectal, vaginal et pénile. Il s'agit d'un exemple classique d'inhibition NRTI trans-espèces au sein de la famille des lentivirus.

---

## Preuves d'Essais Cliniques

Aucun essai clinique directement applicable à l'indication féline (FIV) enregistré actuellement.

> **Note** : 4 essais identifiés (NCT01263015, NCT00951015, NCT02770508, NCT01227824) concernent exclusivement des patients humains atteints de VIH-1, dans lesquels l'emtricitabine est utilisée comme médicament de fond (non comme médicament expérimental pour la FIV). Ces données ne sont pas directement transposables à l'indication féline et ne sont pas comptabilisées dans le niveau de preuve FIV.

---

## Preuves de la Littérature

### Indication principale : Syndrome d'Immunodéficience Acquise Féline (FIV)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Étude clinique animale (vétérinaire) | *Viruses* | Premier POC vétérinaire direct : évaluation pharmacocinétique et de l'immunophénotype d'un protocole cART (Dolutégravir 2,5 mg/kg + Ténofovir 20 mg/kg + **Emtricitabine 40 mg/kg**) chez des chats domestiques infectés par FIV |

### Indication secondaire : Infection à SIV — Preuves Transversales (Primates Non-Humains)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Étude NHP (équivalent ECR) | *J Infect Dis* | TAF seul ou FTC/TAF oral prévient l'infection vaginale à SHIV chez le macaque dans un modèle d'expositions répétées |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Étude NHP | *J Infect Dis* | Gel vaginal FTC/TFV protège contre les expositions rectales répétées à SHIV chez le macaque (protection bi-compartimentale) |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Étude NHP | *J Infect Dis* | FTC/TAF oral prévient l'infection rectale à SHIV chez le macaque dans un modèle de PrEP hebdomadaire |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Étude NHP | *J Infect Dis* | FTC/TDF oral prévient l'infection vaginale à SHIV même en présence de co-infections à *Chlamydia trachomatis* et *Trichomonas vaginalis* |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Étude NHP | *J Infect Dis* | FTC/TDF maintient l'efficacité prophylactique contre un SHIV porteur de la mutation K65R (résistance au ténofovir) |
| [22814162](https://pubmed.ncbi.nlm.nih.gov/22814162/) | 2012 | Étude NHP | *Jpn J Infect Dis* | Double administration orale de FTC/TDF avant exposition protège contre un SHIV hautement pathogène chez le macaque cynomolgus |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Étude NHP | *AIDS Res Hum Retroviruses* | Vaccin VLP + PrEP oral (Truvada/FTC+TDF) prévient l'infection à SHIV ; la PrEP amplifie l'immunité vaccinale en cas d'adhérence partielle |
| [19656878](https://pubmed.ncbi.nlm.nih.gov/19656878/) | 2009 | Étude NHP | *J Virol* | Gel topique TFV seul ou associé à FTC : protection complète (100 %) contre l'infection vaginale à SHIV dans un modèle de challenge bi-hebdomadaire |
| [21632769](https://pubmed.ncbi.nlm.nih.gov/21632769/) | 2011 | Étude NHP | *J Virol* | Truvada (FTC/TDF) en prophylaxie intermittente maintient l'efficacité contre SHIV162p3 portant la mutation M184V (résistance au FTC) |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Étude animale SIV | *J Virol* | Traitement ART (TFV + FTC) dans l'infection à SIVagm chez le singe vert africain : déclin viral documenté malgré la persistance d'un réservoir cellulaire |

---

## Informations de Marché en France

Aucune AMM enregistrée pour l'emtricitabine dans la base de données consultée.

> **Note** : En pratique clinique, l'emtricitabine est commercialisée en France au sein de co-formulations antivirales (ex. Truvada®, Descovy®, Biktarvy®, Odefsey®). Ces associations ne figurent pas dans les données réglementaires fournies pour ce rapport.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Récapitulatif des 3 indications prédites par TxGNN :**

| Rang | Indication | Score TxGNN | Niveau de Preuve | Décision |
|------|-----------|------------|----------------|---------|
| 1 | Syndrome d'Immunodéficience Acquise Féline (FIV) | 99,92% | L3 | **Hold** |
| 2 | Infection à Virus de l'Immunodéficience Simienne (SIV) | 99,92% | L3 | **Proceed with Guardrails** |
| 3 | Trouble neurodéveloppemental avec démarche ataxique, absence de parole et diminution de la substance blanche corticale | 99,92% | L5 | **Hold** |

---

**Décision principale (Rang 1 — FIV) : Hold**

**Justification :**
La prédiction TxGNN est mécanistiquement plausible — FIV est un lentivirus dont la RT est homologue à celle du VIH-1 — et une première étude vétérinaire directe (Kim 2023, *Viruses*) a documenté l'utilisation de l'emtricitabine en protocole cART chez des chats FIV positifs. Cependant, il s'agit d'une unique étude observationnelle sans groupe contrôle formel, insuffisante pour justifier une progression vers un essai prospectif sans données pharmacocinétiques vétérinaires complémentaires.

**Décision secondaire (Rang 2 — SIV) : Proceed with Guardrails**

**Justification :**
Plus de 15 études sur des primates non-humains documentent de manière cohérente l'efficacité de l'emtricitabine en association FTC/TDF ou FTC/TAF contre SIV/SHIV dans des modèles de challenge standardisés (rectal, vaginal, pénile, systémique). La base de preuves précliniques est robuste et multi-voies, justifiant une progression dans un cadre de surveillance défini.

**Décision (Rang 3 — Trouble neurodéveloppemental) : Hold**

**Justification :**
Aucune donnée clinique, préclinique ou mécanistique directe ne soutient cette prédiction. Le score TxGNN élevé reflète probablement une propagation de caractéristiques de nœuds liées aux maladies neurologiques dans le réseau de neurones du graphe, sans fondement biologique établi.

**Pour avancer, les éléments suivants sont nécessaires :**
- **FIV** : Données pharmacocinétiques vétérinaires complémentaires (posologie optimale chez le chat, paramètres ADME félin, tolérance à long terme) ; étude contrôlée prospective en médecine vétérinaire
- **SIV** : Définition du cadre d'application (recherche translationnelle HIV cure, virologie comparée ou application en primatologie vétérinaire)
- **MOA** : Profil pharmacologique complet incluant les mutations de résistance spécifiques aux espèces cibles (FIV RT : sensibilité K65R en contexte félin)
- **Sécurité** : Données de toxicité spécifiques à l'espèce féline et simienne (hépatotoxicité, néphrotoxicité comparées)
- **Réglementaire** : Vérification du statut AMM des co-formulations contenant l'emtricitabine sur le marché français (Truvada®, Descovy®, etc.)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

