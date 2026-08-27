---
layout: default
title: Rilpivirine
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 5
---

# Rilpivirine
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

# Rilpivirine : De l'Infection par le VIH-1 a l'Infection par le Virus de l'Immunodeficience Simienne (VIS)

## Resume en Une Phrase

Rilpivirine (DB08864) est un inhibiteur non nucleosidique de la transcriptase inverse (INNTI) utilise comme piece centrale des traitements antiretroviraux contre le VIH-1 chez l'humain.
Le modele TxGNN predit en tete de liste une activite contre l'**infection par le virus de l'immunodeficience simienne (VIS)** — un lentivirus apparente au VIH-1 utilise comme modele animal de recherche —
avec **0 essai clinique** et **4 publications**, toutes precliniques ou de revue, soutenant cette direction.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Infection par le VIH-1 (traitement antiretroviral) — deduite des donnees d'essais cliniques du dossier ; pas de source AMM France (medicament non commercialise) |
| Nouvelle Indication Predite | Infection par le virus de l'immunodeficience simienne (VIS) |
| Score de Prediction TxGNN | 99.97% |
| Niveau de Preuve | L3 |
| Statut de Marche en France | ✗ Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans ce dossier (DG002). Sur la base des informations presentes dans les essais cliniques recenses, rilpivirine (TMC278) appartient a la classe des inhibiteurs non nucleosidiques de la transcriptase inverse (INNTI), utilisee comme composant central des traitements antiretroviraux contre le VIH-1 chez l'humain, seule ou en association fixe avec cabotegravir ou dolutegravir (cf. essais NCT02938520, NCT02429791). Son efficacite dans le VIH-1 est bien etablie par de multiples essais de Phase 3.

Le virus de l'immunodeficience simienne (VIS/SIV) est un lentivirus proche du VIH-1, utilise comme modele animal standard pour la recherche translationnelle sur le VIH chez le macaque. Rilpivirine, du fait de son activite sur la transcriptase inverse virale, montre une activite antivirale documentee contre des souches chimeriques SIV/VIH (RT-SHIV) chez le macaque, notamment dans des etudes de prophylaxie pre- et post-exposition (PrEP/PEP) a action prolongee (formulation "long-acting", souvent en association avec cabotegravir).

Il est cependant essentiel de souligner que le VIS **n'est pas une maladie humaine** mais un modele animal experimental. Les 4 publications disponibles sont toutes des etudes precliniques chez le macaque (a l'exception d'une revue de synthese), et aucun essai clinique n'existe sur cette indication precise. Cette prediction TxGNN reflete donc une proximite mecanistique/virologique entre deux virus apparentes plutot qu'une veritable nouvelle indication therapeutique humaine directement exploitable.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement pour l'indication "simian immunodeficiency virus infection".

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | Revue | Current Opinion in HIV and AIDS | Revue sur le cabotegravir (inhibiteur d'integrase) pour traitement/PrEP du VIH ; rilpivirine mentionnee comme comparateur INNTI de contexte |
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | Preclinique (modele animal) | Antimicrobial Agents and Chemotherapy | Rilpivirine longue action en PrEP chez des macaques infectes par un SIV chimerique portant la RT du VIH-1 : faible frequence de variants resistants selectionnes |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinique (modele animal) | Nature Communications | Traitement precoce + cabotegravir/rilpivirine longue action associe a une remission durable du SHIV chez le macaque |
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | Preclinique (modele animal) | EBioMedicine | Evaluation preclinique de cabotegravir/rilpivirine longue action en prophylaxie post-exposition (PEP) chez le macaque |

---

## Informations de Marche en France

Rilpivirine n'est actuellement pas commercialise en France : 0 AMM enregistree dans ce dossier. Aucune information de licence disponible.

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite. Le dossier signale une lacune bloquante (DG001) : les mises en garde, contre-indications et interactions medicamenteuses TFDA n'ont pas pu etre recuperees, ce qui empeche toute evaluation de securite initiale (S1) pour cette piste.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La piste en tete de classement (infection par le VIS) affiche un niveau de preuve L3, sans aucun essai clinique, uniquement des etudes precliniques chez le macaque sur un virus qui n'affecte pas l'humain — elle n'est donc pas directement actionnable en developpement clinique.
- L'absence totale de donnees de securite TFDA (DG001, bloquant) et de MOA detaille (DG002) rend toute progression premature.
- A titre de comparaison, dans le meme dossier, deux autres pistes affichent un niveau de preuve nettement superieur : "AIDS related complex" (rang 4) et "infection VIH congenitale" (rang 5), toutes deux L1 avec plusieurs essais de Phase 3 completes et une recommandation "Proceed with Guardrails" — ce sont des pistes bien plus matures si l'objectif est un reel repositionnement chez l'humain.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer la notice TFDA (mises en garde, contre-indications) — DG001, bloquant pour l'etape S1
- Recuperer le mecanisme d'action detaille via l'API DrugBank — DG002
- Si la piste VIS est maintenue, clarifier qu'il s'agit de recherche translationnelle sur le VIH et non d'un usage clinique pour une maladie animale, avant toute decision reglementaire
- Envisager une evaluation dediee des pistes rang 4 et rang 5 (niveau de preuve L1, essais de Phase 3 completes), plus prometteuses pour un repositionnement humain
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

