---
layout: default
title: Dapsone
parent: Preuves élevées (L1-L2)
nav_order: 98
evidence_level: L1
indication_count: 1
---

# Dapsone
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **1** 
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

# Dapsone : Vers la Pneumocystose (usage déjà établi)

## Résumé en Une Phrase

La dapsone est une sulfone, connue dans la littérature comme médicament central de la lèpre et de la dermatite herpétiforme. Le modèle TxGNN prédit qu'elle pourrait être efficace contre la **pneumocystose** (pneumonie à *Pneumocystis jirovecii*). **14 essais cliniques** et **19 publications** sont associés à cette prédiction, dont 4 essais de Phase 3 terminés.

Il s'agit plutôt d'un usage déjà établi, absent de la liste d'indications source, que d'une véritable nouvelle piste de repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

Le texte de l'indication approuvée n'est pas renseigné dans les données de l'ANSM, donc l'indication originale n'est pas indiquée ici.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après la littérature fournie (Hughes, 1998, PMID 9675476), la dapsone bloque la synthèse de l'acide folique de *Pneumocystis* en inhibant la dihydroptéroate synthase (DHPS). Le même article décrit une forte activité anti-*Pneumocystis* in vitro, chez l'animal et dans les essais cliniques. La dapsone atteint aussi les liquides alvéolaires.

Le sulfaméthoxazole, composant du traitement de référence (triméthoprime-sulfaméthoxazole), cible la même enzyme. Le mécanisme est donc plausible, et le score TxGNN élevé concorde avec les essais cliniques disponibles.

La dapsone est déjà utilisée en prophylaxie et en traitement de la pneumocystose, notamment chez les patients intolérants au triméthoprime-sulfaméthoxazole. Ce rapport doit donc être lu comme la confirmation d'un usage établi, et non comme la découverte d'une nouvelle indication. Reste à vérifier si l'AMM française couvre formellement cette indication, car le texte de l'indication n'est pas disponible.

---

## Preuves d'Essais Cliniques

