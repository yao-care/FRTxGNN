---
layout: default
title: Glimepiride
parent: Prédiction du modèle uniquement (L5)
nav_order: 365
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Glimepiride : nouvelle indication prédite, Syndrome de la personne raide classique (niveau de preuve L5). Indication d'origine : Diabète de type 2"
monitor_inn: "glimepiride"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Glimépiride : Du diabète de type 2 au syndrome de la personne raide classique

## Résumé en Une Phrase

Le glimépiride est un sulfamide hypoglycémiant, initialement utilisé pour le traitement du diabète de type 2.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la personne raide classique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Diabète de type 2 (le texte d'indication des AMM n'est pas renseigné dans les données compilées ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Syndrome de la personne raide classique |
| Score de Prédiction TxGNN | 99,75 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (dont 0 valide, 20 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances générales, le glimépiride est un sulfamide hypoglycémiant qui bloque les canaux potassiques ATP-dépendants (K-ATP) des cellules bêta pancréatiques et stimule ainsi la sécrétion d'insuline. Son efficacité dans le diabète de type 2 est établie.

Le syndrome de la personne raide est une maladie auto-immune liée aux anticorps anti-GAD65, avec une altération de la signalisation GABAergique. **Aucun lien mécanistique n'est établi** avec le blocage des canaux K-ATP. Le seul rapprochement plausible est la fréquente association du syndrome avec le diabète de type 1 (auto-immunité GAD commune), ce qui ne justifie pas un rôle thérapeutique du glimépiride.

Le score élevé (0,997) reflète donc une proximité dans le graphe de connaissances, et non une preuve clinique. La variante focale (syndrome du membre raide focal) obtient exactement le même score, ce qui suggère que celui-ci provient du voisinage commun dans le graphe plutôt que d'une preuve indépendante.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Les cinq premières sont listées ci-dessous ; le texte d'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 67054585 | Glimépiride Arrow Génériques 2 mg | Comprimé sécable | Annulée |
| 67447122 | Glimépiride Evolugen 3 mg | Comprimé | Annulée |
| 63422748 | Glimépiride Arrow Génériques 3 mg | Comprimé sécable | Annulée |
| 65604468 | Glimépiride Zentiva 2 mg | Comprimé | Annulée |
| 66017203 | Glimépiride EG 2 mg | Comprimé | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance rénale, maladie hépatique, maladie de la vésicule biliaire, insuffisance cardiaque congestive, déficits hypophysaires (dont hypopituitarisme et syndrome de Sheehan), hypogonadisme hypogonadotrope (dont syndrome de Kallmann), déficit en hormone de croissance, ostéoporose (dont post-ménopausique), maladie du thymus et maladies infectieuses.
- **Interactions médicamenteuses** : 599 interactions recensées. Parmi les exemples, la plupart sont de niveau modéré : phénylephrine, acébutolol, acétazolamide, famotidine, ranitidine, acitrétine, formotérol, pseudoéphédrine, kétorolac, épinéphrine, ibuprofène, éthinylestradiol, hydrocortisone, albiglutide, salbutamol, éthanol, nitazoxanide et hydrochlorothiazide. Les corticoïdes topiques (hydrocortisone, alclométasone) sont de niveau mineur.

Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique plausible n'est identifié. De plus, toutes les AMM françaises du glimépiride sont annulées et les données de sécurité de la notice sont manquantes, ce qui empêche l'étape de dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank).
- Mener une recherche bibliographique et d'essais ciblée sur le glimépiride dans le syndrome de la personne raide ; à défaut de signal, ne pas poursuivre.
- Clarifier la situation réglementaire en France (AMM annulées) et la compatibilité des voies d'administration.

**Autres prédictions du modèle (toutes de niveau L5, décision Hold) :** syndrome du membre raide focal, opsismodysplasie, syndrome de dysfonctionnement répondant à la thiamine, lipodystrophie localisée induite par médicament, lipodystrophie centrifuge, lipoatrophie localisée induite par pression, lipodystrophie localisée idiopathique et agénésie pancréatique. Pour l'agénésie pancréatique, le mécanisme est même contradictoire : sans cellules bêta fonctionnelles, un sulfamide hypoglycémiant ne peut être efficace. Seule une publication non pertinente a été retrouvée pour cette dernière.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

