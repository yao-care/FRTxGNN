---
layout: default
title: Ofloxacin
parent: Prédiction du modèle uniquement (L5)
nav_order: 554
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ofloxacin : nouvelle indication prédite, Syndrome d'hyperviscosité polyclonale (niveau de preuve L5). Indication d'origine : Infections bactériennes (fièvre typhoïde, infections urinaires…"
monitor_inn: "ofloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
---

# Ofloxacin
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

# Ofloxacine : Des Infections Bactériennes à la Peste Septicémique

## Résumé en Une Phrase

L'ofloxacine est une fluoroquinolone antibactérienne, initialement utilisée pour traiter notamment les infections urinaires, les bronchites, les pneumonies bactériennes et les diarrhées infectieuses.
Le modèle TxGNN lui attribue un score très élevé pour plusieurs nouvelles indications. La première prédiction (**syndrome d'hyperviscosité polyclonale**) n'est soutenue par aucune preuve. La piste la plus plausible parmi les dix prédictions examinées est la **peste septicémique**, appuyée par **10 publications** (études in vitro et chez l'animal, dont certaines hors sujet) et **aucun essai clinique**.

> Remarque : le modèle classe en rang 1 le syndrome d'hyperviscosité polyclonale. Faute de toute preuve et de tout mécanisme plausible, ce rang 1 n'est pas retenu comme piste pertinente. Ce rapport met en avant la peste septicémique (rang 8), seule prédiction disposant d'un corpus de preuves substantiel, tout en présentant la prédiction de rang 1 de façon transparente.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections bactériennes (fièvre typhoïde, infections urinaires, bronchite, pneumonie bactérienne, etc.) ; le texte d'indication des AMM françaises n'est pas renseigné |
| Nouvelle Indication Prédite (rang 1 du modèle) | Syndrome d'hyperviscosité polyclonale |
| Nouvelle Indication Retenue pour l'analyse | Peste septicémique (rang 8) |
| Score de Prédiction TxGNN | 99,91 % (rang 1) ; 99,79 % (peste septicémique) |
| Niveau de Preuve | L5 pour le rang 1 ; L4 pour la peste septicémique |
| Statut de Marché en France | Uniquement annulé (aucune AMM valide) |
| Nombre d'AMM | 19 (toutes annulées) |
| Décision Recommandée | Hold (rang 1) ; question de recherche pour la peste septicémique |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'ofloxacine est une fluoroquinolone qui inhibe l'ADN gyrase et la topoisomérase IV bactériennes, ce qui bloque la réplication de l'ADN des bactéries sensibles.

**Prédiction de rang 1 (hyperviscosité polyclonale).** Aucun lien mécanistique plausible n'existe : cette affection est due à un excès d'immunoglobulines, sur lequel l'ofloxacine n'a aucun effet connu. Le score élevé reflète uniquement une prédiction issue d'un graphe de connaissances. Il en va de même pour l'hyperamylasémie, l'analbuminémie congénitale, l'incompatibilité de groupe sanguin, les maladies hématologiques prémalignes ou congénitales et la gammapathie monoclonale. La neuropathie périphérique acquise associée à une maladie hématologique est même contraire au profil de l'ofloxacine, car les fluoroquinolones peuvent provoquer des neuropathies périphériques.

**Peste septicémique (rang 8).** Ici, le lien est biologiquement plausible : *Yersinia pestis* est sensible aux fluoroquinolones in vitro, et des modèles animaux (souris, primates) montrent une activité. Il s'agit toutefois d'une extension du spectre antibactérien existant de l'ofloxacine, plutôt que d'un véritable repositionnement mécanistique.

**Kératoconjonctivite épithéliale ponctuée (rang 10).** La plausibilité est indirecte (prévention d'une surinfection par voie ophtalmique) ; l'origine de cette affection est souvent virale ou allergique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Pour la peste septicémique (10 publications les plus pertinentes sur les 12 retrouvées) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Étude animale | Antimicrob Agents Chemother | Modèle murin de peste pulmonaire : comparaison de la streptomycine à des antibiotiques peu utilisés en clinique |
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Étude animale | Antibiot Khimioter | Efficacité de l'ofloxacine en prophylaxie et traitement de la peste expérimentale chez la souris ; CMI de 0,08 mg/L |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Étude animale | Antimicrob Agents Chemother | Comparaison de l'ofloxacine et d'autres antibiotiques dans l'infection murine à *Y. pestis* |
| [11871319](https://pubmed.ncbi.nlm.nih.gov/11871319/) | 2001 | Étude animale | Antibiot Khimioter | Évaluation d'antibactériens dans la peste bubonique expérimentale chez le singe |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Étude animale | Antibiot Khimioter | Prévention combinée d'urgence (fluoroquinolones) et spécifique (vaccin) de la peste chez la souris |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | Sensibilité de 78 souches de *Y. pestis* : ceftriaxone et ciprofloxacine les plus actives, puis ofloxacine |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | 100 isolats humains : lévofloxacine et ofloxacine très actives (CMI90 < 0,03 µg/mL) |
| [18644132](https://pubmed.ncbi.nlm.nih.gov/18644132/) | 2008 | Microbiologie (résistance) | BMC Microbiol | Identification de déterminants candidats de résistance aux antibiotiques chez *Y. pestis* |
| [13677133](https://pubmed.ncbi.nlm.nih.gov/13677133/) | 2003 | Microbiologie (résistance) | Antibiot Khimioter | Mutants de la peste résistants à la rifampicine et aux quinolones |
| [19121669](https://pubmed.ncbi.nlm.nih.gov/19121669/) | 2008 | Microbiologie (hors sujet) | Trans R Soc Trop Med Hyg | Résistance aux fluoroquinolones chez *Burkholderia pseudomallei* ; hors sujet |

Pour les autres prédictions, les seules références retrouvées sont sans pertinence réelle : [22808724](https://pubmed.ncbi.nlm.nih.gov/22808724/) (2012, streptocoques bêta-hémolytiques résistants à la bacitracine, correspondance fortuite pour l'incompatibilité de groupe sanguin), [11858365](https://pubmed.ncbi.nlm.nih.gov/11858365/) (2002, cas de discite à *S. lugdunensis* traité par ofloxacine chez un patient atteint de myélome, correspondance fortuite pour la gammapathie monoclonale) et [16670489](https://pubmed.ncbi.nlm.nih.gov/16670489/) (2006, cas d'ulcère vernal en bouclier guéri après débridement, sans lien démontré avec l'ofloxacine).

## Informations de Marché en France

Les 19 AMM recensées sont annulées. Les 5 premières sont listées ci-dessous ; le texte d'indication n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63535151 | OFLOXACINE VIATRIS 1,5 mg/0,5 mL, solution auriculaire en récipient unidose | Solution | Non renseignée |
| 65376801 | OFLOXACINE EVOLUGEN 200 mg | Comprimé pelliculé sécable | Non renseignée |
| 62461303 | OFLOXACINE ALMUS 200 mg | Comprimé pelliculé sécable | Non renseignée |
| 63286593 | OFLOXACINE CRISTERS 200 mg | Comprimé pelliculé sécable | Non renseignée |
| 65021031 | OFLOXACINE SANDOZ 200 mg | Comprimé pelliculé sécable | Non renseignée |

Les autres formes recensées comprennent des solutions auriculaires, des collyres (par exemple QUINOFREE, MONOOX, EXOCINE), une solution pour perfusion et des comprimés (OFLOCET, MONOFLOCET).

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : syndrome du QT long (y compris familial), torsades de pointes, insuffisance et maladies hépatiques, lésions hépatiques d'origine médicamenteuse, épilepsie, maladies et insuffisance rénales, tendinite et périarthrite, neuropathie périphérique, myasthénie grave et maladies de la jonction neuromusculaire, rhabdomyolyse, diabète et acidocétose diabétique, carence en potassium, thrombocytopénie, leucopénie, anémie, colite à *Clostridium difficile*, entérocolite nécrosante périnatale.
- **Interactions médicamenteuses** : 383 interactions recensées. Les interactions de niveau majeur incluent l'hydrocortisone, la dexaméthasone, la bétaméthasone, la triamcinolone (risque tendineux), le bupropion et le chlorpropamide. Parmi les interactions modérées figurent les antidiabétiques (metformine, pioglitazone, acarbose, alogliptine, canagliflozine, albiglutide), la famotidine, le lopéramide, l'acide acétylsalicylique, ainsi que des sels de calcium et de potassium (chélation).

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être obtenues.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le rang 1 et la plupart des autres prédictions, le score élevé du modèle n'est étayé par aucun essai, aucune publication pertinente ni mécanisme plausible (niveau L5).
- La peste septicémique (L4) repose sur des données in vitro et animales uniquement, sans essai humain, et correspond à une extension du spectre antibactérien connu. Toutes les AMM françaises étant annulées, aucune voie de mise sur le marché n'est actuellement disponible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Obtenir les données sur le mécanisme d'action via DrugBank.
- Pour la peste : confronter les données aux recommandations de traitement existantes et à des données cliniques humaines.
- Clarifier le statut réglementaire et la disponibilité de formulations (voie systémique) en France.
- Ne pas poursuivre les prédictions de rang 1 à 7 et 9 sans nouvelles données biologiques.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

