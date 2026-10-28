---
layout: default
title: Disopyramide
parent: Prédiction du modèle uniquement (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Disopyramide : nouvelle indication prédite, Syndrome de Gilles de la Tourette (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées (médicament antiaryth…"
monitor_inn: "DISOPYRAMIDE"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
---

# Disopyramide
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

## Disopyramide : D'un antiarythmique de classe Ia au Syndrome de Gilles de la Tourette
{: .text-alpha }

## Résumé en Une Phrase

Disopyramide est un antiarythmique de classe Ia (bloqueur des canaux sodiques à activité anticholinergique), dont les spécialités françaises sont aujourd'hui toutes annulées.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Gilles de la Tourette**, avec un score très élevé.
Toutefois, **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées (médicament antiarythmique) |
| Nouvelle Indication Prédite | Syndrome de Gilles de la Tourette |
| Score de Prédiction TxGNN | 0,9986 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, le disopyramide fait partie des antiarythmiques de classe Ia : il bloque les canaux sodiques cardiaques et possède une activité anticholinergique.

**En réalité, aucun lien mécanistique établi ne relie le disopyramide au syndrome de Gilles de la Tourette.** Les tics impliquent un dysfonctionnement dopaminergique et des circuits cortico-striato-thalamo-corticaux, sans rapport avec la pharmacologie connue du médicament. Une hypothèse purement spéculative serait que son effet anticholinergique modifie la signalisation cholinergique striatale.

Le score très élevé (0,9986) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ou clinique. Il doit être interprété avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 4 AMM sur 4 sont valides (médicament commercialisé) ; le texte d'indication n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 66198796 | ISORYTHM L.P. 125 mg | Gélule à libération prolongée | Active |
| 63063487 | RYTHMODAN 100 mg | Gélule | Active |
| 66308461 | ISORYTHM L.P. 250 mg | Gélule à libération prolongée | Active |
| 69235837 | RYTHMODAN 250 mg à libération prolongée | Comprimé enrobé | Active |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, non issues du texte de la notice) : syndrome du QT long (y compris familial), insuffisance rénale, maladie hépatique, maladie de la vésicule biliaire, hypokaliémie, hypertrophie bénigne de la prostate, glaucome à angle fermé, myasthénie et maladies de la jonction neuromusculaire, hypoglycémie, hypotension, bloc auriculo-ventriculaire, cardiomyopathies (dont hypertrophique), myocardite, fibrose endomyocardique, fibrillation et flutter auriculaires.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - **Majeures** : citrate de potassium, clarithromycine, acide picosulfurique.
  - **Modérées** : famotidine, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), amphotéricine B, médicaments anticholinergiques (hyoscyamine, atropine, glycopyrronium, clidinium), lopéramide, aprépitant, bisacodyl, chlorpropamide.
  - **Mineure** : cimétidine.
- Dans une population pédiatrique (Tourette, TDAH), les effets indésirables cardiaques et anticholinergiques seraient particulièrement préoccupants.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai, sans publication ni mécanisme plausible, et le médicament n'a plus d'AMM valide en France. Le profil de sécurité (cardiaque et anticholinergique) est défavorable pour cette indication.
- Les autres prédictions du même médicament présentent le même manque de preuves (TDAH, trichotillomanie, etc.). Les seules plus plausibles au niveau de la classe pharmacologique (flutter auriculaire néonatal, tachycardie auriculaire multifocale) restent indirectes (niveau L4) et sans données dédiées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice (mises en garde, contre-indications), actuellement bloquante pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (par ex. via DrugBank)
- Études précliniques démontrant un effet sur les circuits cholinergiques ou dopaminergiques impliqués dans les tics
- Clarification du statut réglementaire, les AMM étant toutes annulées
- Évaluation du rapport bénéfice/risque cardiaque pour une population jeune
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

