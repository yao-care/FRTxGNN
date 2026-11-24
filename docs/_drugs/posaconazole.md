---
layout: default
title: Posaconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 617
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole : nouvelle indication prédite, Pneumocystose (pneumocystosis) (niveau de preuve L5). En France, AMM dans la BDPM : 12 (valides : 10)"
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

## Posaconazole: Pneumocystose (pneumocystosis)
{: .text-alpha }

## Résumé en Une Phrase

Le posaconazole est un antifongique triazolé, initialement utilisé pour traiter et prévenir plusieurs mycoses (aspergillose, candidose, histoplasmose, fusariose, sporotrichose, coccidioïdomycose, entre autres).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **pneumocystose**, mais **aucun essai clinique pertinent** ni aucune publication directement concernée ne soutient actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Pneumocystose (pneumocystosis) |
| Score de Prédiction TxGNN | 0.9977 |
| Niveau de Preuve | L5 (prédiction du modèle sans étude directe ; les données compilées indiquent L4) |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 12) |
| Nombre d'AMM | 12 (valides : 10) |
| Décision Recommandée | Hold |

*Note : le texte d'indication des AMM n'est pas renseigné.*

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Posaconazole (traduction non officielle) : « Le posaconazole est un agent antifongique azolé. […] Le posaconazole bloque la synthèse de l'ergostérol, un composant essentiel de la membrane cellulaire fongique, par inhibition de l'enzyme lanostérol 14α-déméthylase dépendante du cytochrome P-450, responsable de la conversion du lanostérol en ergostérol dans la membrane cellulaire fongique. Il en résulte une accumulation de précurseurs stéroliques méthylés et une déplétion en ergostérol au sein de la membrane cellulaire, ce qui affaiblit la structure et la fonction de la membrane cellulaire fongique. » Texte original en anglais : "Posaconazole is an azole antifungal agent. […] Posaconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84), version du 2026-02-13 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, le posaconazole est un triazole qui inhibe la lanostérol 14-alpha-déméthylase (CYP51) et bloque ainsi la synthèse de l'ergostérol, constituant essentiel de la membrane des champignons.

Le score très élevé du modèle (0,9977) semble refléter la proximité du posaconazole avec d'autres antifongiques et maladies fongiques dans le réseau de connaissances, plutôt qu'une réelle adéquation mécanistique. *Pneumocystis jirovecii* ne possède pratiquement pas d'ergostérol dans sa membrane (il utilise du cholestérol), de sorte que le mécanisme azolé n'est pas censé être efficace. Le traitement de référence reste l'association triméthoprime-sulfaméthoxazole.

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
| 69380042 | NOXAFIL 100 mg | Comprimé gastro-résistant | Non renseignée (AMM active) |
| 65644772 | NOXAFIL 300 mg | Solution à diluer pour perfusion | Non renseignée (AMM active) |
| 62076503 | NOXAFIL 40 mg/mL | Suspension buvable | Non renseignée (AMM active) |
| 63689562 | POSACONAZOLE ZENTIVA 100 mg | Comprimé gastro-résistant | Non renseignée (AMM active) |
| 62713448 | POSACONAZOLE FRESENIUS KABI 100 mg | Comprimé gastro-résistant | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées dans les données compilées. Parmi les principales :
  - **Majeures** : lopéramide, triamcinolone, budésonide.
  - **Modérées** : famotidine, ranitidine, cimétidine, oméprazole, rabéprazole, hydrocortisone, dexaméthasone, bétaméthasone, aprépitant, clarithromycine, saxagliptine, bisacodyl, acide picosulfurique, polyéthylène glycol.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle TxGNN (deep learning), qui peut refléter des similitudes apprises entre maladies proches, et non une preuve biologique. Aucun essai ni publication ne soutient directement le posaconazole dans la pneumocystose, et le mécanisme (absence d'ergostérol chez *Pneumocystis*) plaide contre son efficacité. Le médicament est commercialisé en France : 10 AMM valides sur 10.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action et justification mécanistique d'une activité contre *Pneumocystis*
- Études précliniques ou cliniques spécifiques au posaconazole dans la pneumocystose
- Mises en garde et contre-indications issues de la notice (ANSM), nécessaires avant toute évaluation de sécurité
- Clarification du statut réglementaire et de la disponibilité des formes (comprimé, suspension, perfusion)

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

