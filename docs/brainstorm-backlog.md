# Backlog de brainstorm

Grandes questions à trancher avant de construire. Chaque entrée suit le
flux : comprendre → rechercher → comparer → documenter → décider (ADR).
Ordre indicatif, pas figé.

## 1. Architecture de connaissances
- [x] Décidé — voir [ADR-0004](../adr/0004-architecture-connaissances-v1.md) :
  vault = `research/`+`learning/`+`observatory/` (déjà existant), index
  local SQLite `FTS5` via `scripts/index-vault.py`
- [ ] Réévaluer si le volume grossit fortement ou qu'un besoin de graphe/liens apparaît

## 2. Système de mémoire (agent + perso)
- [x] Décidé — voir [ADR-0005](../adr/0005-memoire.md) : mémoire agent =
  système auto de Claude Code (rien à construire) ; mémoire de
  contenu/décisions = déjà couverte par ADR-0004 + les ADR eux-mêmes
- [ ] Gap de portabilité noté dans disaster-recovery.md (mémoire agent hors git)

## 3. Écosystème d'agents Afkar
- [x] Premier état des lieux fait — voir [ADR-0003](../adr/0003-agents-et-outils.md)
- [ ] Réévaluer si un besoin récurrent concret apparaît (veille répétée, review systématique)

## 4. Infrastructure & hébergement
- [x] Décidé — voir [ADR-0006](../adr/0006-infrastructure-hebergement.md) :
  même VPS qu'Orion (partagé), pas de backup de `data/vault.db`
  (reconstruit à la demande)

## 5. Automatisation — quand et comment
- [x] Décidé — voir [ADR-0008](../adr/0008-automatisation.md) : aucune
  tâche répétitive établie, rien à automatiser maintenant, seuil défini
  pour l'avenir (3 répétitions manuelles + doc + checklist outil)

## 6. Interface / UX quotidienne
- [x] Décidé — voir [ADR-0009](../adr/0009-interface-ux.md) : Claude Code
  (CLI) uniquement, pas de dashboard dédié pour l'instant

## 7. Sécurité & secrets
- [x] Décidé — voir [ADR-0007](../adr/0007-securite-secrets.md) : pratiques
  secrets formalisées + [tool-adoption-checklist.md](tool-adoption-checklist.md)

## 8. Portabilité / résilience
- [x] Premier jet fait — voir [disaster-recovery.md](disaster-recovery.md)
- [ ] Revérifier périodiquement que le repo seul suffit à tout reconstruire
- [ ] Lister précisément ce qui n'est PAS dans git (clés SSH, tokens MCP) et où c'est documenté

## 9. Règle de promotion Lab → Core
- [x] Décidé — voir [ADR-0010](../adr/0010-promotion-lab-core.md) et
  [promotion-checklist.md](promotion-checklist.md)
