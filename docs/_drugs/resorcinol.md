---
layout: default
title: Resorcinol
parent: Prédiction du modèle uniquement (L5)
nav_order: 662
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
monitor_inn: "resorcinol"
predicted_indications: ["acne keloid", "amyopathic dermatomyositis", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial"]
description: "Resorcinol : nouvelle indication prédite, Acné chéloïdienne (acne keloid) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Resorcinol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Resorcinol: Acné chéloïdienne (acne keloid)
{: .text-alpha }

## Résumé en Une Phrase

Le résorcinol est un agent kératolytique et antiseptique à usage topique, initialement utilisé dans le traitement de l'acné et de certaines dermatites.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**acné chéloïdienne** (acne keloid),
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Acné chéloïdienne (acne keloid) |
| Score de Prédiction TxGNN | 0.9983 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, le résorcinol est un agent kératolytique topique, déjà utilisé dans l'acné. Il favorise l'élimination de la couche cornée et possède une action antiseptique locale.

L'acné chéloïdienne est une affection inflammatoire folliculaire proche de l'acné. Un lien plausible existe donc, fondé sur la similarité des indications. Cependant, il repose uniquement sur le score du modèle TxGNN et sur cette proximité. Aucune donnée mécanistique, aucun essai ni aucune publication ne le confirment.

Les cinq autres prédictions du modèle (dermatomyosite amyopathique, dermatomyosite néonatale, pneumopathie interstitielle de l'enfant associée à une connectivite, acrodermatite chronique atrophiante, hydroa vacciniforme familial) n'ont pas de lien mécanistique crédible avec un kératolytique topique. Leurs scores proviennent du modèle TxGNN (deep learning) et peuvent refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Pour la dermatomyosite néonatale, l'absorption systémique du résorcinol chez le nouveau-né (risque de méthémoglobinémie) constitue en outre une préoccupation de sécurité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 62223316 | SYNTHOL, gel | Gel | Non renseignée | Active |
| 67679220 | SYNTHOL, solution pour application cutanée | Solution pour application | Non renseignée | Active |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : épilepsie, déficit en G6PD, méthémoglobinémie (y compris par déficit en méthémoglobine réductase), sulfhémoglobinémie, maladie rénale, diabète et acidocétose diabétique, arrêt cardiaque soudain, maladie de la conduction cardiaque, insuffisance respiratoire, maladie artérielle périphérique et claudication intermittente, folliculite, dermatite séborrhéique, dermatite, exanthème, verrues communes et infection anogénitale à papillomavirus humain, pyourétère, glycogénose, cystinurie, galactosémie, déficit en pyruvate déshydrogénase E3.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans les données compilées.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Les données de sécurité officielles sont absentes et les deux AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle de l'ANSM (mises en garde et contre-indications) afin de permettre le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (par ex. via DrugBank)
- Réaliser une revue de la littérature et des registres d'essais sur le résorcinol dans l'acné chéloïdienne
- Évaluer l'absorption systémique et le risque de méthémoglobinémie, en particulier pour les peaux lésées et les populations pédiatriques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

