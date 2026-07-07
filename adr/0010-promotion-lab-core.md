# ADR-0010: Règle de promotion Lab → Core

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Backlog point 9. ADR-0001 pose la séparation Lab/Core mais sans critère
concret et vérifiable pour décider *quand* une brique passe de l'un à
l'autre — risque de décision arbitraire ("on sent que c'est prêt").

## Décision

Critères formalisés dans
[promotion-checklist.md](../docs/promotion-checklist.md) : documentation
propre, ADR de justification, testé en usage réel (pas en démo),
revu par l'utilisateur, passe la tool-adoption-checklist si dépendance
externe. Les 5 doivent être cochés — pas de promotion partielle.

## Alternatives considérées

- Critère temporel seul ("après X semaines") — écarté : le temps ne
  garantit pas la qualité, un usage réel insuffisant reste un risque.
- Décision au cas par cas sans grille — écarté : c'est exactement ce que
  cet ADR devait éviter (arbitraire).

## Conséquences

- Aucune brique ne passe encore cette checklist aujourd'hui (rien n'a
  encore été construit/testé en usage réel dans Afkar) — normal à ce
  stade.
- Prochaine brique candidate à évaluer avec cette grille dès qu'elle
  existe (ex: `scripts/index-vault.py` après usage réel prolongé).
