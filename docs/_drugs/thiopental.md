---
layout: default
title: Thiopental
parent: Prédiction du modèle uniquement (L5)
nav_order: 754
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "thiopental"
predicted_indications: ["trichotillomania", "Prinzmetal angina", "migraine disorder", "Tourette syndrome", "migraine with brainstem aura", "obsolete bundle branch block", "substance abuse/dependence", "nephrogenic syndrome of inappropriate antidiuresis"]
description: "Thiopental : nouvelle indication prédite, Trichotillomanie (trichotillomania) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Thiopental
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Thiopental: Trichotillomanie (trichotillomania)
{: .text-alpha }

## Résumé en Une Phrase

Le thiopental est un barbiturique injectable, initialement utilisé pour l'épilepsie, la pseudotumeur cérébrale et l'hypertension intracrânienne.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **trichotillomanie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trichotillomanie (trichotillomania) |
| Score de Prédiction TxGNN | 0.9995 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le thiopental est un barbiturique qui renforce l'activité du récepteur GABA-A et exerce ainsi un effet inhibiteur sur le système nerveux central. Cela explique son usage dans l'épilepsie et dans le contrôle de la pression intracrânienne.

Pour la trichotillomanie, aucun lien mécanistique convaincant n'est identifié. Cette affection est prise en charge par des approches comportementales (thérapies cognitivo-comportementales) et des approches sérotoninergiques ou glutamatergiques, et non par la potentialisation GABAergique d'un anesthésique. Le score très élevé (0,9995) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Il convient de noter que la trichotillomanie n'est que la prédiction la mieux classée. Parmi les autres prédictions, **l'épilepsie du lobe frontal** et **l'épilepsie-absence** sont mécanistiquement plus plausibles (niveau L4), mais elles restent dans le même domaine thérapeutique que l'indication d'origine : il s'agirait d'une extension plutôt que d'un véritable repositionnement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour la trichotillomanie.

À titre d'information, pour la deuxième prédiction (épilepsie du lobe frontal), la littérature disponible se limite à des études de cohorte et des cas cliniques, dont aucune n'est un essai contrôlé :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8223422](https://pubmed.ncbi.nlm.nih.gov/8223422/) | 1993 | Cohorte | Epilepsy Research | Test au thiopental chez 103 patients en bilan préchirurgical de l'épilepsie ; outil d'évaluation, pas un traitement |
| [18759609](https://pubmed.ncbi.nlm.nih.gov/18759609/) | 2009 | Cohorte | Journal of Neurosurgery | Absence d'activité épileptique à l'EEG chez des traumatisés crâniens traités selon un protocole ciblant la pression intracrânienne |
| [9805996](https://pubmed.ncbi.nlm.nih.gov/9805996/) | 1998 | Cas clinique | Rinsho Shinkeigaku | État de mal épileptique d'origine frontale traité avec succès par corticoïdes |
| [12446223](https://pubmed.ncbi.nlm.nih.gov/12446223/) | 2002 | Cas clinique | Epileptic Disorders | Chirurgie de l'épilepsie chez un nourrisson en état de mal épileptique dû à une dysplasie corticale |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65708762 | THIOPENTAL VUAB 1 g | Poudre pour solution injectable | Non renseignée (AMM active) |
| 65000261 | THIOPENTAL PANPHARMA 500 mg | Poudre pour solution injectable | Non renseignée (AMM active) |
| 60010084 | THIOPENTAL VUAB 500 mg | Poudre pour solution injectable | Non renseignée (AMM active) |
| 68942457 | THIOPENTAL PANPHARMA 1 g | Poudre pour solution injectable | Non renseignée (AMM active) |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (à confirmer avec la notice, elles ne proviennent pas du texte réglementaire) : insuffisance rénale et urémie, maladie hépatique, maladie de la vésicule biliaire, asthme (y compris allergique et intrinsèque), troubles hypotensifs, anémie, insuffisance surrénalienne (maladie d'Addison, hyperplasie surrénalienne congénitale et formes apparentées), myasthénie et maladies de la jonction neuromusculaire, porphyries (aiguë intermittente et variégée), myxœdème et hypothyroïdie.
- **Interactions médicamenteuses** : 45 interactions recensées. Les plus importantes sont de niveau **majeur** avec l'**éthanol** et la **warfarine**. Plusieurs interactions modérées concernent notamment les opioïdes et dérivés (morphine, codéine, hydrocodone), le dextrométhorphane, les antihistaminiques (cétirizine, carbinoxamine, clémastine), les cannabinoïdes (dronabinol, nabilone), la doxycycline, le nitisinone, le bleu de méthylène et les iodes radioactifs (I-131, I-123).
- **Risque général des barbituriques** (selon les éléments de littérature compilés) : potentiel d'abus et de dépendance, dépression respiratoire, hypotension et dépression myocardique.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la trichotillomanie repose uniquement sur le score du modèle (L5), sans essai, sans littérature ni mécanisme plausible. De plus, le médicament est commercialisé en France (4 AMM valides sur 4) mais les données de sécurité réglementaires sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) ; cette lacune est bloquante.
- Compléter les données de mécanisme d'action (DrugBank).
- Si une piste doit être poursuivie, réorienter l'évaluation vers l'épilepsie du lobe frontal ou les états de mal épileptique réfractaires (niveau L4, mécanisme plausible), en tant que question de recherche.
- Établir un lien mécanistique et des données précliniques pour la trichotillomanie avant toute étude clinique.
- Vérifier la disponibilité réelle du produit en France, compte tenu de l'annulation de toutes les AMM.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

