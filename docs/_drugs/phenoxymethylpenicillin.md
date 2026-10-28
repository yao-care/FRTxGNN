---
layout: default
title: Phenoxymethylpenicillin
parent: Prédiction du modèle uniquement (L5)
nav_order: 597
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "phenoxymethylpenicillin"
predicted_indications: ["epiglottitis", "laryngitis"]
description: "Phenoxymethylpenicillin : nouvelle indication prédite, Épiglottite (epiglottitis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Phenoxymethylpenicillin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Phenoxymethylpenicillin: Épiglottite (epiglottitis)
{: .text-alpha }

## Résumé en Une Phrase

La phénoxyméthylpénicilline (pénicilline V) est un antibiotique de la famille des bêta-lactamines, utilisé à l'origine dans les infections streptococciques et les infections des voies respiratoires (otite moyenne, pharyngite, érysipèle, scarlatine, etc.).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**épiglottite** (score de 0,9990), mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.
Une seconde indication prédite, la laryngite, dispose d'une seule publication, qui porte sur l'érythromycine et non sur la pénicilline V.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Épiglottite (epiglottitis) |
| Score de Prédiction TxGNN | 0.9990 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la phénoxyméthylpénicilline est une pénicilline à spectre étroit qui inhibe la synthèse de la paroi bactérienne en se liant aux protéines de liaison aux pénicillines. Son efficacité est établie dans les infections streptococciques et respiratoires hautes.

L'épiglottite est une infection bactérienne aiguë des structures supraglottiques. Depuis la vaccination, elle est plus souvent due à *Streptococcus pyogenes*, *Streptococcus pneumoniae* et *Staphylococcus aureus* qu'à *Haemophilus influenzae* de type b. La couverture streptococcique de la pénicilline V est donc cohérente avec la prédiction, ce qui explique en partie le score élevé.

Cette plausibilité biologique est toutefois limitée. Le médicament est administré par voie orale, son spectre est étroit, et il est inactif contre les souches d'*H. influenzae* et de nombreux *S. aureus* producteurs de bêta-lactamases. L'épiglottite, potentiellement menaçante pour les voies aériennes, requiert un traitement parentéral à large spectre (par exemple une céphalosporine de troisième génération). Le lien repose sur des connaissances générales de classe, et non sur une annotation validée du mécanisme.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'épiglottite.

Pour la seconde indication prédite (laryngite, score de 0,9985), une seule publication a été retrouvée :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1632252](https://pubmed.ncbi.nlm.nih.gov/1632252/) | 1992 | ECR | Acta Oto-Laryngologica. Supplementum | Laryngite aiguë de l'adulte : l'érythromycine (106 patients) réduit le portage nasopharyngé de *B. catarrhalis* par rapport au placebo. Les auteurs rappellent que la phénoxyméthylpénicilline n'avait pas d'effet sur l'évolution clinique. Cette étude ne soutient donc pas directement le médicament. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67151899 | ORACILLINE 1 000 000 UI, comprimé sécable (TEOFARMA), statut : active | Comprimé sécable | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, mononucléose infectieuse, syndrome d'infection chronique à virus d'Epstein-Barr.
- **Interactions médicamenteuses** : 32 interactions recensées. Parmi celles listées :
  - Modérées : doxycycline, minocycline, tétracycline, néomycine, balsalazide, acide picosulfurique, iodure I-123, iodure I-131, dicoumarol, warfarine.
  - Mineure : clarithromycine.
  - Niveau inconnu : oméprazole, lansoprazole, simvastatine, prednisolone, dexaméthasone, acide acétylsalicylique, clopidogrel, héparine, ibuprofène.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication directe. L'épiglottite est une urgence nécessitant un traitement parentéral à large spectre, ce qui s'accorde mal avec une pénicilline orale à spectre étroit.
- L'AMM française est abrogée et les données de sécurité de la notice manquent. Cette lacune bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Rechercher des études cliniques ou observationnelles sur la pénicilline V dans l'épiglottite, ainsi que des données de sensibilité des germes en cause.
- Évaluer la compatibilité de la voie d'administration (orale contre parentérale) avec les besoins de cette indication.
- Pour la laryngite, rechercher des preuves directes, car la seule publication disponible concerne l'érythromycine.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