Sur les 14 essais recensés, 10 sont listés ici. Les 4 autres ne sont pas repris : le lien avec la dapsone n'est pas démontré, ou l'essai n'apporte aucune donnée (essai retiré). Les 4 essais de Phase 3 terminés, tous sur la pneumocystose, sont les plus solides.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Terminé | 290 | Dapsone/triméthoprime et clindamycine/primaquine comparées au triméthoprime-sulfaméthoxazole dans la pneumocystose légère à modérée (SIDA) |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Terminé | 400 | Pentamidine en aérosol mensuelle vs dapsone 3 fois par semaine en prophylaxie, chez des patients VIH intolérants au triméthoprime/sulfamides |
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Terminé | 700 | Dapsone quotidienne vs atovaquone quotidienne en prophylaxie, chez des patients VIH intolérants au triméthoprime/sulfamides |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Terminé | 600 | Trois régimes anti-*Pneumocystis* + zidovudine en prévention primaire ; le rôle de la dapsone ne peut pas être confirmé (titre tronqué) |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | Non applicable | Terminé | Non rapportée | Dapsone 100 mg vs 50 mg en prophylaxie primaire ; tolérance à long terme |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | Non applicable | Terminé | Non rapportée | Dapsone (+ triméthoprime) vs triméthoprime-sulfaméthoxazole dans le premier épisode de pneumocystose |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Terminé | 20 | Triméthrexate + leucovorine + dapsone vs triméthoprime-sulfaméthoxazole ; sécurité et pharmacocinétique (faisabilité, pas d'efficacité) |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Terminé | 96 | Dapsone quotidienne vs hebdomadaire en prophylaxie chez l'enfant infecté par le VIH ; toxicité et pharmacocinétique |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Statut inconnu | 3130 | Dépistage de l'allèle HLA-B*13:01 pour prévenir le syndrome d'hypersensibilité à la dapsone ; utile pour la sécurité, pas pour l'efficacité |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | Non applicable | Terminé | 168 | Étude cas-témoins des facteurs de risque de pneumocystose après greffe allogénique ; mentionne une incidence jusqu'à 7,2 % sous dapsone à faible dose |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Revue systématique / méta-analyse en réseau | Clin Microbiol Infect | Compare les schémas de prophylaxie chez les personnes vivant avec le VIH : triméthoprime-sulfaméthoxazole, schémas à base de dapsone, pentamidine en aérosol, atovaquone |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Revue systématique / méta-analyse en réseau | Clin Microbiol Infect | Compare les schémas de traitement de la pneumocystose chez les personnes vivant avec le VIH ; le triméthoprime-sulfaméthoxazole reste le traitement de référence |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Recommandations (ECIL-5) | J Antimicrob Chemother | Prophylaxie chez les patients d'hématologie et greffés de cellules souches non infectés par le VIH ; le triméthoprime-sulfaméthoxazole 2 à 3 fois par semaine est le premier choix |
| [39603840](https://pubmed.ncbi.nlm.nih.gov/39603840/) | 2025 | Publication sur la prophylaxie alternative | Transpl Infect Dis | Atovaquone et dapsone souvent utilisées comme alternatives chez les greffés d'organe solide, malgré des données limitées |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Revue | Clin Infect Dis | Forte activité anti-*Pneumocystis* de la dapsone ; inhibition de la DHPS ; bonne absorption (70-80 %) et bonne distribution alvéolaire |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Revue | Expert Opin Pharmacother | Revue de la prévention et du traitement de *P. jirovecii* chez les hôtes immunodéprimés |
| [7979291](https://pubmed.ncbi.nlm.nih.gov/7979291/) | 1994 | Pharmacocinétique / sécurité | Antimicrob Agents Chemother | Dapsone hebdomadaire avec ou sans pyriméthamine ; dose maximale tolérée de 200 mg/semaine chez les patients sous au moins 500 mg de zidovudine |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Rapport de cas (sécurité) | Ann Pharmacother | Méthémoglobinémie sous dapsone en prophylaxie de la pneumocystose |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Rapport de cas (sécurité) | Cureus | Hypoxie due à une méthémoglobinémie sous dapsone |
| [33280223](https://pubmed.ncbi.nlm.nih.gov/33280223/) | 2021 | Étude rétrospective (sécurité) | Pediatr Transplant | Méthémoglobinémie sous dapsone chez des enfants greffés rénaux, où le triméthoprime-sulfaméthoxazole est contre-indiqué |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 67654911 | DISULONE 100 mg/200 mg | Comprimé sécable |

Titulaire : SANOFI WINTHROP INDUSTRIE. Le texte de l'indication approuvée n'est pas disponible dans les données.

---

## Considérations de Sécurité

Aucune mise en garde, contre-indication ou interaction médicamenteuse n'est disponible dans les données de l'ANSM. Veuillez consulter la notice pour les informations de sécurité.

La littérature et les essais fournis signalent les points suivants :
- **Méthémoglobinémie et hypoxie** : effet indésirable connu, parfois grave (PMID 9606476, 32714715, 33280223).
- **Déficit en G6PD** : dépistage à prévoir avant l'utilisation (garde-fou du dossier).
- **Atteinte hépatique** : complications hépatiques décrites (PMID 31631707).
- **Photosensibilité** : cas rares décrits (PMID 18309716).
- **Syndrome d'hypersensibilité** : l'essai NCT02550080 étudie le dépistage de HLA-B*13:01, mais ses résultats ne sont pas disponibles.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Quatre essais de Phase 3 terminés sur la pneumocystose (prophylaxie et traitement) soutiennent l'usage de la dapsone, et des méta-analyses récentes la placent parmi les alternatives au triméthoprime-sulfaméthoxazole. Le profil de sécurité (méthémoglobinémie, G6PD) impose toutefois des garde-fous.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice ANSM (RCP) pour vérifier l'indication approuvée, les contre-indications et les interactions.
- Compléter les données sur le mécanisme d'action depuis DrugBank.
- Prévoir le dépistage du déficit en G6PD et la surveillance de la méthémoglobinémie et de l'oxygénation.
- Vérifier le contenu des essais dont le titre est tronqué (NCT00000991) et la population de l'essai NCT02550080.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

