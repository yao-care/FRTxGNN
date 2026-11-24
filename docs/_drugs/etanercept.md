---
layout: default
title: Etanercept
parent: Prédiction du modèle uniquement (L5)
nav_order: 303
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "etanercept"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
description: "Etanercept : nouvelle indication prédite, Hypermobility of coccyx (niveau de preuve L5). En France, AMM dans la BDPM : 20 (valides : 20)"
---

# Etanercept
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Etanercept: Hypermobility of coccyx
{: .text-alpha }

## Résumé en Une Phrase

L'étanercept est une protéine de fusion inhibitrice du TNF, initialement utilisée dans le traitement de la polyarthrite rhumatoïde, du rhumatisme psoriasique, de la spondylarthrite ankylosante et de l'arthrite juvénile idiopathique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **vascularite rhumatoïde** (rang 1 de la liste de prédictions).
Cette prédiction repose sur **1 essai clinique** (sans lien direct avec l'indication) et **20 publications**, dont une seule revue systématique pertinente ; les preuves directes restent très limitées.

*Remarque : d'autres indications prédites (spondylopathie inflammatoire, arthrite juvénile polyarticulaire) correspondent en réalité à des indications déjà reconnues de l'étanercept ; elles sont présentées dans la conclusion.*

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypermobility of coccyx |
| Score de Prédiction TxGNN | 0.9963 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 20 sur 20) |
| Nombre d'AMM | 20 (valides : 20) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Etanercept (traduction non officielle) : « Le TNF est une cytokine naturelle impliquée dans les réponses inflammatoires et immunitaires normales. Il joue un rôle important dans les processus inflammatoires de la PR, de l'AJI polyarticulaire, du RPso et de la SA, ainsi que dans l'atteinte articulaire qui en résulte. […] L'étanercept est une forme soluble dimérique du récepteur p75 du TNF capable de se lier aux molécules de TNF. » Texte original en anglais : "TNF is a naturally occurring cytokine that is involved in normal inflammatory and immune responses. It plays an important role in the inflammatory processes of RA, polyarticular JIA, PsA, and AS and the resulting joint pathology. […] Etanercept is a dimeric soluble form of the p75 TNF receptor that can bind TNF molecules." ([DailyMed: Enbrel (etanercept) prescribing information, Immunex Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a002b40c-097d-47a5-957f-7a7b1807af7f), version du 2026-05-11 ; consulté le 2026-11-19). Sur la base des connaissances générales, l'étanercept est une protéine de fusion composée du récepteur soluble du TNF (p75) et d'un fragment Fc d'IgG1. Elle neutralise le TNF-alpha, cytokine pro-inflammatoire centrale dans plusieurs maladies auto-immunes.

La vascularite rhumatoïde est une complication extra-articulaire sévère de la polyarthrite rhumatoïde, indication déjà reconnue de l'étanercept. L'inflammation médiée par le TNF y joue un rôle, ce qui rend le blocage du TNF biologiquement plausible.

