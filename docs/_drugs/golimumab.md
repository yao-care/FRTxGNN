---
layout: default
title: Golimumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 370
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "GOLIMUMAB"
predicted_indications: ["hypermobility of coccyx", "Kummell disease"]
description: "Golimumab : nouvelle indication prédite, Hypermobility of coccyx (niveau de preuve L5). En France, AMM dans la BDPM : 8 (valides : 8)"
---

# Golimumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Golimumab: Hypermobility of coccyx
{: .text-alpha }

## Résumé en Une Phrase

Le golimumab est un anticorps monoclonal anti-TNF-alpha, utilisé à l'origine dans les rhumatismes inflammatoires (polyarthrite rhumatoïde, rhumatisme psoriasique, spondylarthrite ankylosante) et les maladies inflammatoires de l'intestin (rectocolite hémorragique).
Le modèle TxGNN prédit qu'il pourrait être efficace dans la **vascularite rhumatoïde**.
À ce jour, les preuves sont **indirectes** : **1 essai clinique** enregistré, sans rapport avec l'efficacité du golimumab dans cette maladie, et **6 publications** (cas cliniques, revues, méta-analyse portant sur la polyarthrite rhumatoïde).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypermobility of coccyx |
| Score de Prédiction TxGNN | 0.9967 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 8 sur 8) |
| Nombre d'AMM | 8 (valides : 8) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Golimumab (traduction non officielle) : « Le golimumab est un anticorps monoclonal humain qui se lie aux formes bioactives, solubles et transmembranaires, du TNFα humain. Cette interaction empêche la liaison du TNFα à ses récepteurs, inhibant ainsi l'activité biologique du TNFα (une protéine de type cytokine). » Texte original en anglais : "Golimumab is a human monoclonal antibody that binds to both the soluble and transmembrane bioactive forms of human TNFα. This interaction prevents the binding of TNFα to its receptors, thereby inhibiting the biological activity of TNFα (a cytokine protein)." ([DailyMed: Simponi (golimumab) prescribing information, Janssen Biotech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f86cb4a7-c358-4136-ae57-b32bda9bba00), version du 2026-11-02 ; consulté le 2026-11-19). Sur la base des informations connues, le golimumab neutralise le TNF-alpha, une cytokine clé de l'inflammation dans la polyarthrite rhumatoïde. Son efficacité dans cette maladie est établie, et mécanistiquement il pourrait être applicable à la vascularite rhumatoïde.

La vascularite rhumatoïde est une complication extra-articulaire grave de la polyarthrite rhumatoïde. Elle survient plus souvent chez les patients séropositifs, et son incidence a diminué depuis l'arrivée des biothérapies anti-TNF. Il existe donc un lien biologique plausible entre l'indication d'origine et la nouvelle indication prédite.

