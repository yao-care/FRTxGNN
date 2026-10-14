---
layout: default
title: Etoricoxib
parent: Preuves modérées (L3-L4)
nav_order: 309
evidence_level: L4
indication_count: 10
---

# Etoricoxib
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Étoricoxib : Des affections inflammatoires douloureuses à la migraine

## Résumé en Une Phrase

L'étoricoxib est un inhibiteur sélectif de la COX-2, utilisé dans le traitement de pathologies douloureuses et inflammatoires (arthrose, polyarthrite rhumatoïde, spondylarthrite ankylosante, goutte, douleur aiguë).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine**, mais aucun essai clinique n'est enregistré et une seule publication indirecte (une revue de portée sur les céphalées liées au jeûne) est associée à cette prédiction.
Le niveau de preuve est donc faible : la prédiction repose essentiellement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM ; les données pharmacologiques mentionnent l'arthrose, la polyarthrite rhumatoïde, la lombalgie chronique, la spondylarthrite ankylosante, la douleur aiguë et la goutte |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 14 (toutes annulées, aucune valide) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les informations pharmacologiques connues, l'étoricoxib cible la COX-2 (gène PTGS2) et réduit la synthèse des prostaglandines, notamment la PGE2.

La PGE2 intervient dans l'inflammation neurogène et la sensibilisation trigémino-vasculaire de la migraine. Un lien mécanistique plausible existe donc entre l'indication d'origine (douleur inflammatoire) et la migraine. Une étude préclinique chez le rat (PMID 29209105) a examiné l'effet d'AINS, dont l'étoricoxib, sur la libération de CGRP et de PGE2 par les ganglions trigéminés, ce qui soutient indirectement cette hypothèse.

Il faut toutefois rester prudent : la seule publication liée à la prédiction « migraine » est une revue de portée sur les céphalées de jeûne pendant le Ramadan, qui ne teste pas l'étoricoxib dans la migraine. Le score très élevé du modèle n'est pas confirmé par des données cliniques.

**Autres prédictions du modèle (à titre d'information) :**
- **Céphalées (headache disorder)** : le signal le plus étayé, avec des cas rapportés de réponse à l'étoricoxib (céphalée poignardante primaire, céphalée de toux secondaire, céphalées sensibles à l'indométacine). Niveau L4, uniquement des cas cliniques.
- **Céphalalgies trigémino-autonomiques** : une seule série observationnelle (PMID 35277974). Niveau L4.
- **Hypertension pulmonaire** : probable faux positif. L'inhibition de la COX-2 réduit la prostacycline vasodilatatrice, ce qui serait défavorable, et le seul article est un cas d'hyperkaliémie et d'insuffisance rénale aiguë.
- **Cardiopathie cyphoscoliotique** : aucun lien plausible, et le risque cardiovasculaire des coxibs plaide contre cet usage.
- **Atrophodermie vermiculée, ulérythème ophryogène, hypertrophie bénigne de la prostate** : aucune donnée, prédiction uniquement (L5).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune publication ne teste directement l'étoricoxib dans la migraine. Les publications ci-dessous sont celles liées aux prédictions les plus proches (migraine et céphalées).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42841395](https://pubmed.ncbi.nlm.nih.gov/42841395/) | 2026 | Revue de portée | Pain management | Synthèse sur les céphalées liées au jeûne pendant le Ramadan ; preuve indirecte, sans test de l'étoricoxib dans la migraine |
| [29209105](https://pubmed.ncbi.nlm.nih.gov/29209105/) | 2017 | Préclinique (rat) | Mediators of inflammation | Effets de l'étoricoxib, du nimésulide et du kétoprofène sur la libération de CGRP et de PGE2 par les ganglions trigéminés du rat |
| [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/) | 2022 | Série de cas | Headache | Céphalées sensibles à l'indométacine répondant à l'étoricoxib et au célécoxib |
| [36893522](https://pubmed.ncbi.nlm.nih.gov/36893522/) | 2023 | Cas clinique | Clinical neurology and neurosurgery | Deux patients atteints de céphalée de toux secondaire ayant répondu à l'étoricoxib |
| [17883876](https://pubmed.ncbi.nlm.nih.gov/17883876/) | 2007 | Cas clinique | Journal of medical case reports | Utilisation de l'étoricoxib dans une céphalée poignardante idiopathique |
| [18171381](https://pubmed.ncbi.nlm.nih.gov/18171381/) | 2008 | Cas clinique / série | European journal of neurology | La céphalée poignardante primaire peut répondre à l'étoricoxib |
| [25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/) | 2014 | Cas clinique (événement indésirable) | Clinical neuropharmacology | Syndrome de vasoconstriction cérébrale réversible possiblement induit par l'étoricoxib (signal de sécurité) |
| [21373319](https://pubmed.ncbi.nlm.nih.gov/21373319/) | 2010 | Cas clinique (événement indésirable) | International journal of emergency medicine | Hyperkaliémie menaçante et insuffisance rénale aiguë induites par l'étoricoxib, avec le telmisartan (signal de sécurité) |

## Informations de Marché en France

Les 14 AMM recensées sont annulées. Aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas renseigné pour ces AMM. Les cinq premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66514714 | ETORICOXIB BIOGARAN 30 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 65716563 | ETORICOXIB VIATRIS 30 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 65646086 | ARCOXIA 30 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 61350702 | ETORICOXIB KRKA 60 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 65612340 | ETORICOXIB BIOGARAN 60 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Interactions médicamenteuses** : une seule entrée, de nature pharmacologique, correspondant à la cible COX-2 (PTGS2) de l'étoricoxib ; aucun niveau de gravité n'est précisé.
- **Signaux issus de la littérature** :
  - syndrome de vasoconstriction cérébrale réversible possiblement induit par l'étoricoxib (cas clinique) ;
  - hyperkaliémie menaçante et insuffisance rénale aiguë, dans un contexte de traitement par telmisartan et de régime pauvre en sodium (cas clinique) ;
  - les inhibiteurs de la COX-2 sont associés à un risque cardiovasculaire accru, qui doit être pris en compte pour toute nouvelle indication.

Les mises en garde et contre-indications officielles ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ne soutient la migraine, la preuve se limite à une prédiction du modèle, à des données précliniques et à une revue indirecte (niveau L4). Les produits n'ont plus d'AMM valide en France, et les données de sécurité officielles sont absentes, ce qui bloque le passage à l'évaluation de sécurité.
- Le signal le plus solide concerne des phénotypes de céphalées spécifiques (céphalée poignardante, céphalée de toux, céphalées sensibles à l'indométacine), mais uniquement sous forme de cas cliniques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), ce qui constitue un point bloquant.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Élucider les raisons de l'annulation des 14 AMM, et vérifier si l'étoricoxib reste disponible par un autre circuit.
- Mener une revue systématique ou un essai randomisé ciblant la migraine ou les céphalées sensibles aux AINS.
- Établir un plan d'évaluation du risque cardiovasculaire, rénal (hyperkaliémie) et cérébrovasculaire avant toute évaluation clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

