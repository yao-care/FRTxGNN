---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cytarabine : De la Leucémie Aiguë au Carcinome Pulmonaire à Petites Cellules

## Résumé en Une Phrase

Cytarabine (Ara-C) est un antimétabolite pyrimidinique historiquement utilisé dans le traitement des leucémies aiguës, en particulier la leucémie aiguë myéloïde (LAM).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Carcinome Pulmonaire à Petites Cellules (SCLC)**,
avec **3 essais cliniques** et **20 publications** soutenant actuellement cette direction de recherche.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie aiguë (usage établi ; aucune AMM française répertoriée) |
| Nouvelle Indication Prédite | Carcinome pulmonaire à petites cellules (SCLC) |
| Score de Prédiction TxGNN | 99.78% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Cytarabine est un analogue de la déoxycytidine appartenant à la classe des antimétabolites pyrimidiniques. Bien que les données détaillées sur le mécanisme d'action (MOA) ne soient pas disponibles dans cet Evidence Pack, cytarabine est reconnu comme l'un des agents les plus actifs contre les leucémies aiguës de l'adulte. Son mécanisme implique l'inhibition de l'ADN polymérase α et l'incorporation dans la chaîne d'ADN naissante, entraînant une terminaison de chaîne et une mort cellulaire spécifique de la phase S du cycle cellulaire.

Le SCLC présente un index de prolifération extrêmement élevé (Ki-67 > 90%), ce qui en fait une cible théorique pour les agents S-phase-spécifiques comme cytarabine. Cette hypothèse a été explorée cliniquement dès les années 1970–1980 : cytarabine a été intégrée dans des protocoles combinés pour le SCLC (PMID 232239, 1979), et des études de phase II ont évalué sa combinaison avec l'étoposide dans les SCLC réfractaires (PMID 2841844, 1988), montrant des taux de réponse de l'ordre de 29%. Cytarabine a ensuite été largement supplantée par les associations étoposide-platine, devenues le standard.

Des données précliniques apportent un argument mécanistique complémentaire : les lignées cellulaires SCLC résistantes aux anthracyclines et à l'étoposide (via une topoisomérase II altérée) développent paradoxalement une sensibilité croisée à cytarabine et à la gemcitabine (PMID 11331076, 2001). Ce phénomène de « collateral sensitivity » suggère que cytarabine pourrait conserver une activité dans les SCLC multi-traités en rechute, là où les thérapies standard ont échoué.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Terminé | 34 | Chimiothérapie intrathécale (pemetrexed) + radiothérapie impliquant le champ pour métastases leptoméningées de tumeurs solides ; cytarabine et cytarabine liposomale citées comme agents intrathécaux de référence auxquels se compare le protocole |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Terminé | 13 | Pemetrexed intrathécal pour métastases leptoméningées de NSCLC récidivant après TKI ; cytarabine liposomale identifiée comme agent de comparaison standard pour la voie intrathécale |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Arrêté prématurément | 34 | Chimiothérapie adjuvante dans le NSCLC précoce post-chirurgie (vinorelbine, cisplatine, docétaxel, gemcitabine, pemetrexed) ; arrêté prématurément, sans lien direct avec cytarabine dans le SCLC |

