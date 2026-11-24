---
layout: default
title: Omeprazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 560
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "omeprazole"
predicted_indications: ["duodenal obstruction"]
description: "Omeprazole : nouvelle indication prédite, Duodenal obstruction (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Omeprazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Omeprazole: Duodenal obstruction
{: .text-alpha }

## Résumé en Une Phrase

L'oméprazole est un inhibiteur de la pompe à protons, initialement utilisé pour traiter l'ulcère gastrique et duodénal, le reflux gastro-œsophagien, l'œsophagite et le syndrome de Zollinger-Ellison.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Duodenal obstruction |
| Score de Prédiction TxGNN | 0.9964 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 18) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Omeprazole (traduction non officielle) : « L'oméprazole appartient à une classe de composés antisécrétoires, les benzimidazoles substitués, qui suppriment la sécrétion d'acide gastrique par inhibition spécifique du système enzymatique H + /K + ATPase au niveau de la surface sécrétoire de la cellule pariétale gastrique. Ce système enzymatique étant considéré comme la pompe à acide (à protons) de la muqueuse gastrique, l'oméprazole a été caractérisé comme un inhibiteur de la pompe à acide gastrique, en ce qu'il bloque l'étape finale de la production d'acide. » Texte original en anglais : "Omeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H + /K + ATPase enzyme system at the secretory surface of the gastric parietal cell. Because this enzyme system is regarded as the acid (proton) pump within the gastric mucosa, omeprazole has been characterized as a gastric acid-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Prilosec (omeprazole magnesium) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b6761f84-53ac-4745-a8c8-1e5427d7e179), version du 2024-03-19 ; consulté le 2026-11-19). Sur la base des informations connues, l'oméprazole fait partie de la classe des inhibiteurs de la pompe à protons : il réduit la sécrétion d'acide gastrique et son efficacité dans le reflux gastro-œsophagien et les ulcères est établie.

Le reflux duodéno-gastrique est toutefois dû à la remontée de bile et de sécrétions pancréatiques dans l'estomac. La suppression de l'acide ne traite donc pas la cause principale. L'oméprazole pourrait au mieux soulager les symptômes en réduisant la composante acide de la lésion muqueuse. De petites études cliniques rapportent un effet sur le reflux biliaire dans l'œsophage de Barrett et chez l'enfant.

Le score très élevé (0,9964) est une simple prédiction, probablement dû à la forte proximité avec les indications approuvées de reflux. Par ailleurs, des études animales (PMID 10389684, 8943968, 33027361) suggèrent qu'en présence de reflux duodéno-gastrique, le blocage de l'acide pourrait favoriser la croissance de la muqueuse et la cancérogenèse gastrique, ce qui constitue une préoccupation de sécurité.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | Non applicable | Terminé | 157 | Étude d'imagerie endoscopique tri-modale pour distinguer la dyspepsie fonctionnelle du reflux ; étude diagnostique, sans preuve directe d'efficacité de l'oméprazole |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Étude clinique | Scand J Gastroenterol | Effet de l'oméprazole sur le reflux duodéno-gastrique antral dans l'œsophage de Barrett |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Étude clinique | Gut | Effet de l'oméprazole 20 mg deux fois par jour sur le reflux biliaire duodéno-gastrique et gastro-œsophagien dans l'œsophage de Barrett |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Étude prospective | J Pediatr Gastroenterol Nutr | Traitement du reflux biliaire œsophagien par oméprazole chez l'enfant |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revue | Eur J Clin Pharmacol | Mise à jour sur l'usage clinique et la pharmacocinétique des inhibiteurs de la pompe à protons |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | Étude physiologique | Gastroenterology | Relation entre pH, reflux duodéno-gastro-œsophagien et œsophage de Barrett |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Étude clinique | Eur J Pediatr | Reflux duodéno-gastrique primaire chez six enfants et adolescents, résistant aux antiacides classiques |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Étude animale (rat) | Dig Dis Sci | Le blocage de l'acide par oméprazole favorise la cancérogenèse gastrique induite par le reflux |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Étude animale (rat) | Dig Dis Sci | Le reflux stimule la croissance de la muqueuse, potentialisée par le blocage de l'acide |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Étude animale (rat) | Acta Cir Bras | Effet protecteur éventuel de l'oméprazole sur l'adénocarcinome gastrique avec reflux |

## Informations de Marché en France

