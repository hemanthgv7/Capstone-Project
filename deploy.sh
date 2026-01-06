#!/bin/bash
set -e

echo "Starting deployment..."

echo "Stopping old containers..."
docker compose down

echo "Building latest images..."
docker compose build

echo "Starting containers..."
docker compose up -d

echo "Waiting for services..."
sleep 10

echo "Verifying backend health..."
curl -f http://localhost:5000/health

echo "Deployment successful"