> **Note :** Les 3 essais identifiés présentent une pertinence indirecte (grade C) vis-à-vis de cytarabine dans le SCLC. Aucun essai clinique prospectif moderne spécifiquement dédié à cytarabine dans le SCLC n'est actuellement enregistré.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Cohorte historique | Med Pediatr Oncol | 20 patients SCLC traités par cyclophosphamide + adriamycine + cytarabine (CAC) + radiothérapie ; RC + RP : 78%, survie médiane 49+ semaines pour les répondeurs complets |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Essai clinique (2 bras) | Am J Clin Oncol | Ara-C 100 mg/m²/j en perfusion continue dans le SCLC : aucune réponse en monothérapie (n=10, rechute) ; ajout au CAV (n=25, SCLC extensif) insuffisant pour valider l'indication |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Essai clinique | Am J Clin Oncol | VP-16 + Ara-C (45 mg/m²/j × 72h) chez 17 patients SCLC réfractaires ; 2 RC + 3 RP (taux de réponse ≈ 29%) malgré toxicité hématologique sévère ; 3 décès précoces |
| [11331076](https://pubmed.ncbi.nlm.nih.gov/11331076/) | 2001 | Préclinique | Biochem Pharmacol | Lignées SCLC résistantes (daunorubicine/VM-26) montrent une sensibilité croisée à cytarabine et gemcitabine via topoisomérase II altérée ; plaide pour cytarabine en rattrapage multi-résistant |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Série de cas | Am J Med | 60 patients SCLC avec méningite carcinomateuse ; chimiothérapie intensive (incluant cytarabine intrathécale) ; taux de réponse globale 78%, survie médiane 49+ semaines (RC) |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Rapport de cas | Gan to Kagaku Ryoho | SCLC stade IV (cT4N2M1b) avec méningite carcinomateuse traité par approche multidisciplinaire ; cytarabine intrathécale intégrée dans la stratégie thérapeutique avec réponse partielle |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II | Tumori | Cytarabine (15 mg/m² SC × 6 doses) + cisplatine + vindesine chez 32 patients NSCLC avancé ; taux de réponse 18% (5/28), toxicité hématologique notable |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II | Cancer | Cytarabine haute dose (3 g/m²) + cisplatine chez 37 patients NSCLC vierges de chimio ; réponse globale 14% ; myélosuppression Grade IV dans 32% des cas, 4 décès sous traitement |
| [1360876](https://pubmed.ncbi.nlm.nih.gov/1360876/) | 1992 | Préclinique | Cancer Chemother Pharmacol | Panel de 3 lignées SCLC avec différents profils de résistance multidrogue ; corrélation de sensibilité entre doxorubicine, étoposide et vincristine, avec cytarabine évaluée comme agent alternatif |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | ECR | J Clin Oncol | Essai randomisé CALGB dans le SCLC stade limité : chimiothérapie (protocole N4SE incluant 5-FU/cytarabine/hydroxyurée dans le contexte S-phase) + radiothérapie ± warfarine ; l'ajout de warfarine non significatif |

---

## Cytotoxicité

Cytarabine répond aux critères d'identification d'un agent antinéoplasique cytotoxique : antimétabolite de la classe des analogues nucléosidiques pyrimidiniques, utilisé en traitement de première ligne des leucémies aiguës.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (classe Antimétabolite – Analogue nucléosidique pyrimidinique, S-phase spécifique) |
| Risque de Myélosuppression | Élevé — neutropénie et thrombocytopénie dose-limitantes ; Grade IV observé dans 32% des cas à haute dose (3 g/m²), Grade III dans 14% (PMID 2156598) |
| Classification d'Émétogénicité | Modérée à élevée selon la dose (haute dose Ara-C ≥ 1 g/m² : hautement émétogène) |
| Éléments de Surveillance | NFS avec formule différentielle (bihebdomadaire à quotidienne selon l'intensité du traitement), bilan hépatique et rénal, examen neurologique (syndrome cérébelleux décrit à haute dose) |
| Protection de Manipulation | Manipulation obligatoire sous isolateur ou hotte à flux laminaire ; élimination et traçabilité conformes aux réglementations de manipulation des médicaments cytotoxiques (EPI complets obligatoires) |

---

## Considérations de Sécurité

> Veuillez consulter la notice officielle pour les informations de sécurité. Les données spécifiques de mises en garde, contre-indications et interactions médicamenteuses ne sont pas disponibles dans cet Evidence Pack.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les données historiques (1979–1988) révèlent un signal d'activité clinique de cytarabine dans le SCLC — notamment un taux de réponse de ~29% avec l'association VP-16 + Ara-C en situation réfractaire (PMID 2841844) — et les données précliniques de sensibilité croisée sont biologiquement plausibles. Cependant, l'absence d'essais cliniques modernes spécifiques au SCLC, la toxicité hématologique sévère à haute dose, et la disponibilité de protocoles standard supérieurs (étoposide-platine, immunothérapies anti-PD-L1) ne permettent pas de justifier un repositionnement clinique sans données complémentaires substantielles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtention des données complètes sur le mécanisme d'action (MOA) via DrugBank (DG002)
- Données de sécurité ANSM : mises en garde officielles, contre-indications et interactions médicamenteuses (DG001)
- Étude préclinique moderne sur des modèles SCLC actuels (PDX, organoïdes) pour valider et quantifier la sensibilité croisée observée in vitro
- Évaluation de la pharmacogénomique des transporteurs nucléosidiques (hENT1/hCNT1) dans les biopsies SCLC pour identifier les sous-populations susceptibles de répondre (PMID 18600541)
- Exploration du potentiel de synergie avec les immunothérapies anti-PD-L1 dans le SCLC réfractaire, sur la base du signal ADORA1–PD-L1 (PMID 32183950)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

