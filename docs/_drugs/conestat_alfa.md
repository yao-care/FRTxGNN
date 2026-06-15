---
layout: default
title: Conestat Alfa
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Conestat Alfa
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

# Conestat Alfa : De l'Absence d'AMM en France au Traitement du Déficit en Inhibiteur C1

## Résumé en Une Phrase

Conestat Alfa (Ruconest®) est un inhibiteur recombinant humain de la C1-estérase (rhC1-INH), produit dans des lapins transgéniques, qui ne dispose actuellement d'aucune AMM enregistrée en France dans notre base de données.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Déficit en Inhibiteur C1 (Angiœdème Héréditaire)**, avec **41 essais cliniques** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non enregistré en France |
| Nouvelle Indication Prédite | Déficit en Inhibiteur C1 |
| Score de Prédiction TxGNN | 99.999% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de Conestat Alfa ne sont pas disponibles dans notre système. Cependant, sur la base des informations connues dans la littérature médicale internationale, conestat alfa est une forme recombinante de l'inhibiteur humain C1 (rhC1-INH), appartenant à la superfamille des serpines (inhibiteurs de sérine protéases), codée par le gène SERPING1.

L'inhibiteur C1 endogène (C1-INH) régule deux voies majeures : la voie du complément classique, en inhibant les protéases C1r et C1s, et la voie d'activation par contact (système kallicréine-kinine), en inhibant le Facteur XIIa et la kallicréine plasmatique. Dans le déficit en inhibiteur C1 (AHH de type I ou II), une mutation de SERPING1 entraîne une insuffisance quantitative ou fonctionnelle de C1-INH, provoquant une surproduction de bradykinine — principal médiateur de la perméabilité vasculaire — et des épisodes récurrents d'œdème sous-cutané et muqueux pouvant mettre en jeu le pronostic vital.

