# Checklist avant d'adopter un nouvel outil

À passer avant toute installation (lib, service, MCP, API tierce) :

- [ ] Existe-t-il déjà quelque chose qui répond au besoin (dans Afkar ou Orion) ?
- [ ] Quel problème réel ça résout (pas hypothétique) ?
- [ ] Quel coût de maintenance (mises à jour, casse possible, dette) ?
- [ ] Quel impact sur les tokens (verbosité, nouveaux MCP/skills à charger) ?
- [ ] Quelle dépendance ça crée (lock-in, portabilité — cf. disaster-recovery.md) ?

Si une réponse manque ou est faible → documenter la question ouverte plutôt
que d'installer.
