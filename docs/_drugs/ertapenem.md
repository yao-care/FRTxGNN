---
layout: default
title: Ertapenem
parent: Prédiction du modèle uniquement (L5)
nav_order: 296
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "ertapenem"
predicted_indications: ["bacterial arthritis", "staphylococcus aureus infection"]
description: "Ertapenem : nouvelle indication prédite, Arthrite bactérienne (bacterial arthritis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Ertapenem
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Ertapenem: Arthrite bactérienne (bacterial arthritis)
{: .text-alpha }

## Résumé en Une Phrase

L'ertapénème est un antibiotique carbapénème à large spectre, initialement utilisé pour le traitement de la pneumonie bactérienne (dont la pneumonie streptococcique) et des infections à *Peptostreptococcus*.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**arthrite bactérienne**, mais aucun essai clinique n'est enregistré pour cette indication, et seules des publications de faible niveau (cas cliniques, cohortes, études in vitro) la soutiennent.
Une seconde prédiction, l'**infection à *Staphylococcus aureus***, est mieux étayée (2 essais cliniques en cours et de nombreuses publications), mais uniquement en association avec la céfazoline.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Arthrite bactérienne (bacterial arthritis) |
| Score de Prédiction TxGNN | 0.9972 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 6) |
| Nombre d'AMM | 6 (valides : 6) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'ertapénème est un carbapénème qui inhibe la synthèse de la paroi bactérienne en se liant aux protéines de liaison à la pénicilline (PLP). Son efficacité dans la pneumonie bactérienne et les infections à anaérobies a été établie.

Les infections ostéo-articulaires à entérobactéries sensibles et à anaérobies relèvent d'un spectre de pathogènes qui recoupe celui des indications d'origine. Le mécanisme est donc biologiquement plausible.

Il faut toutefois rester prudent : l'arthrite bactérienne est déjà une cible antibactérienne conventionnelle, et non une véritable opportunité de repositionnement. Le score très élevé du modèle (0,9972) est une prédiction computationnelle, non confirmée par des essais cliniques.

## Preuves d'Essais Cliniques

Aucun essai clinique associé à l'arthrite bactérienne n'est enregistré actuellement.

À titre indicatif, pour la deuxième indication prédite (infection à *S. aureus*), deux essais sont en cours :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | En recrutement | 60 | Céfazoline + ertapénème dans la bactériémie à SASM ; sous-étude de l'essai SNAP ; pas de résultats |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | Inclusion sur invitation | 300 | Double antibiothérapie précoce vs monothérapie dans la bactériémie à *S. aureus* ; pas de résultats ; non spécifique à l'ertapénème |

## Preuves de la Littérature

Publications relatives à l'arthrite bactérienne :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Cohorte rétrospective | Antimicrob Agents Chemother | Sécurité et efficacité de l'ertapénème ambulatoire prolongé chez 306 patients, dont des infections osseuses et articulaires |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohorte | J Antimicrob Chemother | Traitement suppressif sous-cutané par β-lactamine dans les infections ostéo-articulaires (10 patients) |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Cas clinique | J Chemother | Arthrite septique du poignet à *Klebsiella pneumoniae* traitée avec succès par ertapénème et lévofloxacine |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Cas clinique | BMJ Case Rep | Ostéomyélite et arthrite septique à *Citrobacter koseri* traitées par ertapénème |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Cas clinique et revue | Anaerobe | Arthrite septique à *Clostridium paraputrificum* de l'épaule |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Cas clinique et revue | J Investig Med High Impact Case Rep | Arthrite septique à *Prevotella bivia* |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro | Diagn Microbiol Infect Dis | L'auranofine restaure la sensibilité d'*E. coli* résistant aux carbapénèmes à l'ertapénème |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohorte | Clin Lab | Distribution des pathogènes et résistances dans les infections ostéo-articulaires du jeune enfant |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Cohorte / in vitro | J Antimicrob Chemother | Témocilline comme alternative aux carbapénèmes dans les infections ostéo-articulaires à entérobactéries résistantes aux C3G |

Aucun essai randomisé n'est disponible. Pour l'infection à *S. aureus*, la littérature (séries de cas, cohortes, données in vitro) soutient l'association céfazoline + ertapénème dans la bactériémie persistante à SASM (par ex. [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/), [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/)).

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69931556 | ERTAPENEM PANPHARMA 1 g | Poudre pour solution à diluer pour perfusion | Non disponible (AMM active) |
| 65077051 | INVANZ 1 g | Poudre pour solution à diluer pour perfusion | Non disponible (AMM active) |
| 68956656 | ERTAPENEM HIKMA 1 g | Poudre pour solution à diluer pour perfusion | Non disponible (AMM active) |
| 62637897 | ERTAPENEM SUN 1 g | Poudre pour solution à diluer pour perfusion | Non disponible (AMM active) |
| 66810994 | ERTAPENEM ARROW 1 g | Poudre pour solution à diluer pour perfusion | Non disponible (AMM active) |

Une sixième AMM (60926401, ERTAPENEM QILU 1 g) est également annulée.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : épilepsie, maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale.
- **Interactions médicamenteuses** : 38 interactions recensées.
  - Majeure : bupropion (risque convulsif à considérer).
  - Modérées : acide picosulfurique, polyéthylène glycol (3350 avec électrolytes), sulfate de sodium.
  - Niveau non précisé : notamment vancomycine, métronidazole, morphine, metformine, oméprazole, pantoprazole, doxycycline, prednisone, simvastatine, acide acétylsalicylique.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'arthrite bactérienne repose uniquement sur le modèle et sur des publications de faible niveau (cas cliniques, cohortes), sans aucun essai clinique. Il s'agit d'une indication antibactérienne conventionnelle plutôt que d'un vrai repositionnement. De plus, le médicament est commercialisé en France, avec 6 AMM valides sur 6.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications), actuellement manquante et bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Clarifier la raison de l'annulation des AMM et la disponibilité réelle de l'ertapénème en France
- Disposer d'études comparatives ou d'essais prospectifs dans les infections ostéo-articulaires
- Suivre les résultats des essais NCT04886284 et NCT07148960 : l'indication *S. aureus* (en association avec la céfazoline, niveau L3) constitue une piste de recherche plus solide à examiner séparément
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

