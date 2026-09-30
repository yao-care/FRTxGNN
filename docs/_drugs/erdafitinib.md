---
layout: default
title: Erdafitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 122
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Erdafitinib : De l'indication d'origine (non renseignée) à l'hypertension pulmonaire

## Résumé en Une Phrase

Erdafitinib est un inhibiteur de tyrosine kinase pan-FGFR (FGFR1 à 4), commercialisé en France sous le nom BALVERSA. Les données fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension pulmonaire**, mais **aucun essai clinique** ni **aucune publication spécifique** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM fournies |
| Nouvelle Indication Prédite | Hypertension pulmonaire |
| Score de Prédiction TxGNN | 99,38 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, erdafitinib est un inhibiteur pan-FGFR. La voie FGF/FGFR est impliquée dans la prolifération et le remodelage de nombreux tissus.

Pour l'hypertension pulmonaire, des travaux précliniques relient la signalisation FGFR1 à la prolifération des cellules musculaires lisses des artères pulmonaires et au remodelage vasculaire. L'hypothèse est plausible mais non validée. La voie FGF/FGFR a aussi été décrite comme protectrice dans certains contextes vasculaires, si bien que le sens de l'effet reste incertain. Le score TxGNN (0,994) est une simple prédiction, sans appui clinique.

Les autres indications prédites sont plus faibles :
- **Polyarthrite rhumatoïde** (99,25 %) : rationnel faible, par analogie de classe (les inhibiteurs de kinases sont une classe établie dans cette maladie).
- **Aménorrhée** (99,26 %) : l'inhibition de FGFR pourrait aggraver le dysfonctionnement de l'axe reproductif.
- **Sclérose latérale amyotrophique** (99,06 %) : la signalisation FGF est plutôt neuroprotectrice, donc l'inhibition pourrait être contre-productive.
- **Cardiopathie cyphoscoliotique** (99,27 %) et **syndrome de brachydactylie-syndactylie** (99,03 %) : aucun lien mécanistique clair, et une kinase inhibitrice postnatale est peu susceptible de corriger une malformation congénitale.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Revue | Pharmacological Research | Mise à jour sur les propriétés des inhibiteurs de protéine kinase approuvés par la FDA, dont erdafitinib. Aucune donnée spécifique sur l'hypertension pulmonaire. |

Cette publication est liée à la polyarthrite rhumatoïde, non à l'hypertension pulmonaire. Il s'agit d'une revue générale sans donnée spécifique à erdafitinib dans cette maladie, elle n'est donc pas comptée comme preuve clinique indirecte.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66039107 | BALVERSA 3 mg, comprimés pelliculés | Comprimé pelliculé | Non renseignée |
| 65760218 | BALVERSA 4 mg, comprimés pelliculés | Comprimé pelliculé | Non renseignée |
| 60039171 | BALVERSA 5 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |

Titulaire des trois AMM : JANSSEN CILAG INTERNATIONAL NV.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase pan-FGFR) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice |
| Protection de Manipulation | Veuillez consulter la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune mise en garde, contre-indication ni interaction médicamenteuse n'est disponible dans le dossier.

À titre indicatif, l'analyse de la polyarthrite rhumatoïde mentionne l'hyperphosphatémie et les toxicités oculaires et unguéales. La toxicité osseuse et unguéale est également citée pour les indications de développement. Ces éléments sont à évaluer avec prudence dans un contexte de traitement chronique.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5). Aucun essai ni publication ne la soutient, et le sens de l'effet de l'inhibition de FGFR sur l'hypertension pulmonaire est incertain. Les données de sécurité de la notice ANSM manquent, ce qui bloque le passage à l'étape de sécurité (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), à télécharger et analyser
- Données détaillées sur le mécanisme d'action (MOA), par exemple via l'API DrugBank
- Indication d'origine issue des AMM, actuellement non renseignée
- Études précliniques sur FGFR1 et le remodelage vasculaire pulmonaire, pour trancher le sens de l'effet
- Compatibilité de voie d'administration et similarité avec l'indication d'origine, actuellement en attente

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

