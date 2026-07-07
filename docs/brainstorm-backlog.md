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

---

## Backlog v2 — approfondissement (2026-07-07)

Le backlog initial (1-9) tranche l'architecture. Cette suite creuse plus
loin : suivi dans le temps des décisions déjà prises, nouveaux domaines de
contenu, et premier passage à l'action.

## 10. LLMs
- [ ] 10.1 Cartographier les providers actuels et leurs forces (Claude, GPT, Gemini, open-weights)
- [ ] 10.2 Comparer les coûts pour un usage perso (tokens, contexte, cache)
- [ ] 10.3 Matrice "quel modèle pour quelle tâche" (recherche / code / résumé / brainstorm)
- [ ] 10.4 Décider si Afkar a besoin d'une politique de bascule multi-modèle
  (comme `sm glm`/`sm claude` chez Orion) ou si un seul modèle suffit

## 11. UX quotidienne (approfondissement ADR-0009)
- [ ] 11.1 Observer les frictions réelles après un usage prolongé en CLI
- [ ] 11.2 Étudier des inspirations d'interfaces agent/PKM existantes
- [ ] 11.3 Ne redécider que si une friction concrète est constatée

## 12. Observabilité (nouveau domaine)
- [ ] 12.1 Définir ce qui vaut la peine d'être mesuré (nb de notes, fréquence d'usage, taille du vault)
- [ ] 12.2 Décider si un rapport à la demande suffit (pas de dashboard, cf ADR-0009)
- [ ] 12.3 Relier au rythme de l'observatoire (point 13)

## 13. Observatoire — première vraie exécution
- [ ] 13.1 Remplir une première entrée hebdo réelle (template existant, jamais utilisé)
- [ ] 13.2 Décider du rythme réaliste (hebdo vs mensuel) selon la charge

## 14. Idées futures — processus de tri
- [ ] 14.1 Définir où atterrissent les idées non mûres (`research/future-ideas` existe déjà)
- [ ] 14.2 Définir quand une idée devient un point de backlog officiel

## 15. Sécurité — suivi dans le temps (approfondissement ADR-0007)
- [ ] 15.1 Fréquence de revue périodique du repo (secrets oubliés)
- [ ] 15.2 Procédure si un secret est accidentellement commité (rotation, purge d'historique git)

## 16. Infrastructure — suivi dans le temps (approfondissement ADR-0006)
- [ ] 16.1 Comment repérer si Afkar commence à peser sur les ressources partagées du VPS
- [ ] 16.2 Seuil à partir duquel reconsidérer une infra séparée

## 17. Automatisation — liste vivante des candidats (approfondissement ADR-0008)
- [ ] 17.1 Tenir une liste des tâches répétées observées, pas encore automatisées
- [ ] 17.2 Revue périodique : seuil des 3 répétitions atteint ou non

## 18. Premier prototype réel
- [ ] 18.1 Choisir quoi construire en premier dans `experiments/` pour tester le flux complet
- [ ] 18.2 Définir le critère de succès avant de construire

## 19. Crédits Google Cloud (~260€)
- [ ] 19.1 Vérifier les modalités exactes (montant réel, date d'expiration,
  services couverts/exclus — souvent limités dans le temps)
- [ ] 19.2 Lister les usages pertinents pour Afkar (Vertex AI/Gemini API,
  Cloud Storage pour backup du vault, Compute Engine, BigQuery pour l'observabilité #12...)
- [ ] 19.3 Confronter à ADR-0006 (pas de nouveau service sans besoin réel) —
  des crédits gratuits ne créent pas un besoin, ils changent juste le coût
- [ ] 19.4 Décider un usage concret seulement si un vrai besoin déjà identifié
  matche un service GCP, pas l'inverse ("on a des crédits donc on va s'en servir")
- ⚠️ Urgence potentielle : si les crédits expirent, ce point doit être
  priorisé avant qu'ils ne soient perdus — à vérifier en 19.1
