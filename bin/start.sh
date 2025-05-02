# Activer le venv
source .venv/bin/activate

if [[ $? -ne 0 ]]; then
  echo "Échec de l'activation de l'environnement virtuel."
  exit 1
fi

# Aller dans le dossier monitoring
cd monitoring || exit 1

# Lancer Docker Compose
docker-compose up -d
