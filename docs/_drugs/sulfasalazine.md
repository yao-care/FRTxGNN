---
layout: default
title: Sulfasalazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 721
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sulfasalazine : nouvelle indication prédite, Arthrose (candidate la mieux étayée (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, rectocolite hémorragique…"
monitor_inn: "SULFASALAZINE"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "osteoarthritis susceptibility", "congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "WHIM syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis"]
---

# Sulfasalazine
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

# Sulfasalazine : De la polyarthrite rhumatoïde à l'arthrose

## Résumé en Une Phrase

La sulfasalazine est un médicament anti-inflammatoire utilisé à l'origine dans la polyarthrite rhumatoïde, la rectocolite hémorragique et les maladies inflammatoires chroniques de l'intestin.
Le modèle TxGNN la prédit comme potentiellement efficace pour l'**arthrose**, la prédiction la mieux documentée parmi les dix candidates (la première, le syndrome de brachydactylie-syndactylie, n'a aucune preuve).
Aucun essai clinique n'est enregistré, mais **20 publications** ont été retrouvées, dont quatre études précliniques directement pertinentes (cellules, explants de cartilage, modèles animaux).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, rectocolite hémorragique, maladies inflammatoires chroniques de l'intestin, arthrite juvénile idiopathique, spondylarthropathie (le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Arthrose (candidate la mieux étayée ; la première du classement TxGNN est le syndrome de brachydactylie-syndactylie, sans aucune preuve) |
| Score de Prédiction TxGNN | 99,64 % (arthrose) ; 99,94 % pour le syndrome de brachydactylie-syndactylie |
| Niveau de Preuve | L4 (arthrose) |
| Statut de Marché en France | Uniquement annulée |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold (l'arthrose reste une question de recherche) |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la sulfasalazine est un anti-inflammatoire immunomodulateur, dont l'efficacité dans les rhumatismes inflammatoires et les maladies inflammatoires de l'intestin est établie.

La littérature préclinique décrit la sulfasalazine comme un inhibiteur de NF-κB et du transporteur cystine/glutamate (système xc-). Dans ce cadre, elle a atténué la destruction du cartilage dans un modèle de rupture du ligament croisé antérieur avec méniscectomie (PMID 26466556), bloqué la libération de protéoglycanes et de collagène par du cartilage stimulé par des cytokines avec une baisse des métalloprotéinases (PMID 19690126), et, sous forme de formulation avec l'acide hyaluronique, réduit l'inflammation et la dégradation du cartilage chez le rat (PMID 29548914).

Le lien avec l'indication d'origine est la composante inflammatoire commune aux affections articulaires. Il reste toutefois indirect : aucune donnée d'efficacité chez l'humain atteint d'arthrose n'a été retrouvée.

Les autres candidates du classement (syndromes malformatifs rares, syndrome WHIM, dysplasies squelettiques, myosclérose, etc.) n'ont aucun essai ni publication et aucun lien mécanistique identifié. Leurs scores élevés reflètent probablement la topologie du graphe de connaissances plutôt qu'une logique biologique. La « spondylarthropathie, susceptibilité » correspond à une indication déjà existante, et non à un véritable repositionnement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Publications les plus pertinentes pour l'arthrose (aucun ECR retrouvé) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Préclinique (modèle animal) | J Orthop Res | La sulfasalazine atténue la destruction du cartilage après section du LCA et méniscectomie, via l'inhibition du transporteur cystine/glutamate |
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Préclinique (formulation/in vivo) | Int J Biol Macromol | Acide hyaluronique contenant de la sulfasalazine : libération prolongée jusqu'à 60 jours, réduction de l'inflammation et de la dégradation du cartilage chez le rat |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | Préclinique (in vitro/explant) | Rheumatology (Oxford) | Blocage de la libération de protéoglycanes et de collagène par du cartilage stimulé par des cytokines ; baisse des métalloprotéinases |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | Préclinique (in vitro) | Mod Rheumatol | Modification du profil protéique des chondrocytes articulaires par la sulfasalazine et le tofacitinib |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Préclinique (in vitro) | Wien Klin Wochenschr | Effet de la sulfasalazine et de ses métabolites sur la libération de prostaglandines et de leucotriènes par du tissu synovial humain |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Revue | Front Immunol | Rôle de la ferroptose dans les arthrites inflammatoires, dont l'arthrose |
| [25413361](https://pubmed.ncbi.nlm.nih.gov/25413361/) | 2014 | Cas-témoins (pharmacogénétique) | BMC Pharmacol Toxicol | Polymorphismes de la NAT dans la spondylarthrite ankylosante chez des patients chinois Han et lien avec les effets indésirables de la sulfasalazine |

Les autres publications retrouvées sont surtout des revues générales de rhumatologie, de peu de pertinence directe.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67124724 | SALAZOPYRINE 500 mg, comprimé enrobé gastro-résistant (PFIZER HOLDING FRANCE) | Comprimé enrobé gastro-résistant | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, et non du texte de la notice)** : porphyries (héréditaire et métabolisme des porphyrines), maladie rénale, maladie hépatique, maladie de la vésicule biliaire, asthme (intrinsèque et allergique), neutropénie, agranulocytose, anémie aplasique (dont idiopathique), acétylation lente, déficit en G6PD, glycogénose, cystinurie, galactosémie, obstruction des voies urinaires, pyourètre.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi celles listées, les interactions **majeures** concernent la prilocaïne (topique), les immunoglobulines G humaines (intraveineuses) et la méthénamine. Des interactions modérées concernent notamment l'azathioprine, les AINS (ibuprofène, kétorolac, célécoxib), l'acyclovir, l'amphotéricine B, l'amikacine, les œstrogènes (éthinylestradiol, estradiol), l'alpélisib et l'apalutamide. Une interaction mineure concerne l'acide folique.

Les mises en garde et contre-indications issues de la notice française ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour l'arthrose, les preuves se limitent à des études précliniques (niveau L4), sans essai clinique ni donnée d'efficacité chez l'humain. Les neuf autres candidates n'ont aucune preuve (L5) ou correspondent à une indication déjà existante.
- La notice française n'est pas disponible, ce qui bloque l'évaluation de sécurité, et la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir des données détaillées sur le mécanisme d'action (DrugBank)
- Réaliser ou identifier des essais cliniques de phase 2 sur l'arthrose, avec une évaluation de la voie d'administration (par exemple, formulation intra-articulaire avec acide hyaluronique)
- Évaluer le rapport bénéfice/risque, vu les contre-indications hématologiques, hépatiques et rénales et le nombre élevé d'interactions
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

