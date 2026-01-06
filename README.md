End-to-End CI/CD Pipeline for a 2-Tier Web Application

Project Overview
This project demonstrates a complete CI/CD system that automatically builds, tests, scans, publishes, and deploys a Dockerized 2-tier web application to a staging environment.

Application Architecture
The application follows a 2-tier architecture:
Frontend: Static web application served using Nginx
Backend: Flask-based REST API
Database: PostgreSQL

Request Flow:
User Browser → Frontend → Backend API → PostgreSQL

Technology Stack
Frontend: HTML, JavaScript, Nginx
Backend: Python, Flask
Database: PostgreSQL
Containerization: Docker
Orchestration: Docker Compose
CI/CD: GitHub Actions
Security Scanning: Trivy
Image Registry: Docker Hub
Deployment: Shell Scripts

Containerization Best Practices
Multi-stage Docker builds
Non-root containers
Optimized image size
Environment variable configuration

CI/CD Pipeline
Code checkout
Docker image build
Container testing
Security scanning
Image push to Docker Hub
Staging deployment

Deployment Automation
Pull latest images
Stop old containers
Start new containers
Run database migrations
Verify deployment success

Key Outcomes
End-to-end CI/CD automation
Production-style deployment
Reusable Docker images
Professional DevOps workflow
