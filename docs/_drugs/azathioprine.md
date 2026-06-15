---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine : De l'Immunosuppression en Transplantation à la Maladie Inflammatoire Chronique de l'Intestin

## Résumé en Une Phrase

L'azathioprine est un immunosuppresseur thiopurinique historiquement utilisé dans la prévention du rejet de greffe d'organe et le traitement des maladies auto-immunes.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Maladie Inflammatoire Chronique de l'Intestin (MICI)**,
avec **50 essais cliniques** et **20 publications** soutenant actuellement cette direction.

> **Note méthodologique :** Le premier candidat TxGNN par score brut (rang 56 — *colobomatous microphthalmia-rhizomelic dysplasia syndrome*, score 99.999 %) ne possède aucune preuve clinique ou préclinique et son mécanisme est biologiquement incompatible avec l'azathioprine (probable biais topologique lié aux nœuds rares dans le graphe de connaissances). Le présent rapport porte sur la **MICI (rang TxGNN 3 648, score 99.52 %, niveau de preuve L1)**, indication cliniquement la plus solide du package.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible (aucun AMM enregistré dans la base de données consultée) |
| Nouvelle Indication Prédite | Maladie Inflammatoire Chronique de l'Intestin (MICI) |
| Score de Prédiction TxGNN | 99.52 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Non commercialisé (données régionales) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de l'azathioprine ne sont pas disponibles dans la base consultée. Sur la base des informations connues dans la littérature scientifique et des rationalisations mécanistiques présentes dans le dossier, l'azathioprine est un promédicament thiopurinique : après absorption, il est converti en 6-mercaptopurine (6-MP), puis en 6-thioguanine nucléotides (6-TGN) par l'enzyme HPRT. Ces métabolites actifs inhibent la synthèse de novo des purines dans les lymphocytes T et B, bloquant leur prolifération. Parallèlement, l'azathioprine déclenche l'apoptose des lymphocytes T activés via la voie Rac1, supprimant directement les voies inflammatoires Th1 et Th17.

La MICI — qui regroupe la maladie de Crohn (MC) et la rectocolite hémorragique (RCH) — est caractérisée par une dérégulation immune chronique de la muqueuse intestinale, précisément médiée par ces mêmes populations lymphocytaires. Le mécanisme d'action de l'azathioprine cible donc directement le moteur biologique de la maladie, ce qui explique la cohérence de la prédiction TxGNN. Les lignes directrices des sociétés savantes européenne (ECCO) et américaine (ACG) recommandent d'ailleurs l'azathioprine comme immunomodulateur de première ligne pour le maintien de la rémission dans la MICI.

