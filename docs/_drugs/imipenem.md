---
layout: default
title: Imipenem
parent: Prédiction du modèle uniquement (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imipenem : nouvelle indication prédite, Sclérodermie diffuse (niveau de preuve L5). Indication d'origine : Non disponible dans les données d'AMM (texte d'indication vide)"
monitor_inn: "imipenem"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
---

# Imipenem
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Imipenem : Des infections bactériennes graves à la sclérodermie diffuse
{: .text-alpha }

## Résumé en Une Phrase

L'imipénem (associé à la cilastatine) est un antibiotique de la famille des carbapénèmes, utilisé à l'origine contre des infections bactériennes graves : pneumonie bactérienne, péritonite, endocardite, arthrite bactérienne et endométrite.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **sclérodermie diffuse** (score le plus élevé), mais **aucun essai clinique ni aucune publication** ne soutient cette prédiction ; elle repose uniquement sur le modèle.
Parmi les dix indications prédites, les pistes les mieux documentées sont de nature infectieuse (fièvre typhoïde, salmonellose, infection à *Staphylococcus aureus*), mais les preuves restent indirectes.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans les données d'AMM (texte d'indication vide) ; les indications d'origine du graphe de connaissances sont les infections bactériennes (pneumonie, péritonite, endocardite, arthrite bactérienne, endométrite) |
| Nouvelle Indication Prédite | Sclérodermie diffuse |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 9 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'imipénem est un carbapénème à large spectre : il inhibe les protéines de liaison aux pénicillines des bactéries et résiste à de nombreuses bêta-lactamases. Son efficacité est établie dans les infections bactériennes graves, mais il n'a pas de mécanisme antifibrosant ou immunomodulateur connu.

Pour la sclérodermie diffuse, le score très élevé du modèle ressemble donc à un **artefact du réseau de connaissances** plutôt qu'à une piste biologiquement plausible. Il ne faut pas le considérer comme un signal thérapeutique.

Les autres prédictions sont plus cohérentes avec le profil antibactérien du médicament :
- **Fièvre typhoïde, fièvre paratyphoïde, salmonellose** : plausibles, car les carbapénèmes sont une option reconnue contre les souches de *Salmonella* résistantes (XDR). Les données disponibles se limitent toutefois à des études de sensibilité et à un cas clinique.
- **Infection à *S. aureus*** : l'imipénème seul n'est pas actif contre le SARM ; seule une utilisation en association (synergie) est envisageable.
- **Sinusites et rhinosinusite chronique** : l'imipénème est un agent parentéral réservé aux infections graves, peu adapté à ces indications courantes.
- **Néoplasme des sinus paranasaux, syndrome éosinophilie-myalgie** : aucun lien mécanistique plausible.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré pour la sclérodermie diffuse.

À titre indicatif, deux essais de phase 4 existent pour une autre indication prédite (infection à *Staphylococcus aureus*) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Phase 4 | Terminé | 50 | Fosfomycine + imipénème versus vancomycine dans l'endocardite infectieuse à SARM ; aucun résultat fourni |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Inconnu | 60 | Linézolide seul ou associé à un carbapénème contre le SARM dans la pneumonie sous ventilation ; le carbapénème n'est pas précisé comme étant l'imipénème |

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour la sclérodermie diffuse.

À titre indicatif, pour la fièvre typhoïde (indication prédite n° 6) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | Étude clinique | Cureus | Place des carbapénèmes comme dernier recours dans la typhoïde MDR/XDR à Peshawar |
| [36277244](https://pubmed.ncbi.nlm.nih.gov/36277244/) | 2022 | Observationnelle | Infect Drug Resist | Monothérapie versus association dans la typhoïde XDR au Pakistan |
| [19208884](https://pubmed.ncbi.nlm.nih.gov/19208884/) | 2009 | In vitro | J Med Microbiol | CMI des carbapénèmes (dont l'imipénème) contre 210 souches de *Salmonella* |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Cas clinique | J Med Liban | Rhabdomyolyse et infection à *S. typhi* traitées avec succès par imipénème/cilastatine et hémodialyse |
| [40212028](https://pubmed.ncbi.nlm.nih.gov/40212028/) | 2025 | Cohorte | Open Forum Infect Dis | Tendances de la typhoïde et émergence de souches XDR au Pakistan |

Ces travaux constituent des preuves indirectes (surveillance de la résistance, cas isolés) et ne démontrent pas l'efficacité clinique de l'imipénème.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69426034 | Imipenem Cilastatine Viatris 500 mg/500 mg | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 64326051 | Imipenem/Cilastatine Tamrisa 500 mg/500 mg | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 62866789 | Imipenem/Cilastatine Arrow 500 mg/500 mg | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 65336568 | Imipenem Cilastatine Panpharma 500 mg/500 mg | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 65465495 | Imipenem/Cilastatine Sun 500 mg/500 mg | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |

Au total, 9 AMM sont recensées, toutes annulées (dont Recarbrio, association avec le relébactam). Aucune AMM valide n'est actuellement répertoriée.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : épilepsie, maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale.
- **Interactions médicamenteuses** : 15 interactions recensées.
  - **Majeures** : bupropion, iohexol, iopamidol.
  - **Modérées** : théophylline, aminophylline, dyphylline, oxtriphylline, warfarine, dicoumarol, ciclosporine, acide mycophénolique, pémétrexed, éthinylestradiol, lindane, polyéthylène glycol (3350 avec électrolytes).

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être consultées ; veuillez vous référer à la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (sclérodermie diffuse) repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, et sans mécanisme plausible. Toutes les AMM françaises sont annulées. Les pistes infectieuses (typhoïde, salmonellose, infection à *S. aureus* en association) sont plus crédibles mais restent au stade de questions de recherche (L3 à L4).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action et sur les mises en garde et contre-indications officielles de la notice (ANSM)
- Pour la sclérodermie diffuse : preuves précliniques démontrant un effet antifibrosant ou immunomodulateur, sinon abandon de cette piste
- Pour les infections à *Salmonella* résistantes : études cliniques comparatives spécifiques à l'imipénème, face au méropénème et à l'azithromycine
- Pour l'infection à SARM : publication des résultats de l'essai NCT00871104
- Clarification du statut réglementaire en France (AMM annulées) et de la disponibilité réelle du produit
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

