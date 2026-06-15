---
layout: default
title: Clomipramine
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Clomipramine
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

# Clomipramine : Du Trouble Obsessionnel Compulsif au Trouble Anxieux

## Résumé en Une Phrase

La Clomipramine est un antidépresseur tricyclique (ATC) historiquement reconnu pour le traitement du trouble obsessionnel compulsif (TOC), pour lequel elle a obtenu l'approbation FDA en 1989, ainsi que pour les épisodes dépressifs majeurs résistants.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **Trouble Anxieux** (au sens large du spectre anxieux), avec **19 essais cliniques répertoriés** et **20 publications** soutenant actuellement cette direction.
Cette prédiction s'explique par le fait que le TOC était historiquement classé parmi les troubles anxieux dans le DSM-IV, établissant un continuum direct entre l'indication connue de la Clomipramine et la nouvelle indication prédite.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans les données réglementaires françaises (médicament non commercialisé en France) |
| Nouvelle Indication Prédite | Trouble Anxieux |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action de la Clomipramine ne sont pas disponibles dans les bases interrogées. Sur la base des informations connues dans la littérature scientifique, la Clomipramine est un antidépresseur tricyclique dont l'efficacité dans le TOC et la dépression est établie depuis les années 1980. D'après les données du dossier clinique, son mécanisme d'action repose sur l'inhibition puissante du transporteur de la sérotonine (SERT), qui module le circuit cortico-striato-thalamo-cortical (CSTC) — voie physiopathologique centrale du TOC et des troubles anxieux. Son métabolite actif, la desméthylclomipramine, exerce également une inhibition significative du transporteur de la noradrénaline (NET), conférant à la molécule un profil d'action dual SERT+NET.

Le TOC était classé parmi les troubles anxieux dans le DSM-IV, établissant un continuum direct entre l'indication historique de la Clomipramine et la nouvelle indication prédite. Les troubles anxieux (trouble panique, agoraphobie, trouble anxieux généralisé) partagent des mécanismes sérotoninergiques communs avec le TOC, et la Clomipramine a été documentée comme « médicament de référence » (*reference drug*) pour le trouble panique avec ou sans agoraphobie dans plusieurs pays européens. Plusieurs essais cliniques et revues Cochrane confirment son efficacité dans le TOC réfractaire aux ISRS, le trouble panique et les troubles du spectre obsessionnel-compulsif (ex. : trichotillomanie).

