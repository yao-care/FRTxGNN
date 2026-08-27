---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab : De l'Asthme Allergique Severe a la Bronchite

## Resume en Une Phrase

Omalizumab est un anticorps monoclonal anti-IgE, historiquement associe au traitement de l'asthme allergique severe (les donnees precises d'indication d'origine et de MOA ne sont pas disponibles dans ce dossier — voir Data Gaps DG001/DG002 ci-dessous).
Le modele TxGNN predit qu'il pourrait etre efficace pour la **Bronchite**,
avec **2 essais cliniques** et **8 publications** identifies, mais ces preuves restent **indirectes** : les populations etudiees sont majoritairement asthmatiques, pas specifiquement des patients bronchitiques.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non disponible dans ce dossier (donnee TFDA specifique manquante — voir DG001) |
| Nouvelle Indication Predite | Bronchite |
| Score de Prediction TxGNN | 99.9992% |
| Niveau de Preuve | L4 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action (MOA) et sur les indications d'origine ne sont pas disponibles dans ce dossier de preuves (Data Gaps DG001 — mises en garde/contre-indications TFDA — et DG002 — MOA DrugBank, toutes deux non resolues). Sur la base des informations generalement connues sur cette molecule, l'omalizumab est un anticorps monoclonal humanise dirige contre l'IgE, dont l'usage historique concerne l'asthme allergique severe persistant ; son efficacite dans cette indication a ete largement demontree, et mecanistiquement cela pourrait s'appliquer a d'autres pathologies inflammatoires des voies aeriennes.

Cliniquement, la « bronchite asthmatique » (notamment la bronchite eosinophilique) et l'asthme allergique partagent une inflammation des voies aeriennes mediee par les eosinophiles et l'IgE. Sur le plan theorique, un traitement anti-IgE pourrait donc beneficier a ce sous-type. Cependant, les essais cliniques fournis (NCT02477332, NCT02049294) portent en realite sur des populations d'asthmatiques et non sur la bronchite en tant qu'entite propre — il s'agit d'un lien indirect entre termes ontologiquement proches, et non d'une preuve directe. C'est ce qui explique le niveau de preuve L4 (preclinique/mecanistique) et le stade de decision precoce S1.

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Termine | 382 | Etude de determination de dose phase 2b (QGE031) en add-on chez l'urticaire chronique spontanee ; mecanisme lie mais population hors bronchite/asthme direct — preuve indirecte (grade B). |
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Termine | 11 | Effet d'epargne cortisonique de l'omalizumab chez patients avec asthme et bronchite eosinophilique persistante ; echantillon tres limite (n=11) — preuve faible (grade C). |

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Revue | Clin Rev Allergy Immunol | Approbation et experience post-approbation de l'omalizumab dans l'asthme (revue generale, non specifique a la bronchite). |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revue | Expert Opin Pharmacother | Defis de prise en charge de l'asthme associe aux maladies des voies respiratoires liees au tabagisme, incluant la bronchite chronique. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohorte | Postepy Dermatol Alergol | Omalizumab chez patients d'age moyen/ages avec chevauchement asthme allergique severe-BPCO. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Rapport de cas | J Investig Allergol Clin Immunol | Cas rare de bronchite plastique apres thermoplastie bronchique (evenement associe, pas efficacite therapeutique). |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Revue | Masui | Prise en charge preoperatoire des patients avec asthme bronchique ou bronchite chronique. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Non classifie | Curr Med Res Opin | Securite et tolerance de l'omalizumab chez les enfants avec asthme allergique. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Non classifie | Allergol Immunopathol | Anticorps monoclonaux en pediatrie : utilisation en prevention et traitement (revue generale). |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Non classifie | Rev Mal Respir | Exacerbations de l'asthme de l'adulte en questions. |

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

*(Note : la mise en garde TFDA — DG001, severite Blocking — et le MOA DrugBank — DG002 — ne sont pas encore disponibles dans ce dossier, ce qui empeche actuellement toute evaluation de securite de niveau S1.)*

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- L'evaluation de securite S1 est bloquee par l'absence des mises en garde/contre-indications TFDA (DG001, severite Blocking).
- Le niveau de preuve pour la Bronchite reste L4 (mecanistique/preclinique) : les essais et la litterature disponibles portent majoritairement sur l'asthme, pas sur la bronchite en tant qu'entite distincte.
- Le statut de recommandation source associe a cette indication est explicitement « Research Question », coherent avec un stade de decision precoce (S1).

**Pour avancer, les elements suivants sont necessaires :**
- Obtenir la notice/les mises en garde TFDA (DG001) pour lever le blocage de l'evaluation de securite.
- Obtenir les donnees detaillees de mecanisme d'action via DrugBank (DG002).
- Identifier des essais cliniques cibles specifiquement sur la bronchite (et non uniquement sur l'asthme) afin de renforcer le lien mecanistique.
- A titre indicatif : l'indication predite « obstructive lung disease » (rang 3 dans ce meme dossier) presente un niveau de preuve nettement superieur (L1, stade S3, recommandation « Proceed with Guardrails ») et pourrait constituer une piste prioritaire alternative a documenter separement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

