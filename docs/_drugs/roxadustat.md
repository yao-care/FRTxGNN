---
layout: default
title: Roxadustat
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 4
---

# Roxadustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Roxadustat : De l'Anémie Rénale au Syndrome de l'Œil Sec

## Résumé en Une Phrase

Roxadustat est un inhibiteur de la prolyl-hydroxylase de HIF (HIF-PHI), une classe de médicaments utilisée dans le traitement de l'**anémie rénale** (anémie liée à la maladie rénale chronique) — ce lien est mentionné dans les données d'essais cliniques disponibles, le médicament n'étant pas commercialisé en France.
Le modèle TxGNN prédit qu'il pourrait présenter un intérêt pour le **Syndrome de l'Œil Sec**,
mais cette direction ne repose actuellement que sur **1 essai clinique observationnel non interventionnel** (statut inconnu) et **aucune publication**, ce qui en fait une piste de recherche préliminaire plutôt qu'une preuve d'efficacité.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Anémie rénale (mentionnée dans les données d'essais cliniques disponibles ; aucune donnée d'AMM française n'existe car le médicament n'est pas commercialisé) |
| Nouvelle Indication Prédite | Syndrome de l'Œil Sec (dry eye syndrome) |
| Score de Prédiction TxGNN | 99.51 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le champ officiel de mécanisme d'action (MOA) n'est pas renseigné dans les données DrugBank de ce dossier. Toutefois, l'analyse de repositionnement disponible dans le pack de preuves indique que Roxadustat agit comme un **inhibiteur de la prolyl-hydroxylase de HIF (HIF-PHI)**, stabilisant HIF-1α et HIF-2α — le mécanisme bien connu de cette classe thérapeutique, utilisée pour stimuler la production endogène d'érythropoïétine chez les patients atteints d'anémie liée à la maladie rénale chronique.

Le lien avec le syndrome de l'œil sec n'est pas direct : la voie de signalisation HIF participe théoriquement à l'adaptation de l'épithélium de la surface oculaire et des glandes de Meibomius en contexte d'hypoxie ou d'inflammation, ce qui pourrait en théorie influencer la stabilité du film lacrymal. Cependant, le seul essai clinique identifié n'évalue pas Roxadustat comme traitement de l'œil sec : il observe la morphologie et la fonction des glandes de Meibomius chez des patients souffrant d'**anémie rénale** (une population susceptible d'être traitée par Roxadustat ou d'autres agents stimulant l'érythropoïèse), sans que le médicament soit lui-même l'intervention étudiée.

Il s'agit donc d'un lien fondé sur un **chevauchement de population de patients** plutôt que sur une preuve directe d'efficacité médicament-maladie. Le raisonnement mécanistique reste indirect et non validé expérimentalement à ce stade.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | N/A (observationnel) | Statut inconnu | 50 | Étude observationnelle sur la morphologie et la fonction des glandes de Meibomius chez des patients atteints d'anémie rénale traités notamment par Roxadustat ; l'essai ne teste pas Roxadustat comme traitement de l'œil sec, mais caractérise cette population de patients présentant des symptômes de sécheresse oculaire. Évaluation de pertinence : **Grade C** (association indirecte, hypothèse-génératrice uniquement). |

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Roxadustat n'est actuellement **pas commercialisé en France** (0 AMM enregistrée, aucune licence disponible dans les données réglementaires). Aucun tableau de spécialités ne peut donc être présenté.

---

## Autres Pistes Prédites par TxGNN (Signaux Complémentaires)

Le pack de preuves inclut trois autres indications prédites pour Roxadustat, toutes classées **Hold** (niveau de preuve L5 — prédiction du modèle uniquement, aucune étude clinique ni littérature) :

| Indication Prédite | Score TxGNN | Raison du Hold |
|------|------|------|
| Maladie osseuse de Paget | 99.12 % | Direction mécanistique potentiellement contradictoire : l'activation de HIF-1α favorise plutôt l'activité ostéoclastique via l'axe RANKL/VEGF, ce qui pourrait aggraver la résorption osseuse excessive caractéristique de la maladie de Paget, au lieu de l'améliorer. |
| Dentinogenèse imparfaite | 99.06 % | Maladie génétique structurelle (mutations COL1A1/COL1A2/DSPP) sans rapport physiopathologique établi avec la voie HIF ; lien jugé faible, probable faux positif du modèle. |
| Carcinome épidermoïde (squamous cell carcinoma) | 99.02 % | **Signal de sécurité, non d'opportunité thérapeutique.** La stabilisation de HIF par Roxadustat pourrait théoriquement favoriser la croissance tumorale (angiogenèse, métabolisme glycolytique) plutôt que la freiner — cohérent avec la surveillance oncologique déjà requise pour les HIF-PHI dans les essais sur l'anémie rénale. Ce signal doit être traité comme une **contre-indication potentielle**, pas comme une piste de repositionnement. |

---

## Considérations de Sécurité

Les données structurées de sécurité (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans ce dossier. Veuillez consulter la notice pour les informations de sécurité.

À noter cependant, sur la base de l'analyse mécanistique des prédictions TxGNN elles-mêmes : la classe des HIF-PHI (dont Roxadustat) fait l'objet d'une surveillance oncologique connue, la prédiction « carcinome épidermoïde » de ce même dossier suggérant un risque théorique de stimulation tumorale plutôt qu'un bénéfice thérapeutique (voir section ci-dessus).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La seule piste avec un début de preuve clinique (syndrome de l'œil sec) repose sur un essai observationnel unique, non interventionnel, à statut inconnu, jugé de pertinence faible (Grade C) par l'évaluation même du pack de preuves. Aucune publication ne soutient cette direction. Les trois autres prédictions (Paget, dentinogenèse imparfaite, carcinome épidermoïde) n'ont aucun essai clinique ni littérature, et l'une d'elles constitue potentiellement un signal de risque plutôt qu'une opportunité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résolution du data gap bloquant (DG001) : obtention du RCP/notice TFDA (ou équivalent EMA/ANSM) pour les mises en garde et contre-indications, indispensable avant toute évaluation de sécurité (S1)
- Résolution du data gap MOA (DG002) : confirmation du mécanisme d'action via DrugBank pour affiner l'analyse mécanistique
- Un essai clinique interventionnel spécifique testant Roxadustat pour le syndrome de l'œil sec (et non une simple étude observationnelle de population)
- Clarification du profil de risque oncologique de Roxadustat avant toute exploration ultérieure, compte tenu du signal mécanistique contradictoire identifié pour le carcinome épidermoïde
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

