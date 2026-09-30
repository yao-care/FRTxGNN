---
layout: default
title: Elbasvir
parent: Prédiction du modèle uniquement (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Elbasvir
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

# Elbasvir : De l'hépatite C chronique à l'infection par le virus de l'hépatite B

## Résumé en Une Phrase

Elbasvir est un inhibiteur de la protéine virale NS5A, utilisé en association fixe avec le grazoprévir (Zepatier) pour traiter l'hépatite C chronique.
Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection par le virus de l'hépatite B (VHB)**, avec un score élevé (99,71 %).
Les **13 essais cliniques** et **18 publications** rattachés à cette prédiction portent tous sur l'hépatite C : **aucun ne teste l'activité d'elbasvir contre le VHB**.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hépatite C chronique (déduite des essais et de la littérature ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B |
| Score de Prédiction TxGNN | 99,71 % |
| Niveau de Preuve | L5 (prédiction du modèle, aucune étude sur le VHB) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

Le pack de données attribue L4 à cette prédiction. Selon la grille de niveaux, L4 exige des études précliniques ou mécanistiques sur le VHB, et il n'y en a aucune ici. Je retiens donc L5.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas renseignées dans le pack. On sait toutefois qu'elbasvir cible la protéine NS5A du virus de l'hépatite C (VHC), impliquée dans la réplication virale et l'assemblage des particules. Son efficacité dans l'hépatite C est bien établie : le taux de réponse virologique soutenue est très élevé dans les essais de phase 2 et 3 (génotypes 1, 4 et 6).

Le VHB et le VHC sont tous deux des virus hépatotropes. Le score élevé du modèle reflète probablement ce voisinage dans le graphe de connaissances (« hépatites virales »), et non une véritable communauté de cible. Le VHB n'a **aucun homologue de NS5A** : c'est un virus à ADN qui se réplique par transcription inverse, avec une machinerie différente de celle du VHC.

Le lien est donc surtout **statistique**, sans base mécanistique démontrée. Le VHB reste pertinent seulement comme sujet de sécurité : une co-infection ou une réactivation de l'hépatite B est possible pendant un traitement antiviral direct contre le VHC.

---

## Preuves d'Essais Cliniques

Tous les essais ci-dessous portent sur l'hépatite C. Aucun ne mesure un critère lié au VHB.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02332720](https://clinicaltrials.gov/study/NCT02332720) | Phase 2 | Terminé | 413 | Grazoprévir + uprifosbuvir + elbasvir ou ruzasvir dans l'hépatite C de génotypes 3, 4, 5 et 6 ; pas de donnée sur le VHB |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Terminé | 33 808 | Sécurité des antiviraux directs dans l'hépatite C, comparée aux patients non traités ; pas de test d'activité anti-VHB |
| [NCT02105688](https://clinicaltrials.gov/study/NCT02105688) | Phase 3 | Terminé | 301 | Grazoprévir/elbasvir 12 semaines dans l'hépatite C (génotypes 1, 4, 6) sous traitement de substitution aux opiacés |
| [NCT02115321](https://clinicaltrials.gov/study/NCT02115321) | Phase 2/3 | Terminé | 40 | Grazoprévir/elbasvir dans l'hépatite C avec cirrhose Child-Pugh B |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Terminé | 80 | Hépatite C aiguë de génotype 1/4 chez des patients VIH+ |
| [NCT01717326](https://clinicaltrials.gov/study/NCT01717326) | Phase 2 | Terminé | 573 | Grazoprévir + elbasvir ± ribavirine dans l'hépatite C chronique ; critère principal : RVS12 |
| [NCT01532973](https://clinicaltrials.gov/study/NCT01532973) | Phase 1 | Terminé | 48 | Sécurité, pharmacocinétique et pharmacodynamie d'elbasvir chez des hommes infectés par le VHC |
| [NCT03110055](https://clinicaltrials.gov/study/NCT03110055) | N/A | Inconnu | 20 | Grazoprévir/elbasvir + chimioembolisation vs chimioembolisation seule dans le carcinome hépatocellulaire lié au VHC |
| [NCT03797066](https://clinicaltrials.gov/study/NCT03797066) | Phase 4 | Arrêté | 13 | Dépistage et traitement de l'hépatite C sur site chez des personnes sans domicile |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Terminé | 87 | Risque cardiovasculaire après éradication du VHC chez des patients avec ou sans VIH |

---

## Preuves de la Littérature

Aucune publication ne démontre une activité d'elbasvir contre le VHB.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revue | Liver Int | Vers l'éradication du VHC et la guérison du VHB ; contexte général, sans donnée sur elbasvir |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Cohorte | Klin Mikrobiol Infekc Lek | Évaluation rétrospective du traitement antiviral des hépatites B et C chez l'enfant à Ostrava |
| [29077864](https://pubmed.ncbi.nlm.nih.gov/29077864/) | 2018 | ECR | Clin Infect Dis | Retraitement (sofosbuvir + grazoprévir/elbasvir + ribavirine) après échec d'un traitement contenant un inhibiteur de NS5A ou de NS3 (ANRS HC34 REVENGE) |
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Essai de phase 4 à un bras | Antimicrob Agents Chemother | Efficacité et tolérance de grazoprévir/elbasvir chez des transplantés hépatiques ou rénaux avec VHC de génotype 1b |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Étude en vie réelle | J Viral Hepat | Expérience à Taïwan, centrée sur les effets indésirables hépatiques et rénaux |
| [32306039](https://pubmed.ncbi.nlm.nih.gov/32306039/) | 2020 | Étude clinique | J Antimicrob Chemother | Traitement immédiat de l'hépatite C récente chez des hommes ayant des rapports sexuels avec des hommes |
| [32925725](https://pubmed.ncbi.nlm.nih.gov/32925725/) | 2020 | Étude de cohorte | Medicine | Incidence et facteurs prédictifs d'élévation des ALAT sous antiviraux directs |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revue | Clin Pharmacokinet | Considérations pharmacocinétiques et pharmacodynamiques des traitements de l'hépatite C (mise à jour 2019) |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Revue | Acta Pharm Sin B | Antiviraux directs anti-VHC ; rappelle que, contrairement au VHB et au VIH, le VHC est curable |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Revue | Ann Hepatol | Comparaison mondiale des prix des traitements des hépatites B et C |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66198173 | ZEPATIER 50 mg/100 mg, comprimé pelliculé (MERCK SHARP & DOHME, Pays-Bas) | Comprimé pelliculé | Texte d'indication non renseigné dans les données reçues |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune mise en garde, contre-indication ni interaction médicamenteuse n'a pu être extraite du pack. La notice de l'ANSM n'y figure pas et la recherche d'interactions n'a rien retourné. Il faut donc obtenir la notice avant toute évaluation de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,71 %), mais aucun élément clinique ou mécanistique ne soutient une activité contre le VHB, car le VHB n'a pas de cible NS5A. Les preuves rattachées concernent uniquement le VHC.
- Les autres indications prédites (hépatites E et A, fièvres hémorragiques virales, VIH, maladies animales, trouble neurodéveloppemental rare) sont aussi en Hold, sans preuve directe. Les essais chez des patients co-infectés VIH/VHC renseignent seulement sur la sécurité et les interactions, pas sur une efficacité anti-VIH.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, interactions) ; ce point bloque la suite, y compris le criblage de sécurité.
- Compléter les données sur le mécanisme d'action depuis DrugBank.
- Obtenir des données précliniques *in vitro* de l'activité d'elbasvir sur la réplication du VHB, sans quoi le passage à l'étape suivante est injustifié.
- Examiner séparément la sécurité en cas de co-infection VHB/VHC (risque de réactivation du VHB sous antiviraux directs contre le VHC), qui est le seul lien clinique réel avec le VHB.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute utilisation.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

