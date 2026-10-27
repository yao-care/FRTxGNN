---
layout: default
title: Flubendazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Flubendazole : nouvelle indication prédite, Carcinome de la vessie (urinary bladder carcinoma) (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées (texte d'indicatio…"
monitor_inn: "FLUBENDAZOLE"
predicted_indications: ["urinary bladder carcinoma", "urinary bladder neoplasm", "infiltrating bladder urothelial carcinoma", "non-invasive bladder urothelial carcinoma", "bladder urachal urothelial carcinoma", "bladder squamous papilloma", "bladder signet ring cell adenocarcinoma", "bladder colloid adenocarcinoma", "bladder mixed adenocarcinoma", "bladder colonic type adenocarcinoma"]
---

# Flubendazole
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

## Flubendazole : D'un antiparasitaire à usage humain au carcinome de la vessie
{: .text-alpha }

## Resume en Une Phrase

Flubendazole est un antihelminthique de la famille des benzimidazoles, commercialisé en France sous les noms FLUVERMAL (comprimé et suspension buvable), dont les deux AMM sont aujourd'hui annulées.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **carcinome de la vessie** (urinary bladder carcinoma).
Aucun essai clinique n'est enregistré, et les deux seules publications liées à la tumeur de la vessie portent sur le fenbendazole (un composé voisin), et non sur le flubendazole : la prédiction repose donc essentiellement sur le modèle.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées (texte d'indication vide pour les deux AMM) |
| Nouvelle Indication Predite | Carcinome de la vessie (urinary bladder carcinoma) |
| Score de Prediction TxGNN | 99,99 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marche en France | Uniquement annulé (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Decision Recommandee | Hold |

Remarque : pour la tumeur de la vessie au sens large (« urinary bladder neoplasm », 2e prédiction), le niveau de preuve est L4 (deux études précliniques indirectes sur le fenbendazole), avec la mention « question de recherche ».

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances générales, le flubendazole fait partie des benzimidazoles antihelminthiques, qui se lient à la tubuline et perturbent la polymérisation des microtubules. Ce mécanisme est plausiblement pertinent pour la prolifération des cellules cancéreuses, car les microtubules sont indispensables à la division cellulaire.

Le lien avec l'indication d'origine reste indirect : le flubendazole était utilisé contre les parasites intestinaux, et la prédiction vers un cancer relève d'un raisonnement de classe pharmacologique, non d'une preuve directe. Le score très élevé du modèle (99,99 %) est à interpréter avec prudence : de nombreuses tumeurs de la vessie, y compris des sous-types rares (adénocarcinome colloïde, urachal, papillome malpighien bénin), obtiennent des scores quasi identiques, ce qui suggère une propagation à partir du nœud général « cancer de la vessie » dans le graphe de connaissances plutôt qu'une biologie spécifique à chaque sous-type.

Les deux publications disponibles (2024 et 2026) concernent le fenbendazole, un benzimidazole structurellement proche : l'une associe l'induction de ferroptose à une photothérapie thermique et à une double immunothérapie, l'autre associe le fenbendazole en instillation intravésicale à CRISPR-Cas13a. Elles semblent précliniques d'après leur titre (résumés non examinés). Elles soutiennent une plausibilité de classe, mais pas une efficacité du flubendazole.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Litterature

Aucune publication portant sur le flubendazole dans cette indication n'est disponible. Les deux références suivantes, liées à la tumeur de la vessie, concernent le **fenbendazole** (preuve indirecte, précliniques d'après le titre) :

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [41861111](https://pubmed.ncbi.nlm.nih.gov/41861111/) | 2026 | Préclinique (déduit du titre) | Advanced Science | Nanoplateforme intravésicale combinant fenbendazole, ferroptose, activation de la mort cellulaire immunogène et photothérapie thermique contre le cancer de la vessie |
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | Préclinique (déduit du titre) | J Exp Clin Cancer Res | Instillation intravésicale synergique associant CRISPR-Cas13a et fenbendazole dans le cancer de la vessie |

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 68636624 | FLUVERMAL 2 POUR CENT, suspension buvable (KENVUE FRANCE) – annulée | Suspension buvable | Non renseignée |
| 60968336 | FLUVERMAL, comprimé (KENVUE FRANCE) – annulée | Comprimé | Non renseignée |

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées, et aucune contre-indication issue du graphe de connaissances n'est signalée.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) pour le carcinome de la vessie ; aucun essai clinique n'existe et les seules publications concernent le fenbendazole, non le flubendazole. Les données de sécurité issues de la notice font défaut, ce qui bloque l'évaluation de sécurité, et aucune AMM n'est valide en France.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications) afin de pouvoir réaliser le criblage de sécurité
- Obtenir les données de mécanisme d'action depuis DrugBank
- Rechercher des études précliniques spécifiques au flubendazole dans le cancer de la vessie (lignées cellulaires, modèles animaux)
- Vérifier la faisabilité d'une voie intravésicale ou autre, la compatibilité de voie d'administration n'étant pas évaluée
- Clarifier l'indication d'origine et le statut réglementaire (AMM annulées)
- Prioriser le carcinome urothélial et la tumeur de la vessie au sens large plutôt que les sous-types rares ou bénins, dont les scores semblent artefactuels
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

