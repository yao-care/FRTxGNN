---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant : Du Cancer du Sein Hormonodépendant à la Néoplasie Endocrinienne Multiple

## Résumé en Une Phrase

Fulvestrant (Faslodex®) est un SERD (dégradeur sélectif des récepteurs aux estrogènes), approuvé internationalement pour le traitement du cancer du sein localement avancé ou métastatique à récepteurs hormonaux positifs chez les femmes ménopausées, bien que non commercialisé à Taiwan.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Néoplasie Endocrinienne Multiple (MEN)** comme piste la plus explorable parmi 10 nouvelles indications prédites, avec un score de **99,85%**.
Sur l'ensemble des 10 indications analysées, aucune ne dispose de preuves cliniques directes ; la MEN représente la seule hypothèse de recherche biologiquement plausible, soutenue indirectement par **50 essais cliniques** dans le cancer du sein ER+ (indication approuvée) mais par **aucun essai ni publication** spécifique à la MEN.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du sein localement avancé ou métastatique, RH+/HER2− (approuvé FDA/EMA ; non approuvé TFDA Taiwan) |
| Nouvelle Indication Prédite | Néoplasie Endocrinienne Multiple (MEN) |
| Score de Prédiction TxGNN | 99,85% |
| Niveau de Preuve | L4 (indirect — essais cancer du sein uniquement, aucun essai MEN-spécifique) |
| Statut de Marché à Taiwan | ✗ Non commercialisé (0 AMM TFDA) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de Fulvestrant ne sont pas disponibles dans ce dossier. Sur la base des informations connues, Fulvestrant fait partie de la classe des SERD (Selective Estrogen Receptor Degrader) : il se lie aux récepteurs aux estrogènes (ER) avec une très haute affinité, bloque leur activité transcriptionnelle et entraîne leur dégradation totale par le protéasome. Contrairement au tamoxifène (SERM), Fulvestrant n'exerce aucun effet agoniste partiel, ce qui en fait un antagoniste pur particulièrement utile dans les cancers ayant développé une résistance aux thérapies endocrines de première ligne.

La Néoplasie Endocrinienne Multiple de type 1 (MEN1) est un syndrome héréditaire impliquant les glandes parathyroïdes, l'hypophyse antérieure et le pancréas endocrine. Des rapports isolés dans la littérature scientifique signalent une expression des récepteurs aux estrogènes (ER-α et ER-β) dans certains adénomes hypophysaires à prolactine et dans des tumeurs pancréatiques neuroendocrines (pNETs) associées à MEN1. Ce contexte constitue la base théorique permettant d'envisager qu'un SERD comme Fulvestrant pourrait exercer un effet antiprolifératif sur ces tumeurs exprimant les ER.

Cependant, l'analyse approfondie des 50 essais cliniques identifiés révèle qu'ils concernent **tous exclusivement le cancer du sein ER+** — l'indication approuvée de Fulvestrant — sans aucun essai ciblant spécifiquement la MEN. Aucune publication PubMed ne soutient directement cette indication. Le score TxGNN très élevé (0,9985) est vraisemblablement dû à la proximité topologique des nœuds « médicaments endocriniens ↔ tumeurs endocrines » dans le graphe de connaissances, et non à une association thérapeutique démontrée. Cette prédiction est classée **hypothèse de recherche**, à valider par des données d'expression ER dans les tissus tumoraux MEN1.

---

## Preuves d'Essais Cliniques

