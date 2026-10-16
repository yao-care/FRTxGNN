---
layout: default
title: Piroxicam
parent: Prédiction du modèle uniquement (L5)
nav_order: 611
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Piroxicam : nouvelle indication prédite, Syndrome de microphtalmie colobomateuse-dysplasie rhizomélique (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, arthrose"
monitor_inn: "PIROXICAM"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
---

# Piroxicam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Piroxicam : De la polyarthrite rhumatoïde au syndrome de microphtalmie colobomateuse-dysplasie rhizomélique

## Résumé en Une Phrase

Piroxicam est un anti-inflammatoire non stéroïdien (AINS), utilisé à l'origine dans la polyarthrite rhumatoïde et l'arthrose.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **syndrome de microphtalmie colobomateuse-dysplasie rhizomélique**, une maladie génétique rare du développement.
**Aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction, qui repose uniquement sur le score du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, arthrose (d'après le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome de microphtalmie colobomateuse-dysplasie rhizomélique |
| Score de Prédiction TxGNN | 99,996 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 13 (dont 13 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, piroxicam fait partie de la classe des AMNS inhibiteurs de la cyclo-oxygénase (COX-1/COX-2). Son efficacité dans les maladies articulaires inflammatoires est établie. Il réduit la synthèse des prostaglandines, ce qui diminue l'inflammation et la douleur.

Pour la nouvelle indication prédite, **aucun lien mécanistique plausible n'a été identifié**. Cette maladie est un syndrome génétique rare du développement, touchant le squelette et l'œil. L'inhibition de la COX n'a pas de rôle connu dans sa physiopathologie. Le score élevé reflète probablement des annotations musculo-squelettiques partagées dans le graphe de connaissances, plutôt qu'un véritable signal thérapeutique.

Les autres prédictions les mieux classées vont dans le même sens. Il s'agit surtout de dysplasies squelettiques génétiques (brachydactylie-syndactylie, dysplasie acromésomélique de type Hunter-Thompson, brachyolmie, pseudoachondroplasie), sans preuve ni lien mécanistique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de Marché en France

Les 13 AMM de piroxicam sont annulées. Les 5 premières sont listées ci-dessous. Le texte d'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67214342 | FELDENE DISPERSIBLE 20 mg (Pfizer) | Comprimé dispersible sécable | Non précisée |
| 68659391 | PIROXICAM BIOGARAN 10 mg | Gélule | Non précisée |
| 62408891 | PIROXICAM PFIZER 20 mg/1 ml (IM) | Solution injectable | Non précisée |
| 67785736 | PIROXICAM VIATRIS 20 mg | Comprimé dispersible sécable | Non précisée |
| 69721369 | PIROXICAM TEVA 20 mg/1 ml (IM) | Solution injectable | Non précisée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) :
  - Cardiovasculaires : hypertension, insuffisance cardiaque congestive, infarctus du myocarde, thrombose coronarienne, AVC et infarctus cérébral, maladie thrombotique.
  - Rénales et hépatiques : maladie rénale, maladie hépatique, hépatite, insuffisance hépatique aiguë, atteinte hépatique d'origine médicamenteuse, maladie de la vésicule biliaire.
  - Hématologiques : troubles de la coagulation, anémies, hémoglobinopathie.
  - Gastro-intestinales : ulcère gastroduodénal actif.
  - Autres : troubles de la vision et cécité, abus ou dépendance à une substance.
- **Interactions médicamenteuses** : 100 interactions sont recensées. Parmi les principales :
  - Niveau modéré : acide acétylsalicylique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), metformine, glimépiride, chlorpropamide, mésalazine, balsalazide, aprépitant, citrate et bicarbonate de potassium.
  - Niveau mineur : famotidine, ranitidine, cimétidine, linaclotide.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5), sans essai clinique, sans publication ni lien mécanistique plausible avec l'inhibition de la COX.
- Toutes les AMM françaises sont annulées, et le profil de risque cardiovasculaire, rénal, hépatique et digestif est défavorable.

**Piste alternative à noter :** parmi les prédictions de rang inférieur, l'**arthrite juvénile idiopathique** (rang 10, score 99,93 %) est biologiquement cohérente avec l'indication d'origine. Son niveau de preuve est L3, avec 10 publications :
- Deux méta-analyses en réseau sur les AINS (2021, 2024) qui comparent la classe sans être spécifiques au piroxicam.
- Une étude de 1987 comparant piroxicam et naproxène chez 26 patients, avec attribution aléatoire.
- Une étude multicentrique de 1986 comparant les deux produits chez 47 enfants.
- Une étude pharmacocinétique pédiatrique de 1991.

Ces études sont anciennes, antérieures aux biothérapies. Cette piste relève d'une question de recherche (« Research Question ») plutôt que d'une décision Go.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de piroxicam.
- Mises en garde et contre-indications officielles de la notice (ANSM).
- Pour le syndrome prédit : une justification biologique indépendante du graphe (modèles précliniques) avant tout investissement clinique.
- Pour l'arthrite juvénile idiopathique : une revue ciblée des données pédiatriques spécifiques au piroxicam, comparée aux alternatives actuelles.
- Clarification du statut réglementaire, puisqu'aucune AMM n'est en vigueur en France.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

