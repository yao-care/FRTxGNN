---
layout: default
title: Degarelix
parent: Prédiction du modèle uniquement (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Degarelix : nouvelle indication prédite, Hypertrichose (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "degarelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "allergic urticaria", "cold urticaria", "familial male-limited precocious puberty", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Degarelix
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

## Dégarélix : D'un traitement hormonal à l'hypertrichose (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

Le dégarélix (FIRMAGON) est un antagoniste du récepteur de la GnRH, qui freine la production d'hormones sexuelles par les gonades. Le détail de son indication d'origine n'est pas disponible dans les données compilées pour ce rapport.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**hypertrichose**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Hypertrichose |
| Score de Prédiction TxGNN | 0,9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques générales, le dégarélix bloque le récepteur de la GnRH et réduit la sécrétion de LH et de FSH, ce qui diminue la production d'androgènes par les gonades.

Le lien avec l'hypertrichose est **faible et spéculatif**. Contrairement à l'hirsutisme, l'hypertrichose n'est généralement pas liée aux androgènes : freiner l'axe hormonal n'a donc pas de justification mécanistique claire. Le score très élevé (0,9999) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ; il ne s'appuie sur aucun appui clinique ni bibliographique.

Les autres prédictions du modèle sont du même ordre : la plupart (hypertrichose d'Ambras, malformation de Dandy-Walker, anomalies de la tige pilaire, urticaires, etc.) n'ont pas de lien biologique plausible avec le mécanisme du médicament et peuvent refléter des similarités apprises par le modèle TxGNN (apprentissage profond) entre maladies apparentées, et non une preuve biologique. Deux pistes, plus proches de l'axe hormonal, sont conservées comme simples questions de recherche :
- **Puberté précoce familiale limitée au sexe masculin** : la cause (mutations activatrices du récepteur LHCGR) se situe en aval de l'hypophyse, donc le blocage de la GnRH serait probablement inefficace.
- **Puberté précoce centrale** : mécanisme plausible, mais le traitement de référence repose sur des agonistes de la GnRH bien établis, et le dégarélix n'est pas développé ni validé chez l'enfant.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69784330 | FIRMAGON 120 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM active) |
| 64199102 | DEGARELIX ACCORD 120 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM active) |
| 65505947 | DEGARELIX ACCORD 80 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM active) |
| 63329030 | FIRMAGON 80 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM active) |

## Cytotoxicité

Les données compilées ne permettent pas de classer ce médicament comme antinéoplasique (aucune indication d'origine ni catégorie DrugBank disponibles). Cette section est donc omise.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de la notice) : syndrome du QT long (y compris familial), torsades de pointes, maladie hépatique, maladie de la vésicule biliaire, carence en potassium.
- **Interactions médicamenteuses** : 217 interactions recensées. Les plus notables :
  - **Majeures** : cisapride, dolasétron (risque lié à l'allongement de l'intervalle QT).
  - **Modérées** : clarithromycine, lévofloxacine, ondansétron, granisétron, palonosétron, famotidine, lopéramide, ainsi que plusieurs laxatifs et préparations de lavage intestinal (bisacodyl, picosulfate, macrogol avec électrolytes, lactulose, lactitol, citrate et hydroxyde de magnésium, huile de ricin, glycérine, huile minérale).
  - **Mineure** : métronidazole.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et le lien mécanistique avec l'hypertrichose est faible. Le médicament est commercialisé en France (4 AMM valides sur 4), mais les données de sécurité de la notice manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Confirmer l'indication d'origine et les raisons de l'annulation des AMM.
- Réaliser une revue de la littérature ciblée ; si l'on souhaite explorer les pistes hormonales (puberté précoce), évaluer formellement la justification mécanistique et la sécurité pédiatrique.
- Étudier la sécurité cardiaque (risque d'allongement du QT) au vu des contre-indications du graphe et des interactions majeures.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

