---
layout: default
title: Paclitaxel
parent: Preuves élevées (L1-L2)
nav_order: 570
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Paclitaxel : nouvelle indication prédite, Carcinome du sein féminin (niveau de preuve L1). Indication d'origine : Cancer de l'ovaire"
monitor_inn: "PACLITAXEL"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Paclitaxel
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

## Paclitaxel : Du Cancer de l'Ovaire au Carcinome du Sein Féminin
{: .text-alpha }

## Résumé en Une Phrase

Le paclitaxel est un agent cytotoxique de la famille des taxanes, initialement utilisé pour le traitement du cancer de l'ovaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome du sein féminin**, avec **41 essais cliniques** et **20 publications** recensés dans les données compilées pour cette indication. Il s'agit en pratique d'un usage déjà établi plutôt que d'un repositionnement au sens strict.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer de l'ovaire (le texte d'indication des AMM françaises n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Carcinome du sein féminin |
| Score de Prédiction TxGNN | 99,995 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 12 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, le paclitaxel fait partie de la classe des taxanes. Il stabilise les microtubules et empêche le désassemblage du fuseau mitotique, ce qui provoque un arrêt du cycle cellulaire en phase G2/M puis l'apoptose des cellules à division rapide.

Ce mécanisme antimitotique ne dépend ni du type d'organe ni du statut des récepteurs hormonaux. Le cancer de l'ovaire, indication d'origine, et le cancer du sein sont tous deux des tumeurs solides sensibles à ce type de cytotoxique, ce qui rend la prédiction du modèle cohérente.

Les données indiquent que le paclitaxel est déjà un taxane de référence dans le cancer du sein. La prédiction correspond donc à un usage établi, et non à une découverte nouvelle.

---

## Preuves d'Essais Cliniques

