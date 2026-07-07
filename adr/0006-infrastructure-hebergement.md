# ADR-0006: Infrastructure & hébergement

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Backlog point 4. Afkar Lab n'a aujourd'hui aucun service tournant en
continu (que des fichiers + un script ponctuel `index-vault.py`). Question
posée à l'utilisateur : partager le VPS HermesAgent (Orion, 2 cœurs/3.7Gi)
ou une infra séparée.

## Décision

1. **Même VPS que Orion (HermesAgent).** Pas de coût ni de machine
   supplémentaire à maintenir/sécuriser.
2. **Contrainte retenue** : ressources partagées (2 cœurs / 3.7Gi RAM,
   déjà utilisés par Orion : n8n Docker, nginx, uvicorn). Tout futur
   process Afkar qui tournerait en continu doit être justifié au regard
   de cette contrainte avant d'être lancé (pas de nouveau service sans
   évaluer l'impact sur Orion).
3. **Pas de backup de `data/vault.db`.** C'est un index dérivé,
   reconstructible à la demande (`python3 scripts/index-vault.py`,
   cf. ADR-0004). L'utilisateur confirme accepter de repartir de zéro/
   réinitialiser au besoin plutôt que de complexifier avec une politique
   de sauvegarde — cohérent avec la philosophie déjà posée dans
   `docs/disaster-recovery.md`.

## Alternatives considérées

- VPS séparé — écarté : coût récurrent et surface de maintenance en plus
  sans besoin actuel (aucun service Afkar en continu à isoler).
- Sauvegarder `data/vault.db` — écarté : aucune donnée originale n'y vit
  (tout est dans les `.md` déjà versionnés), sauvegarder un dérivé
  reconstructible en une commande ajouterait de la complexité sans valeur.

## Conséquences

- Afkar Lab reste, pour l'instant, un ensemble de fichiers + scripts
  ponctuels — aucune brique infra à opérer (pas de docker/systemd dédié).
- Si un futur besoin (backlog #5 Automatisation) demande un process
  persistant, revenir sur cet ADR pour vérifier l'impact ressources avant
  de le déployer sur le VPS partagé.
