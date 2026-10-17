---
layout: default
title: Meloxicam
parent: Prédiction du modèle uniquement (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Meloxicam : nouvelle indication prédite, Dysplasie acromésomélique de type Hunter-Thompson (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, arthrose, arthropathie…"
monitor_inn: "meloxicam"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
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

# Méloxicam : Des Maladies Articulaires Inflammatoires à la Dysplasie Acromésomélique de type Hunter-Thompson

## Résumé en Une Phrase

Le méloxicam est un anti-inflammatoire non stéroïdien (AINS) préférentiellement inhibiteur de la COX-2, initialement utilisé dans la polyarthrite rhumatoïde, l'arthrose, les arthropathies, l'arthrite juvénile idiopathique et la spondylarthropathie.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **dysplasie acromésomélique de type Hunter-Thompson**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, arthrose, arthropathie, arthrite juvénile idiopathique, spondylarthropathie (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 12 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le méloxicam est un inhibiteur préférentiel de la COX-2 : il réduit la synthèse des prostaglandines impliquées dans l'inflammation et la douleur. Son utilité est établie dans les pathologies articulaires inflammatoires et dégénératives.

La dysplasie acromésomélique de type Hunter-Thompson est une maladie squelettique rare, due à des variants de perte de fonction du gène GDF5 (voie de signalisation BMP). Le méloxicam n'agit pas sur cette voie. Le score élevé du modèle reflète vraisemblablement une proximité dans le graphe de connaissances avec les atteintes articulaires, et non une justification biologique.

Au mieux, un AINS pourrait soulager symptomatiquement les douleurs articulaires, sans modifier la dysplasie sous-jacente. La prédiction doit donc être considérée comme purement hypothétique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 12 AMM recensées sont toutes annulées ; aucune n'est valide actuellement. Le texte d'indication approuvée n'est pas renseigné dans les données compilées. Les 5 premières AMM sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 63922803 | MELOXICAM TEVA 15 mg, comprimé sécable | Comprimé sécable | Annulée |
| 64115225 | MELOXICAM ZENTIVA 15 mg, comprimé sécable | Comprimé sécable | Annulée |
| 65855762 | MELOXICAM ZENTIVA 7,5 mg, comprimé | Comprimé | Annulée |
| 67044235 | MOBIC 7,5 mg, comprimé | Comprimé | Annulée |
| 60330522 | MELOXICAM BIOGARAN 15 mg, comprimé sécable | Comprimé sécable | Annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, insuffisance rénale ou atteinte rénale, insuffisance cardiaque congestive, maladies cardiovasculaires (infarctus du myocarde, accident vasculaire cérébral, infarctus cérébral, thrombose coronaire), ulcère peptique actif, gastrite, troubles de la coagulation, anémies, diabète et acidocétose diabétique, hyperlipidémie, abus de substances.
- **Interactions médicamenteuses** : 273 interactions recensées. Parmi les premières listées, la plupart sont de niveau modéré : corticoïdes (hydrocortisone, dexamethasone, bétaméthasone, triamcinolone, budésonide), acide acétylsalicylique, metformine, glimépiride, chlorpropamide, mésalazine, balsalazide, aprépitant, vancomycine, kanamycine, ainsi que certains laxatifs et sels de potassium. L'interaction avec le linaclotide est de niveau mineur.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, et sans lien mécanistique plausible entre l'inhibition de la COX-2 et la voie GDF5/BMP.
- Toutes les AMM françaises sont annulées, et le profil de risque cardiovasculaire, rénal et digestif des AINS pèse sur toute extension.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action du méloxicam.
- Mises en garde et contre-indications officielles issues de la notice de l'ANSM (lacune bloquante pour le criblage de sécurité).
- Justification biologique reliant le médicament à la physiopathologie de la dysplasie, ou données précliniques.
- Clarification du statut réglementaire en France (AMM toutes annulées).

**Remarque sur les autres candidats prédits :** les autres prédictions du classement sont également pour la plupart sans preuve (L5). Les entrées « spondylarthropathie, susceptibilité », « nodulose rhumatoïde » et « arthrite juvénile idiopathique polyarticulaire à facteur rhumatoïde positif » sont des variantes d'indications déjà existantes et ne constituent pas de véritables repositionnements. Pour cette dernière, la seule publication disponible (registre de phase 4, 2014) porte sur la sécurité du célécoxib et des AINS non sélectifs dans l'AJI, sans être spécifique au méloxicam.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

