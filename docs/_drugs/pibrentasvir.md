---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir : De l'Hépatite C Chronique à l'Infection par le Virus de l'Hépatite B

## Résumé en Une Phrase

Pibrentasvir est un composant de la combinaison glécaprévir/pibrentasvir (G/P, commercialisée sous le nom Maviret), initialement développé pour le traitement de l'hépatite C chronique (VHC).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Infection par le Virus de l'Hépatite B (VHB)** avec un score de 99.84%,
mais les **14 essais cliniques** et **20 publications** identifiés par la recherche automatisée concernent en réalité le VHC et non le VHB — il s'agit d'un appariement erroné de la base de données, et aucune preuve directe ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hépatite C chronique (dans le cadre de la combinaison glécaprévir/pibrentasvir) |
| Nouvelle Indication Prédite | Infection par le Virus de l'Hépatite B (VHB) |
| Score de Prédiction TxGNN | 99.84% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les fiches structurées (drugbank/MOA). Sur la base des informations connues issues des essais cliniques associés, Pibrentasvir fait partie de la combinaison glécaprévir/pibrentasvir, un inhibiteur de la protéine NS5A du virus de l'hépatite C ; son efficacité dans le traitement de l'hépatite C chronique (VHC) a été largement démontrée par de nombreux essais de phase 3 (ENDURANCE, EXPEDITION, CERTAIN, SURVEYOR, etc.).

Cependant, le lien mécanistique entre cette indication d'origine et la nouvelle indication prédite (hépatite B) n'est **pas soutenu** sur le plan biologique. Le VHB est un virus à ADN (famille Hepadnaviridae) dont la réplication dépend d'une transcriptase inverse, tandis que le VHC est un virus à ARN (famille Flaviviridae) dont Pibrentasvir cible spécifiquement la protéine NS5A — une protéine sans homologue chez le VHB. Il n'existe donc aucun mécanisme plausible justifiant une activité antivirale directe de Pibrentasvir contre le VHB.

Le score TxGNN élevé (99.84%) semble refléter une proximité topologique dans le graphe de connaissances (les deux maladies étant classées comme « hépatites virales ») plutôt qu'une similarité pharmacologique réelle. Les 14 essais cliniques et 20 publications retrouvés lors de la recherche automatisée portent tous, à l'examen, sur le traitement du VHC — plusieurs mentionnant le VHB uniquement en tant que comorbidité, critère d'exclusion, ou sujet de vaccination post-traitement, jamais comme cible thérapeutique de Pibrentasvir. Il s'agit d'un artefact d'appariement de la base de données plutôt que d'un signal de preuve réel.

## Preuves d'Essais Cliniques

⚠️ **Note de qualité des données** : les essais listés ci-dessous ont été retrouvés par la recherche automatisée pour la requête « Pibrentasvir + hépatite B », mais portent en réalité tous sur le traitement du VHC (glécaprévir/pibrentasvir, ABT-493/ABT-530). Aucun n'évalue Pibrentasvir dans le VHB.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | Terminé | 89 | Étude de recherche de dose ABT-493/ABT-530 dans le VHC génotype 1 — non lié au VHB (appariement erroné) |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Terminé | 506 | ENDURANCE-3 : G/P vs sofosbuvir+daclatasvir dans le VHC génotype 3 — non lié au VHB |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Terminé | 87 | Risque cardiovasculaire après éradication du VHC chez patients VIH — non lié au VHB |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Terminé | 295 | CERTAIN-1 : efficacité/sécurité de G/P chez adultes japonais avec VHC — non lié au VHB |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Terminé | 177 | G/P ± ribavirine chez patients VHC génotype 1 en échec de NS5A+sofosbuvir — non lié au VHB |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Terminé | 100 | G/P chez adultes naïfs au Brésil avec VHC génotypes 1-6 — non lié au VHB |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Terminé | 384 | Suivi de résistance/durabilité de réponse après traitement VHC par G/P — non lié au VHB |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Terminé | 141 | G/P ± ribavirine chez patients VHC en échec de traitement antérieur — non lié au VHB |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Terminé | 174 | SURVEYOR-I : G/P chez patients VHC génotypes 1,4,5,6 — non lié au VHB |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | Terminé | 304 | ENDURANCE-2 : G/P chez patients VHC génotype 2 — non lié au VHB |

