---
layout: default
title: Acetylcysteine
parent: Prédiction du modèle uniquement (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Acetylcysteine : nouvelle indication prédite, Maladie thrombotique (niveau de preuve L5). Indication d'origine : Bronchite, intoxication au paracétamol, mucoviscidose, bronchectasies…"
monitor_inn: "acetylcysteine"
predicted_indications: ["thrombotic disease", "closed-angle glaucoma", "nasal cavity disease", "dry eye syndrome", "pharyngitis", "acute laryngopharyngitis", "tracheal disease", "transient ischemic attack (disease)", "laryngotracheitis", "angle-closure glaucoma"]
---

# Acetylcysteine
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

## Acétylcystéine : De la bronchite et de l'intoxication au paracétamol à la maladie thrombotique
{: .text-alpha }

## Résumé en Une Phrase

L'acétylcystéine est un mucolytique et antioxydant, utilisé à l'origine dans la bronchite, la mucoviscidose, les bronchectasies et l'intoxication au paracétamol.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie thrombotique**, avec **6 essais cliniques** enregistrés et **20 publications** retrouvées, mais dont les résultats d'efficacité ne sont pas confirmés dans les données compilées pour ce rapport.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Bronchite, intoxication au paracétamol, mucoviscidose, bronchectasies, amyloses (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie thrombotique |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L1 (selon l'évaluation des données compilées ; voir réserve ci-dessous) |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold (voir justification) |

*Réserve sur le niveau de preuve :* l'étape de notation attribue L1 en s'appuyant sur l'essai de Phase 3 (NCT03252925), mais un seul essai de Phase 3 terminé est identifié, et ses résultats ne sont pas résumés dans les données. Le niveau L1 exigeant au moins deux ECR de Phase 3 terminés, ce classement est à considérer comme optimiste ; un niveau L2 serait plus prudent.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des connaissances générales, l'acétylcystéine est un composé thiolé, mucolytique, antioxydant et précurseur du glutathion. Son efficacité est établie dans l'intoxication au paracétamol et dans les pathologies à mucus épais.

Le lien mécanistique proposé repose sur deux axes. D'une part, le groupement thiol peut réduire les ponts disulfure des multimères du facteur von Willebrand (VWF), diminuant leur taille et leur capacité de liaison aux plaquettes ; cela est soutenu par des modèles précliniques de purpura thrombotique thrombocytopénique (PTT) chez la souris et le babouin. D'autre part, ses effets antioxydants et de reconstitution du glutathion pourraient réduire la lésion endothéliale et le phénotype pro-thrombotique, notamment dans la microangiopathie thrombotique associée à la greffe et dans l'insuffisance rénale.

Les preuves cliniques sont toutefois hétérogènes : l'essai de Phase 3 porte sur la microangiopathie thrombotique post-greffe, les données PTT se limitent à un pilote de 3 patients et à des revues systématiques, et plusieurs essais ciblent le purpura thrombopénique immunologique (PTI), un mécanisme différent (numération plaquettaire, et non thrombose).

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Terminé | 170 | NAC dans la microangiopathie thrombotique associée à la greffe (TA-TMA) ; résultats non résumés dans les données |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Actif, non en recrutement | 44 | NAC dans la TA-TMA, essai monobras multicentrique ; résultats non disponibles |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Terminé | 40 | Réduction du phénotype thrombotique dans l'insuffisance rénale (ECR croisé, contre placebo) ; critère de substitution |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Phase 1 précoce | Terminé | 3 | Pilote de NAC IV dans le PTT suspecté, associé aux échanges plasmatiques ; effectif trop faible pour conclure |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Inconnu | 44 | Dexaméthasone à haute dose + NAC dans le PTI nouvellement diagnostiqué (pertinence indirecte) |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Inconnu | 200 | Atorvastatine + NAC + danazol dans le PTI cortico-résistant/en rechute (pertinence indirecte) |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Phase 1 précoce | Terminé | 15 | Atorvastatine + NAC sur la numération plaquettaire dans le PTI (pertinence indirecte) |

---

## Preuves de la Littérature

Parmi les publications retrouvées, les plus pertinentes sont les suivantes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Revue systématique | J Clin Med | Évaluation critique de la NAC dans le PTT |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Revue systématique | Cureus | NAC comme traitement adjuvant dans le PTT réfractaire ou en rechute |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Étude de cohorte rétrospective | Ann Hematol | Association entre NAC et mortalité hospitalière dans le PTT acquis ; usage controversé |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Préclinique (souris/babouin) | Blood | Effet de la NAC dans des modèles animaux de PTT |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Revue | Expert Rev Hematol | Médicaments repositionnés et nouveaux agents dans le PTT, dont la NAC |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Revue | Blood | Vue d'ensemble du PTT |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revue | J Clin Med | Physiopathologie, diagnostic et prise en charge du PTT |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Revue | J Infect Public Health | NAC dans la COVID-19 (état prothrombotique) |

Aucun essai randomisé contrôlé publié sur la maladie thrombotique n'apparaît dans les données compilées. Plusieurs autres références retrouvées (sclérodermie, risque cardiovasculaire en insuffisance rénale, apnée du sommeil) ne sont que peu informatives.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60513655 | HIDONAC 5 g/25 ml, solution injectable pour perfusion | Solution pour perfusion | Non renseignée |
| 66711220 | FLUIMUCIL 600 mg ADULTES | Granulés pour solution buvable | Non renseignée |
| 65483582 | ACETYLCYSTEINE VIATRIS CONSEIL 200 mg | Poudre pour solution buvable | Non renseignée |
| 62636934 | EXOMUC 600 mg | Poudre pour solution | Non renseignée |
| 69148542 | ACETYLCYSTEINE ARROW 200 mg | Comprimé effervescent | Non renseignée |

Les 20 AMM recensées sont au statut « annulée » ; aucune AMM valide n'est actuellement répertoriée. Le tableau ci-dessus ne présente que les 5 premières.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : ulcère peptique, trouble hypotensif, insuffisance respiratoire, asthme, maladie bronchique, varices œsophagiennes.
- **Interactions médicamenteuses** : 247 interactions recensées. Parmi les exemples : charbon activé (mineure), insuline humaine inhalée à action rapide (modérée) ; de nombreuses autres interactions (mannitol, bupropion, calcitriol, pantoprazole, glimépiride, doxycycline, morphine, metformine, oméprazole, vancomycine, atropine, prednisone, etc.) sont de niveau non précisé.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score du modèle est très élevé et un essai de Phase 3 terminé existe, mais ses résultats ne sont pas résumés, et la seule population directement concernée (TA-TMA) est étroite. Les données dans le PTT sont minimes (pilote de 3 patients) et les essais dans le PTI ne portent pas sur la thrombose. Le niveau L1 ne peut donc être confirmé en l'état.
- Aucune AMM n'est valide en France, et les données de sécurité de la notice sont absentes (blocage sur ce point).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser les résultats de NCT03252925 (critères principaux, sécurité) et de NCT07279610 lorsqu'ils seront disponibles.
- Récupérer la notice de l'ANSM (mises en garde, contre-indications) et les données sur le mécanisme d'action.
- Préciser la voie d'administration et la posologie pertinentes (forme injectable IV vs orale) pour l'indication thrombotique ciblée.
- Clarifier le statut réglementaire en France, toutes les AMM étant annulées.

---

### Note sur les autres indications prédites

Parmi les autres prédictions, la **sécheresse oculaire** présente le meilleur soutien après la maladie thrombotique (niveau L2, recommandation « Proceed with Guardrails ») : un essai de Phase 2 terminé, plusieurs essais de Phase 1, et des ECR (dont PMID 28441068 et PMID 39360368). Ces preuves concernent surtout une formulation spécifique (chitosan-NAC en collyre), non transposable telle quelle à l'acétylcystéine injectable. Les autres prédictions (glaucome à angle fermé, maladie de la cavité nasale, pharyngite, laryngopharyngite aiguë, maladie trachéale, accident ischémique transitoire, laryngotrachéite) reposent sur des preuves nulles ou précliniques uniquement (L4-L5) et sont en attente (Hold).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

