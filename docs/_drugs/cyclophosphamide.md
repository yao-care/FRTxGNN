---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
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

# Cyclophosphamide : De l'Agent Alkylant Antinéoplasique à la Leucémie Myéloïde

## Résumé en Une Phrase

Cyclophosphamide est un agent alkylant de la famille des oxazaphosphorines, utilisé en oncologie hématologique comme composant de conditionnement pré-greffe et d'immunomodulation post-transplantation, sans indication formellement enregistrée en France dans le présent système de données.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Leucémie Myéloïde**, avec **50 essais cliniques** identifiés et **20 publications** soutenant actuellement cette direction.
Le score de prédiction de **99,47%** et la présence d'un essai de Phase 3 complété (BuCy2 vs BuFlu dans la LAM, n=252) confirment la solidité de cette association déjà largement documentée en pratique clinique.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non renseignée (aucune AMM enregistrée en France) |
| Nouvelle Indication Prédite | Leucémie myéloïde |
| Score de Prédiction TxGNN | 99,47% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Cyclophosphamide est un agent alkylant de la famille des oxazaphosphorines dont le mécanisme repose sur une activation hépatique par les cytochromes P450 (principalement CYP2B6), générant le métabolite actif phosphoramide moutarde. Ce dernier forme des pontages inter-brins et intra-brins dans l'ADN, bloquant irréversiblement la réplication cellulaire et induisant l'apoptose. Cette cytotoxicité est particulièrement efficace sur les cellules à forte activité proliférative, caractéristique centrale des blastes myéloïdes dans la leucémie myéloïde aiguë (LAM).

La leucémie myéloïde aiguë est définie par une accumulation clonale de progéniteurs myéloïdes bloqués dans leur différenciation. Cyclophosphamide intervient à deux niveaux thérapeutiques majeurs dans cette pathologie : (1) le conditionnement myéloablatif pré-greffe, notamment le schéma BuCy (busulfan + cyclophosphamide), qui éradique la moelle pathologique et prévient le rejet du greffon avant une greffe allogénique de cellules souches hématopoïétiques (allo-GCSH) ; (2) le cyclophosphamide post-transplantation (PTCy, typiquement 50 mg/kg aux jours +3 et +4), qui a transformé la prophylaxie de la maladie du greffon contre l'hôte (GVHD) en éliminant sélectivement les lymphocytes T alloreactifs tout en préservant les cellules T régulatrices et la réponse greffon-contre-leucémie (GVL).

