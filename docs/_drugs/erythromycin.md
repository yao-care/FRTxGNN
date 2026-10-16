---
layout: default
title: Erythromycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 297
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Erythromycin : nouvelle indication prédite, Kératoconjonctivite épithéliale ponctuée (niveau de preuve L5). Indication d'origine : Acné, otite moyenne infectieuse, infections à streptocoques…"
---

# Erythromycin
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

# Érythromycine : Des infections bactériennes (acné, otite, pneumonie…) à la kératoconjonctivite épithéliale ponctuée

## Résumé en Une Phrase

L'érythromycine est un antibiotique de la famille des macrolides, initialement utilisé contre de nombreuses infections bactériennes (acné, otite moyenne infectieuse, pneumonies, infections à streptocoques et à staphylocoques, gonorrhée, coqueluche, urétrite, conjonctivite, etc.).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **kératoconjonctivite épithéliale ponctuée**, mais cette prédiction repose sur **aucun essai clinique** et **une seule publication** (une revue pédiatrique sur la blépharokératoconjonctivite chronique).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Acné, otite moyenne infectieuse, infections à streptocoques, pneumonie bactérienne, conjonctivite, etc. (indications issues du graphe de connaissances ; le texte des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Kératoconjonctivite épithéliale ponctuée |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 8 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. Sur la base des connaissances générales, l'érythromycine est un macrolide qui inhibe la synthèse protéique bactérienne en se fixant à la sous-unité ribosomique 50S. Elle possède aussi une activité anti-inflammatoire reconnue pour cette classe.

La kératoconjonctivite épithéliale ponctuée accompagne souvent la blépharokératoconjonctivite chronique, pour laquelle les macrolides sont employés afin d'agir sur le bord palpébral et la surface oculaire (effets antibactérien et anti-inflammatoire). L'érythromycine étant déjà associée à la conjonctivite, le lien est plausible.

Ce lien reste toutefois théorique : il ne s'appuie que sur un seul article de prise en charge pédiatrique et sur aucune donnée d'essai. Le score élevé du modèle est une simple prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Revue | Journal of Pediatric Ophthalmology and Strabismus | Description de l'histoire, des symptômes, des signes cliniques et du traitement de la blépharokératoconjonctivite chronique de l'enfant |

## Informations de Marché en France

Les 8 AMM recensées sont toutes annulées ; le texte des indications approuvées n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65371633 | ERY NOURRISSONS 125 mg, granulés en sachet | Granulés | Non renseignée |
| 61572941 | ERY 500 mg, comprimé | Comprimé | Non renseignée |
| 64620665 | ERYTHROCINE 1 g, poudre pour solution à diluer pour perfusion | Poudre pour solution pour perfusion | Non renseignée |
| 65256289 | ERYTHROGEL 4 %, gel pour application cutanée | Gel pour application | Non renseignée |
| 61096983 | ERYFLUID, lotion | Solution | Non renseignée |

Trois autres AMM annulées existent (ERYTHROMYCINE BAILLEUL 4 %, ERY ENFANTS 250 mg, ERYLIK), non détaillées ici.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (hors notice)** : syndrome du QT long (y compris familial) et torsades de pointes ; porphyries ; maladies rénales, hépatiques, de la vésicule biliaire et hématologiques ; colite à *Clostridium difficile* ; entérocolite nécrosante périnatale ; dermatite et dermatite exfoliative ; myasthénie et maladies de la jonction neuromusculaire ; anémie par carence en acide folique ; troubles de l'audition.
- **Interactions médicamenteuses** : 755 interactions recensées. Parmi les principales, deux sont de niveau **majeur** : la **clarithromycine** et le **lopéramide**. De nombreuses interactions de niveau modéré concernent notamment les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), la famotidine, la cimétidine, la pioglitazone, l'alosétron, l'aprépitant, le chlorpropamide et plusieurs laxatifs.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), avec une seule revue pédiatrique et aucun essai clinique.
- Toutes les AMM françaises sont annulées et les données de sécurité issues de la notice manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (site de l'ANSM) pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Rechercher des études cliniques ou observationnelles de l'érythromycine (notamment ophtalmique) dans la kératoconjonctivite épithéliale ponctuée
- Clarifier la disponibilité d'une formulation ophtalmique, les AMM actuelles étant toutes annulées

**Autres indications prédites (pour information) :** la conjonctivite aiguë contagieuse (L4, Hold) est surtout une extension d'un usage existant, sans donnée directe ; la kératite d'exposition (L4, Hold) n'a qu'un soutien indirect ; la lymphogranulomatose vénérienne (L4) et la gingivite ulcéro-nécrotique (L4) restent au stade de question de recherche, avec des données surtout indirectes ou historiques.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

