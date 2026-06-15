---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 1
---

# Dapsone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dapsone : De la Lèpre à la Pneumocystose

## Résumé en Une Phrase

Dapsone est un agent sulfoné à double propriété antibactérienne et anti-inflammatoire, historiquement utilisé comme traitement de référence de la **lèpre** et de diverses dermatoses neutrophiliques (dermatite herpétiforme, pemphigoïde).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Pneumocystose** (*Pneumocystis jirovecii*),
avec **14 essais cliniques recensés** et **19 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Lèpre, dermatoses neutrophiliques |
| Nouvelle Indication Prédite | Pneumocystose (*Pneumocystis jirovecii*) |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Dapsone (4,4'-diaminodiphénylsulfone) est une sulfone qui inhibe spécifiquement la dihydroptéroate synthase (DHPS) de *Pneumocystis jirovecii*, bloquant ainsi la voie de biosynthèse de l'acide folique, indispensable à la multiplication du pathogène. Associé au triméthoprime — inhibiteur de la dihydrofolate réductase (DHFR), enzyme en aval — il réalise un double blocage séquentiel de la synthèse des folates, créant un effet synergique particulièrement efficace contre *P. jirovecii*. Ce mécanisme est directement analogue à celui du traitement de référence (TMP-SMX), à ceci près que dapsone substitue le sulfaméthoxazole au niveau de la DHPS.

La pneumocystose est une pneumonie opportuniste grave affectant principalement les immunodéprimés (VIH/SIDA, transplantés, hémopathies malignes). Elle partage avec la lèpre une susceptibilité fondamentale à l'inhibition du métabolisme des folates : dans les deux pathologies, dapsone perturbe la biosynthèse de précurseurs nucléotidiques essentiels chez le pathogène, sans toucher significativement les cellules humaines qui ne synthétisent pas leurs propres folates. Cette analogie mécanistique étaye solidement la prédiction du modèle TxGNN.

La pertinence clinique est par ailleurs largement confirmée : dapsone est déjà reconnu dans les lignes directrices internationales (ECIL, IDSA) comme alternative de deuxième ligne pour les patients intolérants au TMP-SMX, avec un corpus d'essais de phase 3 et deux méta-analyses en réseau publiées entre 2024 et 2025.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Terminé | 290 | Comparaison directe Dapsone/Triméthoprime vs Clindamycine/Primaquine vs TMP-SMX pour PCP légère à modérée chez patients VIH ; essai tête-à-tête de référence |
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Terminé | 700 | Dapsone quotidien vs Atovaquone pour prophylaxie PCP chez patients VIH intolérants au TMP-SMX ; plus grande cohorte de l'ensemble |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Terminé | 400 | Pentamidine en aérosol vs Dapsone trois fois par semaine pour prévention PCP chez patients VIH intolérants aux sulfonamides |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Terminé | 600 | Trois régimes anti-PCP incluant Dapsone + Zidovudine pour prévention primaire chez VIH avancé (CD4 < 200/mm³) |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | Non précisé | Terminé | N/A | Dapsone 100 mg vs 50 mg comme prophylaxie primaire PCP chez patients ARC avec CD4 < 400/mm³ ; optimisation posologique |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | Non précisé | Terminé | N/A | Dapsone + Triméthoprime vs TMP-SMX pour traitement du premier épisode de PCP chez patients SIDA ; évaluation taux d'efficacité et toxicité |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Terminé | 20 | Trimetrexate + Leucovorine + Dapsone vs TMP-SMX pour PCP modérément sévère ; évaluation pharmacocinétique et sécurité |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Inconnu | 3 130 | Dépistage génétique prospectif HLA-B*1301 pour réduire l'incidence du syndrome d'hypersensibilité au dapsone (DHS) ; large cohorte multicentrique |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | Terminé | 30 | Clindamycine-TMP/SMX pour PCP post-transplantation d'organe solide ; dapsone identifié comme alternative de deuxième ligne en cas d'échec TMP-SMX |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | N/A | Terminé | 168 | Étude cas-témoin sur facteurs de risque et incidence de PCP après greffe allogénique de cellules souches ; taux de percée sous dapsone faible dose jusqu'à 7,2 % |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Méta-analyse en réseau | *Clin Microbiol Infect* | Comparaison de l'efficacité et de la sécurité de TMP-SMX, régimes à base de dapsone, pentamidine aérosolisée et atovaquone pour la prophylaxie PCP chez personnes vivant avec le VIH |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Méta-analyse en réseau | *Clin Microbiol Infect* | TMP-SMX reste le traitement de référence de la PCP ; les alternatives thérapeutiques incluant dapsone évaluées chez personnes vivant avec le VIH à faible CD4 |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Recommandations cliniques (ECIL) | *J Antimicrob Chemother* | Lignes directrices ECIL-5 pour la prévention PCP chez patients hématologiques et transplantés : dapsone recommandé comme alternative au TMP-SMX (grade A-II) |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Revue | *Clin Infect Dis* | Dapsone inhibe la DHPS de *P. carinii* ; absorption orale 70–80 % ; pic sérique en 2–6 h ; efficacité démontrée in vitro, en modèle animal et en essais cliniques |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Revue | *Expert Opin Pharmacother* | Revue complète sur la prévention et le traitement de la PCP : facteurs de risque (VIH, transplantation, hémopathie), diagnostic, et options thérapeutiques actuelles |
| [39603840](https://pubmed.ncbi.nlm.nih.gov/39603840/) | 2025 | Revue | *Transplant Infect Dis* | Dapsone et atovaquone utilisés comme alternatives au TMP-SMX pour la prophylaxie PCP chez transplantés d'organe solide malgré données limitées dans cette population |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Revue | *Dermatol Clin* | Dapsone : propriétés antimicrobiennes et anti-inflammatoires ; traitement majeur de la lèpre et prophylaxie PCP établie chez patients VIH ; profil de tolérance détaillé |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Revue | *J Formos Med Assoc* | *P. jirovecii* reclassifié comme champignon ; PCP demeure la principale infection opportuniste chez patients SIDA malgré les traitements antirétroviraux hautement actifs |
| [7979291](https://pubmed.ncbi.nlm.nih.gov/7979291/) | 1994 | Pharmacocinétique | *Antimicrob Agents Chemother* | Pharmacocinétique et sécurité du dapsone hebdomadaire (100–300 mg) pour prévention PCP ; dose maximale tolérée établie à 200 mg/semaine sous AZT |
| [1727534](https://pubmed.ncbi.nlm.nih.gov/1727534/) | 1992 | Revue | *Med Clin North Am* | Pneumocystose presque entièrement prévenable et traitable après une décennie de VIH/SIDA ; rôle établi de dapsone dans la prophylaxie et le traitement |

---

## Informations de Marché en France

Dapsone ne dispose d'aucune autorisation de mise sur le marché (AMM) en France à ce jour. Le médicament n'est pas commercialisé sur le territoire français selon les données disponibles. Un accès pourrait nécessiter une procédure d'autorisation d'accès précoce (AAP) ou une importation dans le cadre d'un usage compassionnel.

---

## Considérations de Sécurité

> Veuillez consulter la notice officielle du médicament pour les informations complètes de sécurité (mises en garde, contre-indications, interactions médicamenteuses).

Les publications identifiées dans ce dossier signalent plusieurs risques connus à intégrer dans tout plan de surveillance :

- **Méthémoglobinémie** : complication rare mais potentiellement grave se manifestant par cyanose et hypoxie ; surveillance de la saturation en oxygène et de la méthémoglobine sanguine recommandée (PMID [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/), [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/), [33280223](https://pubmed.ncbi.nlm.nih.gov/33280223/))
- **Syndrome d'hypersensibilité au dapsone (DHS)** : réaction immunologique grave associée au variant HLA-B\*1301 ; dépistage génétique préalable fortement recommandé (NCT02550080, n = 3 130)
- **Hépatotoxicité** : lésions hépatiques induites par le médicament documentées dans la littérature ; surveillance de la fonction hépatique recommandée (PMID [31631707](https://pubmed.ncbi.nlm.nih.gov/31631707/))

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Dapsone présente un niveau de preuve L1 pour la pneumocystose, soutenu par plusieurs essais randomisés de phase 3 achevés (n total > 2 000 patients), deux méta-analyses en réseau publiées en 2024–2025, et des recommandations internationales (ECIL). Son mécanisme d'inhibition de la DHPS de *P. jirovecii* est solidement établi et reconnu comme complémentaire au triméthoprime. L'absence d'AMM en France et les signaux de sécurité identifiés (méthémoglobinémie, syndrome d'hypersensibilité HLA-dépendant) imposent une mise en œuvre rigoureusement encadrée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données complètes de sécurité officielles (notices EMA/ANSM, FDA) incluant les mises en garde, contre-indications et interactions médicamenteuses
- Évaluer la faisabilité d'un accès via autorisation d'accès précoce (AAP) ou importation compassionnelle en France
- Mettre en place un dépistage HLA-B\*1301 systématique avant initiation pour minimiser le risque de DHS
- Définir un protocole de surveillance de la méthémoglobinémie (oxymétrie de pouls, dosage méthémoglobine à J7, J14, J30)
- Cibler en priorité les populations à fort besoin non satisfait : patients VIH intolérants au TMP-SMX, transplantés d'organe solide et patients sous immunosuppresseurs pour hémopathies malignes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

