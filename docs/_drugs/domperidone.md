---
layout: default
title: Domperidone
parent: Prédiction du modèle uniquement (L5)
nav_order: 254
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Domperidone : nouvelle indication prédite, Syndrome néphrogénique d'antidiurèse inappropriée (niveau de preuve L5). Indication d'origine : Non précisée dans les données d'AMM (usage clinique connu : …"
monitor_inn: "domperidone"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Domperidone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Dompéridone : Du traitement symptomatique des troubles digestifs au Syndrome néphrogénique d'antidiurèse inappropriée

## Résumé en Une Phrase

La dompéridone est un antagoniste périphérique des récepteurs dopaminergiques D2/D3, utilisé pour prendre en charge la dyspepsie, les brûlures d'estomac, les douleurs épigastriques, les nausées et les vomissements.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée (NSIAD)**,
mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM (usage clinique connu : dyspepsie, nausées, vomissements) |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée |
| Score de Prédiction TxGNN | 99,08 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 12 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations pharmacologiques connues, la dompéridone agit comme antagoniste des récepteurs dopaminergiques D2 (gène DRD2) et D3 (gène DRD3), principalement en périphérie.

Le NSIAD est causé par des mutations gain de fonction du gène du récepteur V2 de la vasopressine (AVPR2). Ces mutations rendent le récepteur actif en permanence, avec rétention d'eau malgré une vasopressine indétectable. La dompéridone n'a aucune action directe connue sur le récepteur V2 ni sur la voie AMPc/aquaporine-2 en aval.

Le lien reste donc **spéculatif**. Il pourrait passer par des effets indirects sur la sécrétion de vasopressine (la dopamine module la sécrétion d'AVP) ou sur la prolactine. Cependant, un antagonisme dopaminergique ne devrait pas contrecarrer un récepteur constitutivement actif indépendamment de son ligand. Le score élevé reflète probablement une proximité dans le graphe de connaissances plutôt qu'une relation biologique réelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 12 AMM recensées sont toutes annulées ; le texte de l'indication approuvée n'est pas renseigné. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69742865 | MOTILIUM 1 mg/ml, suspension buvable (Janssen Cilag) | Suspension buvable | Annulée |
| 63333858 | DOMPERIDONE BIOGARAN 10 mg (Biogaran) | Comprimé orodispersible | Annulée |
| 63679194 | MOTILIUM 10 mg (Janssen Cilag) | Comprimé pelliculé | Annulée |
| 62128302 | DOMPERIDONE ARROW 10 mg (Arrow Génériques) | Comprimé orodispersible | Annulée |
| 63394334 | DOMPERIDONE BIOGARAN 10 mg (Biogaran) | Comprimé pelliculé | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : syndrome du QT long, syndrome du QT long familial, torsades de pointes, maladie hépatique, maladie de la vésicule biliaire.
- **Interactions et cibles pharmacologiques** : antagonisme des récepteurs D2 (DRD2) et D3 (DRD3). Aucune interaction médicamenteuse de niveau clinique n'est renseignée.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et le mécanisme est biologiquement peu plausible pour une mutation activatrice du récepteur V2.
- Le profil de risque cardiaque (QT long, torsades de pointes) et l'absence d'AMM valide en France s'ajoutent à ces réserves.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde, contre-indications), étape bloquante pour l'évaluation de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (via DrugBank)
- Rechercher des données précliniques ou des cas rapportés reliant la dompéridone à la régulation de la vasopressine ou au NSIAD
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication d'origine (en attente)
- Clarifier le rapport bénéfice-risque cardiaque pour une éventuelle population de patients atteints de NSIAD
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

