---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 1
---

# Apixaban
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

# Apixaban : De l'Anticoagulation à la Migraine

## Résumé en Une Phrase

Apixaban est un anticoagulant oral de la classe des inhibiteurs directs du facteur Xa, dont les données d'indication originale approuvée ne sont pas disponibles dans ce pack de données.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine**, avec **1 essai clinique** (indirect, grade C) et **4 publications** soutenant actuellement cette direction.
Cependant, les signaux disponibles sont contradictoires : plusieurs rapports de cas suggèrent que l'apixaban pourrait **aggraver** la migraine plutôt que la soulager, ce qui tempère significativement l'optimisme de la prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible (aucune AMM trouvée dans les données) |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99,02% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé (selon les données disponibles) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action de l'apixaban ne sont pas disponibles dans ce pack. Sur la base des informations connues, l'apixaban appartient à la classe des inhibiteurs directs du facteur Xa (anticoagulants oraux directs, AOD/DOAC). Son efficacité dans la prévention des événements thromboemboliques est établie, et son mécanisme pourrait théoriquement s'appliquer à la migraine via la pathologie vasculaire.

L'hypothèse mécanistique centrale repose sur le **foramen ovale perméable (FOP)** : ce défaut de cloison cardiaque crée un shunt droite-gauche permettant à des micro-thrombus veineux de contourner la circulation pulmonaire et d'atteindre la circulation systémique cérébrale. Ces micro-embolies déclencheraient une dépression corticale envahissante (DCS/CSD), mécanisme physiopathologique central de la migraine avec aura. En bloquant la formation de ces micro-caillots via l'inhibition du facteur Xa, l'apixaban pourrait théoriquement réduire la fréquence des crises migraineuses chez les patients porteurs d'un FOP.

Cependant, un **signal clinique préoccupant** fragilise cette hypothèse : des rapports de cas documentent une rémission complète de la migraine sous warfarine, suivie d'une réapparition des symptômes lors du passage à l'apixaban, et d'une nouvelle résolution au retour à la warfarine. Cette dissociation intra-classe suggère que l'effet anti-migraine observé avec les anticoagulants serait spécifique aux antagonistes de la vitamine K (AVK) — dont le spectre d'action est plus large que la seule inhibition du facteur Xa — et non généralisable à l'apixaban. Un rapport de cas supplémentaire décrit même une **aggravation** directe de la migraine après introduction de l'apixaban.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Terminé | 664 | Essai CLOSE — Fermeture percutanée du FOP versus anticoagulants (warfarine/AVK, **non apixaban**) versus antiplaquettaires pour la prévention des récidives d'AVC ischémique. La migraine constitue un critère d'évaluation secondaire/observationnel, non le critère principal. Fournit un contexte indirect sur le lien FOP-migraine mais ne teste pas directement l'apixaban. Pertinence : grade C (indirecte). |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Étude pilote rétrospective | *Lupus* | 75 patients porteurs d'anticorps antiphospholipides et de migraine réfractaire : amélioration symptomatique sous traitement antithrombotique, soutenant l'existence d'un lien entre hypercoagulabilité et migraine. Signal positif pour la classe, non spécifique à l'apixaban. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Rapport de cas + revue de littérature | *The Neurologist* | Aggravation de la migraine avec aura après introduction de l'apixaban. La revue de littérature conclut que l'impact des AOD sur la fréquence et la sévérité de la migraine reste peu documenté et contradictoire. **Signal négatif direct** pour l'apixaban. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Rapport de cas | *Headache* | Femme de 55 ans : rémission complète de la migraine avec aura sous warfarine pendant 12 ans, réapparition dans les 3 semaines suivant le passage à l'apixaban, résolution en quelques jours à la reprise de la warfarine. Suggère une **spécificité de la warfarine** non reproductible avec l'apixaban. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Rapport de cas | *Headache* | Migraine vestibulaire résolue sous warfarine associée au topiramate — contexte AVK combiné à un antiépileptique, non spécifique à l'apixaban. Résumé non disponible dans les données. |

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché (AMM) n'a été trouvée pour l'apixaban dans les données disponibles de ce pack. Le statut réglementaire français complet (Eliquis®) devra être vérifié directement auprès de l'ANSM ou de la base de données publique des médicaments.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les preuves actuelles ne soutiennent pas l'avancement de l'apixaban dans la migraine : le niveau de preuve est L4 (reposant sur des rapports de cas et une étude pilote rétrospective), et les signaux disponibles sont non seulement insuffisants mais **activement contradictoires** — un rapport de cas documente une aggravation directement imputable à l'apixaban, et un second montre que l'effet bénéfique observé avec les anticoagulants est spécifique à la warfarine et non reproductible avec l'apixaban. Le score TxGNN élevé (99,02%) reflète probablement la relation pharmacologique générale entre anticoagulants et migraine associée au FOP, sans distinguer les différences d'effet intra-classe (AVK vs inhibiteurs directs du Xa).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action détaillées (MOA) de l'apixaban, notamment la comparaison AVK vs inhibiteurs du facteur Xa dans le contexte FOP-migraine (combler DG002)
- Données de sécurité complètes : mises en garde et contre-indications officielles (combler DG001)
- Vérification du statut AMM français réel de l'apixaban (Eliquis®) auprès de l'ANSM
- Étude de cohorte prospective ou essai pilote randomisé comparant directement apixaban versus warfarine dans la migraine associée au FOP
- Clarification de la spécificité intra-classe : pourquoi les AVK montrent un signal bénéfique absent chez les inhibiteurs directs du facteur Xa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

