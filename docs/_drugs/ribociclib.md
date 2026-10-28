---
layout: default
title: Ribociclib
parent: Preuves modérées (L3-L4)
nav_order: 664
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Ribociclib : nouvelle indication prédite, Leucémie myéloïde (niveau de preuve L5). Indication d'origine : Non disponible dans les données d'AMM (texte d'indication vide)"
monitor_inn: "ribociclib"
predicted_indications: ["myeloid leukemia", "thrombocytopenia", "marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets"]
---

# Ribociclib
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **4** 
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

## Ribociclib : Du Cancer du Sein HR+/HER2- à la Leucémie Myéloïde
{: .text-alpha }

## Résumé en Une Phrase

Le ribociclib (Kisqali) est un inhibiteur de CDK4/6. Les données réglementaires compilées pour ce rapport ne précisent pas son indication originale ; la littérature le associe au cancer du sein métastatique HR+/HER2-.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **leucémie myéloïde**, mais cette prédiction repose sur **aucun essai clinique** et seulement **2 publications** peu pertinentes (une étude préclinique et un rapport de cas hors sujet).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans les données d'AMM (texte d'indication vide) |
| Nouvelle Indication Prédite | Leucémie myéloïde |
| Score de Prédiction TxGNN | 0,9935 |
| Niveau de Preuve | L4 (études précliniques uniquement) |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances générales, le ribociclib est un inhibiteur sélectif de CDK4/6, des kinases qui contrôlent la transition de la phase G1 à la phase S du cycle cellulaire. Son efficacité a été établie dans le cancer du sein HR+/HER2- avancé ou métastatique, en association avec un traitement endocrinien.

Dans la leucémie myéloïde aiguë (LMA), les cellules leucémiques peuvent dépendre de la signalisation CDK4/6 pour leur prolifération, ce qui donne un rationnel plausible. Une étude préclinique *in vitro* (2020) suggère de plus que les inhibiteurs de CDK4/6 pourraient contrecarrer la résistance pharmacocinétique (transporteurs ABCB1 et ABCG2) des cellules de LMA, ce qui ouvre une piste indirecte pour des associations.

Ce lien reste toutefois hypothétique : le score élevé de TxGNN est une prédiction computationnelle, et aucune donnée clinique ne la confirme. Il s'agit à ce stade d'une question de recherche.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Préclinique (in vitro) | Cancers | Les inhibiteurs de CDK4/6 pourraient contrer la résistance pharmacocinétique des cellules de LMA liée aux transporteurs ABCB1/ABCG2 |
| [41641105](https://pubmed.ncbi.nlm.nih.gov/41641105/) | 2026 | Rapport de cas | Frontiers in Oncology | Adénocarcinome vulvaire de type mammaire associé à un cancer du sein : non pertinent pour la LMA |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68343525 | KISQALI 200 mg, comprimé pelliculé (NOVARTIS EUROPHARM, Irlande) | Comprimé pelliculé | Non renseignée (AMM active) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de kinases CDK4/6) |
| Risque de Myélosuppression | Élevé : neutropénie, leucopénie et thrombopénie rapportées de façon récurrente dans la littérature sur les inhibiteurs de CDK4/6 |
| Classification d'Émétogénicité | Données non disponibles ; nausées, vomissements et diarrhées rapportés parmi les effets indésirables |
| Éléments de Surveillance | NFS (avec formule), fonction hépatique, ECG (allongement de l'intervalle QT rapporté pour cette classe) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

**Interactions médicamenteuses** : 579 interactions ont été recensées. Parmi les principales :
- **Majeures** : clarithromycine, dolasétron
- **Modérées** : famotidine, hydrocortisone, métformine, pioglitazone, alosétron, lopéramide, aprépitant, dexaméthasone, cimétidine, saxagliptine, entre autres

**Effets indésirables rapportés dans la littérature** : myélosuppression (neutropénie, thrombopénie), pneumopathie, hallucinations visuelles.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la leucémie myéloïde repose sur un score computationnel élevé et une seule étude préclinique, sans aucun essai clinique. Le profil myélosuppresseur du ribociclib est en outre une préoccupation majeure dans une hémopathie maligne. L'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice de l'ANSM (nécessaires pour le criblage de sécurité)
- Études précliniques complémentaires dans la LMA (modèles *in vivo*, associations)
- Évaluation de la tolérance hématologique dans une population leucémique avant tout essai clinique

---

### Note sur les autres prédictions

Les autres indications prédites (thrombopénie, macrothrombopénie avec insuffisance mitrale, thrombopénie héréditaire à plaquettes normales) ne sont **pas recommandées** (Hold, niveau L5). La littérature décrit la thrombopénie comme un **effet indésirable** du ribociclib, et non comme un effet thérapeutique. Ces scores élevés proviennent du modèle TxGNN (apprentissage profond) et peuvent refléter des similitudes apprises par le modèle entre maladies apparentées, et non une preuve biologique. Utiliser un médicament myélosuppresseur pour traiter un trouble plaquettaire serait mécanistiquement inapproprié.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

