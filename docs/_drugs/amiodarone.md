---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarone : Des Arythmies Ventriculaires à la Tachycardie Ventriculaire Polymorphe Catécholaminergique (CPVT)

## Résumé en Une Phrase

L'amiodarone est un antiarythmique de classe III à spectre large, largement utilisé dans le traitement des arythmies ventriculaires graves et des arythmies supraventriculaires réfractaires.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Tachycardie Ventriculaire Polymorphe Catécholaminergique (CPVT)**,
avec **0 essai clinique enregistré** et **10 publications** disponibles, dont aucune n'étudie directement l'amiodarone comme traitement de première ligne dans cette indication.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non renseignée — aucune AMM dans la base de données actuelle |
| Nouvelle Indication Prédite | Tachycardie ventriculaire polymorphe catécholaminergique (CPVT) |
| Score de Prédiction TxGNN | 99,78 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé (base de données actuelle) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de l'amiodarone ne sont pas disponibles dans la présente base de données. Sur la base des informations connues dans la littérature cardio-pharmacologique, l'amiodarone est un antiarythmique à action multi-canaux appartenant à la classe III de Vaughan-Williams. Il bloque principalement les canaux potassiques à rectification retardée (IKr/IKs), avec des effets additionnels sur les canaux sodiques (blocage use-dependent), les canaux calciques de type L, ainsi qu'un effet bloquant α/β-adrénergique non compétitif. Ces propriétés prolongent la durée du potentiel d'action et la période réfractaire effective, supprimant ainsi les circuits de réentrée et les activités déclenchées.

La CPVT est une canalopathie ionique héréditaire rare, le plus souvent liée à une mutation du récepteur à la ryanodine 2 (RYR2) ou de la calséquestrine-2 (CASQ2). En conditions adrénergiques (exercice, stress), ces mutations provoquent une libération anormale de calcium du réticulum sarcoplasmique, générant des post-dépolarisations retardées (DAD) et une activité déclenchée. Théoriquement, le blocage des canaux calciques de type L par l'amiodarone pourrait atténuer ces mécanismes.

Toutefois, les recommandations actuelles pour la CPVT placent clairement les β-bloquants en première ligne, et le flécaïnide (inhibiteur direct des canaux RYR2) en deuxième ligne. L'amiodarone ne figure pas dans les algorithmes de traitement établis pour la CPVT, et sa propriété de prolongation du QT représente un risque potentiellement défavorable dans ce contexte. Les données de la littérature suggèrent que son efficacité dans les orages rythmiques liés à la CPVT est limitée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Revue | Expert Opinion Pharmacotherapy | Synthèse des avancées pharmacologiques dans les arythmies ventriculaires ; rôle des antiarythmiques dont l'amiodarone dans la CPVT discuté comme option limitée |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Cohorte rétrospective | Life (Basel) | Revue systématique des caractéristiques cliniques, génétiques et des issues arythmiques des patients CPVT en Chine ; traitement antiarythmique décrit |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohorte rétrospective | Reviews in Cardiovascular Medicine | Caractéristiques cliniques, base génétique et utilisation des ressources de santé pour la CPVT dans une cohorte chinoise |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Série de cas prospective | PACE | Flécaïnide pour suppression de la tempête rythmique déclenchée par le DAI dans la CPVT ; amiodarone mentionné comme alternative en cas d'échec |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Rapport de cas | Frontiers in Cardiovascular Medicine | Résolution de CPVT réfractaire par dénervation sympathique cardiaque droite après échec de la dénervation gauche chez un adolescent |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Rapport de cas | BMJ Case Reports | Arrêt cardiaque chez l'enfant avec CPVT ; amiodarone utilisée en réanimation, 40 chocs défibrillation administrés |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Rapport de cas | Turk Pediatri Arsivi | CPVT comme cause rare d'arrêt cardiaque soudain chez l'enfant de 2 ans ; tableau clinique et prise en charge décrits |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Rapport de cas | Medicine | Diagnostic retardé de 6 ans d'une CPVT avec mutation RYR2 chez un enfant de 9 ans en Chine |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Rapport de cas | Anesthesia & Analgesia | Syndrome du QT long avec arythmies ventriculaires réfractaires chez un nouveau-né ; pharmacothérapie multimodale incluant amiodarone + esmolol + pacing ventriculaire |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Rapport de cas | Revista Española de Cardiología | Orage rythmique induit par les chocs du DAI dans la CPVT ; amiodarone utilisée dans la prise en charge de la tempête électrique |

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché (AMM) n'est enregistrée pour l'amiodarone dans la base de données actuelle. Ce résultat reflète une absence de données dans la source interrogée, et ne signifie pas nécessairement que l'amiodarone est indisponible en France — ce médicament est en effet largement commercialisé en Europe sous différentes spécialités (Cordarone®, génériques). Une vérification auprès de la base de données de l'ANSM est recommandée.

---

## Considérations de Sécurité

Les données de sécurité spécifiques à l'amiodarone ne sont pas disponibles dans la base de données actuelle (source TFDA non renseignée). Sur la base des données de sécurité établies pour ce médicament dans la littérature internationale :

- **Mises en Garde Principales** : Toxicité pulmonaire (pneumopathie interstitielle, BOOP) ; toxicité thyroïdienne (hypothyroïdie, hyperthyroïdie) ; hépatotoxicité ; prolongation du QT et risque de torsades de pointes ; toxicité oculaire (micro-dépôts cornéens, neuropathie optique) ; neuropathie périphérique ; photosensibilisation cutanée
- **Contre-indications** : Bradycardie sinusale grave ; blocs auriculoventriculaires de haut degré (sans pacemaker) ; dysfonction sinusale ; hypersensibilité à l'iode ; grossesse et allaitement ; dysthyroïdie préexistante

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'amiodarone présente une connexion mécanistique théorique avec la CPVT via le blocage calcique, mais les recommandations cliniques actuelles ne le retiennent pas comme traitement établi de cette pathologie. L'absence totale d'essais cliniques dans cette indication et un niveau de preuve L4 (uniquement littérature observationnelle et rapports de cas) ne permettent pas de soutenir une progression vers un usage structuré. De plus, la propriété de prolongation du QT intrinsèque à l'amiodarone constitue un risque potentiellement antagoniste au contexte électrophysiologique de la CPVT.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) issues de DrugBank — actuellement manquantes (Data Gap DG002)
- Données de sécurité complètes issues de la notice officielle ANSM/TFDA (Data Gap DG001 — Blocking)
- Recherche d'études précliniques sur l'amiodarone dans des modèles CPVT (RYR2 knock-in) pour évaluer son effet sur les DAD
- Consultation des recommandations EHRA/ESC 2022 sur la CPVT pour repositionner l'amiodarone dans l'algorithme thérapeutique (3ème ligne ou thérapie de sauvetage uniquement)
- Évaluation de la pertinence de la prédiction TxGNN à la lumière des trois meilleures indications : la **Tachycardie Ventriculaire** (rang 3, L1, Proceed with Guardrails) constitue une cible de repositionnement nettement plus solide et cliniquement actionnable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

