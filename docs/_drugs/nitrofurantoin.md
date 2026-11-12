---
layout: default
title: Nitrofurantoin
parent: Prédiction du modèle uniquement (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Nitrofurantoin : nouvelle indication prédite, Polyarthrite rhumatoïde (niveau de preuve L5). Indication d'origine : Non renseignée dans les AMM compilées"
monitor_inn: "nitrofurantoin"
predicted_indications: ["rheumatoid arthritis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "sclerosing cholangitis", "methemoglobinemia, alpha type", "gout", "methemoglobinemia"]
---

# Nitrofurantoin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Nitrofurantoïne : De l'infection urinaire à la polyarthrite rhumatoïde (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

La nitrofurantoïne est un antibactérien urinaire. Le dossier français compilé pour ce rapport ne contient toutefois aucun texte d'indication.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **polyarthrite rhumatoïde**, mais **aucun essai clinique** ne soutient cette direction.
Les **9 publications** retrouvées décrivent surtout des effets indésirables (fibrose pulmonaire, interaction avec le méthotrexate), pas un bénéfice thérapeutique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM compilées |
| Nouvelle Indication Prédite | Polyarthrite rhumatoïde |
| Score de Prédiction TxGNN | 0,9989 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la nitrofurantoïne est un antibactérien utilisé dans les infections urinaires. Aucun mécanisme anti-inflammatoire ou immunomodulateur utile dans la polyarthrite rhumatoïde n'est documenté dans les données compilées.

La littérature associe la nitrofurantoïne à la polyarthrite rhumatoïde uniquement sous l'angle des effets indésirables : fibrose pulmonaire médicamenteuse, interaction avec le méthotrexate provoquant une fibrose pulmonaire irréversible, et une étude sur l'utilisation d'antibiotiques et les poussées de la maladie. Le score élevé du modèle reflète probablement une association dans le réseau de connaissances (traitements ou comorbidités de la polyarthrite), et non un effet thérapeutique.

Les autres prédictions (rang 2 à 10) ne sont pas non plus étayées : certaines sont de simples prédictions sans donnée, d'autres, comme la méthémoglobinémie, indiquent un risque d'aggravation.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohorte (série de cas auto-contrôlée) | Scientific Reports | Étude de l'association entre antibiotiques et poussées de polyarthrite rhumatoïde dans une cohorte de 31 992 patients |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohorte | Chest | Mauvais pronostic des patients atteints de polyarthrite hospitalisés pour fibrose pulmonaire interstitielle (non spécifique à la nitrofurantoïne) |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Revue | Saudi Med J | Fibrose pulmonaire médicamenteuse ; la nitrofurantoïne figure parmi les médicaments responsables |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Revue | Rev Prat | Pneumopathies interstitielles médicamenteuses ; la nitrofurantoïne est citée parmi les antibiotiques impliqués |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Rapport de cas | Cureus | Fibrose pulmonaire irréversible après association méthotrexate et nitrofurantoïne chez une patiente de 94 ans atteinte de polyarthrite |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Rapport de cas | Cureus | Hépatite auto-immune : la nitrofurantoïne est citée parmi les causes médicamenteuses à écarter |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Rapport de cas | Ann Dermatol Venereol | Sialadénite médicamenteuse (phénylbutazone) ; la nitrofurantoïne est citée parmi les médicaments rapportés |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Rapport de cas | Rev Pneumol Clin | Pneumopathie induite par les sels d'or (nitrofurantoïne non concernée) |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Autre | Acta Med Scand | Traitement de la bactériurie par nitrofurantoïne chez des femmes d'âge moyen (indication antibactérienne) |

Aucune de ces publications ne démontre un bénéfice de la nitrofurantoïne dans la polyarthrite rhumatoïde.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62013296 | FURADANTINE 50 mg, gélule (TAMRISA ACCESS (FRANCE)) | Gélule | Non renseignée (AMM active) |

## Considérations de Sécurité

Les données compilées ne contiennent pas de mises en garde ni de contre-indications issues de la notice. Les éléments suivants proviennent du graphe de connaissances et non du texte de la notice :

- **Contre-indications issues du graphe de connaissances** : insuffisance rénale et anurie, déficit en G6PD, atteintes hépatiques (hépatite, lésion hépatique médicamenteuse, ictère obstructif, maladie des voies biliaires), atteintes pulmonaires (maladie pulmonaire interstitielle, fibrose pulmonaire), atteintes neurologiques (neuropathie périphérique, névrite optique), carence en vitamine B12 ou en vitamines du groupe B, diabète et acidocétose diabétique, colite à *Clostridium difficile*, ainsi que certaines maladies métaboliques (galactosémie, cystinurie, glycogénose).
- **Interactions médicamenteuses** : 172 interactions recensées. Les interactions de niveau modéré incluent le métronidazole, la naltrexone, la rosuvastatine, la simvastatine, la balsalazide et l'acide picosulfurique. Les interactions mineures concernent surtout les anticholinergiques (atropine, hyoscyamine, scopolamine) et les antiacides à base de magnésium.
- **Signaux issus de la littérature** : toxicité pulmonaire (aggravée par le méthotrexate), hépatotoxicité, hémolyse et méthémoglobinémie en cas de déficit en G6PD.

Pour toute information de sécurité faisant foi, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni preuve de bénéfice, alors que la littérature signale surtout des risques pulmonaires, hépatiques et hématologiques chez les patients atteints de polyarthrite.

<!-- review:begin fr-lic-20261106-nitrofurantoin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni preuve de bénéfice, alors que la littérature signale surtout des risques pulmonaires, hépatiques et hématologiques chez les patients atteints de polyarthrite. L'AMM française est de plus annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-nitrofurantoin-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action et justification mécanistique d'un effet dans la polyarthrite rhumatoïde
- Notice officielle de l'ANSM (mises en garde et contre-indications) pour l'évaluation de sécurité
- Indication d'origine documentée et situation réglementaire actuelle du produit
- Preuves précliniques, puis cliniques, d'un bénéfice thérapeutique avant toute reconsidération

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « L'AMM française est de plus annulée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

