---
layout: default
title: Posaconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 617
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Posaconazole : nouvelle indication prédite, Pneumocystose (niveau de preuve L5). Indication d'origine : Mycoses invasives et superficielles (aspergillose, candidose…"
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Posaconazole : Des Mycoses Invasives à la Pneumocystose

## Résumé en Une Phrase

Le posaconazole est un antifongique triazolé, initialement utilisé pour traiter et prévenir plusieurs mycoses (aspergillose, candidose, histoplasmose, fusariose, sporotrichose, coccidioïdomycose, entre autres).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **pneumocystose**, mais **aucun essai clinique pertinent** ni aucune publication directement concernée ne soutient actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mycoses invasives et superficielles (aspergillose, candidose, histoplasmose, etc.) |
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 (prédiction du modèle sans étude directe ; les données compilées indiquent L4) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 10 (toutes annulées) |
| Décision Recommandée | Hold |

*Note : le texte d'indication des AMM n'est pas renseigné ; l'indication originale provient des liens d'indication du graphe de connaissances.*

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques générales, le posaconazole est un triazole qui inhibe la lanostérol 14-alpha-déméthylase (CYP51) et bloque ainsi la synthèse de l'ergostérol, constituant essentiel de la membrane des champignons.

Le score très élevé du modèle (99,77 %) semble refléter la proximité du posaconazole avec d'autres antifongiques et maladies fongiques dans le réseau de connaissances, plutôt qu'une réelle adéquation mécanistique. *Pneumocystis jirovecii* ne possède pratiquement pas d'ergostérol dans sa membrane (il utilise du cholestérol), de sorte que le mécanisme azolé n'est pas censé être efficace. Le traitement de référence reste l'association triméthoprime-sulfaméthoxazole.

La prédiction doit donc être considérée avec prudence : le lien mécanistique est faible, voire défavorable.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Terminé | 602 | Rezafungine IV versus schéma antimicrobien standard pour prévenir les infections fongiques invasives après greffe allogénique de moelle. Ne concerne pas le posaconazole et n'apporte aucune preuve directe pour la pneumocystose (pertinence faible). |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Revue | The Lancet Infectious Diseases | Recommandations de la société britannique de mycologie médicale sur le diagnostic des mycoses graves (mise à jour 2025). |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Revue (lignes directrices) | Zhonghua Jie He He Hu Xi Za Zhi | Lignes directrices chinoises sur le diagnostic et la prise en charge des mycoses pulmonaires invasives. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Revue | Swiss Medical Weekly | Vue d'ensemble des mycoses invasives courantes (candidose, aspergillose, cryptococcose, pneumocystose) ; mentionne la réduction des infections avec la prophylaxie par posaconazole chez les patients hémato-oncologiques. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revue | Clinical Pharmacokinetics | Pénétration des anti-infectieux dans le liquide épithélial pulmonaire, dont les antifongiques. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohorte | Transplant Infectious Disease | Complications infectieuses de la maladie du greffon contre l'hôte aiguë après greffe hépatique. |

Ces publications sont générales (diagnostic, lignes directrices, pharmacocinétique) et ne démontrent pas l'efficacité du posaconazole dans la pneumocystose.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69380042 | NOXAFIL 100 mg | Comprimé gastro-résistant | Non renseignée (AMM annulée) |
| 65644772 | NOXAFIL 300 mg | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 62076503 | NOXAFIL 40 mg/mL | Suspension buvable | Non renseignée (AMM annulée) |
| 63689562 | POSACONAZOLE ZENTIVA 100 mg | Comprimé gastro-résistant | Non renseignée (AMM annulée) |
| 62713448 | POSACONAZOLE FRESENIUS KABI 100 mg | Comprimé gastro-résistant | Non renseignée (AMM annulée) |

Au total, 10 AMM sont enregistrées, toutes annulées ; aucune n'est actuellement valide dans les données compilées.

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées dans les données compilées. Parmi les principales :
  - **Majeures** : lopéramide, triamcinolone, budésonide.
  - **Modérées** : famotidine, ranitidine, cimétidine, oméprazole, rabéprazole, hydrocortisone, dexaméthasone, bétaméthasone, aprépitant, clarithromycine, saxagliptine, bisacodyl, acide picosulfurique, polyéthylène glycol.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle. Aucun essai ni publication ne soutient directement le posaconazole dans la pneumocystose, et le mécanisme (absence d'ergostérol chez *Pneumocystis*) plaide contre son efficacité. Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action et justification mécanistique d'une activité contre *Pneumocystis*
- Études précliniques ou cliniques spécifiques au posaconazole dans la pneumocystose
- Mises en garde et contre-indications issues de la notice (ANSM), nécessaires avant toute évaluation de sécurité
- Clarification du statut réglementaire et de la disponibilité des formes (comprimé, suspension, perfusion)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

