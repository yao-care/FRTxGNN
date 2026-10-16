---
layout: default
title: Mesalazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 482
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Mesalazine : nouvelle indication prédite, Hypotrichose congénitale avec dystrophie maculaire juvénile (niveau de preuve L5). Indication d'origine : Rectocolite hémorragique…"
monitor_inn: "mesalazine"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "osteoarthritis susceptibility", "vulvar inverted follicular keratosis", "pseudoachondroplasia"]
---

# Mesalazine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Mésalazine : De la rectocolite hémorragique à la dysplasie congénitale hypotrichose-maculopathie juvénile

## Résumé en Une Phrase

La mésalazine (acide 5-aminosalicylique, 5-ASA) est un anti-inflammatoire intestinal utilisé à l'origine pour traiter la rectocolite hémorragique, les maladies inflammatoires chroniques de l'intestin et la rectosigmoïdite ulcéreuse.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypotrichose congénitale avec dystrophie maculaire juvénile** (score de 99,65 %), mais cette prédiction repose uniquement sur le graphe de connaissances : **aucun essai clinique** et **aucune publication** ne la soutiennent.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rectocolite hémorragique, maladie inflammatoire chronique de l'intestin, rectosigmoïdite ulcéreuse (source : graphe de connaissances, le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypotrichose congénitale avec dystrophie maculaire juvénile |
| Score de Prédiction TxGNN | 99,65 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 19 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la mésalazine est un aminosalicylé dont l'effet anti-inflammatoire repose sur l'inhibition des voies COX/LOX (moindre synthèse de prostaglandines et de leucotriènes), l'activation de PPAR-gamma et la modulation de NF-kB. Son efficacité dans les maladies inflammatoires de l'intestin est établie.

**Le lien mécanistique avec la nouvelle indication n'est pas établi.** Cette maladie est un trouble génétique ultra-rare (mutation de CDH3) qui altère le développement du follicule pileux et de la rétine. Le défaut sous-jacent concerne la cadhérine, et l'action anti-inflammatoire de la mésalazine n'a aucun lien plausible avec lui. Le score élevé du modèle reflète une proximité dans le graphe de connaissances, et non une preuve biologique ou clinique.

À titre de comparaison, les autres prédictions classées par TxGNN sont tout aussi peu étayées : arthrose (une seule étude computationnelle de 2024), polyarthrite rhumatoïde (littérature indirecte, sans démonstration d'efficacité), kératose séborrhéique, susceptibilité à l'arthrose, kératose folliculaire inversée vulvaire et pseudoachondroplasie (aucune preuve).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hypotrichose congénitale avec dystrophie maculaire juvénile.

À titre d'information, pour la deuxième prédiction (arthrose), une seule publication a été identifiée :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38491514](https://pubmed.ncbi.nlm.nih.gov/38491514/) | 2024 | Analyse computationnelle/transcriptomique | J Transl Med | Identification de cibles thérapeutiques dans l'arthrose par intégration de jeux de données transcriptomiques et de profils d'expression induits par les médicaments ; génératrice d'hypothèses uniquement, sans preuve clinique pour la mésalazine |

---

## Informations de Marché en France

Les 19 AMM recensées sont toutes annulées ; le texte des indications approuvées n'est pas renseigné. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62289729 | PENTASA 500 mg, comprimé | Comprimé | Non renseignée |
| 63599339 | ROWASA 250 mg, comprimé enrobé gastro-résistant | Comprimé enrobé gastro-résistant | Non renseignée |
| 60329160 | OSPERZO 3 g, granulés à libération prolongée | Granulés à libération prolongée | Non renseignée |
| 69694541 | PENTASA 1 g, suppositoire | Suppositoire | Non renseignée |
| 65855463 | FIVASA 1 g, suppositoire | Suppositoire | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, pyourétère, maladie hépatique, maladie de la vésicule biliaire, neutropénie, agranulocytose, anémie (dont anémie macrocytaire), sténose du pylore, néphrose lipoïdique, néphrite interstitielle.
- **Interactions médicamenteuses** : 291 interactions recensées. Parmi les exemples listés :
  - *Majeures* : cidofovir, immunoglobuline humaine anti-neurotoxine botulinique A/B.
  - *Modérées* : kétorolac, ibuprofène, célécoxib (AINS), aciclovir, amphotéricine B (et formes lipidiques), amikacine, azathioprine, bacitracine, capréomycine, cisplatine, ainsi que certains sulfamides hypoglycémiants (acétohexamide, chlorpropamide) et l'anisindione.
  - Beaucoup de ces associations touchent des médicaments néphrotoxiques, ce qui est cohérent avec les signaux rénaux ci-dessus.
- **Signaux de la littérature** : des cas d'effets indésirables graves sont rapportés (syndrome DRESS avec insuffisance rénale aiguë, colite induite par le 5-ASA).

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau de preuve L5), sans essai clinique ni publication, et sans lien mécanistique plausible avec un défaut génétique de la cadhérine (CDH3).
- Les AMM françaises sont toutes annulées et les données de sécurité officielles sont absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM.
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank).
- Démontrer un lien biologique entre la mésalazine et la voie de la cadhérine/le développement rétinien et folliculaire, par des études précliniques.
- Pour les autres candidats (arthrose, polyarthrite rhumatoïde), si une piste est jugée prioritaire, réaliser une revue de la littérature clinique ciblée et évaluer le profil de sécurité rénale.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

