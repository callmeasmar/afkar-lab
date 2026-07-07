# Backlog de brainstorm

Grandes questions à trancher avant de construire. Chaque entrée suit le
flux : comprendre → rechercher → comparer → documenter → décider (ADR).
Ordre indicatif, pas figé.

## 1. Architecture de connaissances
- [ ] Étudier options (fichiers .md, SQLite+FTS, vector DB, Notion API, hybride)
- [ ] Définir critères (portabilité, coût, résistance à une réinstall complète)
- [ ] Prototyper un cas d'usage réel dans `experiments/`
- [ ] Décider + ADR

## 2. Système de mémoire (agent + perso)
- [ ] Voir ce qu'Orion utilise déjà (MCP `memory`, `sqlite`) — réutilisable ?
- [ ] Définir ce que "mémoire Afkar" doit retenir (idées, décisions, sources)
- [ ] Comparer approches (fichiers plats vs graph vs vector)
- [ ] Décider + ADR

## 3. Écosystème d'agents Afkar
- [x] Premier état des lieux fait — voir [ADR-0003](../adr/0003-agents-et-outils.md)
- [ ] Réévaluer si un besoin récurrent concret apparaît (veille répétée, review systématique)

## 4. Infrastructure & hébergement
- [ ] Même VPS qu'Orion ou séparé ?
- [ ] Politique de sauvegarde des données hors-git (secrets, DB locale)
- [ ] Contraintes réelles (2 cœurs partagés)

## 5. Automatisation — quand et comment
- [ ] Lister les tâches répétitives candidates
- [ ] Étudier n8n existant (déjà utilisé par Orion) vs scripts simples
- [ ] Définir le seuil "assez compris pour automatiser"

## 6. Interface / UX quotidienne
- [ ] Lister les modes d'interaction possibles (CLI, dashboard web, chat)
- [ ] Voir ce qu'Orion a déjà (dashboard existant)
- [ ] Décider le MVP d'interaction

## 7. Sécurité & secrets
- [ ] Politique de gestion des secrets (jamais en clair — règle héritée d'Orion)
- [ ] Grille de décision avant tout nouvel outil (besoin réel, coût, dépendance, maintenance)

## 8. Portabilité / résilience
- [x] Premier jet fait — voir [disaster-recovery.md](disaster-recovery.md)
- [ ] Revérifier périodiquement que le repo seul suffit à tout reconstruire
- [ ] Lister précisément ce qui n'est PAS dans git (clés SSH, tokens MCP) et où c'est documenté

## 9. Règle de promotion Lab → Core
- [ ] Définir des critères concrets et vérifiables (pas juste "quand c'est prêt")
- [ ] Rédiger une checklist de promotion (doc propre + ADR + testé + revu)
