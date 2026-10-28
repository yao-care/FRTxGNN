---
layout: default
title: Daptomycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 215
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Daptomycin : nouvelle indication prédite, Arthrose (osteoarthritis) (niveau de preuve L4). Indication d'origine : Non renseignée dans les données d'AMM compilées (les textes d'indicat…"
monitor_inn: "daptomycin"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "gout", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Daptomycin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Daptomycine : De l'infection bactérienne à Gram positif à l'arthrose (prédiction peu étayée)
{: .text-alpha }

## Résumé en Une Phrase

La daptomycine est un antibiotique lipopeptidique cyclique administré par voie intraveineuse, utilisé contre les infections à bactéries Gram positif (infections cutanées, bactériémies, endocardites droites). Le modèle TxGNN la prédit comme potentiellement efficace pour l'**arthrose** (score élevé), mais **aucun essai clinique** n'est enregistré et la littérature disponible concerne des infections ostéo-articulaires bactériennes, et non l'arthrose dégénérative. Cette prédiction repose donc essentiellement sur le modèle seul.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées (les textes d'indication sont vides) |
| Nouvelle Indication Prédite | Arthrose (osteoarthritis) |
| Score de Prédiction TxGNN | 0,9986 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la daptomycine est un lipopeptide cyclique dont l'activité antibactérienne vise les bactéries Gram positif (action sur la membrane bactérienne). Son efficacité est établie dans les infections cutanées, les bactériémies et les endocardites droites, mais elle n'a pas de mécanisme connu sur l'arthrose dégénérative.

L'examen des données montre que le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Les publications retrouvées portent sur des infections de prothèses articulaires, des arthrites septiques et des ostéomyélites à Gram positif : il s'agit d'un usage antibactérien, non d'un traitement de l'arthrose.

Parmi les autres prédictions, la **polyarthrite rhumatoïde** (2e rang, score 0,9984) présente un signal plus intéressant : une étude préclinique de 2025 (PMID 39571268) rapporte que la daptomycine atténue l'arthrite induite par le collagène chez l'animal, via la suppression des cytokines inflammatoires et de la voie NF-κB. Cela reste une hypothèse, sans donnée humaine. Les autres prédictions (goutte, dysplasies squelettiques, brachyolmie, etc.) ne reposent sur aucune base mécanistique plausible ; pour la goutte, la seule publication décrit un effet indésirable (rhabdomyolyse induite par la daptomycine compliquée d'une crise de goutte).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Publications relatives à l'arthrose (aucune ne démontre un effet sur l'arthrose dégénérative) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohorte | International Orthopaedics | Sécurité et efficacité de la daptomycine à forte dose avec rifampicine dans les infections ostéo-articulaires à Gram positif |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohorte | J Antimicrob Chemother | Évolution des infections ostéo-articulaires associées à une bactériémie à *S. aureus* : daptomycine vs traitement standard |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohorte | J Antimicrob Chemother | Expérience clinique de la daptomycine dans les infections de prothèses de hanche et de genou |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohorte | Int J Antimicrob Agents | Daptomycine à forte dose (>6 mg/kg) dans les infections osseuses et articulaires complexes |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Cohorte | Medicina Clínica | Données espagnoles du registre EU-CORE sur l'usage de la daptomycine |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | Sensibilité de *S. aureus* et *S. epidermidis* isolés d'infections de prothèses articulaires |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Enquête | Int J Antimicrob Agents | Pratiques de prise en charge des infections de prothèses articulaires |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohorte | Surg Infect | Profil microbiologique des staphylocoques dans les infections ostéo-articulaires |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Cas clinique | Case Rep Orthop | Arthrite septique chronique à *Corynebacterium striatum* chez un patient arthrosique |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Cas clinique | ASM Case Reports | Arthrite septique à *Corynebacterium propinquum* sur articulation native |

Publication préclinique la plus pertinente, pour la polyarthrite rhumatoïde :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/) | 2025 | Préclinique (modèle animal) | Int Immunopharmacol | La daptomycine atténue l'arthrite induite par le collagène en réduisant les cytokines inflammatoires et la voie NF-κB |
| [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/) | 2025 | Préclinique (animal/in vitro) | J Med Chem | Nouveaux lipopeptides cycliques dérivés de la daptomycine, actifs contre l'inflammation cellulaire et l'arthrite chez la souris |

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes **annulées** ; le texte d'indication approuvée n'est pas renseigné. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66921973 | Daptomycine Medac 500 mg | Poudre pour solution injectable ou pour perfusion | Non renseignée |
| 69064891 | Daptomycine Accordpharma 350 mg | Poudre pour solution injectable ou pour perfusion | Non renseignée |
| 65858420 | Daptomycine Accordpharma 500 mg | Poudre pour solution injectable ou pour perfusion | Non renseignée |
| 65568538 | Daptomycine Hikma Pharma 350 mg | Poudre pour solution injectable ou pour perfusion | Non renseignée |
| 69024555 | Daptomycine Medac 350 mg | Poudre pour solution injectable ou pour perfusion | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe TxGNN/PrimeKG, et non le texte de la notice) : myopathie, maladie musculaire, maladie du muscle squelettique, paralysie périodique familiale, maladies diarrhéiques, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, pneumonie à éosinophiles, éosinophilie pulmonaire, neuropathie périphérique, maladie du système nerveux périphérique.
- **Signal de sécurité musculaire** : élévation des CPK et myopathie, avec un cas publié de rhabdomyolyse induite par la daptomycine compliquée d'une crise de goutte (PMID 36693494). Ce point est particulièrement limitant pour un usage chronique.
- **Interactions médicamenteuses** (12 interactions recensées) :
  - Modérées : acide picosulfurique, rosuvastatine, simvastatine, iobenguane (I-131), ibuprofène, diclofénac, éthinylestradiol, célécoxib, ciclosporine, acide mycophénolique.
  - Mineures : dicoumarol, warfarine.
  - Les interactions avec les statines sont à souligner en raison du risque musculaire cumulé ; les AINS et les antiarthrosiques courants figurent aussi parmi les médicaments concernés.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être obtenues : veuillez consulter la notice pour les informations de securité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour l'arthrose, le score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises entre maladies apparentées, et non une preuve biologique ; il n'existe ni essai clinique ni preuve de bénéfice. De plus, la daptomycine est un antibiotique intraveineux dont le profil de risque musculaire est peu compatible avec un traitement chronique.
- La polyarthrite rhumatoïde constitue une piste plus plausible (« question de recherche »), mais uniquement préclinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice (mises en garde et contre-indications) auprès de l'ANSM, ainsi que des indications approuvées, absentes des données compilées
- Données détaillées sur le mécanisme d'action (MOA)
- Pour la polyarthrite rhumatoïde : confirmation de l'effet anti-inflammatoire dans d'autres modèles précliniques, évaluation de la faisabilité (voie IV, durée de traitement) et de la sécurité musculaire
- Clarification du statut commercial en France (médicament commercialisé, 20 AMM valides)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

