---
layout: default
title: Benralizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 96
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Benralizumab : De la pneumonie à éosinophiles à la dermatite

## Résumé en Une Phrase

Benralizumab est un anticorps monoclonal dirigé contre le récepteur alpha de l'interleukine 5 (IL-5Rα), initialement associé aux indications de pneumonie à éosinophiles et d'éosinophilie pulmonaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dermatite** (deuxième prédiction du classement ; la première, la thrombopénie immune, ne dispose d'aucune preuve), avec **3 essais cliniques** (dont un seul terminé) et **19 publications**, essentiellement des revues générales, qui soutiennent actuellement cette piste de manière limitée.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pneumonie à éosinophiles ; éosinophilie pulmonaire (source : graphe de connaissances, aucun texte d'indication dans les AMM) |
| Nouvelle Indication Prédite | Dermatite (rang 2 ; voir la note ci-dessous sur le rang 1) |
| Score de Prédiction TxGNN | 99,16 % |
| Niveau de Preuve | L2 (selon le classement du dossier ; voir la réserve ci-dessous) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

**Note sur le choix de l'indication :** la prédiction n° 1 (thrombopénie par destruction immunitaire, score 99,34 %) n'a ni essai clinique ni publication (L5, Hold). La dermatite (rang 2) est présentée ici car c'est la première prédiction qui dispose de preuves exploitables.

**Réserve sur le niveau L2 :** il est attribué par le dossier, mais aucun essai de phase 2/3 n'a fourni de résultat positif. L'essai principal (HILLIER) a été interrompu, et la publication associée rapporte une **absence d'effet** sur les signes et symptômes de la dermatite atopique. Le niveau doit donc être lu avec prudence.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations pharmacologiques connues, benralizumab cible l'IL-5Rα (gène *IL5RA*) et élimine les éosinophiles et les basophiles par cytotoxicité cellulaire dépendante des anticorps (ADCC). Aux États-Unis, il est approuvé dans l'asthme sévère à phénotype éosinophilique et, depuis septembre 2024, dans la granulomatose éosinophilique avec polyangéite.

Les indications d'origine (pneumonie à éosinophiles, éosinophilie pulmonaire) sont des maladies où les éosinophiles jouent un rôle central. Certaines dermatites, comme la dermatite atopique ou les réactions médicamenteuses avec éosinophilie (DRESS), impliquent aussi l'inflammation de type 2, avec éosinophiles, basophiles et cellules lymphoïdes innées de type 2. Ce lien mécanistique est plausible.

Cependant, les données cliniques tempèrent cette plausibilité. L'essai de phase 2 HILLIER (n=194, contrôlé par placebo) a été terminé prématurément, et sa publication conclut à l'absence d'effet de benralizumab dans la dermatite atopique modérée à sévère. L'élimination des éosinophiles ne suffit donc probablement pas à contrôler la dermatite atopique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Terminé | 20 | Étude mécanistique des effets de benralizumab sur les éosinophiles, basophiles et cellules lymphoïdes innées dans la dermatite atopique ; petite taille, non dimensionnée pour l'efficacité |
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | Arrêté | 194 | Étude HILLIER, randomisée, en double aveugle, contrôlée par placebo (16 semaines + extension de 36 semaines) dans la dermatite atopique modérée à sévère ; arrêtée, sans effet démontré |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Pas encore en recrutement | 96 | Efficacité et sécurité dans le syndrome DRESS ; début prévu en 2027, pas de résultats |

## Preuves de la Littérature

Le dossier compte 19 publications. Voici les plus pertinentes ; les autres sont des revues générales sur les biothérapies des maladies atopiques ou de l'asthme.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Essai de phase 2 randomisé (HILLIER) | J Eur Acad Dermatol Venereol | Absence d'effet de benralizumab sur les signes et symptômes de la dermatite atopique modérée à sévère |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Revue | J Allergy Clin Immunol Pract | Sécurité des biothérapies atopiques, dont benralizumab, pendant la grossesse |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Revue | Allergologie select | Mise à jour sur les biothérapies des maladies atopiques, de l'urticaire et de l'angiœdème, et sur les réactions d'hypersensibilité |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Revue | Immunol Allergy Clin North Am | Anticorps monoclonaux dans la rhinite allergique, l'asthme et la dermatite atopique pendant la grossesse et l'allaitement |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Revue | Ann Allergy Asthma Immunol | Aide au choix d'une biothérapie dans l'allergie et l'asthme, y compris la dermatite atopique |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Revue | Allergy Asthma Proc | Immunobiologiques (dont anti-IL-5) dans l'asthme sévère, la dermatite atopique et l'urticaire chronique |

Aucune de ces revues ne démontre une efficacité de benralizumab dans la dermatite. La seule publication d'essai va dans le sens inverse.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63562134 | FASENRA 30 mg, solution injectable en seringue préremplie (annulée) | Solution injectable | Non renseignée |
| 63094493 | FASENRA 30 mg, solution injectable en stylo prérempli (annulée) | Solution injectable | Non renseignée |

Les deux AMM, détenues par AstraZeneca AB, sont annulées : aucune AMM valide n'est actuellement recensée.

## Considérations de Sécurité

- **Interactions médicamenteuses :** la seule entrée recensée est pharmacologique et correspond à la cible du médicament, l'IL-5Rα, et non à une interaction avec un autre médicament. Aucune interaction médicamenteuse cliniquement documentée n'est disponible.

Les mises en garde et les contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le lien mécanistique est plausible (inflammation de type 2 à éosinophiles), mais le seul essai randomisé contrôlé par placebo dans la dermatite atopique a été arrêté et sa publication rapporte une absence d'effet. Les autres essais sont soit trop petits, soit pas encore commencés.
- Les informations de sécurité de la notice sont absentes et aucune AMM n'est valide en France, ce qui bloque le passage à l'étape de dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice (mises en garde et contre-indications) auprès de l'ANSM.
- Compléter les données sur le mécanisme d'action de benralizumab (par exemple via DrugBank).
- Examiner en détail les résultats complets de l'essai HILLIER (NCT04605094) et les raisons de son arrêt.
- Envisager des sous-populations plus ciblées, par exemple les dermatoses à éosinophiles comme le DRESS, dont l'essai NCT06734884 attend ses premiers résultats.
- Clarifier la situation réglementaire en France (annulation des AMM).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

