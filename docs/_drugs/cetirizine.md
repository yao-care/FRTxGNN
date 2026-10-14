---
layout: default
title: Cetirizine
parent: Preuves élevées (L1-L2)
nav_order: 157
evidence_level: L2
indication_count: 6
---

# Cetirizine
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **6** 
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

# Cétirizine : De la rhinite allergique à l'urticaire allergique

## Résumé en Une Phrase

La cétirizine est un antihistaminique de deuxième génération (antagoniste des récepteurs H1), initialement utilisé pour la rhinite allergique, les conjonctivites allergiques et l'urticaire idiopathique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**urticaire allergique**, avec **1 essai clinique** (pilote de phase 3, 36 patients) et **18 publications** recensés dans les données compilées pour ce rapport.
Cette indication est toutefois très proche de l'usage déjà établi (urticaire idiopathique) : il s'agit davantage d'une extension au sein d'une même famille de maladies que d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique, rhinite vasomotrice, conjonctivites (atopique, papillaire, printanière), urticaire idiopathique, etc. (les textes d'indication des AMM françaises ne sont pas renseignés ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Urticaire allergique |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, la cétirizine est un antagoniste sélectif des récepteurs H1 de l'histamine, métabolite carboxylé de l'hydroxyzine. Son efficacité dans l'urticaire idiopathique et la rhinite allergique est établie.

Dans l'urticaire, la libération d'histamine par les mastocytes provoque la formation de papules et l'érythème réflexe. Le blocage des récepteurs H1 agit donc directement sur la physiopathologie. L'urticaire allergique appartient à la même famille de maladies que l'urticaire idiopathique, déjà couverte par l'usage d'origine ; le score très élevé du modèle (0,9999) est cohérent avec ce rationnel biologique.

Il convient de rester prudent : ce score reflète en partie la proximité avec une indication existante. Par ailleurs, la cétirizine ne s'applique pas de la même façon à toutes les prédictions du modèle (voir ci-dessous).

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 (pilote) | Terminé | 36 | Étude pilote multicentrique, randomisée, en double aveugle, comparant la cétirizine injectable (10 mg, IV) à la diphénhydramine injectable (50 mg) dans l'urticaire aiguë aux urgences, en soins urgents et en cliniques d'allergologie. Vise à évaluer la faisabilité d'un essai de phase 3, et non à démontrer l'efficacité de façon définitive. |

---

## Preuves de la Littérature

La littérature associée à l'urticaire allergique est composée surtout de revues sur les antihistaminiques ; aucune n'est un essai randomisé contrôlé spécifique. Principales références :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Revue | Ann Pharmacother | Efficacité et sécurité des antihistaminiques de première et nouvelle génération dans la rhinite allergique et l'urticaire chronique idiopathique |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Revue | Drugs | Réévaluation de la cétirizine : traitement efficace et bien toléré de la rhinite saisonnière/perannuelle et de l'urticaire chronique idiopathique chez l'adulte |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Revue | Drugs | Propriétés pharmacologiques et potentiel clinique de la cétirizine dans la rhinite allergique, l'asthme pollinique et l'urticaire chronique |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Revue | Allergy | Études cliniques de la cétirizine dans la rhinite allergique et l'urticaire chronique |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Revue | Drugs | Causes et traitement de l'urticaire ; les antihistaminiques non sédatifs sont le traitement de base de l'urticaire chronique idiopathique |
| [17017922](https://pubmed.ncbi.nlm.nih.gov/17017922/) | 2006 | Revue | Curr Med Chem | Mise à jour sur la lévocétirizine, énantiomère R de la cétirizine |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Revue | Allergy Asthma Proc | Lévocétirizine dans la rhinite allergique et l'urticaire chronique idiopathique |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Rapport de cas | J Clin Gastroenterol | Cas de cholestase induite par la cétirizine (signal de sécurité hépatique) |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64939766 | REACTINE 10 mg (KENVUE FRANCE) | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 62636293 | ZYRTECSET 10 mg (BB FARMA, Italie) | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 64949486 | ZYRTECSET 10 mg (UCB PHARMA) | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non le texte de la notice) : maladie hypertensive/hypertension, maladie rénale (dont insuffisance rénale chronique et terminale), maladie hépatique, maladie de la vésicule biliaire, diabète et acidocétose diabétique, hyperplasie bénigne de la prostate, maladie coronarienne et athérosclérose, glaucome (dont glaucome à angle fermé), hyperthyroïdie (maladie de Basedow, thyréotoxicose), pyourètre. Ces éléments sont à vérifier avec la notice officielle.
- **Interactions médicamenteuses** : 570 interactions recensées. Parmi les principales, de niveau modéré : bupropion, dronabinol, lopéramide, métoclopramide, morphine (y compris liposomale), nabilone, opium, sibutramine, difénoxine, diphénoxylate (renforcement possible des effets sédatifs/dépresseurs du système nerveux central). D'autres interactions de niveau inconnu concernent notamment le calcitriol, la vitamine A, la phentermine, le pantoprazole, le glimépiride, la mésalazine, la doxycycline, le clotrimazole et l'acarbose.
- **Signal hépatique** : un cas publié de cholestase induite par la cétirizine (PMID 11034010).

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être obtenues ; veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- L'urticaire allergique est proche de l'indication déjà établie (urticaire idiopathique), le mécanisme H1 est cohérent et un essai pilote de phase 3 achevé existe. Toutefois, cet essai est de petite taille (n = 36) et de faisabilité : le niveau de preuve est donc L2 et non L1.

**Autres prédictions du modèle (pour information) :**

| Maladie prédite | Score TxGNN | Niveau | Recommandation | Remarque |
|------|------|------|------|------|
| Urticaire au froid | 99,95 % | L3 | Proceed with Guardrails | Petites études et rapports de cas ; la cétirizine réduit les papules induites par le froid de ~50 % dans une étude (PMID 17225008) |
| Maladie de la cavité nasale | 99,77 % | L4 | Research Question | Catégorie trop large ; définir une sous-indication précise |
| Laryngopharyngite aiguë | 99,72 % | L5 | Hold | Aucune preuve ; maladie surtout infectieuse |
| Conjonctivite de la rosacée | 99,41 % | L5 | Hold | Aucune preuve ; adéquation mécanistique faible |
| Dermatite atopique récalcitrante | 99,19 % | L5 | Hold | Aucune preuve ; bénéfice limité des antihistaminiques attendu |

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice officielle (mises en garde, contre-indications) auprès de l'ANSM : donnée bloquante pour le dépistage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par ex. via DrugBank)
- Clarifier la situation réglementaire : toutes les AMM françaises sont annulées, il faut vérifier la disponibilité réelle du produit (y compris sous d'autres noms commerciaux ou en vente libre)
- Un essai randomisé de plus grande taille dans l'urticaire allergique (ou au froid), et la vérification des plans d'étude des articles cités
- Un plan de surveillance de sécurité pour les populations à risque (insuffisance rénale ou hépatique, glaucome, hypertrophie prostatique) et pour l'association avec des dépresseurs du système nerveux central
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

