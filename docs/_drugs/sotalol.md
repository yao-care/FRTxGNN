---
layout: default
title: Sotalol
parent: Prédiction du modèle uniquement (L5)
nav_order: 711
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "SOTALOL"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "stroke disorder", "manic bipolar affective disorder", "macrocephaly, dysmorphic facies, and psychomotor retardation"]
description: "Sotalol : nouvelle indication prédite, Syndrome du sinus malade, forme autosomique dominante 2 (sick sinus syndrome 2, autosomal dominant) (niveau de preuve L5). Indication d'origine : Non renseignée…"
---

# Sotalol
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

## Sotalol: Syndrome du sinus malade, forme autosomique dominante 2 (sick sinus syndrome 2, autosomal dominant)
{: .text-alpha }

## Résumé en Une Phrase

Le sotalol est un antiarythmique bêta-bloquant (classe III), initialement utilisé pour le traitement de la **fibrillation auriculaire**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome du sinus malade, forme autosomique dominante 2**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.
Les données compilées indiquent même que ce score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises entre maladies apparentées, et non un réel potentiel thérapeutique ni une preuve biologique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome du sinus malade, forme autosomique dominante 2 (sick sinus syndrome 2, autosomal dominant) |
| Score de Prédiction TxGNN | 0.9976 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Selon les connaissances pharmacologiques générales, le sotalol est un bêta-bloquant doté d'une activité antiarythmique de classe III (blocage des canaux potassiques). Il ralentit la fréquence sinusale et la conduction auriculo-ventriculaire.

**La prédiction ne paraît pas plausible sur le plan mécanistique.** Dans le syndrome du sinus malade, ces effets constituent un problème de sécurité (bradycardie, pauses sinusales) et non un mécanisme thérapeutique. La forme autosomique dominante est liée à des variants du canal HCN4, et rien ne relie le sotalol à la correction de ce défaut. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises entre maladies apparentées (troubles du rythme cardiaque), et non une preuve biologique ; il ne doit pas être interprété comme un soutien thérapeutique.

Il est à noter que, dans le graphe de connaissances, le syndrome du sinus malade (y compris sa forme familiale) figure parmi les **contre-indications** du sotalol.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour cette indication.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 62193524 | SOTALOL SANDOZ 160 mg, comprimé sécable | Comprimé sécable | Active |
| 62519799 | SOTALEX 80 mg, comprimé sécable | Comprimé sécable | Active |
| 64820630 | SOTALEX 160 mg, comprimé sécable | Comprimé sécable | Active |

Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

---

## Considérations de Sécurité

Les données issues de la notice n'étant pas disponibles, les éléments ci-dessous proviennent du graphe de connaissances et des bases d'interactions.

- **Contre-indications (graphe de connaissances, et non texte de notice)** : syndrome du QT long (y compris familial), torsades de pointes, asthme (intrinsèque et allergique), maladie bronchique, carence en potassium, diabète et acidocétose diabétique, hypotension, insuffisance rénale, bloc auriculo-ventriculaire, syndrome du sinus malade (y compris familial), anaphylaxie.
- **Interactions médicamenteuses** (100 interactions recensées ; extrait des principales) :
  - *Majeures* : épinéphrine, clarithromycine, acide picosulfurique, polyéthylène glycol (3350 avec électrolytes).
  - *Modérées* : famotidine, méthscopolamine, hyoscyamine, lopéramide, bupropion, morphine, atropine, bisacodyl, phosphate de calcium, acétate de calcium, canagliflozine, chlorpropamide, cimétidine, dapagliflozine, dicyclomine.
  - *Mineure* : acide acétylsalicylique.

**Point d'attention :** l'indication prédite est précisément un état où le sotalol est contre-indiqué, ce qui constitue un signal de sécurité majeur.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et le mécanisme du sotalol va à l'encontre de l'objectif thérapeutique, le syndrome du sinus malade étant une contre-indication connue.
- Par ailleurs, le médicament est commercialisé en France (3 AMM valides sur 3), mais le dépistage de sécurité ne peut pas avancer faute de données de notice.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (mises en garde et contre-indications) sur le site de l'ANSM.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Réexaminer les autres indications prédites, en particulier l'**AVC** (score 0,9944, niveau L4) : un essai de phase 3 (NCT00007605, 706 participants, terminé) a évalué le sotalol et l'amiodarone dans le maintien du rythme sinusal en fibrillation auriculaire, mais pas la prévention de l'AVC. Ce lien reste indirect, la prévention de l'AVC reposant sur l'anticoagulation.
- Les autres prédictions (syndrome de Wildervanck, sarcoglycanopathie, trouble bipolaire maniaque, syndrome macrocéphalie-dysmorphie-retard psychomoteur, susceptibilité obsolète à l'AVC ischémique) n'ont aucun soutien clinique. Dans le cas du trouble bipolaire, la littérature disponible signale uniquement des risques d'interaction (QT, torsades de pointes) avec les antipsychotiques.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