Cependant, la littérature rapporte aussi des vascularites cutanées et des néphropathies **associées** à l'étanercept. L'inhibition du TNF peut donc, paradoxalement, induire des lésions vascularitiques ou immuno-médiées. Le rapport bénéfice/risque est incertain.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | En recrutement | 80 | Gestion des immunosuppresseurs chez des patients de rhumatologie avant arthroplastie de l'épaule ; ne teste pas l'étanercept dans la vascularite rhumatoïde, donc aucune preuve directe d'efficacité |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revue systématique | Clinical Rheumatology | Revue systématique sur l'usage des biothérapies dans la vascularite rhumatoïde |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Revue | Nephrol Dial Transplant | Rôle possible du blocage du TNF-alpha dans la vascularite associée aux ANCA |
| [16624928](https://pubmed.ncbi.nlm.nih.gov/16624928/) | 2006 | Revue | J Am Soc Nephrol | Rôle du TNF-alpha dans la vascularite associée aux ANCA, enseignements d'autres maladies inflammatoires |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohorte | RMD Open | Risque d'événements de type lupus et vascularite sous anti-TNF dans la polyarthrite rhumatoïde (registre BSRBR-RA) |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Rapport de cas | Cureus | Néphropathie associée à l'étanercept |
| [10955351](https://pubmed.ncbi.nlm.nih.gov/10955351/) | 2000 | Rapport de cas | J Rheumatol | Vascularite leucocytoclasique due à l'étanercept |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Rapport de cas | Arthritis Rheum | Nodulose accélérée et vascularite après étanercept dans la polyarthrite rhumatoïde |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Rapport de cas | Case Rep Med | Vascularite des gros vaisseaux sous anti-TNF chez un patient atteint de polyarthrite rhumatoïde |
| [19648728](https://pubmed.ncbi.nlm.nih.gov/19648728/) | 2009 | Rapport de cas | Dermatology | Zona disséminé simulant une vascularite rhumatoïde sous étanercept |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Revue | Scand J Immunol | Immunologie des vascularites cutanées associées à l'étanercept et à l'infliximab |

La plupart de ces publications décrivent des vascularites **induites** par les anti-TNF plutôt qu'un bénéfice thérapeutique.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63061721 | NEPEXTO 50 mg, solution injectable en seringue préremplie | Solution injectable | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |
| 68672848 | ENBREL 50 mg, solution injectable en seringue pré-remplie | Solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 63886766 | ENBREL 10 mg, poudre et solvant pour solution injectable pour usage pédiatrique | Poudre et solvant pour solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 64784134 | ERELZI 50 mg, solution injectable en stylo prérempli | Solution injectable | SANDOZ (AUTRICHE) | Active |
| 64959320 | ENBREL 25 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 61382671 | ERELZI 25 mg, solution injectable en seringue préremplie | Solution injectable | SANDOZ (AUTRICHE) | Active |
| 69653644 | BENEPALI 50 mg, solution injectable en stylo prérempli | Solution injectable | SAMSUNG BIOEPIS NL (PAYS-BAS) | Active |
| 67599870 | ENBREL 50 mg, solution injectable en cartouche distributrice de dose | Solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 62130342 | BENEPALI 25 mg, solution injectable en seringue préremplie | Solution injectable | SAMSUNG BIOEPIS NL (PAYS-BAS) | Active |
| 66071293 | NEPEXTO 50 mg, solution injectable en stylo prérempli | Solution injectable | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |
| 64504550 | BENEPALI 50 mg, solution injectable en seringue préremplie | Solution injectable | SAMSUNG BIOEPIS NL (PAYS-BAS) | Active |
| 61320748 | ENBREL 25 mg, solution injectable en cartouche distributrice de dose | Solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 67270711 | ERELZI 50 mg, solution injectable en seringue préremplie | Solution injectable | SANDOZ (AUTRICHE) | Active |
| 68667580 | ENBREL 25 mg, solution injectable en seringue pré-remplie | Solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 60529218 | NEPEXTO 25 mg, solution injectable en seringue préremplie | Solution injectable | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |
| 61187835 | ENBREL 25 mg, solution injectable en stylo pré-rempli | Solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 66393935 | ENBREL 50 mg, solution injectable en stylo pré-rempli | Solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 62314125 | FUBELV 25 mg, solution injectable en seringue préremplie | Solution injectable | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |
| 65073779 | FUBELV 50 mg, solution injectable en seringue préremplie | Solution injectable | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |
| 67347225 | FUBELV 50 mg, solution injectable en stylo prérempli | Solution injectable | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Au total, 20 AMM sont recensées.

<!-- review:begin fr-lic-20261106-etanercept-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Au total, 17 AMM sont recensées, toutes annulées (Enbrel, Benepali, Erelzi, Nepexto). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 17 AMM pour ce médicament, dont 17 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261106-etanercept-1 -->

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 352 interactions sont recensées. Les principales, de niveau majeur, concernent les corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisone, prednisolone), ainsi que la défériprone, l'iobenguane (I-131), l'ibritumomab tiuxétan et le tositumomab. Des interactions modérées sont signalées avec le métronidazole, le tinidazole, la rosuvastatine et la simvastatine, et mineures avec les sels de zinc.
- **Signaux issus de la littérature** : vascularites cutanées, néphropathies, réactivation de tuberculose, infections opportunistes (dont zona disséminé).

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold** (pour la vascularite rhumatoïde)

**Justification :**
- Le score TxGNN est élevé, mais aucune preuve clinique directe n'existe, et la littérature signale surtout des vascularites induites par l'étanercept. Le rapport bénéfice/risque est incertain.

**Autres indications prédites (pour information) :**

| Indication prédite | Score TxGNN | Niveau de preuve | Décision |
|------|------|------|------|
| Maladie vertébrale | 0,9916 | L5 | Question de recherche (catégorie trop large, preuves indirectes) |
| Hypermobilité du coccyx | 0,9963 | L5 | Hold (prédiction purement computationnelle) |
| Maladie de Kümmell | 0,9955 | L5 | Hold (aucune preuve, aucun rationnel lié au TNF) |

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action issues de DrugBank
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Études cliniques directes de l'étanercept dans la vascularite rhumatoïde
- Pour les indications déjà reconnues : mesures standard des anti-TNF (dépistage de la tuberculose et des infections, surveillance de l'uvéite et des maladies inflammatoires de l'intestin, suivi pédiatrique et vaccinal)

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-24 | Supprimé : « toutes annulées (Enbrel, Benepali, Erelzi, Nepexto) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Enbrel (etanercept) prescribing information, Immunex Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a002b40c-097d-47a5-957f-7a7b1807af7f) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

