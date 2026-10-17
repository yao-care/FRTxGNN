---
layout: default
title: Candesartan Cilexetil
parent: Prédiction du modèle uniquement (L5)
nav_order: 134
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Candesartan Cilexetil : nouvelle indication prédite, Hypertension rénovasculaire maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle"
monitor_inn: "candesartan cilexetil"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Candesartan Cilexetil
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Candésartan cilexétil : De l'hypertension à l'hypertension rénovasculaire maligne

## Résumé en Une Phrase

Le candésartan cilexétil est un antagoniste des récepteurs de l'angiotensine II (sartan), initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**, mais **aucun essai clinique** ni **aucune publication** directement pertinente ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (d'après les relations d'indication du graphe de connaissances ; aucun texte d'indication n'est renseigné dans les AMM) |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99,68 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le candésartan cilexétil fait partie de la classe des antagonistes des récepteurs AT1 de l'angiotensine II, son efficacité dans l'hypertension est établie, et mécanistiquement il pourrait être applicable à l'hypertension rénovasculaire.

L'hypertension rénovasculaire est dominée par l'activation du système rénine-angiotensine (SRA). Bloquer le récepteur AT1 est donc biologiquement plausible. Toutefois, les sartans comportent un risque connu en cas de sténose bilatérale des artères rénales (insuffisance rénale aiguë, baisse du débit de filtration glomérulaire), ce qui impose une réflexion prudente sur le profil de sécurité dans ce contexte.

Le score très élevé (0,997) reflète probablement la proximité avec l'indication déjà approuvée (hypertension) dans le graphe de connaissances, et non une preuve indépendante. La deuxième prédiction (maladie rénale hypertensive maligne) est essentiellement une forme sévère de l'hypertension déjà traitée : elle relève davantage d'un rappel de pharmacologie connue que d'un véritable signal de repositionnement. Les autres prédictions (hypertension pulmonaire de mécanisme multifactoriel, hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie, syndrome de Braddock) sont encore moins étayées ; la dernière semble être un artefact du graphe de connaissances.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour l'hypertension rénovasculaire maligne.

À titre d'information, deux publications précliniques ont été rattachées à une autre prédiction (hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie), sans soutien clinique direct :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31396238](https://pubmed.ncbi.nlm.nih.gov/31396238/) | 2019 | Préclinique (souris) | Frontiers in Immunology | Le candésartan cilexétil améliore les résultats neurologiques dans un modèle murin d'hypoxie néonatale (effet anti-inflammatoire ; pas d'atteinte pulmonaire étudiée) |
| [21423692](https://pubmed.ncbi.nlm.nih.gov/21423692/) | 2011 | Préclinique (rat) | Evid Based Complement Alternat Med | Effet de l'hachimijiogan (autre composé) sur la dysfonction rénale et HIF-1α dans un modèle de rein restant, comparé à un sartan |

---

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Les 5 premières sont listées ci-dessous ; aucun texte d'indication n'est renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64358070 | CANDESARTAN HCS 8 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |
| 65969730 | ATACAND 4 mg, comprimé sécable | Comprimé sécable | Non renseignée (AMM annulée) |
| 65776902 | CANDESARTAN ARROW 4 mg, comprimé sécable | Comprimé sécable | Non renseignée (AMM annulée) |
| 66847149 | CANDESARTAN ARROW LAB 16 mg, comprimé sécable | Comprimé sécable | Non renseignée (AMM annulée) |
| 62910207 | ATACAND 32 mg, comprimé sécable | Comprimé sécable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : pancréatite, maladie hépatique, maladie de la vésicule biliaire, lupus érythémateux systémique (y compris pédiatrique), carence en potassium, diabète et acidocétose diabétique, hyperuricémie, goutte, hypotension, hyperparathyroïdie, ostéite fibreuse, coma et encéphalopathie hépatiques, ictère néonatal, anurie, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, obstruction de l'artère rénale, insuffisance rénale.
- **Point d'attention propre à l'indication prédite** : risque d'insuffisance rénale aiguë en cas de sténose bilatérale des artères rénales. L'obstruction de l'artère rénale figure d'ailleurs parmi les contre-indications du graphe, ce qui est en tension directe avec l'indication rénovasculaire prédite.

Pour les mises en garde et contre-indications officielles ainsi que les interactions médicamenteuses, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pertinente. Le score élevé traduit surtout la proximité avec l'indication hypertension, et un signal de sécurité potentiel (obstruction de l'artère rénale) va à l'encontre de l'indication prédite. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (à récupérer depuis DrugBank)
- Mises en garde et contre-indications officielles de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Revue de la littérature clinique sur les sartans dans l'hypertension rénovasculaire, en particulier selon la sténose unilatérale ou bilatérale
- Clarification du statut commercial actuel du candésartan en France
- Évaluation de la pertinence clinique réelle de cette indication (forme sévère de l'hypertension déjà traitée, où la prise en charge aiguë repose en général sur d'autres agents)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

