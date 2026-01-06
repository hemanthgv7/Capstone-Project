#!/bin/bash
set -e

echo "=============================="
echo " STAGING DEPLOYMENT STARTED"
echo "=============================="

# Load environment variables
export $(grep -v '^#' env/staging.env | xargs)

echo "Pulling latest images..."
docker pull $BACKEND_IMAGE
docker pull $FRONTEND_IMAGE

echo "Stopping old containers..."
docker compose -f docker-compose.staging.yml down

echo "Starting new containers..."
docker compose -f docker-compose.staging.yml up -d

echo "Waiting for services..."
sleep 15

echo "Running database migrations..."
docker exec backend python migrate.py

echo "Verifying backend health..."
curl -f http://localhost:5000/health

echo "=============================="
echo " STAGING DEPLOYMENT SUCCESSFUL"
echo "=============================="
