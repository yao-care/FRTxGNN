---
layout: default
title: Clarithromycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 177
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
monitor_inn: "clarithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
description: "Clarithromycin : nouvelle indication prédite, Syndrome d'hyperviscosité polyclonale (polyclonal hyperviscosity syndrome) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données …"
---

# Clarithromycin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Clarithromycin: Syndrome d'hyperviscosité polyclonale (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Résumé en Une Phrase

La clarithromycine est un antibiotique de la famille des macrolides, utilisé à l'origine pour traiter des infections bactériennes (otite moyenne infectieuse, pneumonies, sinusite maxillaire, infections à streptocoques et à staphylocoques).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome d'hyperviscosité polyclonale**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome d'hyperviscosité polyclonale (polyclonal hyperviscosity syndrome) |
| Score de Prédiction TxGNN | 0.9935 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la clarithromycine est un antibiotique macrolide, dont l'efficacité dans les infections respiratoires et ORL est établie. Elle est également connue pour des effets immunomodulateurs (modulation de la production de cytokines et de l'activité des lymphocytes B et plasmocytes).

Ces effets pourraient théoriquement être rapprochés d'un syndrome d'hyperviscosité lié à une production excessive d'immunoglobulines. Toutefois, aucune donnée compilée pour ce rapport ne relie la clarithromycine au syndrome d'hyperviscosité polyclonale. Le score élevé du modèle (0,9935) reste une prédiction computationnelle, sans soutien clinique ou bibliographique. Le lien mécanistique est donc **non étayé** à ce stade.

Pour information, les autres indications prédites sont l'hyperamylasémie (score 0,9935), l'analbuminémie congénitale (0,9921), la kératoconjonctivite épithéliale ponctuée (0,9911) et l'incompatibilité de groupe sanguin (0,9907). Parmi elles, seule la kératoconjonctivite épithéliale ponctuée présente un lien plausible, mais indirect : les macrolides ont des propriétés anti-inflammatoires utilisées dans les atteintes de la surface oculaire liées aux glandes de Meibomius, avec toutefois des données surtout pour l'azithromycine.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le syndrome d'hyperviscosité polyclonale.

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Le texte d'indication approuvée n'est pas renseigné pour ces AMM. Les cinq premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65880178 | CLARITHROMYCINE VIATRIS 25 mg/ml | Granulés pour suspension buvable | Non renseignée (AMM active) |
| 69132627 | CLARITHROMYCINE SUN 500 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 65040811 | CLARITHROMYCINE ARROW 50 mg/mL | Granulés pour suspension buvable | Non renseignée (AMM active) |
| 67997205 | ZECLAR 500 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 67197409 | CLARITHROMYCINE VIATRIS 250 mg | Comprimé pelliculé | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non le texte de la notice) : syndrome du QT long, torsades de pointes, tachycardie ventriculaire, insuffisance hépatique et maladies hépatiques, cholestase, porphyries, maladie rénale, maladie de la vésicule biliaire, ostéoporose et fractures, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, myasthénie grave et maladies de la jonction neuromusculaire, mononucléose infectieuse.
- **Interactions médicamenteuses** : 822 interactions recensées. Parmi les exemples : interactions **majeures** avec l'abémaciclib, le fentanyl et l'acalabrutinib ; interactions **modérées** avec le paclitaxel, l'abiratérone, le tramadol, la nifédipine, l'adénosine, l'afatinib, l'éthinylestradiol et l'hydrocortisone ; interactions **mineures** avec le dolutégravir, la zidovudine et la loratadine.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le syndrome d'hyperviscosité polyclonale repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication ni lien mécanistique documenté.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Réaliser une revue de la littérature ciblée sur la clarithromycine et les syndromes d'hyperviscosité ou les troubles plasmocytaires
- Clarifier la situation réglementaire (raisons de l'annulation des AMM, disponibilité réelle en France)
- Si une piste alternative est explorée, vérifier le texte intégral de la publication PMID 38472959 pour la kératoconjonctivite épithéliale ponctuée (niveau L4, à traiter comme question de recherche)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

