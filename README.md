
How to build Docker Image:
git pull
make sure you are in your project root directory
docker build -t calculator-app .

docker run -p 8000:8000 calculator-app

## CI/CD Pipeline Description
This project uses GitHub Actions to automate:
- Building a Docker image
- Pushing the image to Docker Hub
- Deploying the app to AWS EC2

## How to Run Locally

```bash
docker build -t calculator-app .
docker run -p 8000:8000 calculator-app
```
## Changelog
### v3.0 - CI/CD Integration
Added GitHub Actions workflow
Automated Docker build and deployment
Connected Docker Hub and EC2
### v2.0 - Docker Setup
Created Dockerfile
Containerized Django app
### v1.0 - Initial Version
Basic Django calculator app created


