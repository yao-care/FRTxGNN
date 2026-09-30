---
layout: default
title: Velpatasvir
parent: Prédiction du modèle uniquement (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Velpatasvir
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

# Velpatasvir : De l'hépatite C chronique à l'infection par le virus de l'hépatite B

## Résumé en Une Phrase

Velpatasvir est un inhibiteur de la protéine virale NS5A, commercialisé en France dans les associations Epclusa et Vosevi. D'après les essais et publications associés, il est utilisé contre l'hépatite C chronique (le texte d'indication des AMM n'est pas renseigné dans les données reçues).
Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection par le virus de l'hépatite B (VHB)**. **26 essais cliniques** et **20 publications** sont rattachés à cette prédiction, mais tous portent sur le virus de l'hépatite C (VHC) et aucun ne démontre une efficacité contre le VHB.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hépatite C chronique (déduite des essais et publications ; texte d'indication des AMM non renseigné) |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B |
| Score de Prédiction TxGNN | 99,87 % |
| Niveau de Preuve | L4 (selon l'Evidence Pack ; aucune étude d'efficacité contre le VHB) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 5 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, velpatasvir fait partie des associations sofosbuvir/velpatasvir (Epclusa) et sofosbuvir/velpatasvir/voxilaprevir (Vosevi). Son efficacité dans l'hépatite C a été prouvée, mais rien ne montre mécanistiquement qu'il soit applicable à l'hépatite B.

Velpatasvir cible NS5A, une protéine propre au VHC, et le VHB n'a pas d'homologue de NS5A. Le score TxGNN élevé reflète donc probablement la proximité, dans le graphe de connaissances, entre antiviraux à tropisme hépatique, plutôt qu'un lien pharmacologique réel.

Le seul lien clinique documenté concerne les patients co-infectés VHB/VHC. Dans ce cas, velpatasvir traite le VHC et le VHB est géré séparément, par exemple par un analogue nucléos(t)idique comme le ténofovir. La seule publication spécifique au VHB (PMID 31542053) décrit une **réactivation du VHB** pendant un traitement anti-VHC : c'est un signal de sécurité, pas une preuve d'efficacité.

## Preuves d'Essais Cliniques

Sur les 26 essais rattachés, voici les 10 plus pertinents. Aucun n'évalue l'activité anti-VHB de velpatasvir.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Inconnu | 120 | SOF/VEL 12 semaines avec prophylaxie par TAF chez des patients co-infectés VHC/VHB (Chine) ; vise à prévenir la réactivation du VHB, pas à le traiter |
| [NCT02625909](https://clinicaltrials.gov/study/NCT02625909) | Phase 3 | Terminé | 222 | Traitement raccourci par SOF/VEL de l'hépatite C récente chez des usagers de drogues injectables, avec ou sans co-infection VIH ; aucune donnée VHB |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Terminé | 102 | SOF/VEL ± ribavirine dans l'hépatite C avec cirrhose décompensée |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | Terminé | 268 | SOF/VEL dans l'hépatite C avec cirrhose Child-Pugh B |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Terminé | 379 | SOF + velpatasvir ± ribavirine chez des patients naïfs atteints d'hépatite C (génotypes 1 à 6) |
| [NCT02994056](https://clinicaltrials.gov/study/NCT02994056) | Phase 2 | Terminé | 32 | SOF/VEL + ribavirine dans l'hépatite C avec cirrhose Child-Pugh C |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | Terminé | 281 | Ajout de ribavirine à SOF/VEL/VOX chez des non-répondeurs à l'hépatite C ; lien avec le VHB indirect au mieux |
| [NCT03570112](https://clinicaltrials.gov/study/NCT03570112) | N/A | Terminé | 40 | Étude observationnelle de l'hépatite C pendant la grossesse ; traitement par SOF/VEL après l'accouchement |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | En recrutement | 200 | Cohorte prospective de Vosevi chez des patients en échec d'un traitement antiviral direct contre le VHC |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Terminé | 15 | Interaction médicamenteuse SOF/VEL/VOX avec un contraceptif hormonal ; contexte pharmacocinétique et de sécurité uniquement |

## Preuves de la Littérature

Sur les 20 publications rattachées, voici les 10 plus pertinentes, classées par niveau de preuve. Aucun essai randomisé ni aucune revue systématique n'évalue velpatasvir contre le VHB.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Essai à bras unique | Lancet Gastroenterol Hepatol | Sécurité et efficacité de SOF/VEL dans l'hépatite C (génotype 4) chez des patients naïfs au Rwanda |
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Essai à bras unique | Lancet Gastroenterol Hepatol | SOF/VEL/VOX en retraitement de l'hépatite C après échec d'un antiviral direct, au Rwanda |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Étude de cohorte | J Viral Hepat | Stratégie simplifiée SOF/VEL au Myanmar, y compris chez des patients co-infectés VIH et/ou VHB, traités en parallèle par ténofovir |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Étude en vie réelle | J Virus Erad | Efficacité et sécurité de SOF/VEL chez des patients chinois, y compris co-infectés VHC/VHB |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Étude en vie réelle | J Gastroenterol Hepatol | SOF/VEL ± ribavirine dans l'hépatite C de génotype 3, y compris en cas de co-infection |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Étude rétrospective | Klin Mikrobiol Infekc Lek | Fréquence, efficacité et tolérance du traitement antiviral des hépatites B et C chez l'enfant à Ostrava |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revue | World J Gastroenterol | Avancées dans la prise en charge des hépatites virales pédiatriques ; le traitement curatif du VHB reste hors de portée |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Revue | Eur J Gen Pract | Diagnostic et traitement de l'hépatite C chronique en médecine générale |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Rapport de congrès | AIDS Rev | Compte rendu de la conférence internationale sur les hépatites virales 2017 (VHB et VHC) |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Rapport de cas | J Med Case Rep | Réactivation du VHB (mutant d'échappement de l'AgHBs) chez un patient anti-HBc positif traité par sofosbuvir/velpatasvir pour le VHC |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60348342 | EPCLUSA 200 mg/50 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée dans les données reçues |
| 60704272 | EPCLUSA 150 mg/37,5 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée dans les données reçues |
| 68425495 | EPCLUSA 200 mg/50 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée dans les données reçues |
| 63434686 | EPCLUSA 400 mg/100 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée dans les données reçues |
| 61932485 | VOSEVI 400 mg/100 mg/100 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée dans les données reçues |

Titulaire des cinq AMM : Gilead Sciences Ireland UC (Irlande).

## Considérations de Sécurité

- **Signal de réactivation du VHB** : une publication (PMID 31542053) rapporte une réactivation du VHB chez un patient anti-HBc positif traité par sofosbuvir/velpatasvir pour le VHC. Un dépistage du VHB et une surveillance sont donc à prévoir avant tout traitement antiviral direct.
- **Interactions médicamenteuses** : la revue de la littérature signale des interactions avec les antirétroviraux chez les patients VIH (PMID 28689442). Une étude de phase 1 montre que l'absorption de velpatasvir dépend du pH et diminue sous inhibiteur de la pompe à protons (NCT03513393).

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,87 %), mais il ne s'appuie sur aucune donnée d'efficacité contre le VHB : les 26 essais et 20 publications portent sur le VHC, et le VHB n'a pas de cible NS5A.
- La littérature spécifique au VHB décrit un risque de réactivation, pas un bénéfice thérapeutique. Le passage à l'étape de criblage de sécurité est bloqué faute de notice ANSM.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice de l'ANSM (mises en garde et contre-indications) en téléchargeant et en analysant le PDF.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Disposer de données in vitro ou précliniques montrant une activité anti-VHB de velpatasvir, ce qui n'existe pas à ce jour.
- Récupérer les indications approuvées dans le texte des AMM pour confirmer l'indication d'origine.

Les neuf autres prédictions du modèle (hépatites E et A, VIH, virus animaux, etc.) sont au niveau L4 ou L5 et aussi en Hold, sans preuve directe.

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

