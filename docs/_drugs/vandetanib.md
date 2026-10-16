---
layout: default
title: Vandetanib
parent: Prédiction du modèle uniquement (L5)
nav_order: 805
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vandetanib : nouvelle indication prédite, Carcinome rénal à cellules (renal cell carcinoma) (niveau de preuve L5). Indication d'origine : Carcinome de la thyroïde"
monitor_inn: "vandetanib"
predicted_indications: ["renal cell carcinoma (disease)", "renal cell carcinoma associated with neuroblastoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal pelvis carcinoma", "clear cell renal carcinoma", "childhood kidney cell carcinoma", "renal carcinoma", "angiolipoma", "familial spontaneous pneumothorax"]
---

# Vandetanib
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

# Vandetanib : Du Carcinome de la Thyroïde au Carcinome Rénal

## Résumé en Une Phrase

Vandetanib est un inhibiteur de tyrosine kinase, initialement utilisé pour le traitement du carcinome de la thyroïde (cancer médullaire de la thyroïde avancé).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome rénal à cellules claires et le carcinome rénal en général**,
avec **4 essais cliniques** (de phase 1/2 et 2, petits ou arrêtés prématurément) et **plusieurs publications** surtout de nature générale ou centrées sur la sécurité des inhibiteurs de tyrosine kinase.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome de la thyroïde (source : graphe de connaissances TxGNN ; aucun texte d'indication n'est disponible dans les AMM) |
| Nouvelle Indication Prédite | Carcinome rénal à cellules (renal cell carcinoma) |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L2 (selon la grille de l'analyse ; voir la réserve ci-dessous) |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

Réserve sur le niveau de preuve : le niveau L2 correspond à la classification issue des données compilées. Strictement, aucun essai de phase 2/3 mené à terme avec résultats disponibles dans le carcinome rénal n'est documenté : seul un essai de phase 2 achevé (n=37, maladie de von Hippel-Lindau) existe, sans résultats fournis. Le niveau doit donc être interprété avec prudence, plutôt comme un niveau de preuve limité.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques générales, vandetanib inhibe plusieurs récepteurs à activité tyrosine kinase : VEGFR2, EGFR et RET. Son efficacité dans le cancer médullaire de la thyroïde, où RET est activé de façon constitutive, est établie.

Le carcinome rénal à cellules claires est caractérisé par la perte de VHL, qui active la voie HIF/VEGF et rend la tumeur fortement dépendante de l'angiogenèse. L'inhibition de VEGFR2 est une cible validée dans ce cancer, comme le montre l'usage d'autres inhibiteurs de tyrosine kinase anti-VEGFR. Cela offre une base mécanistique plausible à la prédiction.

Cette base reste toutefois inférée et non démontrée pour vandetanib : les études disponibles sont petites ou interrompues et aucun résultat d'efficacité n'est fourni. Les autres sous-types prédits (carcinome rénal associé à une translocation Xp11.2/TFE3, carcinome rénal non classé, carcinome rénal de l'enfant, carcinome du bassinet rénal) ne reposent que sur le score du modèle ou sur des données indirectes.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Terminé | 37 | Vandetanib dans la maladie de von Hippel-Lindau avec tumeurs rénales ; essai le plus informatif, mais aucun résultat fourni |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Terminé | 82 | Carboplatine + gemcitabine ± vandetanib dans le cancer urothélial avancé (patients non éligibles au cisplatine) ; lien indirect avec le carcinome rénal, aucun résultat fourni |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Arrêté | 7 | Vandetanib + metformine dans les cancers du rein HLRCC/SDH ou carcinome papillaire sporadique ; arrêté avec 7 patients, non concluant |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Arrêté | 3 | Vandetanib dans le carcinome rénal à cellules claires avancé ; arrêté avec 3 patients, non informatif |

## Preuves de la Littérature

Aucune publication ne rapporte de résultats d'efficacité de vandetanib dans le carcinome rénal. La littérature disponible est composée de revues générales, de données de sécurité de classe et d'études précliniques.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Revue | Clin Exp Metastasis | Carcinome rénal déficient en fumarate hydratase : absence de traitement standard, plusieurs essais de phase 2 de thérapies ciblées en cours |
| [32691271](https://pubmed.ncbi.nlm.nih.gov/32691271/) | 2021 | Suivi à long terme | Endocrine | Suivi à long terme et sécurité de vandetanib dans le cancer médullaire de la thyroïde avancé (indication d'origine) |
| [23981115](https://pubmed.ncbi.nlm.nih.gov/23981115/) | 2014 | Méta-analyse (sécurité) | Br J Clin Pharmacol | Incidence et risque de toxicité hépatique des inhibiteurs de tyrosine kinase anti-angiogéniques |
| [22651902](https://pubmed.ncbi.nlm.nih.gov/22651902/) | 2012 | Méta-analyse (sécurité) | Cancer Treat Rev | Mortalité liée au traitement avec les inhibiteurs de tyrosine kinase anti-VEGFR dans les tumeurs solides avancées |
| [32105149](https://pubmed.ncbi.nlm.nih.gov/32105149/) | 2020 | Méta-analyse (sécurité) | Expert Rev Clin Pharmacol | Incidence et risque de protéinurie sous inhibiteurs de VEGFR, dont vandetanib |
| [42107510](https://pubmed.ncbi.nlm.nih.gov/42107510/) | 2026 | Revue | Pharmacol Res | Inhibiteurs de RET approuvés dans les cancers de la thyroïde et du poumon pilotés par RET |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Revue | OncoTargets Ther | Profil du nintedanib ; mention des antiangiogéniques dont vandetanib |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Revue | ASCO Educ Book | Approches systémiques des cancers avancés de la thyroïde ; place de vandetanib dans le cancer médullaire |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Préclinique (modèle murin) | Mol Cancer Res | Modèle murin du carcinome rénal à translocation TFE3 ; cibles thérapeutiques potentielles |
| [23185843](https://pubmed.ncbi.nlm.nih.gov/23185843/) | 2012 | Commentaire | Prescrire Int | « Vandetanib : trop dangereux dans le cancer médullaire de la thyroïde » ; critique du rapport bénéfice-risque |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65808531 | CAPRELSA 100 mg, comprimé pelliculé (statut : annulée) | Comprimé pelliculé | Texte d'indication non disponible |
| 69269825 | CAPRELSA 300 mg, comprimé pelliculé (statut : annulée) | Comprimé pelliculé | Texte d'indication non disponible |

Les deux AMM, détenues par Genzyme Europe (Pays-Bas), sont annulées : aucune AMM valide n'est actuellement recensée en France.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur multikinase : VEGFR2, EGFR, RET) |
| Risque de Myélosuppression | Non documenté dans les données compilées ; veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Non documentée dans les données compilées ; veuillez consulter la notice |
| Éléments de Surveillance | Compte tenu des signaux de sécurité de la classe : ECG et QT, électrolytes (potassium, calcium, magnésium), fonction thyroïdienne, fonction hépatique et rénale (protéinurie), tension artérielle |
| Protection de Manipulation | Veuillez consulter la notice pour les précautions de manipulation des médicaments antinéoplasiques |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de notice) : hypertension, syndrome du QT long (y compris familial) et torsades de pointes, hypothyroïdie (myxœdème, hypothyroïdie congénitale), carence en potassium, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, insuffisance rénale, pneumopathie interstitielle, insuffisance cardiaque (congestive), ischémie cérébrale et accident ischémique transitoire, syndrome de leucoencéphalopathie postérieure.
- **Interactions médicamenteuses** : 296 interactions recensées. Les interactions de niveau majeur incluent notamment :
  - clarithromycine,
  - lévofloxacine,
  - dolasétron,
  - palonosétron,
  - acide picosulfurique,
  - polyéthylène glycol (3350 avec électrolytes),
  - sulfate de sodium.

  Plusieurs interactions modérées concernent la famotidine, la metformine, le lopéramide, la dexaméthasone, le bisacodyl et le lactitol. Les interactions mineures concernent notamment la ranitidine, l'oméprazole, le lansoprazole, le dexlansoprazole, le rabéprazole, le métronidazole et le naloxégol. Plusieurs interactions majeures sont probablement liées au risque d'allongement du QT, cohérent avec les contre-indications ci-dessus.
- **Données de sécurité de classe** : la littérature signale une toxicité hépatique, une protéinurie, une mortalité liée au traitement et des réactions de photosensibilité avec les inhibiteurs de tyrosine kinase anti-VEGFR, dont vandetanib. Un commentaire critique de 2012 (Prescrire) jugeait vandetanib trop dangereux dans le cancer médullaire de la thyroïde.

Les mises en garde et contre-indications de la notice française n'ont pas pu être obtenues ; veuillez consulter la notice pour les informations de sécurité officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le rationnel mécanistique (inhibition de VEGFR2 dans un cancer dépendant de l'angiogenèse) est plausible, mais les essais dans le carcinome rénal sont petits, arrêtés prématurément ou sans résultats disponibles, et aucune publication n'établit l'efficacité.
- Le profil de sécurité est préoccupant (risque cardiaque lié au QT, nombreuses interactions majeures), les données de sécurité de la notice sont manquantes et aucune AMM française n'est valide. Le dépistage de sécurité ne peut donc pas être mené à bien à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM.
- Compléter les données sur le mécanisme d'action depuis DrugBank.
- Récupérer les résultats publiés de l'essai de phase 2 NCT00566995 (maladie de von Hippel-Lindau) et des autres essais.
- Comparer vandetanib aux inhibiteurs de tyrosine kinase déjà établis dans le carcinome rénal à cellules claires pour juger de l'intérêt d'un développement.
- Définir un plan de gestion du risque cardiaque (QT, électrolytes) et des interactions médicamenteuses avant toute étude chez l'humain.
- Clarifier le statut réglementaire en France, les deux AMM étant annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

