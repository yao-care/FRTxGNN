---
layout: default
title: Arginine
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 1
---

# Arginine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Le skill txgnn-pipeline confirme le contexte. Voici le rapport généré à partir de l'Evidence Pack fourni :

---

# Arginine : D'Acide Aminé Essentiel à la Gastroparésie

## Résumé en Une Phrase

L-Arginine est un acide aminé essentiel conditionnel, dont l'usage médical actuel se limite principalement à la supplémentation nutritionnelle et aux tests de stimulation diagnostique (test à l'arginine). Le modèle TxGNN prédit qu'il pourrait être efficace pour la **gastroparésie** (score 99,42 %), avec **0 essai clinique pertinent** et **10 publications précliniques** soutenant actuellement cette direction. L'ensemble des preuves disponibles est exclusivement issu de modèles animaux ; aucun essai clinique humain ciblant cette indication n'a été identifié à ce jour.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Supplément nutritionnel / acide aminé essentiel conditionnel |
| Nouvelle Indication Prédite | Gastroparésie |
| Score de Prédiction TxGNN | 99,42 % |
| Niveau de Preuve | L4 — études précliniques et mécanistiques uniquement |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

L-Arginine est le **seul substrat** de la biosynthèse du monoxyde d'azote (NO) via la NO synthase neuronale (nNOS). Dans le tractus gastro-intestinal, le NO constitue le principal neurotransmetteur inhibiteur des neurones entériques, régulant la relaxation des muscles lisses gastriques et l'ouverture du sphincter pylorique. En l'absence de substrat suffisant, ce mécanisme de relaxation est compromis.

La gastroparésie est caractérisée par une perte sélective des cellules interstitielles de Cajal (ICC) positives pour nNOS et des neurones entériques inhibiteurs, entraînant une déficience en NO, une hypertonie pylorique et un retard de vidange gastrique. Ce mécanisme constitue une cible thérapeutique directe pour la supplémentation en L-arginine.

La preuve mécanistique la plus directe est fournie par PMID 25057793 (*Endocrinology*, 2014) : l'administration orale de dexaméthasone induit une gastroparésie chez la souris par déplétion en L-arginine via un mécanisme GR-dépendant, et la supplémentation en L-arginine inverse complètement ce phénotype. Plusieurs autres études animales confirment le rôle central de la voie nNOS/NO dans la physiopathologie de la gastroparésie (diabétique, parkinsonienne, néonatale), renforçant la cohérence mécanistique de cette prédiction.

---

## Preuves d'Essais Cliniques

Un seul essai a été recensé lors de la recherche (NCT01702051 — transplantation autologue d'îlots pancréatiques après pancréatectomie, Phase N/A, statut inconnu, n = 150). Cet essai porte sur le contrôle glycémique post-chirurgical et **n'est pas pertinent** pour l'évaluation de l'arginine dans la gastroparésie (grade de pertinence : C). L'arginine n'y est mentionnée que comme outil diagnostique (test de stimulation à l'arginine), non comme traitement.

> **Aucun essai clinique évaluant la supplémentation en L-arginine pour le traitement de la gastroparésie n'est actuellement enregistré.**

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Animal (mécanistique, interventionnel) | *Endocrinology* | La dexaméthasone induit une gastroparésie murine par déplétion en L-arginine (mécanisme GR-dépendant) ; la supplémentation en L-arginine inverse le phénotype — **preuve mécanistique directe** |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Animal (mécanistique) | *Am J Physiol Gastrointest Liver Physiol* | Altération de la relaxation nitrergique du sphincter pylorique dans un modèle rat Parkinson (6-OHDA) liée à la déficience en nNOS — confirme le rôle de la voie NO dans la gastroparésie parkinsonienne |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Animal (mécanistique) | *Am J Physiol Gastrointest Liver Physiol* | La déficience en tétrahydrobioptérine (cofacteur obligatoire de nNOS) induit une gastroparésie néonatale chez la souris — souligne la dépendance de la voie NO à la disponibilité en substrats/cofacteurs |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Animal (descriptif) | *Neurogastroenterol Motil* | Diminution de l'expression et de la fonction de nNOS dans le jéjunum de rats BB diabétiques — propose la perte de nNOS comme mécanisme central de la gastroparésie diabétique |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Animal (interventionnel) | *Am J Physiol Gastrointest Liver Physiol* | La stimulation électrique gastrique synchronisée améliore l'accommodation gastrique via la voie nitrergique chez le chien vagotomisé |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Animal (mécanistique) | *Am J Physiol Gastrointest Liver Physiol* | L'inhibition de la motilité gastrique par hyperglycémie est médiée par les canaux KATP du ganglion nodeux — éclaire l'interface glycémie/motilité gastrique dans la gastroparésie diabétique |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Animal (interventionnel) | *Am J Physiol Gastrointest Liver Physiol* | La stimulation du nerf sacré améliore l'accommodation gastrique chez le rat via voie afférente spinale et efférente vagale |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Animal (pharmacologique) | *World J Gastroenterol* | La ghréline et le GHRP-6 améliorent la motilité gastrique dans un modèle murin de gastroparésie diabétique |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Animal (observationnel) | *Gastroenterology* | Retard de vidange gastrique induit par anaphylaxie alimentaire chez le rat sensitisé — médiateurs de la gastroparésie post-anaphylactique |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Rapport de cas | *Am J Case Reports* | Normalisation du lactate sérique par modifications du mode de vie chez une patiente porteuse du variant m.3243A>G (MELAS avec gastroparésie associée) |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les preuves disponibles se limitent à des études précliniques (niveau L4, modèles animaux exclusivement). Bien que le lien mécanistique entre la déplétion en L-arginine et la gastroparésie soit biologiquement cohérent et directement démontré dans au moins un modèle animal (PMID 25057793), aucun essai clinique humain n'a évalué cette approche thérapeutique, et le médicament n'est pas commercialisé en France dans cette indication.

**Pour avancer, les éléments suivants sont nécessaires :**
- Essai clinique de Phase 1/2 évaluant la supplémentation orale en L-arginine chez des patients atteints de gastroparésie (modèle glucocorticoïde-induite en priorité, compte tenu du mécanisme le mieux documenté)
- Données pharmacocinétiques sur les concentrations plasmatiques et tissulaires atteignables (paroi gastrique) après administration orale
- Profil de sécurité formalisé : risques spécifiques à identifier (hyperargininémie, interactions avec des pathologies rénales ou herpétiques, stimulation de l'arginase)
- Données complètes sur le mécanisme d'action (MOA DrugBank)
- Données réglementaires de sécurité (notice/RCP, mises en garde ANSM)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

