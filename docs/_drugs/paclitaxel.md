---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel : D'un Cytotoxique de Référence en Oncologie au Carcinome Mammaire Féminin

## Résumé en Une Phrase

Paclitaxel est un agent cytotoxique de la classe des taxanes, largement utilisé en oncologie ; les données réglementaires fournies ne documentent toutefois pas son indication d'origine (aucune AMM recensée en France, statut « non commercialisé »). Le modèle TxGNN prédit une efficacité pour le **Carcinome Mammaire Féminin**, avec **50 essais cliniques** et **20 publications** recensés à l'appui — un volume de preuves qui correspond en réalité à une **reconfirmation d'un usage oncologique déjà établi** plutôt qu'à un véritable repositionnement inédit.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans les données réglementaires disponibles (aucune AMM identifiée) |
| Nouvelle Indication Prédite | Carcinome Mammaire Féminin (female breast carcinoma) |
| Score de Prédiction TxGNN | 99.99% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées de mécanisme d'action au niveau du médicament (fiche DrugBank) ne sont pas encore disponibles dans ce dossier (lacune de données de sévérité élevée). Sur la base des éléments mécanistiques associés à cette prédiction, paclitaxel stabilise les microtubules et bloque leur dépolymérisation au niveau du fuseau mitotique, ce qui induit un arrêt du cycle cellulaire en phase G2/M puis l'apoptose des cellules à prolifération rapide — mécanisme caractéristique de la classe des taxanes.

Ce mécanisme constitue le fondement pharmacologique classique de la chimiothérapie du cancer du sein. Il est important de noter que le rationnel mécanistique fourni pour cette prédiction indique explicitement qu'il ne s'agit pas d'une hypothèse de repositionnement nouvelle, mais d'une **reconfirmation d'une indication déjà établie** : le cancer du sein figure parmi les usages historiques et documentés de paclitaxel dans la littérature (par exemple, un article de synthèse de 1997 rappelle que le médicament était déjà autorisé pour le cancer de l'ovaire métastatique et le carcinome mammaire métastatique).

Ainsi, la forte densité de preuves cliniques (essais de phase 3 multiples, littérature abondante) reflète surtout la maturité de l'usage clinique de paclitaxel dans cette indication, plutôt qu'une découverte de repositionnement à proprement parler. Cela ne diminue pas la pertinence clinique de la prédiction, mais change la nature de la décision à prendre (validation réglementaire locale plutôt que génération d'hypothèse).

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Terminé | 200 | Paclitaxel + trastuzumab en traitement adjuvant du cancer du sein précoce stade II/IIIA surexprimant HER2 |
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Phase 3 | Terminé | 444 | Lapatinib + paclitaxel vs placebo + paclitaxel dans le cancer du sein métastatique ErbB2 amplifié |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Terminé | 3270 | Chimiothérapie ± trastuzumab (dont paclitaxel hebdomadaire) en adjuvant, cancer du sein HER2-low ganglionnaire positif ou à haut risque |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Terminé | 2005 | Doxorubicine, paclitaxel et cyclophosphamide séquentiels vs concurrents, cancer du sein stade II/IIIA ganglionnaire positif |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Arrêté prématurément | 63 | Paclitaxel + trastuzumab + lapatinib vs placebo, cancer du sein métastatique ErbB2 positif |
| [NCT00455533](https://clinicaltrials.gov/study/NCT00455533) | Phase 2 | Terminé | 384 | Ixabépilone vs paclitaxel après AC en néoadjuvant, biomarqueurs, cancer du sein précoce |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Terminé | 478 | Chimiothérapie dose-dense séquentielle (docétaxel vs paclitaxel) en adjuvant, ganglions axillaires positifs |
| [NCT02280252](https://clinicaltrials.gov/study/NCT02280252) | Phase 2 | Terminé | 69 | Paclitaxel concomitant à la radiothérapie, réponse/résistance dans le cancer du sein localement avancé |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Terminé | 280 | Séquences FEC-75/paclitaxel+trastuzumab (ordre inversé), cancer du sein opérable HER2 positif |
| [NCT00054028](https://clinicaltrials.gov/study/NCT00054028) | Phase 1/2 | Terminé | 31 | Suramine + paclitaxel dans le cancer du sein métastatique avancé stade IIIB/IV |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Revue | Biomolecules | Synthèse des mécanismes et effets cliniques de paclitaxel dans le cancer du sein, y compris la résistance thérapeutique |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revue | Drug and Therapeutics Bulletin | Historique de l'AMM de paclitaxel : cancer de l'ovaire métastatique puis carcinome mammaire métastatique |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohorte | Cancer | Efficacité de doxorubicine + paclitaxel dans le carcinome mammaire avancé, importance de l'anthracycline adjuvante préalable |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Cohorte | BioMed Research International | Chimiothérapie néoadjuvante épirubicine/cyclophosphamide + paclitaxel hebdomadaire + trastuzumab, étude en vie réelle HER2+ |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | pending | Chemical Biology & Drug Design | Potentiel thérapeutique des combinaisons à base de paclitaxel contre le carcinome mammaire, biomarqueurs in vivo |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | pending | Nature Communications | Variations de TEKT4 associées à la résistance du cancer du sein à paclitaxel |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Préclinique | Journal for ImmunoTherapy of Cancer | Rôle de paclitaxel sur les macrophages associés à la tumeur, renforcement du blocage PD-1 dans le TNBC |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | Préclinique | Molecular Pharmacology | Réversion de la résistance médiée par la stathmine à paclitaxel et vinblastine dans les cellules de carcinome mammaire |
| [14508823](https://pubmed.ncbi.nlm.nih.gov/14508823/) | 2003 | pending | Cancer | Trastuzumab + paclitaxel : inhibition plus efficace de l'angiogenèse médiée par ErbB-2 via Akt |
| [15305399](https://pubmed.ncbi.nlm.nih.gov/15305399/) | 2004 | pending | Cancer | Essai randomisé GONO : administration concomitante vs séquentielle d'épirubicine et paclitaxel en première ligne du carcinome mammaire métastatique |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (classe des taxanes — inhibiteur de la dépolymérisation des microtubules) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques applicables aux agents antinéoplasiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le niveau de preuve L1 repose sur de multiples essais de phase 3 complétés et une littérature abondante, mais cette indication (cancer du sein) constitue une reconfirmation d'un usage oncologique déjà établi plutôt qu'un repositionnement nouveau — la robustesse scientifique est donc élevée, mais l'intérêt en tant que « découverte » de repositionnement est limité.
- Une lacune de données bloquante (仿單警語/禁忌 TFDA) empêche à ce stade toute évaluation de sécurité initiale (S1), ce qui justifie la retenue de garde-fous malgré le bon niveau de preuve d'efficacité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice/仿單 TFDA (avertissements, contre-indications) — bloquant pour l'évaluation de sécurité
- Données de mécanisme d'action structurées (DrugBank) au niveau du médicament
- Vérification du statut réglementaire réel en France/Taïwan (le statut « non commercialisé » avec 0 AMM doit être confirmé, car il est incohérent avec un usage clinique aussi documenté du paclitaxel)
- Profil détaillé de toxicité (myélosuppression, émétogénicité) pour compléter la section Cytotoxicité
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