Conestat Alfa agit comme thérapie de substitution directe en restaurant les niveaux fonctionnels de C1-INH, bloquant ainsi la cascade de production de bradykinine à l'origine des crises d'angiœdème. La correspondance entre le mécanisme d'action et la physiopathologie de la maladie est parfaite (remplacement précis de la protéine déficiente). Ce médicament est d'ailleurs déjà approuvé par l'EMA sous le nom Ruconest® dans plusieurs pays européens pour le traitement des crises aiguës d'AHH chez l'adulte et l'adolescent, ce qui renforce la pertinence de la prédiction TxGNN.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00462709](https://clinicaltrials.gov/study/NCT00462709) | Phase 3 | Terminé | 146 | CHANGE 3 : évaluation de l'efficacité et de la sécurité de C1INH-nf en prophylaxie de longue durée et en traitement des crises aiguës d'AHH |
| [NCT00289211](https://clinicaltrials.gov/study/NCT00289211) | Phase 3 | Terminé | 83 | LEVP2005-1/Partie A : essai double aveugle contrôlé par placebo sur l'efficacité et la sécurité de C1INH-nf dans les crises aiguës d'AHH |
| [NCT01188564](https://clinicaltrials.gov/study/NCT01188564) | Phase 3 | Terminé | 75 | Essai randomisé double aveugle contrôlé par placebo avec extension ouverte, confirmant l'efficacité de rhC1INH 50 U/kg et son profil d'immunogénicité dans les crises aiguës d'AHH |
| [NCT00262301](https://clinicaltrials.gov/study/NCT00262301) | Phase 3 | Terminé | 75 | Essai randomisé double aveugle contrôlé par placebo évaluant l'efficacité, la sécurité et la pharmacocinétique/pharmacodynamie du rhC1INH dans les crises aiguës d'AHH |
| [NCT00225147](https://clinicaltrials.gov/study/NCT00225147) | Phase 2/3 | Terminé | 77 | Essai randomisé double aveugle contrôlé par placebo évaluant la sécurité, la tolérance, l'efficacité et la pharmacocinétique du rhC1INH — essai pivot avant l'approbation européenne |
| [NCT00851409](https://clinicaltrials.gov/study/NCT00851409) | Phase 2 | Terminé | 25 | Étude ouverte exploratoire évaluant la sécurité et l'immunogénicité d'administrations répétées de rhC1INH 50 U/kg en prophylaxie hebdomadaire chez les patients avec déficit héréditaire en C1-INH |
| [NCT01095510](https://clinicaltrials.gov/study/NCT01095510) | Phase 2 | Terminé | 9 | Étude à dose unique ouverte évaluant la réponse et la pharmacocinétique/pharmacodynamie de différentes doses de CINRYZE chez les enfants de moins de 12 ans avec AHH |
| [NCT01467947](https://clinicaltrials.gov/study/NCT01467947) | Phase 4 | Terminé | 46 | Étude multicentrique post-commercialisation évaluant la formation d'anticorps inhibiteurs anti-C1-INH chez des patients AHH traités par Berinert® sur 9 mois |
| [NCT06690047](https://clinicaltrials.gov/study/NCT06690047) | Phase 4 | Terminé | 5 | Évaluation de l'efficacité de Ruconest® dans la prise en charge des prodromes d'AHH pour prévenir la progression vers une crise aiguë d'angiœdème |
| [NCT04414631](https://clinicaltrials.gov/study/NCT04414631) | Phase 2 | Arrêté | 80 | PROTECT-COVID-19 : essai pilote multicentrique évaluant si conestat alfa réduit la progression vers une lésion pulmonaire aiguë chez des patients hospitalisés pour COVID-19 (même médicament, indication différente) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30021471](https://pubmed.ncbi.nlm.nih.gov/30021471/) | 2018 | ECR / Essai Clinique | Expert Review of Clinical Immunology | Conestat alfa pour la prophylaxie de l'AHH chez l'adulte et l'adolescent : synthèse des données d'enregistrement, des essais de phase 2/3 et de la pratique clinique |
| [31982824](https://pubmed.ncbi.nlm.nih.gov/31982824/) | 2020 | Cohorte Prospective | International Immunopharmacology | Évaluation de l'efficacité et de la sécurité du rhC1-INH administré lors des crises et en prophylaxie de courte durée dans l'AHH, en conditions réelles |
| [22171564](https://pubmed.ncbi.nlm.nih.gov/22171564/) | 2012 | ECR | BioDrugs | Inhibiteur C1 recombinant : effets sur la coagulation et la fibrinolyse chez les patients AHH — pas d'augmentation du risque thromboembolique par rapport aux produits plasmatiques |
| [28754491](https://pubmed.ncbi.nlm.nih.gov/28754491/) | 2017 | ECR | Lancet | Essai de phase 2 multicentrique randomisé double aveugle contrôlé par placebo évaluant le rhC1INH en prophylaxie de l'angiœdème héréditaire — réduction significative de la fréquence des crises |
| [26250409](https://pubmed.ncbi.nlm.nih.gov/26250409/) | 2015 | Revue Systématique | Immunotherapy | Revue systématique de la thérapie de substitution recombinante pour l'AHH par déficit en C1-INH, comparant les formulations plasmatiques et recombinantes |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Revue Systématique | Pneumonologia i Alergologia Polska | Comparaison de l'efficacité clinique de conestat alfa, C1-INH humain et icatibant dans les crises aiguës d'AHH chez l'adulte — sur la base d'une revue systématique |
| [22946752](https://pubmed.ncbi.nlm.nih.gov/22946752/) | 2012 | Revue Médicamenteuse | BioDrugs | Conestat alfa : revue de son efficacité thérapeutique dans les crises d'angiœdème chez les patients AHH, à partir de deux essais randomisés pivots |
| [24801469](https://pubmed.ncbi.nlm.nih.gov/24801469/) | 2014 | Cohorte Prospective | Allergy and Asthma Proceedings | Traitement à domicile avec conestat alfa dans l'AHH par déficit en C1-INH : analyse de 65 épisodes œdémateux chez deux patientes en conditions réelles |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Recommandation Clinique | Current Opinion in Allergy and Clinical Immunology | Prise en charge diagnostique et thérapeutique de l'AHH par déficit en C1-INH : l'expérience italienne — place des traitements à la demande versus prophylaxie |
| [27940765](https://pubmed.ncbi.nlm.nih.gov/27940765/) | 2016 | Recommandation Clinique | Pediatrics | Recommandations du Medical Advisory Board de l'association des patients AHH pour la prise en charge des enfants atteints d'AHH par déficit en inhibiteur C1 |

---

## Informations de Marché en France

Aucune AMM française n'est enregistrée pour Conestat Alfa dans notre base de données. À titre contextuel, le médicament est approuvé par l'EMA sous le nom **Ruconest®** pour le traitement des crises aiguës d'angiœdème chez les adultes et adolescents atteints d'AHH de type I et II ; cette approbation centralisée est en principe applicable dans l'ensemble des États membres de l'Union européenne, y compris la France.

> Aucune AMM nationale distincte enregistrée en France dans notre base de données. Vérification du statut de commercialisation réelle auprès de l'ANSM recommandée.

---

## Considérations de Sécurité

> Veuillez consulter la notice officielle et les informations ANSM/EMA pour les mises en garde, contre-indications et interactions médicamenteuses complètes (données non disponibles dans notre système).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais cliniques de Phase 3 randomisés, en double aveugle, contrôlés par placebo, publiés dans des revues internationales de premier rang (dont le *Lancet*), démontrent avec un niveau de preuve L1 l'efficacité et la sécurité de conestat alfa pour le traitement des crises aiguës d'angiœdème héréditaire par déficit en C1-INH. Le score TxGNN de 99,999 % est cohérent avec la réalité clinique : ce médicament est précisément indiqué pour cette pathologie et dispose déjà d'approbations réglementaires internationales (EMA, FDA).

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmer le statut de commercialisation réel en France auprès de l'ANSM (AMM EMA active ? Disponibilité effective ?)
- Obtenir les données complètes sur le mécanisme d'action (MOA) via DrugBank (DG002)
- Récupérer et analyser la notice officielle ANSM/EMA pour les mises en garde, contre-indications et interactions (DG001)
- Évaluer les conditions de remboursement via la Haute Autorité de Santé (HAS) et vérifier l'existence d'une inscription sur la liste des médicaments pris en charge
- Établir un plan de surveillance de sécurité pour les populations spéciales (enfants dès 2 ans, femmes enceintes, patients avec antécédents d'allergie aux protéines de lapin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

