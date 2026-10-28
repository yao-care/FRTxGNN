---
layout: default
title: Ivermectin
parent: Prédiction du modèle uniquement (L5)
nav_order: 420
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "neonatal candidiasis", "candida glabrata", "congenital candidiasis", "postmenopausal atrophic vaginitis", "candidiasis, invasive"]
description: "Ivermectin : nouvelle indication prédite, Candidose vulvovaginale (vulvovaginal candidiasis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Ivermectin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Ivermectin: Candidose vulvovaginale (vulvovaginal candidiasis)
{: .text-alpha }

## Résumé en Une Phrase

L'ivermectine est un antiparasitaire oral, initialement utilisé pour traiter la strongyloïdose et l'onchocercose.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **candidose vulvovaginale**, mais **aucun essai clinique** et **aucune publication pertinente** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Candidose vulvovaginale (vulvovaginal candidiasis) |
| Score de Prédiction TxGNN | 0.9995 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 13 sur 13) |
| Nombre d'AMM | 13 (valides : 13) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, l'ivermectine agit sur les canaux chlorure glutamate-dépendants des invertébrés, ce qui explique son efficacité dans les helminthiases comme la strongyloïdose et l'onchocercose.

Aucun lien mécanistique n'est établi avec les champignons responsables de la candidose : les données compilées ne montrent pas d'équivalent de cette cible chez les pathogènes fongiques. Le score élevé du modèle TxGNN (apprentissage profond) (0,9995) provient du modèle et peut refléter des similitudes apprises entre maladies apparentées, et non une preuve biologique.

Cette prédiction doit donc être considérée comme une hypothèse à explorer, non comme un résultat étayé. Les autres indications prédites (candidose œsophagienne, infection anogénitale à papillomavirus, vulvovaginite, candidose néonatale, candidose invasive, etc.) présentent le même profil : niveau de preuve L5 et recommandation Hold.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la candidose vulvovaginale.

Remarque : les seules publications rattachées aux autres indications prédites sont sans rapport avec la candidose (erreurs de recherche) : un cas de strongyloïdose disséminée sous corticoïdes (PMID 35835488, 2022) et un cas de gale croûteuse chez deux enfants immunodéprimés (PMID 10098288, 1999). Elles ne constituent pas des preuves en faveur des indications prédites.

---

## Informations de Marché en France

Les 13 AMM recensées sont toutes annulées ; le texte d'indication approuvée n'est pas renseigné. Les 5 premières sont présentées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61064455 | IVERMECTINE EG LABO 3 mg, comprimé | Comprimé | Non renseignée |
| 62026945 | IVERMECTINE BIOGARAN 3 mg, comprimé | Comprimé | Non renseignée |
| 68665113 | IVERMECTINE PIERRE FABRE 3 mg, comprimé | Comprimé | Non renseignée |
| 69444281 | SOOLANTRA 10 mg/g, crème | Crème | Non renseignée |
| 64296537 | IVERMECTINE SANDOZ 3 mg, comprimé | Comprimé | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : loase, filariose.
- **Interactions médicamenteuses** : 101 interactions recensées. Parmi les principales de niveau modéré : aprépitant, clarithromycine, éthanol, cobicistat, déférasirox, iodure I-123 et I-131, dicoumarol, fostamatinib, warfarine, abamétapir (topique). Plusieurs autres (oméprazole, lansoprazole, prednisone, prednisolone, ranitidine, famotidine, dexaméthasone, acide ursodésoxycholique, héparine) sont de niveau non déterminé.
- Les données de sécurité néonatale sont limitées, ce qui constituerait une préoccupation supplémentaire pour la candidose néonatale.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle TxGNN (apprentissage profond), sans essai clinique, sans publication pertinente ni lien mécanistique plausible. De plus, le médicament est commercialisé en France (13 AMM valides sur 13), mais les données de sécurité de la notice manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action via DrugBank
- Démontrer une activité antifongique par des études précliniques (in vitro, modèles animaux)
- Vérifier la compatibilité des voies d'administration (orale ou topique) avec une candidose vulvovaginale
- Clarifier le statut réglementaire actuel du médicament en France, au vu de l'annulation de toutes les AMM
- Rechercher la littérature de façon ciblée, les résultats actuels étant hors sujet
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

