# ADR-0001: Séparer Afkar Lab et Afkar Core

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Afkar est un projet long terme, exploratoire par nature. Mélanger
expérimentation brute et documentation stable dans un même dépôt risque de
créer du bruit et d'exposer des idées immatures ou des erreurs publiquement.

## Décision

Afkar est séparé en deux espaces :

- **Afkar Lab** (ce dépôt, privé) — laboratoire d'expérimentation. Erreurs
  autorisées, recherche libre, prototypes, notes brutes.
- **Afkar Core** (public, plus tard) — version propre, documentation
  stable, code testé. Un composant n'y entre qu'après validation dans le Lab.

## Alternatives considérées

- Un seul dépôt public dès le départ — rejeté : trop de bruit, pression à
  la perfection, expose des idées non mûres.
- Deux dépôts privés — rejeté : pas d'objectif de partage/portfolio.

## Conséquences

- Le Lab peut rester désordonné sans risque.
- La promotion Lab → Core nécessite une règle explicite (voir CLAUDE.md).
- Core n'existe pas encore : pas de repo créé avant maturité suffisante.