La rectocolite hémorragique (rang 9 de TxGNN, niveau L1 également) partage ce même socle mécanistique — la voie Th2/Th9 caractéristique de la RCH étant également supprimée par les 6-TGN. Cette convergence entre MICI et RCH dans les prédictions du modèle, toutes deux au niveau L1, renforce la plausibilité biologique et la robustesse de l'évaluation.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Inconnu | 84 | AZA faible dose + allopurinol vs AZA monothérapie dans la RCH : évaluation de la stratégie métabolique (↑ 6-TGN, ↓ 6-MMP) pour améliorer réponse et tolérance — essai de référence direct |
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Terminé | 508 | Infliximab vs infliximab + AZA vs AZA seul dans la MC naive aux biologiques et immunomodulateurs — essai SONIC, preuve de supériorité de la combinaison |
| [NCT03464136](https://clinicaltrials.gov/study/NCT03464136) | Phase 3 | Terminé | 386 | Ustekinumab vs adalimumab dans la MC modérée à sévère après échec aux traitements conventionnels (dont AZA) — essai multicenter randomisé en aveugle |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | Terminé | 211 | Infliximab + antimetabolites (dont AZA) vs infliximab seul vs antimetabolites seuls pour maintien en rémission sans corticoïdes dans la MC — essai SPARE |
| [NCT00984568](https://clinicaltrials.gov/study/NCT00984568) | Phase 3 | Terminé (arrêté prématurément) | 28 | Stratégie « step-up » (prednisolone + AZA) vs infliximab monothérapie dans la RCH active modérée à sévère |
| [NCT07248644](https://clinicaltrials.gov/study/NCT07248644) | Phase 4 | Pas encore en recrutement | 304 | Arrêt des thiopurines (dont AZA) vs continuation chez les patients âgés (≥ 60 ans) en rémission soutenue sous RCH — essai IDEA |
| [NCT01015391](https://clinicaltrials.gov/study/NCT01015391) | N/A | Inconnu | 100 | T2 (dosage guidé par métabolites thiopuriniques) vs AZA standard pour maintien de rémission post-chirurgicale dans la MC — RCT ouvert |
| [NCT02929706](https://clinicaltrials.gov/study/NCT02929706) | N/A | Inconnu | 400 | Optimisation de la dose de thiopurine selon le génotype NUDT15 R139C pour réduire la leucopénie induite dans la MICI — RCT portant sur la sécurité pharmacogénomique |
| [NCT04304950](https://clinicaltrials.gov/study/NCT04304950) | Phase 4 | Terminé | 28 | Chronothérapie dans la MICI : impact du moment de prise (matin vs soir) de l'AZA ou 6-MP sur l'efficacité et les résultats cliniques |
| [NCT05014555](https://clinicaltrials.gov/study/NCT05014555) | N/A | Inconnu | 400 | Impact de l'immunosuppression systémique (dont AZA) sur la persistance des anticorps anti-COVID-19 chez les patients atteints de MICI vaccinés |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Revue | Journal of Crohn's & Colitis | Synthèse experte et actualisée sur les thiopurines (AZA, 6-MP, thioguanine) dans la MICI : efficacité, pharmacogénomique, gestion des effets indésirables et nouvelles perspectives thérapeutiques |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Revue | Expert Review of Gastroenterology & Hepatology | Mécanismes moléculaires actualisés de l'AZA dans la MICI, synthèse de nombreux essais cliniques et méta-analyses confirmant l'efficacité en induction et maintenance |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Revue | Scandinavian Journal of Gastroenterology Supplement | Efficacité et sécurité à long terme de l'AZA dans la MC : données fondant l'approbation pour le traitement de maintenance chronique |
| [30954317](https://pubmed.ncbi.nlm.nih.gov/30954317/) | 2019 | Revue | Gastroenterología y Hepatología | Revue des données sur l'arrêt des thiopurines (dont AZA) dans la MICI : quel patient peut interrompre le traitement et à quel moment ? |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Basic/Translational | Cell Reports Medicine | *Blautia wexlerae* identifié comme facteur de résistance à l'AZA via réduction de la biodisponibilité de la 6-MP : implications pour l'échec thérapeutique dans la MICI |
| [36462311](https://pubmed.ncbi.nlm.nih.gov/36462311/) | 2023 | Pharmacocinétique | Biomedicine & Pharmacotherapy | Méthylation du gène TPMT et pharmacocinétique de l'AZA chez les enfants atteints de MICI d'apparition très précoce (VEO-IBD) — données pédiatriques importantes |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Revue | Journal of Gastroenterology and Hepatology | Pharmacogénétique de l'AZA et 6-MP dans la MICI : variabilité inter-individuelle des métabolites, polymorphismes enzymatiques et implications pour la surveillance |
| [30889246](https://pubmed.ncbi.nlm.nih.gov/30889246/) | 2019 | Recherche Fondamentale | Inflammatory Bowel Diseases | L'AZA induit l'autophagie via mTORC1 et le senseur PERK de la réponse au stress du réticulum endoplasmique — mécanisme supplémentaire potentiellement bénéfique dans la MC associée aux gènes d'autophagie |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Revue | World Journal of Gastroenterology | Optimisation thérapeutique de la 6-MP et AZA dans la MICI : monitoring des 6-TGN et 6-MMP pour individualiser la posologie et réduire la toxicité hépatique et hématologique |
| [33305616](https://pubmed.ncbi.nlm.nih.gov/33305616/) | 2021 | Revue | Pharmacogenomics | Pharmacogénétique de la MICI : bilan des marqueurs génétiques (TPMT, NUDT15) prédictifs de la réponse aux thiopurines — très fructueux, contrairement aux biologiques |

---

## Informations de Marché en France

Aucune AMM enregistrée dans la base de données consultée pour l'azathioprine. Le champ `taiwan_regulatory.licenses` est vide et le statut de marché renseigné est « Non commercialisé ».

> Il est recommandé de vérifier directement la base de données de l'ANSM et de l'EMA, car l'azathioprine (ex. : Imurel®) est une molécule ancienne dont le statut réglementaire en France peut ne pas être capturé par ce système de requête.

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes (mises en garde, contre-indications, interactions médicamenteuses).

> Les données de sécurité spécifiques (avertissements ANSM, contre-indications et interactions médicamenteuses) n'ont pas été retrouvées dans la base de données consultée. Pour un médicament immunosuppresseur de ce profil, une attention particulière est attendue sur : la myélosuppression (notamment la leucopénie liée aux polymorphismes TPMT/NUDT15), le risque infectieux, et les interactions avec l'allopurinol (inhibiteur de la xanthine oxydase, entraînant une accumulation toxique des métabolites si combiné sans ajustement posologique).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
L'azathioprine bénéficie d'un niveau de preuve L1 pour la MICI, soutenu par de multiples essais cliniques de Phase 3 complétés, des méta-analyses et des revues systématiques, ainsi que par les lignes directrices ECCO et ACG. Le mécanisme d'action est directement aligné avec la physiopathologie de la MICI, et l'utilisation comme immunomodulateur de maintenance est établie en pratique clinique internationale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les données officielles sur le mécanisme d'action (MOA) via l'API DrugBank (référence DB00993)
- Extraire les mises en garde et contre-indications depuis la notice officielle ANSM (ou EMA) — données actuellement absentes du dossier
- Vérifier le statut réglementaire réel en France via la base de données ANSM/EMA (le système actuel indique 0 AMM, ce qui mérite confirmation)
- Mettre en place un plan de screening pharmacogénomique pré-traitement (TPMT et NUDT15) afin de réduire le risque de leucopénie grave, notamment dans les populations asiatiques à prévalence élevée du variant NUDT15 R139C
- Évaluer les interactions médicamenteuses potentielles, en particulier avec l'allopurinol (risque de toxicité majeure par accumulation de 6-TGN)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

