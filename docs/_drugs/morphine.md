---
layout: default
title: Morphine
parent: Prédiction du modèle uniquement (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Morphine
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

# Morphine : Des antalgiques opioïdes au Syndrome Douloureux Myofascial

## Résumé en Une Phrase

La morphine est un agoniste des récepteurs opioïdes mu, commercialisé en France sous forme de comprimés à libération prolongée (MOSCONTIN). Le texte de l'indication originale n'est pas renseigné dans les données ANSM.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome douloureux myofascial**, avec **33 essais cliniques** et **17 publications** identifiés par la recherche automatisée. **Aucun de ces travaux ne teste directement la morphine dans cette maladie.** La prédiction repose surtout sur la classe analgésique générale.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (textes d'indication vides) |
| Nouvelle Indication Prédite | Syndrome douloureux myofascial |
| Score de Prédiction TxGNN | 99,75 % |
| Niveau de Preuve | L3 (faible : études indirectes, aucune étude morphine et syndrome myofascial) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. On sait que la morphine agit comme agoniste des récepteurs opioïdes mu et réduit la transmission des signaux nociceptifs.

Le syndrome douloureux myofascial est une douleur d'origine musculaire et nociceptive. Un lien plausible existe donc avec un antalgique opioïde. Il reste toutefois théorique, car les opioïdes ne sont pas un traitement standard de cette maladie.

Le score TxGNN très élevé reflète probablement la classe analgésique générale plutôt qu'un signal propre à la morphine. Le seul signal spécifique retrouvé est l'utilisation de la morphine en adjuvant dans une infiltration myofasciale après chirurgie du rachis (PMID 41664327). Ce contexte est postopératoire et ne correspond pas au traitement du syndrome myofascial.

## Preuves d'Essais Cliniques

Sur 33 essais recensés, aucun ne teste la morphine dans le syndrome myofascial. Les 10 essais les plus proches du sujet figurent ci-dessous.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06955923](https://clinicaltrials.gov/study/NCT06955923) | Phase 2 | Terminé | 11 | Injections de points gâchettes après prothèse totale de genou, contre injections simulées. La morphine n'est pas l'intervention étudiée. |
| [NCT04640896](https://clinicaltrials.gov/study/NCT04640896) | Phase 4 | En recrutement | 60 | Injections de points gâchettes contre thérapies classiques pour la douleur myofasciale après chirurgie cervicale antérieure. La morphine n'est pas testée. |
| [NCT07413770](https://clinicaltrials.gov/study/NCT07413770) | Non applicable | En recrutement | 60 | Effets du massage classique dans le syndrome myofascial. Traitement non médicamenteux. |
| [NCT05478928](https://clinicaltrials.gov/study/NCT05478928) | Non applicable | Inconnu | 60 | Techniques invasives (microélectrolyse, aiguilletage sec) sur points gâchettes myofasciaux. |
| [NCT04684784](https://clinicaltrials.gov/study/NCT04684784) | Non applicable | Terminé | 46 | Effet de l'aiguilletage sec sur l'activité électromyographique des points gâchettes latents. |
| [NCT03944889](https://clinicaltrials.gov/study/NCT03944889) | Phase 1 précoce | Terminé | 20 | Sensibilisation d'un muscle sain par la capsaïcine, modèle de sensibilisation centrale. |
| [NCT04504812](https://clinicaltrials.gov/study/NCT04504812) | Phase 3 | Terminé | 1937 | Stratégie séquencée de traitements non chirurgicaux de la douleur de gonarthrose, pour limiter le recours aux opioïdes. |
| [NCT00580294](https://clinicaltrials.gov/study/NCT00580294) | Non applicable | Terminé | 12 | Étude pilote de rotation d'opioïdes (morphine ou oxycodone vers oxymorphone) dans la douleur chronique. |
| [NCT06179199](https://clinicaltrials.gov/study/NCT06179199) | Non applicable | Pas encore en recrutement | 40 | Stimulation transcrânienne à courant continu pour l'analgésie de patients sédatés en réanimation, afin de limiter l'usage de morphine. |
| [NCT03271151](https://clinicaltrials.gov/study/NCT03271151) | Phase 4 | Terminé | 160 | Effet de la duloxétine sur la consommation d'opioïdes après prothèse totale de genou. |

## Preuves de la Littérature

Aucune publication ne montre l'efficacité de la morphine dans le syndrome myofascial. Le tableau présente les 10 publications les plus proches du sujet.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | ECR | Asian Spine J | Dexmédétomidine + morphine contre ropivacaïne 0,2 % seule en infiltration myofasciale lors d'une fusion thoracolombaire. Contexte postopératoire, résumé disponible très limité. |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | ECR | Eur J Pain | Analgésie péridurale (bupivacaïne et morphine) contre cryoanalgésie intercostale après thoracotomie, 107 patients. Hors syndrome myofascial. |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Revue | J Oral Maxillofac Surg | Les opioïdes au long cours dans les dysfonctions de l'articulation temporo-mandibulaire ne peuvent être ni soutenus ni réfutés faute de preuves suffisantes. |
| [16967674](https://pubmed.ncbi.nlm.nih.gov/16967674/) | 2006 | Revue | J Calif Dent Assoc | Utilisation de médicaments oraux, de perfusions et d'injections pour le diagnostic différentiel des douleurs orofaciales. |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohorte rétrospective | Pain Pract | Programme structuré d'étirements pour résoudre la douleur myofasciale et réduire les opioïdes chez des patients à douleur « héritée ». Intervention non médicamenteuse. |
| [22648287](https://pubmed.ncbi.nlm.nih.gov/22648287/) | 2012 | Étude clinique | J Anesth | Ajout d'injections des facettes articulaires cervicales à un traitement multimodal du syndrome myofascial cervical de longue durée. |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Étude clinique | Eur J Obstet Gynecol Reprod Biol | Le bloc du nerf pudendal réduit-il la douleur après injection de toxine botulique pour la douleur myofasciale pelvienne ? |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Pratique clinique | J Oral Maxillofac Surg | Arthrocentèse de l'articulation temporo-mandibulaire, suivie d'une perfusion intra-articulaire de morphine pour un effet prolongé. |
| [20390305](https://pubmed.ncbi.nlm.nih.gov/20390305/) | 2010 | Étude longitudinale | Schmerz | Modification des seuils de douleur pendant et après le sevrage des opioïdes dans la lombalgie chronique. |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Étude descriptive | Rev Assoc Med Bras | Approche thérapeutique de 56 patients atteints du syndrome douloureux post-chirurgie du dos. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 60576901 | MOSCONTIN 60 mg | Comprimé enrobé à libération prolongée |
| 60874417 | MOSCONTIN 100 mg | Comprimé enrobé à libération prolongée |
| 66828412 | MOSCONTIN 10 mg | Comprimé enrobé à libération prolongée |
| 66799334 | MOSCONTIN 30 mg | Comprimé enrobé à libération prolongée |

Les 4 AMM sont détenues par MUNDIPHARMA. Le texte de l'indication approuvée n'est pas renseigné dans les données reçues.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai ni aucune publication ne teste la morphine dans le syndrome douloureux myofasciale. Le score TxGNN élevé reflète surtout la classe analgésique. Les opioïdes ne sont pas un traitement standard de cette maladie.
- Les informations de sécurité de la notice ANSM manquent, ce qui bloque le passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (téléchargement et analyse du PDF)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Le texte de l'indication originale approuvée en France
- Une étude ciblée (ou une revue systématique) sur la morphine dans le syndrome myofascial, avec évaluation du rapport bénéfice/risque (dépendance, hyperalgésie induite par les opioïdes)

Parmi les autres prédictions du même dossier, le **syndrome des jambes sans repos** est la mieux étayée (niveau L3, stade S2). Elle repose sur des revues, un registre et des rapports observationnels, notamment sur la morphine intrathécale, et mériterait une évaluation séparée.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

