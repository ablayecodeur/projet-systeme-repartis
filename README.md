# Projet Système Répartis

Application de démonstration déployée comme un système distribué : API REST Django,
frontend React, base de données PostgreSQL — orchestrés avec Docker Compose pour le
développement et avec Kubernetes (+ Ansible) pour le déploiement sur un cluster local
(Minikube).

## Architecture

```
┌─────────────┐      REST      ┌──────────────┐      SQL      ┌──────────────┐
│   Frontend   │ ─────────────► │   Backend     │ ─────────────► │  PostgreSQL   │
│  React (CRA) │                │ Django + DRF  │                │               │
└─────────────┘                └──────────────┘                └──────────────┘
```

- **Backend** : Django 5 + Django REST Framework, expose deux ressources CRUD
  (`Utilisateur`, `Produit`) via un `DefaultRouter`.
- **Frontend** : application React (Create React App) qui consomme l'API REST.
- **Base de données** : PostgreSQL 15.
- **Orchestration dev** : Docker Compose (`docker-compose.yml`) — 3 services (`db`,
  `backend`, `frontend`).
- **Orchestration cluster** : manifests Kubernetes bruts dans `k8s/` (Deployments +
  Services pour `backend`, `frontend`, `postgres`, plus un `PersistentVolumeClaim`
  pour les données Postgres).
- **Automatisation** : un playbook Ansible (`ansible/playbook.yml`) qui démarre
  Minikube si nécessaire puis applique les manifests `k8s/`.

## Démarrage rapide (Docker Compose)

```bash
git clone https://github.com/ablayecodeur/projet-systeme-repartis.git
cd projet-systeme-repartis
docker compose up --build
```

| Service | URL |
|---|---|
| Backend (API) | http://localhost:8000/api/ |
| Frontend | http://localhost:3001 |
| PostgreSQL | localhost:5432 |

## Déploiement Kubernetes (Minikube)

```bash
# Build des images dans le contexte Docker de Minikube
eval $(minikube docker-env)
docker build -t backend:v1 ./backend
docker build -t frontend:v8 ./frontend

# Créer le secret DB (voir k8s/db-secret.example.yaml pour le détail)
kubectl create secret generic db-credentials \
  --from-literal=POSTGRES_DB=microdb \
  --from-literal=POSTGRES_USER=microuser \
  --from-literal=POSTGRES_PASSWORD='<un-vrai-mot-de-passe>'

# Déploiement via Ansible (démarre Minikube si besoin puis applique k8s/)
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml

# Ou directement
kubectl apply -f k8s/
```

## Structure du projet

```
projet-systeme-repartis/
├── ansible/
│   ├── inventory.ini      # Inventaire local (Minikube)
│   └── playbook.yml       # Démarre Minikube + applique les manifests k8s/
├── backend/
│   ├── api/                # App Django : models, serializers, views, urls
│   ├── config/              # Settings, urls racine, wsgi/asgi
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/                 # Application React (CRA)
│   └── Dockerfile
├── k8s/
│   ├── backend-deployment.yaml / backend-service.yaml
│   ├── frontend-deployment.yaml / frontend-service.yaml
│   └── postgres-deployment.yaml / postgres-service.yaml / postgres-pvc.yaml
└── docker-compose.yml
```

## Variables d'environnement

Copier `.env.example` en `.env` (backend et Docker Compose lisent ces valeurs — voir
`backend/config/settings.py`) :

```env
DB_NAME=microdb
DB_USER=microuser
DB_PASSWORD=change-me
DB_HOST=db
DB_PORT=5432
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=false
```

## Limites connues

- Pas encore de CI/CD (aucun workflow GitHub Actions pour l'instant).
- Le frontend React n'a qu'un écran de démonstration (liste des produits).
- Les migrations `venv/` de l'historique git seront progressivement purgées.
- `CORS_ALLOW_ALL_ORIGINS = True` reste volontairement permissif pour le développement
  local ; à restreindre (`CORS_ALLOWED_ORIGINS`) avant tout déploiement exposé.

## Licence

Projet pédagogique — pas de licence formelle définie pour l'instant.
