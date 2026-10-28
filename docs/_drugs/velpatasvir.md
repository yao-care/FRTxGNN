---
layout: default
title: Velpatasvir
parent: Preuves modérées (L3-L4)
nav_order: 807
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Velpatasvir : nouvelle indication prédite, Infection par le virus de l'hépatite B (niveau de preuve L4). Indication d'origine : Infection chronique par le virus de l'hépatite C (le texte d'indicati…"
monitor_inn: "VELPATASVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Velpatasvir
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Velpatasvir : Infection par le virus de l'hépatite B
{: .text-alpha }

## Résumé en Une Phrase

Velpatasvir est un inhibiteur de la protéine virale NS5A, initialement utilisé pour le traitement de l'infection chronique par le virus de l'hépatite C (VHC).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le virus de l'hépatite B (VHB)**, mais **aucun des 5 essais cliniques** ni des **20 publications** associés ne teste réellement cette hypothèse : tous portent sur le VHC, le VHB n'apparaissant que comme co-infection ou risque de réactivation.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection chronique par le virus de l'hépatite C (le texte d'indication des AMM n'est pas renseigné dans les données compilées) |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B |
| Score de Prédiction TxGNN | 0,9987 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : 5 sur 5) |
| Nombre d'AMM | 5 (valides : 5) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, velpatasvir est un inhibiteur de NS5A du VHC, utilisé en association avec le sofosbuvir (Epclusa) et, dans une triple association, avec le sofosbuvir et le voxilaprévir (Vosevi). Son efficacité dans l'hépatite C est établie par de nombreuses études.

Toutefois, **la plausibilité mécanistique pour l'hépatite B est faible**. Le VHB ne possède pas de protéine NS5A ni d'homologue, et il n'existe donc pas de cible commune directe. Le score élevé du modèle reflète probablement la proximité dans le réseau de connaissances entre les « hépatites virales » plutôt qu'un véritable mécanisme.

Les données du dossier vont dans le même sens : l'essai NCT04997564 associe sofosbuvir/velpatasvir à du ténofovir alafénamide (TAF) chez des patients co-infectés VHC/VHB, mais le TAF y sert à prévenir la réactivation du VHB, et non à le traiter par velpatasvir.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Inconnu | 120 | SOF/VEL 12 semaines avec TAF prophylactique chez des patients co-infectés VHC/VHB ; vise la réactivation du VHB, pas l'efficacité de velpatasvir contre le VHB |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | Inconnu | 25 | Étude pilote de faisabilité chez des patients co-infectés VIH-VHC ; sans critère VHB |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Phase 2 | Terminé | 40 | Traitement sans interféron des lymphomes B indolents associés au VHC ; aucune donnée VHB |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | Terminé | 803 | Projet de démonstration d'un traitement simplifié du VHC au Myanmar ; non pertinent pour le VHB |
| [NCT07560046](https://clinicaltrials.gov/study/NCT07560046) | Phase 4 | Pas encore en recrutement | 1280 | Essai en grappes de dépistage et traitement du VHC sur le lieu de soins ; non pertinent pour l'efficacité sur le VHB |

## Preuves de la Littérature

La littérature associée porte presque exclusivement sur le VHC. Les publications les plus proches du sujet VHB sont les suivantes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42558970](https://pubmed.ncbi.nlm.nih.gov/42558970/) | 2026 | Étude multicentrique | J Clin Transl Hepatol | Sécurité et efficacité de SOF/VEL avec prétraitement par TAF chez des patients co-infectés VHB/VHC, sur la réactivation du VHB |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Rapport de cas | J Med Case Rep | Réactivation du VHB (mutant d'échappement de l'AgHBs) sous sofosbuvir/velpatasvir |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Étude de cohorte | J Viral Hepat | Stratégie simplifiée SOF/VEL au Myanmar, patients co-infectés VHB traités en parallèle par ténofovir |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Étude en vie réelle | J Virus Erad | Efficacité de SOF/VEL contre le VHC chez des patients chinois, y compris co-infections VHC/VHB |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Essai à bras unique | Lancet Gastroenterol Hepatol | SOF/VEL dans l'hépatite C chronique de génotype 4 au Rwanda |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revue | World J Gastroenterol | Hépatites virales pédiatriques ; le traitement du VHB reste non curatif |

Ces travaux évaluent le VHC ou la sécurité en cas de co-infection. Aucun ne démontre une activité de velpatasvir contre le VHB.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60348342 | EPCLUSA 200 mg/50 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |
| 60704272 | EPCLUSA 150 mg/37,5 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée (AMM active) |
| 68425495 | EPCLUSA 200 mg/50 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée (AMM active) |
| 63434686 | EPCLUSA 400 mg/100 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |
| 61932485 | VOSEVI 400 mg/100 mg/100 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |

## Considérations de Sécurité

**Interactions Médicamenteuses** : 57 interactions sont recensées. Parmi celles listées, les principales sont :
- **Majeures** : dexaméthasone, inhibiteurs de la pompe à protons (ésoméprazole, oméprazole, lansoprazole, dexlansoprazole, pantoprazole, rabéprazole)
- **Modérées** : antiacides (hydroxyde d'aluminium, carbonate de calcium, magaldrate, composés de magnésium), antihistaminiques H2 (cimétidine, famotidine, nizatidine), naldémédine
- **Mineures** : fidaxomicine, naloxégol, prucalopride

**Point d'attention lié à l'hépatite B** : des cas de réactivation du VHB ont été rapportés sous antiviraux à action directe contre le VHC chez des patients ayant des antécédents d'infection par le VHB. Un dépistage du VHB avant tout traitement est donc pertinent.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais il ne repose sur aucun mécanisme plausible (absence de NS5A chez le VHB) ni sur aucune étude testant velpatasvir contre le VHB. Les preuves se limitent à des données VHC et de co-infection (L4).
- Les 5 AMM françaises sont toutes annulées, ce qui limite aussi la faisabilité réglementaire locale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de velpatasvir, et analyse de son éventuelle activité sur le VHB
- Études précliniques in vitro sur des modèles d'infection par le VHB
- Notice officielle de l'ANSM (mises en garde et contre-indications)
- Clarification du statut des AMM annulées et de la disponibilité actuelle du produit en France

**Autres prédictions du modèle :** les prédictions suivantes sont toutes de niveau L4 ou L5, sans soutien mécanistique ni clinique, et également en « Hold » : hépatite E, hépatite A, hépatite virale animale, fièvre hémorragique d'Omsk, maladie de la forêt de Kyasanur, infection par le VIH, infection par le virus de l'immunodéficience simienne, syndrome d'immunodéficience acquise féline et un trouble neurodéveloppemental génétique. Pour le VIH, les données portent uniquement sur le traitement du VHC chez des personnes vivant avec le VIH.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

