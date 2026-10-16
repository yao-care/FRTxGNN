---
layout: default
title: Lidocaine
parent: Prédiction du modèle uniquement (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lidocaine : nouvelle indication prédite, Kératoconjonctivite ponctuée épithéliale (niveau de preuve L5). Indication d'origine : Dermatite, névralgie, névralgie post-zostérienne, hémorroïdes, gale…"
---

# Lidocaine
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

# Lidocaïne : De l'anesthésie locale et des douleurs neuropathiques à la kératoconjonctivite ponctuée épithéliale

## Résumé en Une Phrase

La lidocaïne est un anesthésique local, bloqueur des canaux sodiques, utilisé à l'origine dans des indications telles que les névralgies (dont la névralgie post-zostérienne), les hémorroïdes, la dermatite et diverses affections cutanées parasitaires.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **kératoconjonctivite ponctuée épithéliale**, avec un score très élevé mais **aucun essai clinique et aucune publication** soutenant directement cette prédiction.
Le niveau de preuve est donc très faible (L5) : il s'agit d'une prédiction issue du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dermatite, névralgie, névralgie post-zostérienne, hémorroïdes, gale, pédiculose (indications issues du graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Kératoconjonctivite ponctuée épithéliale |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la lidocaïne est un bloqueur des canaux sodiques voltage-dépendants : elle empêche la propagation de l'influx nerveux et produit une anesthésie locale.

Le lien avec la nouvelle indication est faible. Un anesthésique topique peut soulager la douleur de la surface oculaire, mais il ne traite pas la cause inflammatoire ou infectieuse de la kératoconjonctivite. De plus, l'usage topique prolongé d'anesthésiques est connu pour être toxique pour l'épithélium cornéen. Le score élevé du modèle reflète donc une association dans le graphe de connaissances, et non un mécanisme thérapeutique plausible.

D'autres prédictions du même modèle sont à noter à titre de comparaison : pour la **conjonctivite atopique** (niveau L4), une étude préclinique de 2023 suggère un rôle des nerfs sensoriels dans le passage des allergènes, ce qui constitue une piste de recherche indirecte, sans essai thérapeutique. Pour la **kératoconjonctivite ponctuée épithéliale**, aucune donnée de ce type n'existe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la kératoconjonctivite ponctuée épithéliale.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Les 5 premières sont présentées ci-dessous (le texte d'indication approuvée n'est pas renseigné dans les données).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 63572616 | MESOCAÏNE 50 mg/5 ml | Solution injectable | Annulée |
| 66290522 | LIDOCAINE AGUETTANT 20 mg/ml sans conservateur | Solution injectable | Annulée |
| 65191044 | XYLOCONTACT, crème pour usage dentaire | Crème pour usage dentaire | Annulée |
| 65538840 | VERSATIS 700 mg | Emplâtre médicamenteux | Annulée |
| 61164434 | LIDOCAÏNE KABI 20 mg/ml | Solution injectable | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, insuffisance hépatique, cirrhose, épilepsie, maladie rénale, hypothyroïdie, insuffisance surrénalienne, glaucome à angle ouvert, kératite herpétique, infection à varicelle-zona, troubles psychotiques, infections fongiques, dermatophytose, ostéoporose, gastrite, carence en potassium, entre autres.
- **Interactions médicamenteuses** : 534 interactions recensées. Parmi les principales : **majeure** avec le bupropion ; **modérées** avec l'aprépitant, la cimétidine, la morphine liposomale, l'acide obéticholique, le polyéthylène glycol (3350 avec électrolytes), l'acide picosulfurique et le sulfate de sodium ; mineures avec la dexaméthasone, la kanamycine, la néomycine, l'oméprazole, la streptomycine et la troglitazone.
- **Signaux de la littérature** : effets indésirables neuropsychiatriques et cardiaques de la lidocaïne intraveineuse (revue de 2009) ; cas de méthémoglobinémie chez un enfant avec usage topique de lidocaïne associé à d'autres médicaments ; risque de toxicité cornéenne lors d'un usage topique oculaire prolongé.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et le mécanisme d'action de la lidocaïne ne traite pas les causes de la kératoconjonctivite ; l'usage oculaire prolongé comporte un risque de toxicité cornéenne.
- Toutes les AMM françaises sont annulées, ce qui complique toute voie réglementaire immédiate.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice officielle (mises en garde et contre-indications) auprès de l'ANSM : lacune bloquante pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études précliniques ou cliniques directes sur la surface oculaire, avec évaluation de la toxicité épithéliale
- Examen de pistes plus plausibles parmi les prédictions du modèle, notamment la conjonctivite atopique (hypothèse neuro-immune, niveau L4)
- Clarification de la voie d'administration et de la formulation ophtalmique requise
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

