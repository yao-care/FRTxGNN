---
layout: default
title: Tolvaptan
parent: Prédiction du modèle uniquement (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan : Des Antagonistes du Récepteur V2 à la Polykystose Rénale de Type 3 (avec ou sans Atteinte Hépatique)

## Résumé en Une Phrase

Tolvaptan est un antagoniste sélectif du récepteur V2 de la vasopressine, dont l'indication d'origine n'est pas renseignée dans les données réglementaires françaises fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **polykystose rénale de type 3, avec ou sans polykystose hépatique**.
Aucun essai clinique n'est enregistré, mais **20 publications** soutiennent cette direction, dont 2 essais randomisés de phase 3 menés dans la PKAD (polykystose rénale autosomique dominante).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (texte d'indication vide) |
| Nouvelle Indication Prédite | Polykystose rénale de type 3, avec ou sans polykystose hépatique |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L1 (preuves indirectes : essais menés dans la PKAD, non spécifiques du génotype) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 17 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Tolvaptan bloque le récepteur V2 de la vasopressine. Cela réduit la signalisation par l'AMPc dans les cellules du tube collecteur rénal. Or l'AMPc favorise la sécrétion de liquide dans les kystes et leur croissance dans la PKAD. Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le champ dédié du pack. Ce raisonnement provient de l'analyse de rationalité du dossier.

La PKD3 (liée à GANAB) partage le phénotype kystique de la PKAD. Les essais de phase 3 TEMPO 3:4 (PMID 23121377) et REPRISE (PMID 29105594) ont été réalisés dans des populations PKAD, sans stratification selon le génotype GANAB. L'applicabilité à la PKD3 repose donc sur le phénotype et la voie biologique, et non sur des données spécifiques du génotype.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | ECR | N Engl J Med | Essai de tolvaptan dans la PKAD (TEMPO 3:4), motivé par des données précliniques montrant que les antagonistes V2 freinent la croissance des kystes |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | ECR | N Engl J Med | Essai dans la PKAD de stade avancé (REPRISE) ; l'essai précédent avait montré un ralentissement de la croissance du volume rénal total et du déclin du DFGe, avec davantage d'élévations des transaminases et de la bilirubine |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Méta-analyse | Nefrologia | Évaluation systématique de l'efficacité et de la sécurité du tolvaptan dans la PKAD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Revue systématique | Cochrane Database Syst Rev | Interventions pour prévenir la progression de la PKAD, dont les agents modifiant la maladie |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | ECR (analyse rétrospective) | Pediatr Nephrol | Estimation du risque de progression rapide chez l'enfant PKAD dans l'essai pédiatrique de tolvaptan (NCT02964273) |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus | Nephrol Dial Transplant | Mise à jour ERA/ERKNet/PKD International sur l'usage du tolvaptan dans la PKAD, fondée sur l'essai TEMPO 3:4 |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Recommandations | J Hepatol | Recommandations EASL sur la prise en charge des maladies kystiques du foie, dont la polykystose hépatique |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Revue | Clin Liver Dis | Maladie polykystique rénale/hépatique ; le tolvaptan peut ralentir la dégradation de la fonction rénale dans la PKAD |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Revue | JAMA | Revue générale de la PKAD, trouble rénal héréditaire le plus fréquent |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Revue | Curr Opin Nephrol Hypertens | Thérapies au-delà du tolvaptan, seul traitement de fond de la PKAD approuvé par la FDA |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 60108831 | TOLVAPTAN SANDOZ 15 mg + 45 mg | Comprimé |
| 64599993 | TOLVAPTAN TEVA 30 mg + 60 mg | Comprimé |
| 66056341 | JINARC 30 mg | Comprimé |
| 68174566 | JINARC 30 mg + 60 mg | Comprimé |
| 68053529 | TOLVAPTAN SANDOZ 30 mg + 90 mg | Comprimé |

## Considérations de Sécurité

- **Hépatotoxicité** : risque d'atteinte hépatique nécessitant une surveillance de type REMS. Dans l'essai de phase 3 cité (PMID 29105594), des élévations des transaminases et de la bilirubine ont été observées. La prudence est particulière en présence d'une composante hépatique polykystique.
- **Effets liés à l'aquarèse** : soif, polyurie et autres effets indésirables associés à l'effet aquarétique.
- **Limites d'éligibilité** : seuils de DFGe à respecter.

Pour les mises en garde, contre-indications et interactions médicamenteuses détaillées, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Deux essais randomisés de phase 3 (TEMPO 3:4 et REPRISE) soutiennent le mécanisme dans la PKAD, dont le phénotype kystique est partagé avec la PKD3. Aucune donnée spécifique du génotype GANAB n'existe et aucun essai n'est enregistré ; le risque hépatique impose un cadre de surveillance strict.
- Les 9 autres indications prédites (rangs 2 à 10) ont un niveau de preuve L4 ou L5 et sont en attente (Hold) ou question de recherche. Elles ne sont pas retenues à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM pour extraire mises en garde et contre-indications (lacune bloquante pour le criblage de sécurité)
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Rechercher des données cliniques spécifiques du génotype GANAB (PKD3)
- Définir un plan de surveillance hépatique et rénale, en particulier en cas d'atteinte hépatique polykystique
- Vérifier les indications approuvées dans les AMM, dont le texte est vide dans les données fournies
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

