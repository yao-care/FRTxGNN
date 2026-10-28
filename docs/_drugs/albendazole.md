---
layout: default
title: Albendazole
parent: Preuves élevées (L1-L2)
nav_order: 32
evidence_level: L2
indication_count: 3
last_modified_at: 2026-10-14
description: "Albendazole : nouvelle indication prédite, Échinococcose alvéolaire (niveau de preuve L2). Indication d'origine : Échinococcose kystique, cysticercose…"
monitor_inn: "ALBENDAZOLE"
predicted_indications: ["alveolar echinococcosis", "coenurosis", "Cestode infectious disease"]
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

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Albendazole : De l'échinococcose kystique à l'échinococcose alvéolaire
{: .text-alpha }

## Résumé en Une Phrase

Albendazole est un antiparasitaire de la famille des benzimidazoles, initialement utilisé pour traiter l'échinococcose kystique, la cysticercose et l'infection à *Echinococcus granulosus*.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**échinococcose alvéolaire**, avec **3 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il s'agit davantage d'une extension au sein d'une même classe de médicaments et d'un même genre de parasite que d'un repositionnement au sens strict.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Échinococcose kystique, cysticercose, infection à *Echinococcus granulosus* (texte d'indication de l'AMM non renseigné dans les données compilées) |
| Nouvelle Indication Prédite | Échinococcose alvéolaire |
| Score de Prédiction TxGNN | 0,9997 |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

L'albendazole est un antihelminthique de la famille des benzimidazoles. Les données détaillées sur le mécanisme d'action ne figurent pas dans les données compilées pour ce rapport. Selon les connaissances pharmacologiques établies, il se lie à la bêta-tubuline du parasite et inhibe la polymérisation des microtubules, ce qui perturbe l'absorption du glucose et le métabolisme énergétique des helminthes.

*Echinococcus multilocularis*, agent de l'échinococcose alvéolaire, est très proche d'*Echinococcus granulosus*, responsable de l'échinococcose kystique (indication d'origine). Le mécanisme est donc directement transférable d'une espèce à l'autre.

L'albendazole est d'ailleurs déjà le traitement chimiothérapique recommandé par les consensus d'experts pour l'échinococcose alvéolaire. Son action est parasitostatique, et le traitement est prolongé ou administré après chirurgie. Le score TxGNN très élevé est cohérent avec cette situation.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Terminé | 194 | Essai de traitement par albendazole dans l'échinococcose alvéolaire à un stade précoce (foyer détecté au Kirghizistan par dépistage échographique). Correspondance directe, mais plan de randomisation non précisé et résultats non fournis |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | NA | Terminé | 50 | Étude prospective (EchinoVISTA) sur la viabilité du parasite et des marqueurs de suivi chez des patients traités par albendazole. Soutient la surveillance de la réponse plutôt que l'efficacité |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | NA | Inconnu | 24 | Essai randomisé de l'albendazole adjuvant après résection d'un kyste hydatique pulmonaire, versus placebo. Concerne la forme kystique, donc indirect ; effectif faible |

---

## Preuves de la Littérature

Les publications ci-dessous sont les plus pertinentes parmi celles compilées (principalement des revues et des études observationnelles ; aucun ECR n'est répertorié).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Revue (consensus d'experts) | Acta Tropica | Recommandations de consensus pour le diagnostic, le traitement et le suivi des échinococcoses kystique et alvéolaire |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Revue | Clin Microbiol Rev | Avancées du XXIe siècle sur l'échinococcose, y compris les techniques de traitement |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Revue | Semin Liver Dis | Synthèse sur l'échinococcose alvéolaire hépatique |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Revue | Tidsskr Nor Legeforen | Prise en charge : résection chirurgicale étendue associée à un traitement prolongé |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Revue | World J Gastroenterol | Prise en charge actuelle de l'échinococcose hépatique ; la chirurgie reste la pierre angulaire |
| [34432154](https://pubmed.ncbi.nlm.nih.gov/34432154/) | 2021 | Observationnelle (rétrospective) | Parasitol Res | Tolérance clinique et efficacité de l'albendazole chez 117 patients, suivi à long terme |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Observationnelle | J Antimicrob Chemother | Comparaison albendazole/mébendazole chez 35 patients, suivi moyen de 39 mois |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Revue | Zhongguo Xue Xi Chong Bing Fang Zhi Za Zhi | Progrès sur l'albendazole : il peut retarder la progression chez les patients non opérables |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Revue | Parasitology | Le traitement repose exclusivement sur l'albendazole, non parasiticide, avec des effets indésirables parfois sévères ; la pyronaridine est évoquée comme alternative |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Revue | Parasite | Albendazole et mébendazole : options thérapeutiques et pistes nouvelles |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69731801 | ZENTEL 0,4 g/10 mL, suspension buvable (active) | Suspension buvable | Non renseignée |
| 65565944 | ZENTEL 400 mg, comprimé (active) | Comprimé | Non renseignée |
| 68879708 | ESKAZOLE 400 mg, comprimé (active) | Comprimé | Non renseignée |

Les trois AMM (titulaire : GlaxoSmithKline) sont valides ; le médicament est actuellement commercialisé.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : maladie hépatique, maladie de la vésicule biliaire, neutropénie, agranulocytose, anémie (dont anémie macrocytaire), pancytopénie, anémie aplasique idiopathique et anémie aplasique.
- **Interactions médicamenteuses** : 96 interactions répertoriées. Parmi celles listées, la plupart sont de niveau modéré, notamment : aprépitant, cobicistat, déférasirox, iodure I-123 et I-131, fostamatinib, abamétapir (topique), alemtuzumab, amprénavir, anagrélide, apalutamide, bendamustine, bexarotène, binimétinib, bocéprévir et bosentan. Les interactions de niveau mineur concernent la cimétidine, la dexaméthasone, la lidocaïne et l'armodafinil.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations. L'accent sur l'hématotoxicité et l'hépatotoxicité suggère une surveillance de la NFS et des tests hépatiques.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- L'albendazole est déjà le traitement de référence recommandé pour l'échinococcose alvéolaire, et un essai de phase 2 terminé (194 participants) porte directement sur cette indication, ce qui correspond à un niveau de preuve L2. Les AMM françaises étant toutes annulées et les données de sécurité issues de la notice manquantes, la prudence s'impose.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications), étape bloquante pour le dépistage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank
- Obtenir les résultats publiés de l'essai NCT07182305 (plan randomisé, critères d'évaluation)
- Clarifier la situation réglementaire en France (AMM annulées, disponibilité effective du produit)
- Définir un plan de surveillance hématologique et hépatique et examiner les interactions médicamenteuses pertinentes

---

### Note sur les autres indications prédites

Deux autres prédictions figurent dans les données : la **coenurose** (score de 0,9983) et les **infections à cestodes** (score de 0,9974). Elles sont présentées comme L1 dans les données, mais cette classification repose sur des essais de phase 3 portant sur la neurocysticercose (indication déjà existante), et non sur la coenurose elle-même. La coenurose humaine est rare et ne dispose d'aucun essai randomisé dédié ; l'application est donc une extrapolation. La catégorie « infection à cestodes » est un parent des indications d'origine, et son score élevé reflète surtout la hiérarchie de l'ontologie, non un véritable repositionnement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

