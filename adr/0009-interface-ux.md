# ADR-0009: Interface / UX quotidienne

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Backlog point 6. Orion a un dashboard web existant (`apps/dashboard`).
Question : Afkar a-t-il besoin d'une interface dédiée, ou réutilise-t-il
celui d'Orion ?

## Décision

**Claude Code (CLI) uniquement pour l'instant.** Aucune interface web
dédiée. Cohérent avec ADR-0006 (pas de nouveau service sans besoin réel)
et la checklist d'adoption d'outil (ADR-0007) : pas de problème réel
identifié qu'un dashboard résoudrait aujourd'hui.

## Alternatives considérées

- Dashboard dédié Afkar — écarté : développement + maintenance à ajouter
  sans besoin constaté.
- Vue Afkar dans le dashboard d'Orion — écarté pour l'instant : coupling
  avec Orion (contraire à ADR-0001/0003, Lab autonome) ; à reconsidérer
  si un vrai besoin de visualisation apparaît.

## Conséquences

- Toute interaction (lecture, recherche vault, ADR) passe par Claude Code
  et les fichiers du repo.
- Revisiter si le volume de contenu ou un besoin de visualisation
  (ex: graphe de liens, cf. backlog #1) rend le CLI insuffisant.
