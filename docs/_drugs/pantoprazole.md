---
layout: default
title: Pantoprazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 577
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Pantoprazole : nouvelle indication prédite, Ulcère peptique actif (niveau de preuve L5). Indication d'origine : Ulcère peptique, reflux gastro-œsophagien, œsophagite…"
monitor_inn: "pantoprazole"
predicted_indications: ["duodenal obstruction"]
---

# Pantoprazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Pantoprazole : De l'ulcère peptique à l'ulcère peptique actif (indication déjà couverte)
{: .text-alpha }

## Résumé en Une Phrase

Pantoprazole est un inhibiteur de la pompe à protons (IPP), initialement utilisé pour traiter les maladies liées à l'acidité gastrique (ulcère peptique, reflux gastro-œsophagien, œsophagite, syndrome de Zollinger-Ellison).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ulcère peptique actif**, mais cette indication recoupe largement les indications d'origine : il s'agit en pratique d'une indication déjà établie plutôt que d'un véritable repositionnement.
Cette prédiction s'appuie sur **1 essai clinique** (Phase 3 terminé) et **19 publications** pour l'ulcère peptique actif, dont une seule étude a pu être rattachée directement à une comparaison impliquant le pantoprazole.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Ulcère peptique, reflux gastro-œsophagien, œsophagite, syndrome de Zollinger-Ellison (le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Ulcère peptique actif |
| Score de Prédiction TxGNN | 99,69 % |
| Niveau de Preuve | L1 (selon l'évaluation des données compilées ; voir réserve ci-dessous) |
| Statut de Marché en France | Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

Réserve : le niveau L1 suppose au moins deux essais de Phase 3 terminés. Pour l'ulcère peptique actif, un seul essai de Phase 3 terminé est listé (NCT02084420), et le rôle du pantoprazole (bras testé ou comparateur) reste à confirmer. Le niveau L1 attribué repose surtout sur l'ensemble des essais disponibles pour les ulcères duodénaux. Il doit donc être considéré comme provisoire.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances établies, le pantoprazole inhibe de façon irréversible l'H+/K+-ATPase gastrique (pompe à protons) des cellules pariétales. Il doit être activé en milieu acide avant d'agir, ce qui lui confère une sélectivité pour le compartiment acide de la cellule pariétale. Il en résulte une suppression prolongée de la sécrétion acide.

L'ulcère peptique actif est directement lié à l'acidité gastrique. L'indication prédite recoupe donc l'indication d'origine (maladie ulcéreuse peptique), et la prédiction du modèle est cohérente avec l'usage établi de cette classe de médicaments. La publication de revue sur l'efficacité du pantoprazole (cicatrisation plus rapide que les anti-H2, efficacité sur les ulcères résistants) va dans le même sens.

Il faut en conclure que cette prédiction a surtout valeur de confirmation. Les autres indications prédites par le modèle sont plus éloignées de l'usage établi et sont présentées plus bas à titre d'information.

## Preuves d'Essais Cliniques

Pour l'ulcère peptique actif :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Terminé | 323 | Ilaprazole vs pantoprazole en trithérapie de 7 jours pour l'éradication d'*H. pylori* chez des patients avec ulcère gastrique et/ou duodénal. Le rôle exact du pantoprazole (test ou comparateur) est à vérifier. |

Pour l'ulcère duodénal (indication voisine, 15 essais enregistrés, les 10 plus pertinents sont présentés) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00374101](https://clinicaltrials.gov/study/NCT00374101) | Phase 3 | Terminé | 450 | IPP à forte dose vs dose standard après traitement endoscopique d'ulcères hémorragiques : la forte dose IV n'est pas supérieure à la dose standard |
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Terminé | 323 | Ilaprazole vs pantoprazole pour l'éradication d'*H. pylori* (ulcère gastrique/duodénal) |
| [NCT00843063](https://clinicaltrials.gov/study/NCT00843063) | Phase 4 | Terminé | 161 | Famotidine vs pantoprazole pour prévenir la récidive d'ulcère/érosion induit par l'aspirine |
| [NCT02467621](https://clinicaltrials.gov/study/NCT02467621) | Phase 4 | Terminé | 3350 | SUP-ICU : prophylaxie des ulcères de stress par pantoprazole en réanimation (population et critère différents) |
| [NCT02551744](https://clinicaltrials.gov/study/NCT02551744) | Non applicable | Terminé | 101 | Pantoprazole vs famotidine pour prévenir la récidive d'ulcère chez les utilisateurs de thiénopyridines |
| [NCT00261300](https://clinicaltrials.gov/study/NCT00261300) | Phase 3 | Terminé | 100 | Traitement prolongé par pantoprazole pour des symptômes acido-peptiques chroniques |
| [NCT00001191](https://clinicaltrials.gov/study/NCT00001191) | Phase 2 | Terminé | Non renseigné | Oméprazole oral et pantoprazole IV dans l'hypersécrétion acide (type Zollinger-Ellison) |
| [NCT01182597](https://clinicaltrials.gov/study/NCT01182597) | Phase 3 | Statut inconnu | 190 | IPP oral vs IV dans les ulcères hémorragiques à haut risque après hémostase endoscopique |
| [NCT00161096](https://clinicaltrials.gov/study/NCT00161096) | Phase 3 | Statut inconnu | 276 | Pantoprazole 20 mg à la demande vs quotidien après soulagement des symptômes |
| [NCT03998969](https://clinicaltrials.gov/study/NCT03998969) | Phase 3 | Terminé | 70 | DA-5204 associé à un IPP dans le RGO (pertinence faible pour l'ulcère duodénal) |

## Preuves de la Littérature

Pour l'ulcère peptique actif (sélection des publications les plus pertinentes ; la plupart n'ont pas encore été classées en détail) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revue systématique / méta-analyse | Am J Gastroenterol | Comparaison des P-CAB et des IPP pour la cicatrisation de l'œsophagite de grade C/D |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | ECR | Gut Liver | Tegoprazan sur les ulcères artificiels après résection endoscopique (contexte comparateur) |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | Étude multicentrique | Am J Gastroenterol | Pantoprazole vs ranitidine dans l'ulcère duodénal au Brésil |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Étude comparative | Hepato-gastroenterology | Lansoprazole vs pantoprazole dans l'ulcère duodénal actif et l'éradication d'*H. pylori* |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Revue | Clin Drug Investig | Profil du pantoprazole : action prolongée, peu d'interactions identifiées dans les études |
| [21534455](https://pubmed.ncbi.nlm.nih.gov/21534455/) | 2011 | Revue | Med Arh | Place des IPP dans la prise en charge du RGO |
| [16961157](https://pubmed.ncbi.nlm.nih.gov/16961157/) | 2006 | Revue | Int J Clin Pharmacol Ther | Impact du polymorphisme CYP2C19 sur l'action des IPP |
| [15989651](https://pubmed.ncbi.nlm.nih.gov/15989651/) | 1997 | Revue | Expert Opin Investig Drugs | Pantoprazole : cicatrisation plus rapide que les anti-H2, efficacité sur les ulcères résistants |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Étude préclinique (rat) | Inflammopharmacology | Pantoprazole associé à des cellules souches mésenchymateuses dans l'ulcère gastrique expérimental |
| [26439477](https://pubmed.ncbi.nlm.nih.gov/26439477/) | 2016 | Étude préclinique (rat) | J Nat Med | Effet protecteur de la crocine contre les lésions gastriques induites par l'indométacine (pantoprazole en témoin) |

### Autres indications prédites (pour information)

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Essais cliniques | Résumé des preuves | Recommandation |
|------|------|------|------|------|------|------|
| 2 | Ulcère gastro-jéjunal | 99,63 % | L4 | 0 | Littérature indirecte (prophylaxie des ulcères de stress en réanimation, hémorragie ulcéreuse), aucune étude sur les ulcères anastomotiques | Question de recherche |
| 3 | Perforation d'ulcère peptique | 99,63 % | L3 | 0 | Une étude directe (PMID 38222001, pantoprazole après réparation de perforation, conception à vérifier), le reste est indirect | Question de recherche |
| 4 | Reflux duodéno-gastrique | 99,27 % | L3 | 0 | Deux petites études physiologiques/cliniques (PMID 11552908, 19280541) ; le pantoprazole n'agit que sur la composante acide | Question de recherche |
| 5 | Obstruction duodénale | 99,21 % | L5 | 0 | Aucun lien mécanistique clair ; une seule publication (cas clinique), sans rapport avec l'efficacité du pantoprazole | Hold |
| 6 | Ulcère duodénal | 99,18 % | L1 | 15 | Plusieurs essais de Phases 3 et 4 impliquant le pantoprazole, indication essentiellement déjà établie | Proceed with Guardrails |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68729174 | INIPOMP 40 mg, poudre pour solution injectable (IV) (TAKEDA FRANCE) | Poudre pour solution injectable | Non renseignée ; AMM annulée |

Aucune AMM valide n'est actuellement recensée pour ce médicament dans les données compilées pour ce rapport.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, ne provenant pas du texte de la notice) : ostéoporose, ostéoporose post-ménopausique, fracture osseuse, anémie pernicieuse.
- **Interactions médicamenteuses** : 597 interactions sont recensées. Parmi les exemples listés :
  - **Majeures** : acalabrutinib, atazanavir.
  - **Modérées** : hydrochlorothiazide, alpélisib, amphotéricine B, amikacine, amphétamine, fénofibrate, apalutamide, armodafinil, atorvastatine, bosutinib, bumétanide.
  - **Mineures** : acide acétylsalicylique, axitinib, bortézomib, brivaracétam, cyanocobalamine.
- Selon les données de la littérature, il faut également prendre en compte les interactions liées au CYP2C19 (par exemple avec le clopidogrel et les thiénopyridines) et les risques d'un traitement prolongé par IPP.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le pantoprazole agit sur un mécanisme bien établi (inhibition de la pompe à protons) et l'ulcère peptique actif correspond à son usage d'origine ; plusieurs essais de Phases 3 et 4 soutiennent son usage dans les ulcères. Ce n'est donc pas un repositionnement au sens strict.
- L'unique AMM française est annulée, et les données de sécurité issues de la notice sont absentes, d'où la nécessité de garde-fous.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmer le rôle du pantoprazole (bras testé ou comparateur) dans l'essai NCT02084420.
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Confirmer les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Vérifier le statut réglementaire et les formulations disponibles en France (AMM annulée) et selon les régions.
- Établir un plan de gestion des interactions (notamment CYP2C19 / clopidogrel, atazanavir, acalabrutinib) et de surveillance des risques d'un traitement prolongé (ostéoporose, fractures, carence en vitamine B12).
- Pour les autres indications prédites (ulcère gastro-jéjunal, perforation, reflux duodéno-gastrique), des études directes sont nécessaires avant toute évaluation ; l'obstruction duodénale doit rester en attente.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

