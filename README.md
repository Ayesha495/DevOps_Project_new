# Calculator DevOps Project

This is a simple Django calculator application used for our DevOps project. The project was completed in six deliverables, and each deliverable added a new DevOps tool or practice.

## 1. Project Setup and GitHub

In the first deliverable, we created the basic Django calculator project and pushed it to GitHub.

Work done:

- Created the Django project and calculator app.
- Added basic calculator functionality.
- Created the first commits.
- Pushed the project to GitHub.
- Team members made changes through Git commits.

Run locally:

```powershell
python manage.py runserver
```

## 2. Docker

In the second deliverable, we containerized the Django application.

Work done:

- Created a `Dockerfile`.
- Added dependencies in `requirements.txt`.
- Built a Docker image for the calculator app.
- Ran the app inside a Docker container on port `8000`.

Useful commands:

```powershell
docker build -t calculator-app .
docker run -p 8000:8000 calculator-app
```

## 3. EC2 Deployment

In the third deliverable, we deployed the application on an AWS EC2 instance.

Work done:

- Created an EC2 instance.
- Installed Docker on EC2.
- Pulled the Docker image from Docker Hub.
- Ran the calculator app container on the EC2 server.
- Accessed the app using the EC2 public IP.

Basic command:

```powershell
docker run -d -p 8000:8000 --name calculator-app <dockerhub-username>/calculator-app
```

## 4. Jenkins

In the fourth deliverable, we used Jenkins for CI/CD automation.

Work done:

- Created a `Jenkinsfile`.
- Added pipeline stages for pulling code, building the Docker image, and pushing it to Docker Hub.
- Used Docker Hub credentials in Jenkins.
- Tested the Jenkins pipeline.

Pipeline stages:

- Pull code from GitHub
- Build Docker image
- Push Docker image to Docker Hub

## 5. Kubernetes and GitHub Actions

In the fifth deliverable, we deployed the app using Kubernetes and added a GitHub Actions workflow.

Work done:

- Created Kubernetes deployment and service files in the `k8s` folder.
- Deployed the calculator app with 3 replicas.
- Connected the app to PostgreSQL using `postgres-service`.
- Used Kubernetes secrets for database values.
- Added GitHub Actions workflow in `.github/workflows/ci-cd.yml`.
- The GitHub Actions pipeline builds and pushes the Docker image, then deploys it to EC2.

Useful Kubernetes commands:

```powershell
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
kubectl get pods
kubectl get services
```

For local Minikube access:

```powershell
kubectl port-forward service/calculator-service 30080:80
```

Then open:

```text
http://localhost:30080
```

## 6. Prometheus and Grafana

In the sixth deliverable, we added observability using Prometheus and Grafana Cloud.

Work done:

- Installed Prometheus locally.
- Added `django-prometheus` to expose Django metrics.
- Configured the `/metrics` endpoint.
- Added Prometheus scrape targets in `prometheus.yml`.
- Connected Prometheus to Grafana Cloud using `remote_write`.
- Stored the Grafana Cloud token in `.env` and referenced it using `password_file`.
- Added health and backup status monitoring notes in `OBSERVABILITY_GUIDE.md`.

Run Prometheus:

```powershell
G:\Downloads\prometheus-3.11.3.windows-amd64\prometheus.exe --config.file="G:\first PC\BSSE\Semester 7\DevOps\Project1\Calculator\prometheus.yml"
```

Useful URLs:

```text
http://localhost:8000/metrics
http://localhost:8000/app/health/
http://localhost:8000/app/backup-status/
http://localhost:9090/targets
```

If using Kubernetes through port-forward:

```text
http://localhost:30080/metrics
```

Useful Prometheus queries:

```promql
up
calculator_app_requests_total
calculator_app_health_status
calculator_backup_status
calculator_backup_age_seconds
```

Grafana was used to visualize service uptime, request metrics, health status, and backup status. This helped show how observability can detect failures and support RPO/RTO planning.

## Notes

This project was mainly for learning DevOps tools step by step. Local files such as `.env`, database files, backup files, `.tools`, and cache files should not be pushed to GitHub.
