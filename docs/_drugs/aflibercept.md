---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 1
---

# Aflibercept
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

# AFLIBERCEPT : Rapport d'Évaluation Préliminaire — Données Insuffisantes

## Résumé en Une Phrase

Aflibercept (DB08885) est une protéine de fusion recombinante agissant comme piège à VEGF (Vascular Endothelial Growth Factor), utilisée en pratique clinique internationale sous les noms commerciaux Eylea® (ophtalmologie) et Zaltrap® (oncologie). **Aucune prédiction TxGNN n'est actuellement disponible** pour ce médicament, et le pack de données ne contient ni indication originale renseignée, ni données réglementaires françaises exploitables. Ce rapport constitue donc une évaluation préliminaire nécessitant des données complémentaires avant de pouvoir progresser.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le pack de données¹ |
| Nouvelle Indication Prédite | Aucune prédiction TxGNN disponible |
| Score de Prédiction TxGNN | — |
| Niveau de Preuve | L5 (Prédiction du modèle uniquement, aucune donnée exploitable) |
| Statut de Marché en France | ✗ Non commercialisé (données TFDA : 未上市) |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

> ¹ En pratique clinique internationale, l'aflibercept est approuvé pour la dégénérescence maculaire liée à l'âge (DMLA) humide, l'œdème maculaire diabétique, l'occlusion veineuse rétinienne, et le cancer colorectal métastatique (en association avec FOLFIRI).

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, **aucune prédiction TxGNN n'a été générée** pour l'aflibercept. Il n'est donc pas possible d'évaluer la pertinence d'une nouvelle indication à ce stade.

Pour contexte, l'aflibercept est une protéine de fusion recombinante composée de fragments des récepteurs VEGFR-1 et VEGFR-2 fusionnés au fragment Fc de l'IgG1 humaine. Ce « piège à VEGF » se lie avec une haute affinité au VEGF-A, au VEGF-B et au facteur de croissance placentaire (PlGF), bloquant ainsi l'angiogenèse pathologique. Ce mécanisme anti-angiogénique est à la base de ses applications tant en ophtalmologie (inhibition de la néovascularisation choroïdienne) qu'en oncologie (inhibition de l'angiogenèse tumorale).

Toutefois, les données de mécanisme d'action (MOA) ne figurent pas dans le pack de données fourni, ce qui limite la capacité d'analyse mécanistique formelle. L'exécution du modèle TxGNN avec les données de graphe de connaissances appropriées est un prérequis indispensable pour toute évaluation de repositionnement.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

> *En l'absence de prédiction TxGNN pour une nouvelle indication, aucune recherche ciblée d'essais cliniques n'a été effectuée.*

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

> *En l'absence de prédiction TxGNN pour une nouvelle indication, aucune recherche ciblée de littérature n'a été effectuée.*

---

## Informations de Marché en France

| Élément | Statut |
|------|------|
| Statut réglementaire | Non commercialisé (0 AMM enregistrée) |
| Recherche TFDA | Effectuée le 2026-03-29, aucun résultat |

> *Aucune autorisation de mise sur le marché n'a été identifiée dans la base de données interrogée. À noter qu'à l'international, l'aflibercept est commercialisé sous les noms Eylea® (Bayer/Regeneron) et Zaltrap® (Sanofi/Regeneron).*

---

## Cytotoxicité

L'aflibercept possède une indication oncologique reconnue à l'international (cancer colorectal métastatique, sous le nom Zaltrap®). Bien qu'il ne soit pas un agent cytotoxique conventionnel, il est classé comme agent antinéoplasique en raison de son mécanisme anti-angiogénique.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anti-angiogénique — piège à VEGF) |
| Risque de Myélosuppression | Modéré (neutropénie rapportée en association avec FOLFIRI ; veuillez consulter la notice) |
| Classification d'Émétogénicité | Faible (en monothérapie) ; variable en association avec chimiothérapie |
| Éléments de Surveillance | NFS avec différentielle, protéinurie, tension artérielle, fonction hépatique et rénale, surveillance de la cicatrisation |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments biologiques/antinéoplasiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> *Les données de mises en garde, contre-indications et interactions médicamenteuses n'étaient pas disponibles dans le pack de données fourni. Pour l'aflibercept, les risques connus au niveau international incluent : perforations gastro-intestinales, hémorragies, hypertension artérielle, protéinurie, syndrome de leucoencéphalopathie postérieure réversible (SLPR), et événements thromboemboliques artériels. Une consultation des documents réglementaires officiels est indispensable.*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le pack de données actuel présente des lacunes critiques : aucune prédiction TxGNN n'est disponible, le mécanisme d'action n'est pas renseigné, le médicament n'est pas commercialisé sur le marché cible, et les données de sécurité sont absentes. Il est impossible de procéder à une évaluation de repositionnement dans ces conditions.

**Pour avancer, les éléments suivants sont nécessaires :**
- **[Priorité Haute]** Exécution du modèle TxGNN pour générer des prédictions d'indications candidates
- **[Priorité Haute]** Résolution du Data Gap DG002 : Récupération des données de mécanisme d'action (MOA) via l'API DrugBank
- **[Priorité Haute]** Résolution du Data Gap DG001 : Récupération des mises en garde et contre-indications depuis les notices officielles (TFDA/ANSM)
- **[Souhaitable]** Vérification du statut réglementaire auprès de l'ANSM (France) et/ou de l'EMA, étant donné que l'aflibercept est approuvé en Europe sous les noms Eylea® et Zaltrap®
- **[Souhaitable]** Enrichissement des données de sécurité (DDI, pharmacovigilance) via DrugBank et les bases de données réglementaires

---

*⚠️ Ce rapport est généré à des fins de recherche uniquement et ne constitue pas un avis médical. Toute candidature de repositionnement doit faire l'objet d'une validation clinique rigoureuse avant application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

