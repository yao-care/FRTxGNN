---
layout: default
title: Zuclopenthixol
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 9
---

# Zuclopenthixol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Zuclopenthixol : De la Schizophrénie à la Dystrophie Rétinienne avec ou sans Anomalies Extraoculaires

## Résumé en Une Phrase

Zuclopenthixol est un antipsychotique de première génération (classe thioxanthène), traditionnellement utilisé dans le traitement de la schizophrénie via un antagonisme des récepteurs dopaminergiques D1/D2 et adrénergiques α1. Le modèle TxGNN prédit qu'il pourrait être pertinent pour la **Dystrophie rétinienne avec ou sans anomalies extraoculaires**, mais **aucun essai clinique** et **aucune publication spécifiquement liée au médicament** ne soutiennent actuellement cette direction — les 15 références PubMed retrouvées concernent la pathologie oculaire en général, sans mention de zuclopenthixol.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Schizophrénie (trouble psychotique) — non documentée formellement dans ce pack de données, mentionnée uniquement dans l'analyse de mécanisme |
| Nouvelle Indication Prédite | Dystrophie rétinienne avec ou sans anomalies extraoculaires |
| Score de Prédiction TxGNN | 99.99% |
| Niveau de Preuve | L5 |
| Statut de Marché | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action officiel (MOA) ne sont pas disponibles dans ce pack de données (data gap classé « High »). Sur la base des informations connues rapportées dans l'analyse du candidat, le zuclopenthixol est un antipsychotique conventionnel de la classe thioxanthène, agissant par antagonisme des récepteurs dopaminergiques D1/D2 et adrénergiques α1, une efficacité établie dans la schizophrénie.

La dystrophie rétinienne avec ou sans anomalies extraoculaires est une pathologie ophtalmologique d'origine développementale/génétique (gènes de structure des photorécepteurs, protéines ciliaires, etc.). L'analyse fournie avec ce candidat indique explicitement l'absence de lien biologique connu entre l'antagonisme dopaminergique et ces mécanismes de dystrophie rétinienne héréditaire : aucune passerelle mécanistique plausible n'a pu être établie.

En conséquence, le score TxGNN élevé (99,99 %) ne s'accompagne d'aucune preuve mécanistique, clinique ou bibliographique directe. Ce cas illustre une prédiction de type L5 : signal du modèle seul, non corroboré par des données réelles.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

*Note : les publications ci-dessous ont été retrouvées via une recherche PubMed sur la pathologie cible ; aucune ne mentionne le zuclopenthixol spécifiquement.*

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Revue | Semin Ultrasound CT MR | Infections orbitaires, principalement d'origine sinusienne, avec atteinte de la motilité extraoculaire |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Revue | Seminars in Neurology | Approche clinique systématique de la diplopie d'origine oculaire, neurologique ou musculaire |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revue | Pediatric Radiology | Classification des pathologies oculaires congénitales pédiatriques et signes d'imagerie clés |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revue | Taiwan J Ophthalmol | Anomalies congénitales de forme du cristallin et associations avec la dysgénésie du segment antérieur |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Revue | Klin Monbl Augenheilkd | Ptosis congénital simple vs. compliqué, avec fibrose des muscles extraoculaires associée |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Rapport de cas | Am J Ophthalmol | Deux cas de cryptophtalmie unilatérale avec absence de muscles extraoculaires |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Revue | Doc Ophthalmol | Syndrome de Wagner-Stickler : dégénérescence vitréo-rétinienne et manifestations extraoculaires |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Étude de cohorte | Int J Mol Sci | Anomalies de la tête du nerf optique et de la rétine associées à la fibrose congénitale des muscles extraoculaires (CFEOM) |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Revue | J Binocul Vis Ocul Motil | Ophtalmoplégie et troubles congénitaux de dysinnervation crânienne (CCDD) |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Revue | Am J Ophthalmol | Pathogenèse et traitement de la maculopathie associée aux anomalies cavitaires du disque optique |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Malgré un score TxGNN très élevé, aucun essai clinique ni aucune publication ne relie directement le zuclopenthixol à la dystrophie rétinienne ciblée, et l'analyse mécanistique disponible conclut elle-même à l'absence de lien biologique plausible avec l'antagonisme dopaminergique/adrénergique du médicament. Le niveau de preuve est L5 (prédiction du modèle seule).

**Pour avancer, les éléments suivants sont nécessaires :**
- Résolution du data gap bloquant : mises en garde/contre-indications de la notice TFDA (actuellement introuvables, ce qui empêche toute évaluation de sécurité S1)
- Confirmation détaillée du mécanisme d'action (MOA) via DrugBank ou autre source primaire
- Recherche bibliographique ciblée croisant explicitement « zuclopenthixol » et la pathologie rétinienne (les résultats actuels ne sont que des correspondances par mots-clés sur la maladie)
- Toute donnée précl inique ou étude de mécanisme reliant les récepteurs dopaminergiques à la dystrophie rétinienne héréditaire, avant d'envisager une progression au-delà du stade S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

