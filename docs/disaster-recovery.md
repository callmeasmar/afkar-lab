# Reprise après réinstallation complète

Objectif : si le VPS est réinstallé de zéro (y compris Claude Code), tout
ce qui compte doit être reconstructible à partir de **ce repo Git seul**
(GitHub : `callmeasmar/afkar-lab`, privé) + quelques étapes manuelles
listées ici.

## Ce qui est dans le repo (récupéré par `git clone`)

- Toute la doc, les ADR, la structure (`adr/`, `docs/`, `research/`,
  `learning/`, `stack/`, `observatory/`)
- `CLAUDE.md` du projet — Claude Code le lit automatiquement à l'ouverture
- Tout futur agent dédié Afkar (`.claude/agents/`, voir ADR-0003)

## Ce qui N'EST PAS dans le repo (à refaire à la main)

1. **Claude Code lui-même** — réinstaller le CLI.
2. **Clé SSH GitHub** — une clé (`~/.ssh/id_ed25519_orion` sur l'ancien
   VPS) est utilisée pour pousser vers GitHub. Après reinstall : générer
   une nouvelle clé, l'ajouter aux clés SSH du compte GitHub
   `callmeasmar`, configurer `~/.ssh/config` (host `github.com`, user
   `git`, `IdentityFile`).
3. **Serveurs MCP** — configurés dans `~/.claude.json` (user-level, hors
   git, jamais commité car il peut contenir des tokens). État connu au
   2026-07-07 : `memory`, `sequential-thinking`, `filesystem`, `github`,
   `sqlite`, `fetch`, `context7`. À reconfigurer via `claude mcp add`
   après reinstall (tokens à ressaisir).
4. **`gh` CLI** — absent sur le VPS d'origine. Si installé plus tard :
   `gh auth login`, puis les commandes `gh repo ...` redeviennent
   utilisables.
5. **Secrets** — aucun secret ne doit jamais être commité (règle absolue
   héritée d'Orion, voir CLAUDE.md racine). Rien à récupérer ici par
   construction ; tout secret réel vit ailleurs (gestionnaire dédié, pas
   ce repo).

## Procédure de reprise (résumé)

1. Réinstaller Claude Code.
2. Générer une clé SSH, l'ajouter à GitHub, configurer `~/.ssh/config`.
3. `git clone git@github.com:callmeasmar/afkar-lab.git ~/projects/afkar-lab`
4. Ouvrir Claude Code dans ce dossier — `CLAUDE.md` est lu automatiquement.
5. Reconfigurer les serveurs MCP nécessaires (voir liste ci-dessus).
6. Lire `BOOTSTRAP_STATE.md` et `ROADMAP.md` pour savoir où le projet en
   était.

## Vérification périodique

Avant de considérer cette procédure fiable : la retester une fois pour de
vrai (clone dans un dossier vide, vérifier que rien de bloquant ne manque).
Voir backlog point 8.
