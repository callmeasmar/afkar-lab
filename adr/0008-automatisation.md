# ADR-0008: Automatisation — quand et comment

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Backlog point 5. Afkar Lab n'a aujourd'hui aucune tâche répétitive établie
(le projet vient d'être bootstrapé). Seul candidat existant :
`scripts/index-vault.py`, lancé manuellement à la demande.

## Décision

1. **Aucune automatisation construite pour l'instant** — pas de tâche
   répétitive identifiée qui le justifie. Cohérent avec "comprendre avant
   d'automatiser" (AFKAR.md).
2. **Seuil retenu pour automatiser une tâche à l'avenir** :
   - la tâche a été faite manuellement au moins 3 fois,
   - le processus manuel est documenté (dans `learning/` ou `docs/`),
   - elle passe la [tool-adoption-checklist](../docs/tool-adoption-checklist.md)
     si elle introduit un nouvel outil/process.
3. **n8n vs scripts** : si/quand une automatisation est justifiée, préférer
   un script simple (comme `index-vault.py`) tant que le besoin est local
   et ponctuel ; n8n (déjà utilisé par Orion, cf. ADR-0006 ressources
   partagées) seulement si un déclencheur externe/planifié est nécessaire
   (webhook, cron partagé avec interface) — pas par défaut.

## Alternatives considérées

- Automatiser `index-vault.py` via cron dès maintenant — écarté : aucun
  usage régulier constaté, ajouterait un process sur le VPS partagé sans
  justification (ADR-0006).

## Conséquences

- Backlog #5 reste "ouvert" en pratique : à réactiver dès qu'une tâche
  répétitive réelle apparaît et franchit le seuil ci-dessus.
