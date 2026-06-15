---
layout: default
title: Aminophylline
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Aminophylline
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

# Aminophylline : Du Bronchospasme à la Migraine

## Résumé en Une Phrase

Aminophylline est un bronchodilateur de la classe des méthylxanthines, classiquement utilisé dans le traitement du bronchospasme (asthme, BPCO) et de l'apnée de la prématurité.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble migraineux** (migraine disorder),
avec **0 essai clinique enregistré** et **6 publications scientifiques** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---------|---------|
| Indication Originale | Bronchospasme / Apnée de la prématurité |
| Nouvelle Indication Prédite | Trouble migraineux (Migraine disorder) |
| Score de Prédiction TxGNN | 99.88% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Aminophylline est un antagoniste des récepteurs à l'adénosine (principalement A1 et A2A) et un inhibiteur non sélectif de la phosphodiestérase (PDE). Les données actuelles sur son mécanisme d'action détaillé restent partielles dans cet Evidence Pack, mais son appartenance à la classe des méthylxanthines — partagée avec la caféine et la théophylline — est bien documentée dans la littérature biomédicale.

L'adénosine est reconnue comme un facteur déclenchant de la migraine : son infusion exogène peut reproduire des crises migraineuses chez des sujets prédisposés. L'activation des récepteurs A2A entraîne une vasodilatation sélective des artères piales intracrâniennes et une sensibilisation des fibres trigéminales — deux mécanismes centraux dans la physiopathologie migraineuse. En bloquant ces récepteurs, aminophylline pourrait théoriquement interrompre cette cascade pathologique.

Des observations cliniques directes (Phillips & Phillips, 2023 — PMID 38059379) rapportent un effet thérapeutique marqué d'aminophylline dans les douleurs sévères, notamment les céphalées post-ponction durale, une entité mécanistiquement proche de la migraine. Le cas d'une migraine hémiplégique déclenchée par le régadénoson (agoniste A2A sélectif) et documenté dans le contexte d'une imagerie de perfusion myocardique (PMID 34308528) illustre également de façon concrète cette voie adénosinergique. Les preuves restent cependant limitées à des rapports de cas et des revues narratives ; aucun essai contrôlé n'a été conduit à ce jour.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|----------------------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Revue / Série de cas | Pain Management | Aminophylline, en tant qu'antagoniste des récepteurs à l'adénosine, offrirait un soulagement thérapeutique significatif dans la douleur et les céphalées post-ponction durale ; lien avec la perturbation du métabolisme énergétique cérébral et un excès d'adénosine dans la migraine |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Rapport de cas | Journal of Nuclear Cardiology | Migraine hémiplégique déclenchée par le régadénoson (agoniste A2A sélectif) lors d'une imagerie de stress myocardique ; aminophylline employée pour contrer les effets neurologiques indésirables, illustrant directement la voie adénosinergique dans la migraine |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | Mécanistique in vitro | Stroke | Les composés adéniniques (adénosine, AMP, ADP, ATP) dilatent sélectivement les artères piales intracrâniennes félines et humaines in vitro, sans effet sur les artères extracrâniennes ; soutient le rôle de l'adénosine dans la vasodilatation intracrânienne liée à la migraine |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Rapport de cas | The Canadian Journal of Cardiology | Patiente présentant une douleur thoracique invalidante liée à un excès d'effet adénosinergique (syndrome X myocardique) avec test au dipyridamole positif ; illustre l'étendue des manifestations cliniques d'un excès d'adénosine |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Note clinique | Aggiornamenti clinicoterapeutici | Note clinique historique sur le traitement médical des céphalées, sans abstract disponible |
| [5540199](https://pubmed.ncbi.nlm.nih.gov/5540199/) | 1971 | Note de formulation | The Practitioner | Note sur les formes pharmaceutiques suppositoires, pertinence directe limitée |

---

## Informations de Marché en France

Aminophylline ne dispose d'aucune Autorisation de Mise sur le Marché (AMM) enregistrée en France dans la base de données consultée (0 licence, statut : non commercialisé).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve actuel (L4) repose exclusivement sur des études mécanistiques in vitro, des rapports de cas isolés et une revue narrative. En l'absence de tout essai clinique contrôlé et compte tenu de l'absence d'AMM en France, un avancement clinique immédiat ne peut être recommandé, malgré un rationnel mécanistique cohérent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes sur le mécanisme d'action (MOA) via DrugBank API (DG002 — priorité haute)
- Données de sécurité, mises en garde et contre-indications via la notice officielle ANSM/TFDA (DG001 — priorité bloquante)
- Revue systématique formelle des observations cliniques disponibles sur aminophylline dans les céphalées et la migraine
- Conception d'un essai clinique pilote de Phase 2 randomisé contre placebo dans la migraine épisodique, avec sélection de la voie d'administration (IV pour crise aiguë vs oral en prophylaxie)
- Évaluation du profil risque/bénéfice face aux triptans et aux gepants, traitements de référence actuels de la migraine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