Ce raisonnement reste toutefois théorique. Les données disponibles concernent surtout les atteintes articulaires de la polyarthrite rhumatoïde, des revues générales sur les biothérapies et des cas de pathologies voisines (uvéite de la maladie de Behçet, artérite de Takayasu). Aucune étude ne teste le golimumab dans la vascularite rhumatoïde elle-même.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | En recrutement | 80 | Gestion des immunosuppresseurs avant une arthroplastie totale de l'épaule chez des patients de rhumatologie (poussées, douleur, complications de plaie, infections). Cet essai ne teste pas le golimumab dans la vascularite et n'apporte pas de preuve d'efficacité. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Méta-analyse en réseau de 36 ECR | Int J Mol Sci | Les anti-TNF d'origine et biosimilaires, dont le golimumab, réduisent de façon similaire la destruction articulaire dans la polyarthrite rhumatoïde. Preuve indirecte, sans lien avec la vascularite. |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Revue | BMC Med | Mise à jour sur les biothérapies des maladies auto-immunes : alternative aux traitements classiques, avec des limites (voie intraveineuse, coût, effets indésirables). |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Revue | Semin Arthritis Rheum | Fréquence et causes de l'insuffisance rénale terminale dans la polyarthrite rhumatoïde et prise en charge du traitement dans ce contexte. |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Cas clinique | Ocul Immunol Inflamm | Uvéite de la maladie de Behçet traitée avec succès par golimumab. Pathologie voisine, mais ce n'est pas une vascularite rhumatoïde. |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Cas cliniques (2) | Joint Bone Spine | Deux cas d'artérite de Takayasu apparus **sous** traitement anti-TNF. Ce signal de sécurité potentiel ne soutient pas l'efficacité. |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Cas clinique | Rheumatol Int | Pyoderma gangrenosum et arthrite septique avec sepsis sévère chez une patiente atteinte de polyarthrite rhumatoïde traitée par golimumab. Il s'agit d'un événement indésirable grave, non d'une preuve d'efficacité. |

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67700426 | SIMPONI 100 mg, solution injectable en seringue préremplie | Solution injectable | JANSSEN CILAG INTERNATIONAL NV | Active |
| 60035714 | SIMPONI 50 mg, solution injectable en seringue préremplie | Solution injectable | JANSSEN CILAG INTERNATIONAL NV | Active |
| 62534114 | SIMPONI 100 mg, solution injectable en stylo prérempli | Solution injectable | JANSSEN CILAG INTERNATIONAL NV | Active |
| 62222050 | SIMPONI 50 mg, solution injectable en stylo pré-rempli | Solution injectable | JANSSEN CILAG INTERNATIONAL NV | Active |
| 62464897 | GOBIVAZ 100 mg, solution injectable en seringue préremplie | Solution injectable | ADVANZ PHARMA LIMITED | Active |
| 63851320 | GOBIVAZ 50 mg, solution injectable en stylo prérempli | Solution injectable | ADVANZ PHARMA LIMITED | Active |
| 65332908 | GOBIVAZ 50 mg, solution injectable en seringue préremplie | Solution injectable | ADVANZ PHARMA LIMITED | Active |
| 68655966 | GOBIVAZ 100 mg, solution injectable en stylo prérempli | Solution injectable | ADVANZ PHARMA LIMITED | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées au total ; les 20 premières sont présentées ici.
  - **Majeures** :
    - corticoïdes : hydrocortisone, triamcinolone (y compris ophtalmique), dexaméthasone, bétaméthasone, budésonide, prednisone, prednisolone ;
    - déférisprone ;
    - radiopharmaceutiques et anticorps radiomarqués : iobenguane (I-131), ibritumomab tiuxétan, tositumomab, tositumomab (I-131).
  - **Modérées** : métronidazole, tinidazole, rosuvastatine, simvastatine.
  - **Mineures** : sels de zinc (sulfate, acétate, gluconate).
- **Signaux issus de la littérature** : un cas de sepsis sévère sous golimumab et deux cas d'artérite de Takayasu survenus sous anti-TNF appellent à la prudence dans un contexte vasculaire inflammatoire.
- **Précautions classiques des anti-TNF** : dépistage de la tuberculose et de l'hépatite B, revue du statut vaccinal, surveillance des infections et des tumeurs malignes.

<!-- review:begin fr-lic-20261106-golimumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 4 AMM, détenues par JANSSEN CILAG INTERNATIONAL NV, sont annulées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 4 AMM pour ce médicament, dont 4 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-golimumab-1 -->

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les signaux de sécurité des cas cliniques et l'absence d'AMM valide en France justifient d'attendre des données plus solides.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données cliniques directes sur le golimumab (ou d'autres anti-TNF) dans la vascularite rhumatoïde : séries de cas, études observationnelles, puis essai contrôlé.
- Les données de mécanisme d'action détaillées, afin de mieux analyser le lien mécanistique.
- Les mises en garde et contre-indications officielles issues de la notice, pour mener l'évaluation de sécurité.
- Une clarification du statut réglementaire en France et des voies d'accès possibles.
- Une évaluation de l'artérite de Takayasu et des autres vascularites apparues sous anti-TNF, afin de mesurer le risque dans cette population.

<!-- review:begin fr-lic-20261106-golimumab-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Une clarification du statut réglementaire en France (AMM annulées) et des voies d'accès possibles. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 4 AMM pour ce médicament, dont 4 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-golimumab-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 4 AMM, détenues par JANSSEN CILAG INTERNATIONAL NV, sont annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Simponi (golimumab) prescribing information, Janssen Biotech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f86cb4a7-c358-4136-ae57-b32bda9bba00) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

