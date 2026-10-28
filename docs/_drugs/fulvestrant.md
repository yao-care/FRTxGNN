---
layout: default
title: Fulvestrant
parent: Prédiction du modèle uniquement (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "FULVESTRANT"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Fulvestrant : nouvelle indication prédite, Infection par le VIH (HIV infectious disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Fulvestrant
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

## Fulvestrant: Infection par le VIH (HIV infectious disease)
{: .text-alpha }

## Résumé en Une Phrase

Fulvestrant est un antagoniste et dégradeur du récepteur des œstrogènes, utilisé dans le cancer du sein hormonodépendant avancé.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le VIH**,
mais aucun essai clinique n'est enregistré et seules **2 publications** précliniques ou indirectes abordent cette piste. Il s'agit donc d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Infection par le VIH (HIV infectious disease) |
| Score de Prédiction TxGNN | 0.9991 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 10) |
| Nombre d'AMM | 10 (valides : 10) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, fulvestrant est un antagoniste pur du récepteur des œstrogènes (ER) qui favorise aussi sa dégradation. Son efficacité a été établie dans le cancer du sein HR+/HER2-, seul ou en association (par exemple avec le ribociclib ou l'alpélisib).

Le lien avec le VIH reste une hypothèse. Le récepteur ERα est exprimé dans les lymphocytes T CD4+, et une étude de 2026 (PMID 42430506) examine l'effet de ligands du récepteur, dont le fulvestrant, et d'agents de réversion de la latence du VIH sur ERα. Bloquer ou dégrader ce récepteur pourrait théoriquement moduler la latence virale. Cette idée n'a été explorée qu'in vitro, et aucune donnée clinique n'existe.

Le score très élevé du modèle TxGNN (deep learning) (0,9991) peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ou clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour l'infection par le VIH.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Étude préclinique / in vitro | JCI Insight | Effet des œstrogènes, du fulvestrant et des agents de réversion de la latence du VIH sur la translocation nucléaire d'ERα dans les lymphocytes T CD4+ |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Analyse cross-omique de cohortes | Research Square | Étude sur la myélopathie associée à HTLV-1 (un autre rétrovirus) ; contexte indirect uniquement |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60446306 | Fulvestrant EG 250 mg | Solution injectable | Non renseignée |
| 66475706 | Fulvestrant Arrow 250 mg | Solution injectable | Non renseignée |
| 69289895 | Fulvestrant Mylan 250 mg | Solution injectable | Non renseignée |
| 63545028 | Faslodex 250 mg | Solution injectable | Non renseignée |
| 62062457 | Fulvestrant Sandoz 250 mg | Solution injectable | Non renseignée |

Les 10 AMM sont au statut « annulée ».

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Hormonothérapie anticancéreuse (antagoniste/dégradeur du récepteur des œstrogènes), non cytotoxique conventionnelle |
| Risque de Myélosuppression | Aucune donnée de toxicité disponible dans les données compilées |
| Classification d'Émétogénicité | Aucune donnée disponible |
| Éléments de Surveillance | Fonction hépatique, numération plaquettaire et paramètres de coagulation (voir contre-indications issues du graphe de connaissances) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Maladies associées à une contre-indication dans le graphe de connaissances** (liens du graphe, et non texte de notice) : maladie du foie, maladie de la vésicule biliaire, thrombocytopénie, trouble de la coagulation sanguine.
- **Interactions médicamenteuses** : 92 interactions sont recensées, toutes de niveau de gravité non précisé. Parmi elles : warfarine, acide acétylsalicylique, dexaméthasone, prednisone, simvastatine, metformine, oméprazole, pantoprazole, lansoprazole, ondansétron, métoclopramide et morphine. L'association avec la warfarine mérite une attention particulière, compte tenu du risque hémorragique lié à la coagulation et aux plaquettes.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle et sur une étude in vitro, sans essai clinique. Les données de sécurité de la notice sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité. Les 10 AMM françaises sur 10 sont valides et le médicament est commercialisé.

Les autres indications prédites ne sont pas plus solides :
- **Neoplasie endocrinienne multiple** : les 13 essais retrouvés portent sur le cancer du sein HR+/HER2-, et non sur cette maladie. L'association vient probablement d'un mot-clé ou d'un appariement trop large.
- **Polyarthrite rhumatoïde** : les preuves sont indirectes et en partie contradictoires. Une étude chez le rat suggère que le blocage des œstrogènes aggrave l'inflammation, ce qui laisse craindre un effet délétère.
- **Autres prédictions** (infection par le virus de l'immunodéficience simienne, SIDA félin, acné, maladies génétiques rares, hémoglobinopathie) : aucune preuve, avec parfois un modèle animal ou vétérinaire seulement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante)
- Données détaillées sur le mécanisme d'action (à obtenir via DrugBank)
- Indications approuvées des AMM, et clarification de la situation réglementaire des produits annulés
- Études précliniques supplémentaires sur la modulation de ERα dans la latence du VIH, avant d'envisager un essai clinique
- Évaluation du rapport bénéfice/risque d'une hormonothérapie anti-œstrogène dans une population atteinte du VIH
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