Parmi les 41 essais recensés, les plus pertinents sont listés ci-dessous (notés pertinents par l'analyse de pertinence ou à portée directe).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Terminé | 652 | Chimiothérapie à base de taxane avec lapatinib ou trastuzumab en première ligne dans le cancer du sein métastatique HER2+ |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Terminé | Non rapporté | Gemcitabine + paclitaxel versus paclitaxel dans le cancer du sein localement récidivant ou métastatique |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Terminé | 455 | Neo-ALTTO : lapatinib et/ou trastuzumab + paclitaxel en néoadjuvant (HER2+) |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | Terminé | 632 | ETNA : nab-paclitaxel versus paclitaxel en néoadjuvant (HER2-négatif, haut risque) |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Terminé | 280 | Comparaison de séquences FEC-75 / paclitaxel + trastuzumab en néoadjuvant (HER2+) |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Terminé | 478 | Docétaxel versus paclitaxel après FE75C dense en adjuvant (ganglions positifs) |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | Terminé | 580 | Lapatinib + paclitaxel versus paclitaxel seul en première ligne métastatique |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Arrêté | 63 | Paclitaxel + trastuzumab + lapatinib versus placebo (HER2+ métastatique) |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | Terminé | 50 | Paclitaxel hebdomadaire 1 heure + trastuzumab dans le cancer du sein métastatique |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | Inconnu | Non rapporté | Comparaison randomisée de schémas docétaxel ou paclitaxel dans le cancer du sein métastatique |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Essai clinique de phase II | Cancer | Efficacité et toxicité de l'association doxorubicine + paclitaxel dans le cancer du sein métastatique |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Étude clinique | Cancer | Rôle du paclitaxel dans la prise en charge multimodale du cancer du sein inflammatoire |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Revue | Lancet | Les taxanes (paclitaxel, docétaxel) sont des composants reconnus du traitement des cancers du sein, du poumon et de l'ovaire avancés ; approbation aux États-Unis en adjuvant (ganglions positifs) |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revue | Drug Ther Bull | Paclitaxel et docétaxel dans les cancers du sein et de l'ovaire |
| [7904376](https://pubmed.ncbi.nlm.nih.gov/7904376/) | 1993 | Revue | Semin Oncol Nurs | Historique de développement du paclitaxel |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Étude computationnelle | Chem Biol Drug Des | Potentiel des associations de paclitaxel dans le carcinome mammaire et biomarqueurs in vivo |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Étude génomique | Nat Commun | Variations de TEKT4 associées à la résistance du cancer du sein au paclitaxel |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Préclinique (in vitro) | J Cell Physiol | ZD6474 renforce les effets antiprolifératifs et apoptotiques du paclitaxel sur cellules de carcinome mammaire |

---

## Informations de Marché en France

Les 12 AMM recensées sont toutes **annulées** ; aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas renseigné dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61516960 | APEXELSIN 5 mg/mL | Poudre pour dispersion pour perfusion | Non renseignée |
| 68739019 | ABRAXANE 5 mg/mL | Poudre pour dispersion injectable pour perfusion | Non renseignée |
| 67297982 | PACLITAXEL VIATRIS 6 mg/mL | Solution à diluer pour perfusion | Non renseignée |
| 64711759 | PACLITAXEL TEVA 6 mg/mL | Solution à diluer pour perfusion | Non renseignée |
| 69161632 | PACLITAXEL SANDOZ 6 mg/mL | Solution à diluer pour perfusion | Non renseignée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (classe des taxanes, poison du fuseau mitotique) |
| Risque de Myélosuppression | Élevé (neutropénie fréquente ; les données de contre-indications du graphe de connaissances mentionnent neutropénie, thrombopénie et anémie) |
| Classification d'Émétogénicité | Faible à moyenne |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale, surveillance de la neuropathie périphérique et des réactions d'hypersensibilité |
| Protection de Manipulation | Doit suivre la réglementation de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (non issues de la notice) : neutropénie, agranulocytose, thrombopénie, anémie, maladie hépatique, maladie rénale, neuropathie périphérique, infarctus du myocarde, arrêt cardiaque soudain, asthme, diabète, hypotension, hyperbilirubinémie (dont syndrome de Gilbert), psoriasis, troubles anxieux.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Modérées : aprépitant, cimétidine, clarithromycine, clotrimazole, dexaméthasone, éliglustat, métronidazole, miconazole, rolapitant, rosuvastatine, simvastatine, tinidazole, troglitazone.
  - Mineures : acide ascorbique, lévofloxacine.
  - Niveau inconnu : glimépiride, doxycycline, morphine, metformine, oméprazole.
- **Signalements de la littérature** : cas d'uvéite, de pneumopathie interstitielle, de lésions cornéennes, d'érythème thénarien avec onycholyse et de neuropathie induite par les taxanes.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Autres Indications Prédites (Pour Information)

| Indication prédite | Score TxGNN | Niveau de preuve | Recommandation |
|------|------|------|------|
| Cancer du sein ER-négatif | 99,91 % | L1 | Proceed with Guardrails |
| Carcinome mammaire hormono-résistant | 99,91 % | L2 | Proceed with Guardrails |
| Cancer du sein ER-positif | 99,91 % | L1 | Proceed with Guardrails |
| Carcinome d'Ehrlich (modèle murin) | 99,91 % | L4 | Hold |
| Carcinome mammaire bilatéral | 99,89 % | L4 | Hold |
| Carcinome mammaire selon profil d'expression génique | 99,89 % | L3 | Research Question |
| Carcinome du mamelon | 99,89 % | L4 | Hold |
| Rhabdomyosarcome embryonnaire paraméningé | 99,73 % | L5 | Hold |
| Rhabdomyosarcome embryonnaire botryoïde du vagin | 99,73 % | L5 | Hold |

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 terminés (par exemple NCT00667251, NCT00006459, NCT00553358, NCT01822314) et de nombreuses études de phase 2 soutiennent le paclitaxel dans le cancer du sein, ce qui correspond à un niveau de preuve L1. Toutefois, il s'agit d'un usage déjà établi, et les 12 AMM françaises sont toutes annulées, ce qui impose des garde-fous réglementaires.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérifier la situation réglementaire actuelle en France (raisons de l'annulation des AMM, éventuelles autorisations par d'autres procédures) et récupérer les indications approuvées.
- Obtenir les mises en garde et contre-indications de la notice (ANSM), actuellement manquantes et bloquantes pour le criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Définir un plan de surveillance hématologique, neurologique et d'hypersensibilité, ainsi qu'un examen des interactions médicamenteuses.
- Pour les indications à faible niveau de preuve (carcinome du mamelon, carcinome bilatéral, rhabdomyosarcomes), ne pas avancer sans données cliniques supplémentaires.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

