---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mogamulizumab : Du Lymphome T Cutané au Carcinome Urothélial de l'Urètre Prostatique

## Resume en Une Phrase

Mogamulizumab est un anticorps monoclonal anti-CCR4 defucosyle, dont l'indication approuvee de reference est le lymphome T cutane (mycosis fongoide / syndrome de Sezary).
Le modele TxGNN predit qu'il pourrait etre efficace pour le **Carcinome Urothelial de l'Urethre Prostatique**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prediction de similarite relationnelle du graphe de connaissances, non validee cliniquement.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Lymphome T cutane (CTCL) — mycosis fongoide / syndrome de Sezary |
| Nouvelle Indication Predite | Carcinome Urothelial de l'Urethre Prostatique |
| Score de Prediction TxGNN | 99.44% |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Le champ structure de mecanisme d'action (MOA) est marque comme donnee manquante dans la base source. Toutefois, les elements disponibles indiquent que Mogamulizumab est un anticorps monoclonal anti-CCR4 defucosyle, dont le mecanisme repose sur la cytotoxicite cellulaire dependante des anticorps (ADCC) pour eliminer les cellules T regulatrices (Treg) exprimant CCR4.

L'hypothese de repositionnement suggere que la depletion des Treg CCR4+ pourrait lever l'immunosuppression du microenvironnement tumoral et ainsi produire un effet d'activation immunitaire auxiliaire sur diverses tumeurs solides, y compris le carcinome urothelial. Il s'agit cependant d'une extrapolation pharmacologique theorique : aucune donnee ne confirme l'expression de CCR4 dans le carcinome urothelial de l'urethre prostatique, et le score TxGNN eleve reflete uniquement une similarite relationnelle au sein du graphe de connaissances, pas une preuve clinique ou preclinique directe.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement

---

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Immunotherapie (anticorps monoclonal anti-CCR4, mecanisme ADCC — non cytotoxique conventionnel) |
| Risque de Myelosuppression | Veuillez consulter les mises en garde et precautions de la notice |
| Classification d'Emetogenicite | Veuillez consulter les mises en garde et precautions de la notice |
| Elements de Surveillance | Parametres hematologiques generaux (NFS), fonction hepatique et renale — a confirmer selon la notice officielle |
| Protection de Manipulation | Non applicable a priori (anticorps monoclonal, non classe cytotoxique conventionnel) ; a confirmer selon la reglementation locale |

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Le niveau de preuve est L5 (prediction du modele uniquement, aucun essai ni publication), le medicament n'est pas commercialise en France, et les donnees de MOA et de securite sont incompletes — les criteres minimaux pour une evaluation de securite (S1) ne sont pas remplis.

**Pour avancer, les elements suivants sont necessaires :**
- Donnees de mecanisme d'action (MOA) structurees et verifiees (DrugBank ou equivalent)
- Mises en garde, contre-indications et interactions medicamenteuses (notice officielle)
- Preuves precliniques ou cliniques specifiques sur l'expression de CCR4 dans le carcinome urothelial
- Statut reglementaire et disponibilite en France ou en Europe
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

