# Changelog

## 2026-07-07

- Bootstrap initial du Lab (structure, ADR 0001/0002, visuels squelettes,
  research/learning/observatory stubs, stack actuelle documentée).
- Push initial vers GitHub (`callmeasmar/afkar-lab`, privé, via SSH).
- ADR-0003 (agents/outils), backlog de brainstorm, doc de reprise après
  réinstallation complète.
- README réécrit avec suivi (badges, tableau de statut, liens).
- ADR-0004 (architecture de connaissances v1) + `scripts/index-vault.py`
  (index SQLite FTS5 sur research/learning/observatory, testé : 16 notes,
  recherche full-text fonctionnelle).
- ADR-0005 (mémoire) : mémoire agent = système auto Claude Code (rien à
  construire), gap de portabilité noté dans disaster-recovery.md.
- ADR-0006 (infra & hébergement) : même VPS qu'Orion, pas de backup de
  `data/vault.db` (reconstruit à la demande).
- ADR-0007 (sécurité & secrets) + `docs/tool-adoption-checklist.md`.
- ADR-0008 (automatisation), ADR-0009 (interface/UX : CLI uniquement),
  ADR-0010 (promotion Lab→Core) + `docs/promotion-checklist.md`.
  Backlog de brainstorm initial (9 points) entièrement tranché.
- Première vraie recherche sourcée : `research/knowledge/index.md`
  (FTS5 vs vectoriel) — valide ADR-0004, addendum ajouté avec chemin
  d'évolution (`sqlite-vec`) si besoin de rappel flou un jour.
