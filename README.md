# Calculator App - CI/CD Pipeline (DevOps Project)

##  Project Overview
This project is a Django-based Calculator application containerized using Docker and deployed using a fully automated CI/CD pipeline.

The pipeline is implemented using GitHub Actions and automates the process of building, pushing, and deploying the application to an AWS EC2 instance.

---

##  CI/CD Pipeline Description

The CI/CD pipeline performs the following steps:

1. **Build Stage**
   - Builds a Docker image of the application.

2. **Push Stage**
   - Pushes the Docker image to Docker Hub using secure GitHub Secrets.

3. **Deploy Stage**
   - Connects to AWS EC2 via SSH.
   - Pulls the latest Docker image from Docker Hub.
   - Stops and removes the old container (if any).
   - Runs the updated container on port 8000.

The pipeline is triggered automatically on:
- Push to `main` branch
- Pull request to `main` branch

---

##  Docker Setup

### Build Image
```bash
docker build -t calculator-app .
docker run -p 8000:8000 calculator-app
```

Live at: http://51.21.200.161:8000/app/

## Changelog
### v3.0 - CI/CD Pipeline Added
Implemented GitHub Actions workflow
Automated Docker build, push, and deployment
Connected Docker Hub and AWS EC2
### v2.0 - Docker Integration
Added Dockerfile
Containerized Django application
### v1.0 - Initial Release
Basic Django Calculator application
## Technologies Used
Django
Docker
GitHub Actions
AWS EC2
Docker Hub