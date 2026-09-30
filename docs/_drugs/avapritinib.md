---
layout: default
title: Avapritinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib : De l'indication d'origine (non renseignée) à la dysplasie spondylométaphysaire axiale

## Résumé en Une Phrase

L'avapritinib est un inhibiteur de kinases (KIT et PDGFRA) commercialisé en France sous le nom AYVAKYT. Les données transmises ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dysplasie spondylométaphysaire axiale**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Dysplasie spondylométaphysaire axiale |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 5 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, l'avapritinib inhibe les kinases KIT et PDGFRA. Son indication d'origine n'est pas renseignée dans les données réglementaires reçues.

Pour cette prédiction, **aucun lien mécanistique plausible n'a été identifié**. La dysplasie spondylométaphysaire axiale est une maladie squelettique, et aucune connexion n'est connue entre les voies KIT/PDGFRA et la voie de cette dysplasie. Le score TxGNN très élevé (0,9992) reflète une proximité dans le graphe de connaissances, pas une preuve biologique ou clinique.

La similarité avec l'indication d'origine n'a pas pu être évaluée, faute de données. Cette prédiction doit donc être considérée comme une simple hypothèse issue du modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de Marché en France

L'indication approuvée n'est pas renseignée dans les données reçues pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|------|
| 63189920 | AYVAKYT 200 mg | Comprimé pelliculé | Blueprint Medicines (Pays-Bas) |
| 63220091 | AYVAKYT 50 mg | Comprimé pelliculé | Blueprint Medicines (Pays-Bas) |
| 65304816 | AYVAKYT 300 mg | Comprimé pelliculé | Blueprint Medicines (Pays-Bas) |
| 68115906 | AYVAKYT 25 mg | Comprimé pelliculé | Blueprint Medicines (Pays-Bas) |
| 64069767 | AYVAKYT 100 mg | Comprimé pelliculé | Blueprint Medicines (Pays-Bas) |

## Cytotoxicité

L'avapritinib est un inhibiteur de kinases à visée antinéoplasique. Cette classification repose sur sa classe pharmacologique, car les catégories DrugBank et l'indication d'origine ne figurent pas dans le dossier.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de KIT/PDGFRA) |

Veuillez consulter les mises en garde et précautions de la notice pour le risque de myélosuppression, l'émétogénicité, la surveillance biologique et les mesures de protection lors de la manipulation.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Pour la seule hypothèse relative au cerveau (polymicrogyrie), l'analyse de rationalité mentionne des alertes neurologiques centrales de l'avapritinib (hémorragie intracrânienne, effets cognitifs). Ces éléments doivent être vérifiés dans la notice ANSM.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Cette prédiction repose uniquement sur le score du modèle (L5), sans essai clinique, sans publication et sans lien mécanistique plausible entre KIT/PDGFRA et cette dysplasie squelettique.
- Les données de sécurité de la notice ANSM manquent, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications).
- Compléter le mécanisme d'action et l'indication d'origine via DrugBank.
- Consolider dans l'analyse les entrées redondantes de la sclérose latérale amyotrophique (SLA, formes de susceptibilité et de type 22). Parmi les autres prédictions, seule la SLA est classée « Research Question » : l'hypothèse (modulation des mastocytes et de la neuroinflammation par les inhibiteurs de KIT) reste indirecte, et toute exploration devrait commencer par des travaux précliniques.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

