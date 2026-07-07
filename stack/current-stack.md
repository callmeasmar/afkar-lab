# Stack actuelle (VPS HermesAgent)

- OS : Ubuntu 26.04
- Ressources : 2 cœurs, 3.7 Gi RAM, 38G disque (37% utilisé)
- Reverse proxy : Nginx (:80)
- Automatisation : n8n (Docker, derrière Nginx)
- App : uvicorn (:8080)
- Sécurité réseau : UFW + fail2ban
- Orchestration IA : Orion (agents Claude Code) sur le même VPS

## TODO

- Versions exactes des services
- Politique de backup
- Monitoring en place ou non