La prédiction TxGNN s'appuie ainsi sur une base mécanistique et clinique robuste. Au-delà de sa cytotoxicité directe sur les cellules LAM, cyclophosphamide joue un rôle immunomodulateur irremplaçable dans le cadre des greffes allogéniques, qui demeurent le traitement potentiellement curatif pour les LAM à risque intermédiaire et défavorable. Les données de l'essai Phase 3 NCT01191957 (n=252) et de plusieurs grandes cohortes prospectives récentes confirment la centralité de cyclophosphamide dans la prise en charge moderne de la leucémie myéloïde.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT01191957](https://clinicaltrials.gov/study/NCT01191957) | Phase 3 | Terminé | 252 | Étude randomisée multicentrique comparant BuCy2 vs BuFlu comme conditionnement pour allo-GCSH chez patients ≥40 ans avec LAM en RC ; évaluation de la mortalité liée au traitement à 1 an et de l'efficacité anti-leucémique |
| [NCT00002945](https://clinicaltrials.gov/study/NCT00002945) | Phase 3 | Terminé | 61 | Cytarabine haute dose + idarubicine (induction) → étoposide haute dose + cyclophosphamide (intensification) + ASCT + immunomodulation IL-2 pour leucémie myéloïde adulte de novo et secondaire |
| [NCT00852709](https://clinicaltrials.gov/study/NCT00852709) | Phase 1 | Terminé | 35 | Dose-escalation de clofarabine suivie de cyclophosphamide fractionné chez enfants avec leucémies aiguës rechutées/réfractaires ; détermination de la dose maximale tolérée (MTD) et profil de toxicité |
| [NCT00005892](https://clinicaltrials.gov/study/NCT00005892) | N/A | Terminé | N/A | Cyclophosphamide modéré + radiothérapie + greffe allogénique de moelle osseuse pour syndrome myélodysplasique et leucémie aiguë liés à l'anémie de Fanconi ; amélioration de la survie et réduction de la morbidité |
| [NCT07108530](https://clinicaltrials.gov/study/NCT07108530) | Phase 2 | En recrutement | 50 | Protocole intégré multicentrique induction-consolidation-transplantation pour LAM adulte (hors M3) ; évaluation de l'efficacité et de la sécurité des schémas IAV et DAV avec inclusion de cyclophosphamide dans le conditionnement |
| [NCT00002592](https://clinicaltrials.gov/study/NCT00002592) | Phase 2 | Terminé | 40 | Autogreffe de moelle osseuse traitée ex vivo avec oligodésoxyribonucléotide antisens C-MYB (LR-3001) dans la leucémie myéloïde chronique ; cyclophosphamide comme composant du conditionnement |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminé | 16 | Transplantation de sang de cordon ombilical pour patients avec leucémie myéloïde hors RC ; régime myéloablatif cyclophosphamide/fludarabine/irradiation corporelle totale + cellules NK donneurs |
| [NCT00003868](https://clinicaltrials.gov/study/NCT00003868) | Phase 2 | Terminé | 40 | Anticorps BC8 radiomarqué (anti-CD45) + cyclophosphamide + irradiation corporelle totale suivi de greffe de cellules souches HLA-appariées pour LAM avancée et SMD |
| [NCT04835519](https://clinicaltrials.gov/study/NCT04835519) | Phase 1/2 | Terminé | 5 | Évaluation de la sécurité et tolérance de cellules CAR-T anti-CD33 fonctionnellement améliorées dans la LAM rechutée/réfractaire ; cyclophosphamide 250 mg/m² comme agent lymphodéplétant pré-infusion |
| [NCT03602898](https://clinicaltrials.gov/study/NCT03602898) | Phase 2 | Retiré | 0 | Comparaison randomisée ATG vs PTCy vs calcineurine-méthotrexate comme prophylaxie GVHD après GCSH myéloablative de donneur non apparenté dans les leucémies myéloïdes (retiré avant recrutement, mais conception de référence) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohorte/Registre | *Haematologica* | 217 patients LAM en RC recevant HCT myéloablatif + prophylaxie PTCy ; survie globale à 2 ans de 77% (IC 71–83%) ; la classification génétique de risque conserve sa valeur pronostique dans ce contexte |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Cohorte/Registre | *Bone Marrow Transplantation* | 1 823 patients LAM (risque intermédiaire/défavorable) en RC1 recevant PTCy ; l'intensité de conditionnement module les résultats selon le risque cytogénétique/moléculaire ; données EBMT |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Cohorte Comparative | *Eur J Haematology* | MAC vs RIC chez patients LAM <65 ans recevant ATG + PTCy + ciclosporine ; le conditionnement myéloablatif est associé à un meilleur contrôle de la maladie malgré une mortalité non liée à la rechute plus élevée |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Étude Comparative | *Future Oncology* | BuCy vs FluBu pour allo-GCSH dans la LAM ; BuCy reste le standard myéloablatif de référence ; FluBu offre une toxicité réduite avec une efficacité comparable en termes de contrôle leucémique |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Essai Clinique/Phase 2 | *Transplant Immunology* | Cladribine + BuCy comme conditionnement intensif pour allo-GCSH dans la LAM rechutée/réfractaire ; efficacité et sécurité du schéma CladBuCy évaluées |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohorte Rétrospective | *Cytotherapy* | Facteurs pronostiques de la greffe haploidentique avec PTCy pour LAM ; PTCy efficace pour la suppression de GVHD sévère tout en maintenant l'effet greffon contre leucémie |
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Méta-analyse en réseau | *Bone Marrow Transplantation* | Revue systématique et méta-analyse bayésienne des régimes myéloablatifs dans la LAM adulte en RC ; BuCy évalué parmi les schémas de référence, données comparatives exhaustives |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohorte Prospective | *Int J Mol Sciences* | PTCy après GCSH de donneurs appariés (apparentés et non apparentés) chez enfants avec LAM ; premières données pédiatriques publiées sur cette stratégie de prophylaxie GVHD |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Cohorte | *Leukemia & Lymphoma* | Cyclophosphamide haute dose (HDCy 60 mg/kg) pour cytoréduction dans la LAM avec hyperleucocytose (GB ≥50×10⁹/L) ou leucostase ; 27 patients : RC obtenue chez 78%, mortalité précoce 7% |
| [32428903](https://pubmed.ncbi.nlm.nih.gov/32428903/) | 2021 | Cohorte Prospective | *Acta Haematologica* | PTCy (50 mg/kg j+3 et j+4) + ATG (4,5 mg/kg) comme prophylaxie GVHD pour LAM/SMD à haut risque ; comparaison avec d'autres régimes de prophylaxie standards |

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché (AMM) pour Cyclophosphamide n'est enregistrée en France dans le système de données consulté (source : données réglementaires ANSM, résultat de requête : 0 licence). Le médicament est référencé comme **non commercialisé** selon les informations disponibles.

> **Note** : Cyclophosphamide est un médicament de longue date largement utilisé en pratique clinique internationale. L'absence de résultat dans ce système peut refléter un défaut de couverture de la base de données plutôt qu'une absence réelle de commercialisation. Une vérification directe auprès de l'ANSM est recommandée avant toute décision réglementaire.

---

## Cytotoxicité

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | **Cytotoxique conventionnel** — Oxazaphosphorine (agent alkylant bifonctionnel de l'ADN ; classe B de l'IARC : probablement cancérogène pour l'homme à long terme) |
| Risque de Myélosuppression | **Élevé** — Neutropénie, thrombocytopénie et anémie sont des effets dose-dépendants attendus ; le nadir survient généralement entre J10 et J14. Dans le contexte du conditionnement pré-greffe, la myélosuppression profonde est l'effet pharmacologique recherché |
| Classification d'Éméticité | **Modérée à élevée** — Risque modéré aux doses standards (< 1 500 mg/m²) ; risque élevé aux hautes doses de conditionnement (≥ 1 500 mg/m²) selon les guidelines ASCO/MASCC |
| Éléments de Surveillance | NFS avec formule différentielle (suivi du nadir), créatininémie et DFG (néphrotoxicité possible), transaminases et bilirubine (hépatotoxicité), analyse urinaire et bandelette (hématurie : cystite hémorragique par l'acroléine, métabolite urotoxique), ionogramme sanguin |
| Protection de Manipulation | Application obligatoire des procédures cytotoxiques : préparation sous hotte à flux laminaire vertical (PSM de type II B), EPI complets (gants doublement gantés, surblouse, masque FFP2, lunettes), élimination des déchets selon la filière DASRI cytotoxique ; précaution renforcée lors des soins d'excrétion (urine, selles, vomissements pendant 48–72 h post-administration) |

---

## Considérations de Sécurité

Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans ce dossier d'évaluation.

> Veuillez consulter la notice officielle du médicament pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Cyclophosphamide est un composant cliniquement établi et largement documenté des protocoles de traitement de la leucémie myéloïde aiguë, avec un essai de Phase 3 complété (BuCy2 vs BuFlu, n=252) et plus de 20 publications récentes de registres et cohortes de grande taille confirmant son efficacité dans les schémas de conditionnement (BuCy) et de prophylaxie GVHD (PTCy) ; le score TxGNN de 99,47% et le niveau de preuve L2 reflètent cette base de données cliniques solide.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données officielles de mécanisme d'action (MOA) depuis DrugBank — priorité haute (DG002)
- Télécharger et analyser la notice (PDF ANSM) pour les mises en garde, contre-indications et précautions d'emploi officielles — priorité bloquante pour l'évaluation de sécurité complète (DG001)
- Vérifier le statut réglementaire réel en France directement auprès de l'ANSM (l'absence d'AMM dans ce système peut être un artefact de la base de données)
- Définir les populations cibles spécifiques non couvertes par les études existantes (ex. : LAM pédiatrique avec PTCy en greffe appariée, LAM avec mutations IDH1/2 en conditionnement haploidentique) pour orienter une éventuelle étude de repositionnement formelle
- Établir un protocole de surveillance de sécurité adapté aux populations à risque (pédiatrie, patients âgés ≥65 ans, insuffisance rénale/hépatique préexistante) en tenant compte des risques de cystite hémorragique et de myélosuppression prolongée
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

