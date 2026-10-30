---
layout: default
title: Desonide
parent: Prédiction du modèle uniquement (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "desonide"
predicted_indications: ["polyp of vocal cord", "polyp of middle ear", "polyp of external auditory canal", "polyp of frontal sinus", "polyp of ureter", "polyp of vulva", "fibroepithelial polyp", "neoplastic polyp", "epulis", "uterine polyp"]
description: "Desonide : nouvelle indication prédite, Polyp of vocal cord (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Desonide
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

## Desonide: Polyp of vocal cord
{: .text-alpha }

## Resume en Une Phrase

Desonide est un corticoide topique de faible puissance, utilise a l'origine dans des affections inflammatoires et allergiques, notamment la dermatite atopique, la dermatite de contact et la dermatite seborrheique.
Le modele TxGNN predit qu'il pourrait etre efficace pour le **polype des cordes vocales**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prediction purement computationnelle.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Predite | Polyp of vocal cord |
| Score de Prediction TxGNN | 0.9991 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 3) |
| Nombre d'AMM | 3 (valides : 2) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles. Sur la base des informations connues, desonide est un corticoide topique de faible puissance a activite anti-inflammatoire. Son efficacite dans les dermatoses inflammatoires est etablie, et mecanistiquement, un effet glucocorticoide pourrait etre applicable a des lesions associees a une inflammation chronique et a un oedeme.

Les polypes des cordes vocales sont souvent associes a une inflammation chronique et a un oedeme, ce qui rend un effet glucocorticoide concevable. Cependant, cette hypothese reste theorique : le medicament est une formulation dermatologique en creme, sans voie etablie d'administration laryngee, et aucune donnee ne soutient la prediction.

Les autres predictions du modele (polypes de l'oreille moyenne, du conduit auditif externe, du sinus frontal, de l'uretere, de la vulve, polype fibroepithelial, polype neoplasique, epulis, polype uterin) presentent des scores similaires (0,9990 a 0,9991), toutes au niveau de preuve L5 et sans aucune donnee clinique. Le conduit auditif externe, tapisse de peau, offre une plausibilite de voie d'administration un peu superieure. Pour le sinus frontal, la classe des corticoides est etablie dans la polypose nasosinusienne, mais avec des agents intranasaux et non desonide. Pour les polypes neoplasiques, aucune plausibilite biologique n'est identifiee.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 62294181 | LOCATOP 0,1 %, creme (Pierre Fabre Medicament) | Creme | Non renseignee (AMM active) |
| 61243216 | LOCAPRED 0,1 %, creme (Pierre Fabre Medicament) | Creme | Non renseignee (AMM active) |
| 65055507 | TRIDESONIT 0,05 POUR CENT, creme (Alliance Pharma, Irlande) | Creme | Non renseignee (AMM active) |

---

## Considerations de Securite

Les informations de la notice (mises en garde, contre-indications) ne sont pas disponibles dans les donnees compilees pour ce rapport ; veuillez consulter la notice pour les informations de securite.

- **Contre-indications issues du graphe de connaissances** (relations medicament-maladie du graphe, et non texte de la notice) : hypertension, epilepsie, maladie hepatique, maladie de la vesicule biliaire, hyperglycemie, insuffisance cardiaque congestive, keratite herpetique, rougeole, deficits hypophysaires (dont deficit en hormone de croissance et hypogonadisme hypogonadotrope, syndrome de Kallmann, syndrome de Sheehan), ainsi que certains troubles du cycle de l'uree (deficit en carbamoyl phosphate synthetase I, hyperargininemie, citrullinemie). Ces elements sont indicatifs et doivent etre verifies par rapport au texte reglementaire.
- **Interactions medicamenteuses** : aucune interaction retrouvee dans les donnees compilees.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prediction repose uniquement sur le modele (L5), sans essai clinique ni publication. Il n'existe pas de voie d'administration etablie pour une creme topique vers le larynx, et toutes les AMM francaises sont annulees.
- Les donnees de securite de la notice sont manquantes, ce qui empeche de passer a l'etape de criblage de securite.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer la notice de l'ANSM (mises en garde et contre-indications) et le texte des indications approuvees
- Obtenir les donnees sur le mecanisme d'action aupres de DrugBank
- Realiser une revue de la litterature sur les corticoides dans les polypes des cordes vocales et d'autres polypes de sites cutanes ou cutaneo-muqueux
- Evaluer la faisabilite de la voie d'administration (formulation adaptee au site cible), en priorite pour le conduit auditif externe
- Examiner l'interet reel d'une relance, compte tenu de l'annulation de toutes les AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

