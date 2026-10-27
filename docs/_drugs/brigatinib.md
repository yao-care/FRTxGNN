---
layout: default
title: Brigatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brigatinib : nouvelle indication prédite, Fibromatose gingivale (niveau de preuve L5). Indication d'origine : Cancer bronchique non à petites cellules"
monitor_inn: "BRIGATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "pulmonary sulcus neoplasm", "lung germ cell tumor", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Brigatinib
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

## Brigatinib : Du Cancer Bronchique Non à Petites Cellules à la Fibromatose Gingivale
{: .text-alpha }

## Résumé en Une Phrase

Brigatinib est un inhibiteur de tyrosine kinase (notamment de l'ALK), initialement utilisé pour le traitement du cancer bronchique non à petites cellules (CBNPC) ALK-positif.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer bronchique non à petites cellules ; cancer du poumon (selon le graphe de connaissances, le texte d'indication des AMM françaises n'étant pas renseigné) |
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le brigatinib est un inhibiteur de kinases multiples (ALK, EGFR, ROS1, FAK). Son efficacité dans le CBNPC ALK-positif est établie par l'essai de phase 3 ALTA-1L.

Aucun lien mécanistique plausible n'a été établi entre cette inhibition de kinases et la fibromatose gingivale. Le score élevé du modèle (99,89 %) reflète un calcul sur le graphe de connaissances, et non une preuve biologique ou clinique. La similarité avec l'indication d'origine n'a pas été évaluée.

Ce score doit donc être interprété avec prudence : plusieurs autres prédictions du même médicament, également de score très élevé, sont tout aussi dépourvues de soutien (voir la conclusion).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 60648770 | ALUNBRIG 90 mg | Comprimé pelliculé | Non renseignée | Annulée |
| 66949061 | ALUNBRIG 180 mg | Comprimé pelliculé | Non renseignée | Annulée |
| 61066196 | ALUNBRIG 90 mg + 180 mg | Comprimé pelliculé | Non renseignée | Annulée |
| 62626993 | ALUNBRIG 30 mg | Comprimé pelliculé | Non renseignée | Annulée |

Les quatre AMM (titulaire : Takeda Pharma, Danemark) sont annulées ; aucune AMM n'est actuellement valide dans les données compilées.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice ; un cas publié de syndrome de lyse tumorale fatal (PMID 34987411) dans un adénocarcinome pulmonaire justifie une vigilance |
| Protection de Manipulation | Veuillez consulter la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été identifiées (base DDInter) ; les 20 premières sont décrites ici.
  - **Majeures** : aprépitant, dexaméthasone, clarithromycine.
  - **Modérées** : antidiabétiques (acarbose, alogliptine, albiglutide, metformine, pioglitazone, acétohexamide, canagliflozine, chlorpropamide, dapagliflozine), antiacides et inhibiteurs de la sécrétion gastrique (famotidine, ranitidine, rabéprazole, cimétidine), lopéramide, morphine, cisapride, clotrimazole.
- **Signal de sécurité issu de la littérature** : cas de syndrome de lyse tumorale fatal sous brigatinib chez un patient atteint d'adénocarcinome pulmonaire ALK-réarrangé (PMID 34987411).

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la fibromatose gingivale repose uniquement sur le modèle (niveau L5) : aucun essai, aucune publication, aucun lien mécanistique. Les AMM françaises sont toutes annulées et les données de sécurité de la notice manquent, ce qui bloque l'étape de criblage de sécurité.

**Autres prédictions du même médicament (pour information) :**
- **Syndrome de leucomélanodermie-infantilisme… (rang 10)** : les publications retrouvées concernent en réalité la schwannomatose liée à NF2 (étude clinique publiée dans le NEJM, PMID 38904277, et travaux précliniques, PMID 34264955). Il s'agit probablement d'un artefact de correspondance de maladie ; la piste, de niveau L3, mériterait d'être réorientée vers la schwannomatose NF2, comme question de recherche.
- **Tumeur germinale du poumon (rang 8)** : indirectement, des cas rapportés et des données précliniques montrent une activité dans des tumeurs avec altération d'ALK (phéochromocytome, carcinome neuroendocrine à grandes cellules, neuroblastome) ; rien ne concerne les tumeurs germinales (niveau L4, question de recherche).
- **Tumeur bénigne du poumon (rang 5)** : les 20 publications retrouvées concernent le CBNPC ALK-positif (l'indication d'origine), et non cette indication ; elles ne constituent pas une preuve de niveau L1 pour cette maladie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM (mises en garde et contre-indications), point bloquant pour la sécurité.
- Obtenir les données sur le mécanisme d'action via DrugBank.
- Pour la fibromatose gingivale : une hypothèse mécanistique documentée et des données précliniques avant toute évaluation clinique.
- Pour la schwannomatose NF2 : réorienter l'évaluation vers cette indication et examiner les données cliniques disponibles.
- Clarifier la situation réglementaire en France (AMM annulées) avant toute perspective d'utilisation.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