> ⚠️ **Note importante** : Les essais ci-dessous concernent tous le cancer du sein ER+ (indication approuvée de Fulvestrant) et **non** la Néoplasie Endocrinienne Multiple. Ils illustrent le profil clinique établi de Fulvestrant, mais ne constituent pas une preuve directe pour la MEN.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02422615](https://clinicaltrials.gov/study/NCT02422615) | Phase 3 | Terminé | 726 | Ribociclib + Fulvestrant vs placebo dans le cancer du sein avancé HR+/HER2− (MONALEESA-3) |
| [NCT01942135](https://clinicaltrials.gov/study/NCT01942135) | Phase 3 | Terminé | 521 | Palbociclib + Fulvestrant vs Fulvestrant seul dans le cancer du sein métastatique HR+/HER2− (PALOMA-3) |
| [NCT02437318](https://clinicaltrials.gov/study/NCT02437318) | Phase 3 | Terminé | 572 | Alpelisib + Fulvestrant dans le cancer du sein avancé HR+/HER2− avec mutation PIK3CA (SOLAR-1) |
| [NCT06635447](https://clinicaltrials.gov/study/NCT06635447) | Phase 3 | Actif (non recrutant) | 258 | Capivasertib + Fulvestrant dans le cancer du sein avancé HR+/HER2− — cohorte chinoise |
| [NCT04158362](https://clinicaltrials.gov/study/NCT04158362) | Phase 3 | Actif (non recrutant) | 180 | Abemaciclib + thérapie endocrinienne vs chimiothérapie dans le cancer du sein ER+/HER2− avec métastases viscérales (AMBRE) |
| [NCT04059484](https://clinicaltrials.gov/study/NCT04059484) | Phase 2 | Terminé | 367 | Amcenestrant vs monothérapie endocrinienne (dont Fulvestrant) dans le cancer du sein avancé ER+/HER2− (AMEERA-3) |
| [NCT01797120](https://clinicaltrials.gov/study/NCT01797120) | Phase 2 | Terminé | 131 | Fulvestrant + Everolimus vs Fulvestrant + placebo dans le cancer du sein HR+ résistant aux inhibiteurs de l'aromatase |
| [NCT05075512](https://clinicaltrials.gov/study/NCT05075512) | Phase 2 | Recrutement | 40 | Anlotinib + Fulvestrant dans le cancer du sein HR+/HER2− avec résistance endocrinienne secondaire |
| [NCT04936295](https://clinicaltrials.gov/study/NCT04936295) | Phase 2 | Inconnu | 61 | Fulvestrant + Anlotinib dans le cancer du sein métastatique HR+/HER2− avec mutation FGFR |
| [NCT03238196](https://clinicaltrials.gov/study/NCT03238196) | Phase 1 | Terminé | 35 | Fulvestrant + Palbociclib + Erdafitinib dans le cancer du sein métastatique ER+/HER2−/FGFR-amplifié |

---

## Preuves de la Littérature

Aucune littérature associant directement Fulvestrant à la Néoplasie Endocrinienne Multiple n'est disponible actuellement.

---

## Informations de Marché à Taiwan

Fulvestrant n'est pas commercialisé à Taiwan. Aucune AMM TFDA n'est enregistrée (0 licence).

À titre de référence internationale, Fulvestrant est commercialisé sous le nom **Faslodex® 250 mg/5 mL solution injectable** (AstraZeneca) dans l'Union Européenne, aux États-Unis, au Japon et dans de nombreux autres pays, pour le traitement du cancer du sein localement avancé ou métastatique à récepteurs hormonaux positifs, en monothérapie ou en association (CDK4/6i, PI3Ki, etc.).

---

## Cytotoxicité

Fulvestrant est un médicament anticancéreux utilisé dans le traitement du cancer du sein hormonodépendant.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie hormonale ciblée — SERD (antagoniste pur des récepteurs aux estrogènes / dégradeur sélectif) |
| Risque de Myélosuppression | Faible (Fulvestrant en monothérapie ne provoque pas de myélosuppression cliniquement significative) |
| Classification d'Émétogénicité | Minimale à faible |
| Éléments de Surveillance | Fonction hépatique (ALAT/ASAT), bilan osseux (densitométrie DEXA en cas de traitement prolongé), surveillance des signes de thromboembolie veineuse |
| Protection de Manipulation | Administration par voie intramusculaire uniquement (2 × 5 mL, une injection dans chaque fesse) ; précautions standard pour médicaments injectables antinéoplasiques |

---

## Considérations de Sécurité

Les données de sécurité spécifiques TFDA ne sont pas disponibles dans ce dossier (lacune DG001 : notice TFDA non récupérée). Veuillez consulter la notice EMA/FDA pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Parmi les 10 nouvelles indications prédites par TxGNN pour Fulvestrant, aucune ne dispose de preuves cliniques directes justifiant un développement immédiat. Les prédictions #1 (infection VIH), #3 (infection SIV), #4 (syndrome d'immunodéficience féline), #5 (trouble neurodéveloppemental), #8 (brachydactylie-syndactylie), #9 (hémoglobinopathie) et #10 (syndrome de microphtalmie) sont identifiées comme des artefacts de topologie du graphe de connaissances, sans aucun fondement mécanistique. La MEN (prédiction #2) présente la base biologique la plus plausible via l'expression potentielle des ER dans les tumeurs MEN1, mais reste une pure hypothèse de recherche faute de données cliniques directes. La polyarthrite rhumatoïde (#6) est déconseillée car le blocage conjoint de ER-α et ER-β par Fulvestrant risque d'aggraver l'inflammation en supprimant l'effet protecteur de ER-β.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation de l'expression des récepteurs aux estrogènes (ER-α / ER-β) dans les tissus tumoraux MEN1 (adénomes hypophysaires, pNETs) par immunohistochimie ou données transcriptomiques
- Récupération des données MOA complètes depuis DrugBank (lacune DG002)
- Récupération des données de sécurité TFDA depuis le PDF de la notice officielle (lacune DG001 — statut bloquant)
- Développement de modèles précliniques sur lignées cellulaires MEN1 ER+ avant d'envisager tout essai pilote
- Vérification de la faisabilité d'enregistrement à Taiwan (TFDA) si un développement clinique dans cette région est envisagé
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

