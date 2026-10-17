---
layout: default
title: Sulindac
parent: Prédiction du modèle uniquement (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sulindac : nouvelle indication prédite, Dysplasie acromésomélique de type Hunter-Thompson (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, spondylarthrite ankylosante, arthrose…"
monitor_inn: "SULINDAC"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "pseudoachondroplasia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "WHIM syndrome", "hypermobility of coccyx"]
---

# Sulindac
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

# Sulindac : Des Rhumatismes Inflammatoires à la Dysplasie Acromésomélique de type Hunter-Thompson

## Résumé en Une Phrase

Le sulindac est un anti-inflammatoire non stéroïdien (AINS) utilisé à l'origine dans des affections ostéo-articulaires comme la polyarthrite rhumatoïde, la spondylarthrite ankylosante, l'arthrose, la bursite, la tendinite et la goutte.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dysplasie acromésomélique de type Hunter-Thompson**, avec un score élevé.
Cependant, **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, spondylarthrite ankylosante, arthrose, bursite, tendinite, goutte (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le sulindac fait partie de la classe des AINS et agit par inhibition des cyclooxygénases (COX), ce qui réduit la production de prostaglandines inflammatoires. Son efficacité symptomatique dans les affections articulaires inflammatoires est établie.

La dysplasie acromésomélique de type Hunter-Thompson est une dysplasie squelettique rare liée à CDMP1/GDF5, impliquant la voie de signalisation des BMP. Aucun lien mécanistique clair n'existe entre l'inhibition de la COX et cette voie. Le score élevé s'explique vraisemblablement par un artefact du graphe de connaissances, par exemple des liaisons via des phénotypes squelettiques ou articulaires communs.

Les autres prédictions les mieux classées vont dans le même sens : brachyolmie (y compris avec amélogenèse imparfaite), myosclérose, pseudoachondroplasie, syndrome brachydactylie-syndactylie, syndrome WHIM, vasculite rhumatoïde et hypermobilité du coccyx. Toutes restent au niveau L5. La vasculite rhumatoïde est la plus proche de l'indication d'origine, mais elle relève d'une immunosuppression (corticoïdes, cyclophosphamide, rituximab) et non des AINS. Pour l'hypermobilité du coccyx, seul un soulagement symptomatique de la douleur serait envisageable.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65862059 | ARTHROCINE 100 mg, comprimé (MEDAC) | Comprimé | Non renseignée (AMM annulée) |
| 62028152 | ARTHROCINE 200 mg, comprimé sécable (MEDAC) | Comprimé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées pour ce rapport. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (à titre indicatif, ne provenant pas du texte de la notice) : hypertension, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, insuffisance cardiaque congestive, ulcère gastroduodénal (dont actif), lupus érythémateux systémique, maladie du tissu conjonctif, troubles de la coagulation, infarctus du myocarde et thrombose coronarienne, maladies cardiovasculaires, anémies et hémoglobinopathies, néphrolithiase, néphropathie urique aiguë, dépendance/abus de substances.
- **Interactions médicamenteuses** : 100 interactions ont été recensées. Parmi les plus représentatives :
  - Modérées : acide acétylsalicylique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), metformine, glimépiride, chlorpropamide, mésalazine, balsalazide, citrate et bicarbonate de potassium, picosulfate de sodium, polyéthylèneglycol avec électrolytes, sulfate de sodium.
  - Mineures : famotidine, ranitidine, cimétidine, linaclotide.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible entre l'inhibition de la COX et la voie GDF5/BMP. De plus, le profil de contre-indications est lourd et il n'existe plus d'AMM active en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données détaillées sur le mécanisme d'action du sulindac.
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité).
- Des données précliniques ou cliniques spécifiques à la dysplasie ciblée ; à défaut, réévaluer des candidats plus plausibles (par exemple la vasculite rhumatoïde) avec des données directes.
- Une clarification du statut réglementaire, aucune AMM n'étant valide actuellement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

