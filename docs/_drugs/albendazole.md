---
layout: default
title: Albendazole
parent: Preuves élevées (L1-L2)
nav_order: 20
evidence_level: L2
indication_count: 3
---

# Albendazole
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **3** 
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

# Albendazole : D'un Antihelminthique à l'Échinococcose Alvéolaire

## Résumé en Une Phrase

L'albendazole est un antihelminthique commercialisé en France (Zentel, Eskazole), mais son indication d'origine n'est pas renseignée dans le dossier.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**échinococcose alvéolaire**,
avec **5 essais cliniques** et **20 publications** associés à cette direction. Un seul essai de Phase 2 (terminé) évalue directement l'albendazole dans cette maladie.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le dossier (texte d'indication des AMM vide) |
| Nouvelle Indication Prédite | Échinococcose alvéolaire |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier du médicament. D'après la pharmacologie générale, l'albendazole (via son métabolite actif, le sulfoxyde d'albendazole) se lie à la bêta-tubuline du parasite. Il bloque ainsi la polymérisation des microtubules et perturbe l'absorption du glucose chez les métacestodes d'*Echinococcus*.

Ce mécanisme est parasitostatique et non parasiticide : il ralentit la croissance du parasite sans le tuer. C'est pourquoi le traitement est généralement prolongé et souvent associé à la chirurgie. Le consensus d'experts et les revues récentes placent déjà les benzimidazoles (albendazole, mébendazole) comme chimiothérapie de référence de l'échinococcose alvéolaire.

Le score TxGNN très élevé (0,9997) est cohérent avec cette situation. Il s'agit toutefois d'une prédiction du modèle, pas d'une preuve indépendante.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Terminé | 194 | Traitement par albendazole de l'échinococcose alvéolaire à un stade précoce, dans un foyer découvert au Kirghizistan par dépistage échographique. Seule preuve interventionnelle directe. Randomisation et comparateur non confirmés. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | Non applicable | Inconnu | 24 | Essai randomisé de l'albendazole adjuvant après résection d'un kyste hydatique pulmonaire, contre placebo. Concerne la forme kystique : preuve indirecte. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | Non applicable | Terminé | 50 | Étude EchinoVISTA : marqueurs de viabilité du parasite et de suivi chez des patients atteints d'échinococcose alvéolaire hépatique traités par albendazole. Soutient le suivi de la réponse, sans tester l'efficacité. |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | Non applicable | En recrutement | 43 | Nouvelle PCR quantitative multiplex pour le diagnostic de l'échinococcose. Étude diagnostique, sans intervention thérapeutique. |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | Non applicable | Terminé | 1 | Cas clinique d'un kyste hydatique intramusculaire du deltoïde, initialement mal diagnostiqué. Forme kystique, non pertinent pour l'efficacité dans la forme alvéolaire. |

---

## Preuves de la Littérature

Aucun ECR ni revue systématique n'a été identifié parmi les publications. Le tableau présente les consensus, revues et études précliniques les plus pertinents.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Consensus d'experts | Acta Trop | Recommandations actualisées de l'OMS (WHO-IWGE) sur le diagnostic, le traitement et le suivi des échinococcoses kystique et alvéolaire. |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Revue | Parasite | La prise en charge repose sur les benzimidazoles, associés à la chirurgie si possible. Ils sont parasitostatiques : le parasite peut reprendre sa croissance à l'arrêt. Risque d'atteinte hépatique. |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Revue | World J Hepatol | État des lieux du traitement médicamenteux. La chirurgie reste le traitement principal, mais de nombreux patients sont diagnostiqués trop tard pour être opérés. |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Revue | Semin Liver Dis | Revue de l'échinococcose alvéolaire hépatique : zoonose rare et grave, en recrudescence dans les zones historiquement endémiques. |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Revue | Zhongguo Xue Xi Chong Bing Fang Zhi Za Zhi | Progrès sur l'albendazole : il peut retarder la progression chez les patients non opérables ou refusant la chirurgie. |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Revue | Clin Microbiol Rev | Progrès du XXIᵉ siècle sur la génétique, le diagnostic et les techniques de traitement de l'échinococcose, notamment dans l'ouest de la Chine. |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Revue | Tidsskr Nor Laegeforen | Tumeurs multikystiques à croissance lente, évoquant une tumeur maligne. Traitement fréquent par résection chirurgicale et traitement prolongé. |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Revue | World J Gastroenterol | Prise en charge de l'échinococcose hépatique : la chirurgie est la pierre angulaire du traitement. |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Pharmacologie / métabolisme | Antimicrob Agents Chemother | Chez le rat, des formulations solubilisantes cherchent à améliorer la biodisponibilité orale, limitée par la faible solubilité. |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Revue | Parasitology | L'albendazole est le seul traitement antiparasitaire actuel, non parasiticide et parfois responsable d'effets indésirables sévères. La pyronaridine est étudiée comme alternative. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 69731801 | ZENTEL 0,4 g/10 mL | Suspension buvable | GlaxoSmithKline |
| 65565944 | ZENTEL 400 mg | Comprimé | GlaxoSmithKline |
| 68879708 | ESKAZOLE 400 mg | Comprimé | GlaxoSmithKline |

Le texte des indications approuvées n'est pas renseigné pour ces trois AMM.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Un essai de Phase 2 terminé (n=194) évalue directement l'albendazole dans l'échinococcose alvéolaire précoce. Le consensus d'experts et les revues le positionnent déjà comme traitement de référence, d'où le niveau L2. Le plan de l'essai (randomisation, comparateur) reste à vérifier.
- L'absence de données de sécurité issues de la notice ANSM est un manque bloquant pour un passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications), pour lever le manque bloquant
- Confirmer le statut d'indication autorisée en France (indication d'origine non renseignée, texte d'indication des AMM vide)
- Vérifier le plan de l'essai NCT07182305 (randomisation, comparateur) et obtenir ses résultats
- Compléter les données de mécanisme d'action (MOA) dans DrugBank
- Prévoir, en cas de traitement prolongé, une surveillance des enzymes hépatiques et de la numération formule sanguine

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

