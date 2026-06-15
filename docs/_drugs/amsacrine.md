---
layout: default
title: Amsacrine
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 5
---

# Amsacrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# AMSACRINE : De la Leucémie Aiguë au Myélome Plasmocytaire

## Résumé en Une Phrase

AMSACRINE (m-AMSA) est un agent cytotoxique de la classe des intercalants d'ADN et inhibiteurs de Topoisomérase II, historiquement utilisé dans le traitement de la leucémie aiguë myéloblastique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Myélome Plasmocytaire (plasma cell myeloma)**,
avec **0 essai clinique enregistré** et **7 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie aiguë (agent antileucémique reconnu) |
| Nouvelle Indication Prédite | Myélome Plasmocytaire (plasma cell myeloma) |
| Score de Prédiction TxGNN | 99,32% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

AMSACRINE est un agent intercalant de l'ADN appartenant à la famille des acridines. Son mécanisme d'action repose sur la stabilisation du complexe covalent Topoisomérase II–ADN (complexe clivable), entraînant des cassures double-brin irréparables et la mort cellulaire. Ce mécanisme est analogue à celui des anthracyclines (doxorubicine), déjà utilisées en clinique dans le myélome multiple.

Les cellules plasmocytaires myélomateuses présentent une activité Topoisomérase II particulièrement élevée, nécessaire à la réplication accélérée de l'ADN et à la synthèse massive d'immunoglobulines monoclonales. Cette caractérisation biologique fait du myélome plasmocytaire une cible biologiquement cohérente pour un inhibiteur de Topo II tel qu'AMSACRINE. La prédiction TxGNN s'appuie sur cette proximité topologique dans le graphe de connaissances biomédicales, ce qui constitue ici une extrapolation mécanistique rationnelle — non un artefact algorithmique.

Des essais cliniques de Phase II ont effectivement été conduits avec AMSACRINE dans le myélome multiple dès les années 1980, confirmant qu'il existe un historique clinique, même si l'efficacité observée demeure limitée dans des populations lourdement prétraitées.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement sur ClinicalTrials.gov ou l'ICTRP.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|----------------------|
| [2913481](https://pubmed.ncbi.nlm.nih.gov/2913481/) | 1989 | Essai clinique Phase II | Med Pediatr Oncol | 74 patients atteints de myélome multiple traités par AMSACRINE 120 mg/m² toutes les 3 semaines ; 3% de réponse partielle, toxicité sévère chez 33% — efficacité limitée dans cette population |
| [6688199](https://pubmed.ncbi.nlm.nih.gov/6688199/) | 1983 | Essai clinique Phase II | Cancer Treat Rep | Évaluation d'AMSACRINE dans tumeurs solides, myélome et lymphome ; 12 réponses partielles sur 221 patients — activité antitumorale modeste dans le myélome |
| [1958848](https://pubmed.ncbi.nlm.nih.gov/1958848/) | 1991 | Étude in vitro | Anti-Cancer Drugs | Cytotoxicité comparée d'intercalants d'ADN sur cellules de myélome 8226 et cardiomyocytes de rat ; IC50 établies pour AMSACRINE — profil cytotoxique documenté in vitro |
| [2064323](https://pubmed.ncbi.nlm.nih.gov/2064323/) | 1991 | Revue | Anticancer Res | Revue des nouveaux cytotoxiques en leucémie ; fludarabine mentionnée comme active dans le myélome multiple, et AMSACRINE (m-AMSA) discutée dans ce contexte |
| [2419036](https://pubmed.ncbi.nlm.nih.gov/2419036/) | 1985 | Revue | Curr Probl Cancer | Revue du test de clonage tumoral humain avec corrélations cliniques incluant AMSACRINE dans diverses néoplasies hématologiques |
| [3910194](https://pubmed.ncbi.nlm.nih.gov/3910194/) | 1985 | Étude corrélationnelle rétrospective | Cancer Invest | Corrélations cliniques avec le test de clonage tumoral humain appliqué à AMSACRINE |
| [17133426](https://pubmed.ncbi.nlm.nih.gov/17133426/) | 2007 | Série de cas rétrospective | Am J Hematol | 10 patients atteints de myélome réfractaire/rechutant traités par bortézomib ; 60% de zona — données contextuelles sur le myélome traité |

---

## Informations de Marché en France

AMSACRINE ne dispose d'aucune AMM en France. Ce médicament n'est pas commercialisé sur le territoire français.

---

## Cytotoxicité

AMSACRINE est un agent antinéoplasique cytotoxique (intercalant d'ADN / inhibiteur de Topoisomérase II).

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel — intercalant d'ADN de la famille des acridines |
| Risque de Myélossuppression | Élevé — toxicité hématologique dose-limitante documentée (neutropénie, thrombocytopénie) |
| Classification d'Émétogénicité | Modérée |
| Éléments de Surveillance | NFS avec différentielle (suivi régulier), fonction hépatique, fonction rénale, ECG (risque d'arythmie cardiaque documenté avec AMSACRINE) |
| Protection de Manipulation | Doit être manipulé selon les réglementations en vigueur pour les médicaments cytotoxiques (préparation sous hotte à flux laminaire, équipement de protection individuelle adapté) |

---

## Considérations de Sécurité

Les données de sécurité spécifiques (mises en garde ANSM, contre-indications formelles, interactions médicamenteuses) ne sont pas disponibles dans la base de données interrogée pour ce médicament.

Veuillez consulter la notice et la littérature médicale disponible pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
La prédiction TxGNN pour le myélome plasmocytaire repose sur un mécanisme d'action biologiquement cohérent (inhibition de Topoisomérase II sur cellules plasmocytaires à haute activité réplicative), et deux essais cliniques de Phase II ont déjà exploré cette indication dans les années 1980–1989. Bien que les résultats d'efficacité soient modestes dans des populations lourdement prétraitées, la preuve de concept clinique existe. La progression nécessite une réévaluation dans le contexte thérapeutique moderne (combinaisons, populations sélectionnées, biomarqueurs Topo II).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes sur le mécanisme d'action (MOA) issues de DrugBank
- Profil de sécurité complet : mises en garde, contre-indications et interactions médicamenteuses (données manquantes — catégorie Blocking selon le Data Gap DG001)
- Évaluation de la cardiotoxicité spécifique à AMSACRINE (risque d'arythmie documenté dans la littérature)
- Stratégie de repositionnement moderne : sélection de biomarqueurs Topoisomérase II, association potentielle avec bortézomib ou IMiDs dans le myélome réfractaire/rechutant
- Revue réglementaire pour obtention d'une ATU (Autorisation Temporaire d'Utilisation) en France, AMSACRINE n'étant pas commercialisé
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