La prédiction de TxGNN est donc biologiquement cohérente et cliniquement étayée. Elle constitue moins une « nouvelle » indication au sens strict qu'une formalisation et une extension de l'usage établi de la Clomipramine dans le spectre anxieux au sens large du DSM-IV. Le principal obstacle à son utilisation en France reste son absence de commercialisation et d'AMM sur le territoire français.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Terminé | 124 | TOC pédiatrique chez les répondeurs partiels aux ISRS : évaluation de la TCC en complément de la Clomipramine ou des ISRS — amélioration significative des symptômes TOC |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Terminé | 54 | Stratégies d'augmentation pour le TOC non-répondant : fluoxétine seule vs fluoxétine + quétiapine vs fluoxétine + Clomipramine — essai randomisé double aveugle double placebo |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Terminé | 21 | Comparaison directe augmentation quétiapine vs Clomipramine ajoutée aux ISRS dans le TOC après échec des ISRS ; évaluation de l'efficacité de la Clomipramine comme stratégie d'augmentation |
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | Inconnu | 76 | Comparaison de la Clomipramine IV vs orale dans le TOC suivie de 12 semaines de traitement de maintenance ; étude de référence sur les deux voies d'administration |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | Terminé | 44 | Étude pilote : augmentation par quétiapine dans le TOC sévère chez des patients traités par ISRS/Clomipramine ; résultats préliminaires d'une stratégie combinée |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Terminé | 26 | Prédiction de la réponse médicamenteuse dans le TOC : Clomipramine vs escitalopram, identification de biomarqueurs prédictifs de réponse individuelle |
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Terminé | 426 | Troriluzole adjuvant vs placebo dans le TOC chez les non-répondants aux ISRS/Clomipramine ; essai randomisé double aveugle à grande échelle |
| [NCT01148316](https://clinicaltrials.gov/study/NCT01148316) | N/A | Terminé | 144 | Stratégies thérapeutiques adaptatives pour enfants/adolescents atteints de TOC ; Clomipramine et ISRS constituent les pharmacothérapies de référence évaluées |
| [NCT04708834](https://clinicaltrials.gov/study/NCT04708834) | Phase 3 | Arrêté prématurément | 772 | Sécurité à long terme du troriluzole en adjuvant dans le TOC (n=772) ; la Clomipramine fait partie des traitements de fond autorisés — données de tolérance à grande échelle |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Arrêté prématurément | 407 | Pharmacovigilance chez les patients géronto-psychiatriques traités par psychotropes (incluant ATC) ; données de sécurité en population âgée sous polypharmacie |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Méta-analyse en réseau | Cochrane Database Syst Rev | La Clomipramine figure parmi les agents actifs pour le trouble panique de l'adulte, comparée à 20+ médicaments ; profil efficacité/tolérance quantifié à l'échelle de la classe thérapeutique |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Revue complète | Drugs | Vue d'ensemble des propriétés pharmacologiques de la Clomipramine et revue de son usage dans le TOC et le trouble panique ; supériorité sur les ATC non sérotoninergiques clairement établie |
| [7795952](https://pubmed.ncbi.nlm.nih.gov/7795952/) | 1995 | Revue (basée sur ECR) | J Child Adolesc Psychiatr Nurs | Premier agent efficace pour le TOC : l'inhibition sérotoninergique est essentielle à la réduction des symptômes primaires du TOC chez l'enfant et l'adolescent |
| [34582562](https://pubmed.ncbi.nlm.nih.gov/34582562/) | 2021 | Revue systématique Cochrane | Cochrane Database Syst Rev | Mise à jour Cochrane sur la pharmacothérapie de la trichotillomanie (trouble du spectre TOC) ; efficacité de la Clomipramine documentée dans ce trouble apparenté |
| [24214100](https://pubmed.ncbi.nlm.nih.gov/24214100/) | 2013 | Revue systématique Cochrane | Cochrane Database Syst Rev | Première évaluation systématique de la pharmacothérapie de la trichotillomanie ; résultats suggérant l'utilité des agents sérotoninergiques dont la Clomipramine |
| [8263222](https://pubmed.ncbi.nlm.nih.gov/8263222/) | 1993 | Méta-analyse | J Behav Ther Exp Psychiatry | Méta-analyse de 25 études (1975-1991) : la Clomipramine, la fluoxétine et la TCC sont toutes significativement efficaces sur la majorité des variables de résultat dans le TOC |
| [1474179](https://pubmed.ncbi.nlm.nih.gov/1474179/) | 1992 | ECR | J Clin Psychopharmacol | Comparaison de la Clomipramine, clonazépam et clonidine vs diphénhydramine (contrôle) dans le TOC ; la Clomipramine produit les effets les plus cohérents sur la réduction des symptômes |
| [12063477](https://pubmed.ncbi.nlm.nih.gov/12063477/) | 2002 | Revue | J Am Acad Dermatol | La trichotillomanie partage une phénoménologie avec le TOC ; les ISRS et la Clomipramine constituent les options thérapeutiques de référence dans ce trouble du spectre obsessionnel |
| [3887336](https://pubmed.ncbi.nlm.nih.gov/3887336/) | 1985 | Revue clinique | Psychiatr Clin North Am | Article fondateur : la Clomipramine est le premier traitement médicamenteux efficace démontré pour le TOC, ses propriétés sérotoninergiques spécifiques distinguant son mécanisme des autres ATC |
| [3887445](https://pubmed.ncbi.nlm.nih.gov/3887445/) | 1985 | ECR | Psychiatry Res | ECR double aveugle (n=23) comparant Clomipramine vs imipramine dans le TOC sur 12 semaines ; réduction plus cohérente des symptômes obsessionnels-compulsifs avec la Clomipramine |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le corpus de preuves cliniques est de niveau L1 — la Clomipramine dispose d'une approbation FDA pour le TOC depuis 1989 et de plusieurs essais de Phase 3/4 complétés soutenant son efficacité dans le spectre anxieux au sens large. Le score TxGNN de 99,93 % reflète cette base probante solide et historiquement établie. Le principal frein au développement en France est l'absence totale d'AMM sur le territoire français, qui nécessite une démarche réglementaire spécifique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice officielle (EMA/ANSM) pour établir le profil complet de sécurité : mises en garde, contre-indications et interactions médicamenteuses
- Données détaillées sur le mécanisme d'action (MOA) — requête DrugBank API prioritaire (DG002)
- Évaluation de la faisabilité d'une demande d'AMM ou d'une Autorisation d'Accès Exceptionnel (AAE) auprès de l'ANSM pour les patients en impasse thérapeutique
- Plan de surveillance spécifique tenant compte du profil anticholinergique des ATC : risques cardiovasculaires (allongement QTc), seuil épileptogène abaissé, toxicité en cas de surdosage
- Évaluation pharmacogénomique des polymorphismes CYP2D6 et CYP2C19, qui influencent significativement les concentrations plasmatiques de Clomipramine et de la desméthylclomipramine (métabolite actif NRI)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

