---
layout: default
title: Pibrentasvir
parent: Prédiction du modèle uniquement (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Pibrentasvir : De l'Hépatite C Chronique à l'Infection par le Virus de l'Hépatite B

## Résumé en Une Phrase

Le pibrentasvir est un inhibiteur de la protéine NS5A du virus de l'hépatite C (VHC), commercialisé en France dans l'association glécaprévir/pibrentasvir (Maviret). Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection par le virus de l'hépatite B**, mais **aucun des 14 essais cliniques et des 20 publications associés ne porte sur le VHB** : tous concernent le VHC. Cette prédiction repose donc uniquement sur le modèle, sans preuve réelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM françaises (déduite des essais associés : hépatite C chronique) |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L5 (aucune étude sur le VHB ; le pack proposait L4, mais aucune étude préclinique ou mécanistique sur le VHB n'y figure) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, le pibrentasvir fait partie de l'association glécaprévir/pibrentasvir, son efficacité dans l'hépatite C a été démontrée, et il agit comme inhibiteur de NS5A du VHC.

**La plausibilité mécanistique est faible.** Le VHB est un hépadnavirus et ne possède pas d'homologue de NS5A. Il n'existe donc pas de mécanisme antiviral direct plausible. Le score élevé reflète très probablement la proximité entre nœuds « hépatites virales » dans le graphe de connaissances, et non un signal d'efficacité.

Le seul lien clinique connu est indirect et relève de la sécurité : la réactivation du VHB est une préoccupation reconnue lorsque les antiviraux à action directe éliminent le VHC chez des patients co-infectés par le VHB.

---

## Preuves d'Essais Cliniques

Les 14 essais rattachés à cette indication portent tous sur le VHC ; aucun ne teste une activité anti-VHB. Ils sont classés par pertinence « C » (non pertinents pour le VHB) ou en attente d'évaluation. Les 10 plus informatifs sont listés ci-dessous.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Terminé | 506 | ENDURANCE-3 : glécaprévir/pibrentasvir vs sofosbuvir + daclatasvir dans le VHC de génotype 3 |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Terminé | 295 | CERTAIN-1 : efficacité et sécurité chez des adultes japonais atteints de VHC |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Terminé | 177 | Étude pragmatique de G/P ± ribavirine chez des patients VHC génotype 1 préalablement traités par inhibiteur de NS5A + sofosbuvir |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Terminé | 100 | G/P sur 8 ou 12 semaines chez des adultes brésiliens naïfs de traitement (VHC génotypes 1 à 6) |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | Terminé | 304 | ENDURANCE-2 : essai contre placebo dans le VHC de génotype 2 |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | Terminé | 694 | SURVEYOR-II : ABT-493 + ABT-530 ± ribavirine dans le VHC de génotypes 2 à 6 |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Terminé | 141 | Efficacité chez des patients VHC en échec d'un précédent traitement par antiviral à action directe |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Terminé | 384 | Suivi à long terme de la durabilité de la réponse virologique et des résistances |
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | Terminé | 89 | Étude de détermination de dose chez des patients VHC de génotype 1 |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Terminé | 174 | SURVEYOR-I : VHC de génotypes 1, 4, 5 et 6, avec ou sans cirrhose compensée |

---

## Preuves de la Littérature

Aucune publication ne rapporte d'efficacité du pibrentasvir contre le VHB. Les références ci-dessous sont les plus proches du sujet (VHB/VHC, sécurité, pharmacologie).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Revue | The Lancet. Infectious diseases | Commentaire sur la vaccination contre l'hépatite B après traitement de l'hépatite C (résumé non disponible) |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revue | World journal of gastroenterology | Prise en charge des hépatites virales B et C pédiatriques ; le traitement du VHB reste loin d'être curatif |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Rapport de cas | BMJ case reports | Lésion hépatique aiguë associée à G/P chez un patient VHC non cirrhotique sans co-infection VHB |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Étude rétrospective | Klinicka mikrobiologie a infekcni lekarstvi | Fréquence, efficacité et tolérance des traitements antiviraux des hépatites B et C chez l'enfant à Ostrava |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Rapport de conférence | AIDS reviews | Compte rendu de la conférence internationale sur les hépatites virales 2017 (VHB et VHC) |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Étude transversale | Annals of hepatology | Comparaison internationale des prix des traitements des hépatites B et C |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Étude rétrospective | Journal of viral hepatitis | Efficacité et sécurité de G/P chez 108 patients VHC avec insuffisance rénale sévère à Taïwan |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Revue | Seminars in liver disease | Retraitement des patients VHC en échec des antiviraux à action directe |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revue | Clinical pharmacokinetics | Aspects pharmacocinétiques et pharmacodynamiques des traitements de l'hépatite C (mise à jour 2019) |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Revue | The European journal of general practice | Diagnostic et traitement de l'hépatite C chronique |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 62685529 | MAVIRET 50 mg/20 mg, granulés enrobés en sachet | Granulés enrobés |
| 63052124 | MAVIRET 100 mg/40 mg, comprimé pelliculé | Comprimé pelliculé |

Titulaire des deux AMM : AbbVie Deutschland (Allemagne). Le texte de l'indication approuvée n'est pas renseigné dans les données reçues.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune étude clinique ou préclinique ne teste le pibrentasvir contre le VHB, et il n'existe pas de cible plausible : le VHB n'a pas d'homologue de NS5A. Le score de 99,84 % semble être un artefact de proximité dans le graphe.
- Les neuf autres indications prédites par le modèle sont également au niveau L5 (aucune preuve réelle) et en Hold.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), lacune bloquante qui empêche le passage au criblage de sécurité S1
- Données détaillées sur le mécanisme d'action (DrugBank)
- Données in vitro d'activité anti-VHB (modèles cellulaires), seul moyen de lever le doute sur l'artefact de graphe
- Texte de l'indication approuvée des AMM, pour documenter l'indication d'origine
- Protocole de surveillance de la réactivation du VHB chez les patients co-infectés traités par antiviraux à action directe
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