## Preuves de la Littérature

⚠️ De même, les publications ci-dessous traitent majoritairement du VHC ; celles touchant au VHB le font uniquement dans un contexte de comorbidité ou de vaccination post-traitement.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Non classé | Journal of viral hepatitis | GLE/PIB chez patients VHC avec insuffisance rénale sévère à Taïwan — non lié au VHB |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Non classé | Lancet Gastroenterol Hepatol | Revue sur le VHC chez enfants et adolescents — non lié au VHB |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Non classé | World J Gastroenterol | Avancées dans la gestion de l'hépatite virale pédiatrique (VHB et VHC) — traite le VHB comme contexte général, pas comme cible de Pibrentasvir |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Non classé | Eur J Gen Pract | Diagnostic et traitement du VHC chronique en médecine générale — non lié au VHB |
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Revue | Lancet Infect Dis | Vaccination contre le VHB après traitement du VHC — le VHB y est abordé comme prévention post-traitement, pas comme cible thérapeutique de Pibrentasvir |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Non classé | AIDS Reviews | Rapport de conférence sur l'hépatite virale (VHB et VHC), fardeau mondial et perspectives d'éradication — non spécifique à Pibrentasvir |
| [34298832](https://pubmed.ncbi.nlm.nih.gov/34298832/) | 2021 | Revue | Cancers | Carcinome hépatocellulaire et insuffisance rénale chronique — non lié au VHB ni à Pibrentasvir |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Non classé | Semin Liver Dis | Retraitement des échecs d'antiviraux à action directe dans le VHC — non lié au VHB |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Non classé | Clin Pharmacokinet | Considérations pharmacocinétiques des traitements du VHC (dont G/P) — non lié au VHB |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Non classé | Klin Mikrobiol Infekc Lek | Traitement antiviral du VHB et du VHC chez l'enfant à Ostrava — mentionne le VHB en parallèle du VHC, pas de données spécifiques à Pibrentasvir dans le VHB |

## Informations de Marché en France

Pibrentasvir n'est **pas commercialisé** en France de façon isolée (statut : non commercialisé, 0 AMM enregistrée). Il n'existe donc actuellement aucune spécialité pharmaceutique autonome à base de Pibrentasvir sur le marché français ; le principe actif n'est disponible que dans le cadre de la combinaison fixe glécaprévir/pibrentasvir pour le traitement du VHC, selon son AMM d'origine.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les recherches de mises en garde, contre-indications et interactions médicamenteuses spécifiques à Pibrentasvir n'ont retourné aucune donnée exploitable à ce stade (statut de requête DDI : non trouvé).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN élevé n'est corroboré ni par un mécanisme biologique plausible (le VHB et le VHC n'ont pas de cible moléculaire commune pertinente pour Pibrentasvir), ni par des preuves cliniques réelles — l'ensemble des essais et publications retrouvés concerne le VHC et non le VHB. Par ailleurs, l'absence des données d'allertes/contre-indications TFDA (écart bloquant DG001) empêche toute évaluation de sécurité préliminaire (S1), ce qui interdit toute progression du dossier en l'état.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice/les mises en garde TFDA pour Pibrentasvir (écart bloquant DG001) afin de permettre l'évaluation de sécurité S1
- Obtenir les données de mécanisme d'action confirmées via l'API DrugBank (écart DG002)
- Relancer la recherche d'essais cliniques et de littérature avec un filtrage spécifique à la maladie (VHB) pour éliminer les faux positifs liés au VHC
- À titre indicatif : la 2ᵉ prédiction du modèle (infection par le VIH, score 99.80%, niveau de preuve L4, statut « Research Question ») dispose de données indirectes de sécurité en population VIH plus substantielles, bien que le mécanisme antiviral direct contre le VIH reste également non démontré — à envisager comme piste de recherche secondaire, non comme candidat prioritaire
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