Le texte des indications approuvées n'est pas disponible.

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 64103828 | MOPRAL 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE) | Active |
| 67234658 | OMEPRAZOLE VIATRIS 40 mg, poudre pour solution pour perfusion | Poudre pour solution pour perfusion | VIATRIS SANTE | Active |
| 68748071 | OMEPRAZOLE SANDOZ 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | SANDOZ | Active |
| 67993388 | OMEPRAZOLE TEVA PHARMA 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | TEVA SANTE | Active |
| 65204851 | OMEPRAZOLE EVOLUGEN PHARMA 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | EVOLUPHARM | Active |
| 65830008 | OMEPRAZOLE CRISTERS PHARMA 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | CRISTERS | Active |
| 69531932 | OMEPRAZOLE ZENTIVA LAB 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | ZENTIVA FRANCE | Active |
| 67995040 | OMEPRAZOLE BIOGARAN 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | BIOGARAN | Active |
| 68995940 | OMEPRAZOLE SANDOZ CONSEIL 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | SANDOZ | Active |
| 65581090 | OMEPRAZOLE TEVA PHARMA 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | TEVA SANTE | Active |
| 62943125 | OMEPRAZOLE SANDOZ 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | SANDOZ | Active |
| 65658163 | OMEPRAZOLE TEVA SANTE 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | TEVA SANTE | Active |
| 61123131 | OMEPRAZOLE ARROW 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | ARROW GENERIQUES | Active |
| 63244391 | OMEPRAZOLE ZENTIVA LAB 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | ZENTIVA FRANCE | Active |
| 68605333 | OMEPRAZOLE ALMUS 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | ALMUS FRANCE | Active |
| 67450136 | OMEPRAZOLE BIOGARAN 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | BIOGARAN | Active |
| 69036504 | OMEPRAZOLE VIATRIS CONSEIL 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | VIATRIS SANTE | Active |
| 60806188 | OMEPRAZOLE ALMUS 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | ALMUS FRANCE | Active |
| 64261479 | OMEPRAZOLE CRISTERS LAB 10 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | SUN PHARMA FRANCE | Abrogée |
| 61490953 | OMEPRAZOLE CRISTERS LAB 20 mg, gélule gastro-résistante | Gélule gastro-résistant(e) | SUN PHARMA FRANCE | Archivée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique, maladie hépatique, maladie de la vésicule biliaire, insuffisance cardiaque congestive, ostéoporose (dont postménopausique), fracture osseuse, gastrite atrophique chronique.
- **Interactions médicamenteuses** : 673 interactions recensées. Parmi les exemples : interactions **majeures** avec l'acalabrutinib et l'atazanavir ; interactions **modérées** avec l'hydrochlorothiazide, l'alprazolam, l'atorvastatine, le fénofibrate, l'amphotéricine B, l'amikacine, l'amphétamine, l'anagrélide, l'apalutamide et l'armodafinil ; interactions **mineures** avec la lidocaïne, la nifédipine, l'ambrisentan et l'acide acétylsalicylique.
- **Signal animal** : le blocage de l'acide en présence de reflux duodéno-gastrique pourrait favoriser la cancérogenèse gastrique chez le rat (à confirmer chez l'humain).

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à de petites études cliniques et à des études animales, sans essai randomisé évaluant l'oméprazole dans le reflux duodéno-gastrique ; le mécanisme ne cible pas la cause du reflux biliaire, et un signal de cancérogenèse chez l'animal est préoccupant. Le seul essai clinique recensé est diagnostique.
- Le statut réglementaire français et l'absence de données de notice empêchent aussi de passer à l'étape de criblage de sécurité.

<!-- review:begin fr-lic-20261106-omeprazole-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le statut réglementaire français (toutes AMM annulées) et l'absence de données de notice empêchent aussi de passer à l'étape de criblage de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-omeprazole-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (mises en garde et contre-indications) sur le site de l'ANSM
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Vérifier le statut commercial actuel de l'oméprazole en France (AMM actives ou abrogées vs produits réellement commercialisés ; la plupart des AMM sont actives)
- Mener ou identifier des essais contrôlés sur le reflux biliaire/duodéno-gastrique avec critères cliniques
- Évaluer le risque de cancérogenèse gastrique lié à l'inhibition acide prolongée en présence de reflux biliaire

<!-- review:begin fr-lic-20261115-omeprazole-1 -->

> **Correction de vérification (2026-11-15)**: Texte initial : « (AMM annulées vs produits réellement disponibles) » D’après la BDPM complète (CIS_bdpm et CIS_COMPO_bdpm, 2026-11-15), les spécialités contenant OMÉPRAZOLE comptent 48 AMM, dont 46 actives et 2 abrogées ou archivées. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt).

<!-- review:end fr-lic-20261115-omeprazole-1 -->

---

### Note sur la seconde prédiction (obstruction duodénale)

L'obstruction duodénale (score TxGNN 0,9964) est classée au niveau **L5** avec la décision **Hold** : il s'agit d'une affection mécanique ou structurelle (atrésie, sténose, tumeur, pancréas annulaire) relevant d'une prise en charge chirurgicale ou endoscopique, sans lien mécanistique clair avec l'oméprazole. L'unique essai associé (NCT00557921, phase 3, terminé prématurément, 5 000 participants) porte sur l'association clopidogrel + oméprazole pour réduire les événements gastro-intestinaux hauts et ne permet pas d'étayer cette indication.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (toutes AMM annulées) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-15 | « (AMM annulées vs produits réellement disponibles) » → « (AMM actives ou abrogées vs produits réellement co » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Prilosec (omeprazole magnesium) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b6761f84-53ac-4745-a8c8-1e5427d7e179) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

