---
layout: default
title: Metreleptin
parent: Prédiction du modèle uniquement (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptine : De la lipodystrophie congénitale à la lentiginose généralisée familiale

## Résumé en Une Phrase

La metreleptine est un analogue de la leptine, initialement utilisée pour traiter les lipodystrophies (notamment la lipodystrophie congénitale généralisée, ou syndrome de Berardinelli-Seip).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **lentiginose généralisée familiale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction, qui reste purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Lipodystrophie congénitale généralisée (Berardinelli-Seip), lipodystrophie (source : graphe de connaissances, le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Lentiginose généralisée familiale |
| Score de Prédiction TxGNN | 99,71 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la metreleptine est un analogue de la leptine : elle corrige le déficit en leptine observé dans les lipodystrophies, où le tissu adipeux est absent ou insuffisant.

Le lien avec la lentiginose généralisée familiale, un trouble pigmentaire rare, n'est pas évident. Aucun mécanisme plausible reliant la voie de la leptine à ce trouble n'a pu être identifié à partir des données compilées. Le score élevé reflète vraisemblablement une proximité dans le réseau de connaissances (annotations communes de maladies rares, notamment génodermatoses) plutôt qu'une réalité biologique.

Il convient donc de considérer cette prédiction avec prudence : un score élevé ne remplace pas une preuve clinique ou mécanistique.

Les autres indications prédites (rangs 2 à 10) présentent le même profil : score supérieur à 99,5 %, aucune preuve clinique, niveau L5 et recommandation Hold. Parmi elles, le **syndrome de leuconychie totale-lésions de type acanthosis nigricans** repose sur un argument phénotypique faible (résistance à l'insuline, commune aux lipodystrophies), qui reste spéculatif. Pour la **tumeur rhabdoïde**, la leptine ayant des effets pro-prolifératifs dans certains cancers, un risque de sécurité ne peut être exclu et nécessiterait un examen approfondi.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 67974594 | MYALEPTA 5,8 mg | Poudre pour solution injectable | Non renseignée | Annulée |
| 69994784 | MYALEPTA 11,3 mg | Poudre pour solution injectable | Non renseignée | Annulée |
| 60446726 | MYALEPTA 3 mg | Poudre pour solution injectable | Non renseignée | Annulée |

Titulaire : CHIESI FARMACEUTICI. Aucune AMM n'est actuellement valide en France.

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 145 interactions ont été recensées. Les principales, de niveau modéré, concernent notamment l'abémaciclib, le fentanyl, l'acalabrutinib, l'éthinylestradiol, l'alfentanil, l'alpélisib, la noréthistérone, le désogestrel, l'avapritinib, le bictégravir, le brigatinib, la buspirone, le cabozantinib, le capmatinib, la cariprazine, le céritinib et le chlorpropamide. L'interaction avec le bortézomib est de niveau mineur.
- Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible entre la leptine et la lentiginose généralisée familiale. Toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications issues de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Une hypothèse biologique justifiant le lien avec la nouvelle indication, puis des études précliniques ou des cas cliniques
- Une clarification du statut réglementaire en France (AMM annulées)
- Une évaluation spécifique du risque pro-prolifératif avant toute considération en oncologie
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

