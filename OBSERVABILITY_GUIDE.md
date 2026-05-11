# Prometheus and Grafana Observability Guide

## Question 1: Prometheus Integration

### 1. Install and Run Prometheus

Prometheus is installed locally at:

```powershell
G:\Downloads\prometheus-3.11.3.windows-amd64
```

Run Prometheus with the project configuration:

```powershell
G:\Downloads\prometheus-3.11.3.windows-amd64\prometheus.exe --config.file="G:\first PC\BSSE\Semester 7\DevOps\Project1\Calculator\prometheus.yml"
```

Open Prometheus:

```text
http://localhost:9090
```

### 2. Run the Django Application

In a separate terminal:

```powershell
cd "G:\first PC\BSSE\Semester 7\DevOps\Project1\Calculator"
python manage.py runserver 0.0.0.0:8000
```

Useful application URLs:

```text
http://localhost:8000/app/
http://localhost:8000/app/health/
http://localhost:8000/app/backup-status/
http://localhost:8000/metrics
```

### 3. Configured Prometheus Targets

The `prometheus.yml` file monitors:

- Prometheus itself: `localhost:9090`
- Django calculator app: `localhost:8000/metrics`
- Kubernetes NodePort app, if enabled: `localhost:30080/metrics`

Check target status:

```text
http://localhost:9090/targets
```

### 4. Metrics to Demonstrate

Run these queries in Prometheus or Grafana Explore:

```promql
up
```

```promql
calculator_app_requests_total
```

```promql
calculator_app_health_status
```

```promql
calculator_backup_status
```

```promql
django_http_requests_total_by_method_total
```

### 5. Explanation

Prometheus improves observability by continuously scraping metrics from the application and infrastructure. It helps DevOps teams see whether services are up, how many requests are being handled, whether the application is healthy, and whether backup status is acceptable. These metrics make it easier to detect failures early, troubleshoot incidents, and validate that the deployment pipeline is producing reliable releases.

## Question 2: Grafana, RPO, and RTO

### 1. Grafana Tool Selection

Grafana Cloud is used as the visualization and monitoring tool. Prometheus sends metrics to Grafana Cloud using `remote_write`, while the same metrics remain available locally in Prometheus.

### 2. Suggested Grafana Dashboard Panels

Create a dashboard in Grafana Cloud with these panels:

| Panel | Query | Purpose |
| --- | --- | --- |
| Service uptime | `up{job="calculator-local"}` | Shows whether the calculator app is reachable |
| Application health | `calculator_app_health_status` | Shows health endpoint result |
| Request count | `sum(rate(calculator_app_requests_total[5m]))` | Shows application traffic |
| Backup status | `calculator_backup_status` | Shows whether a recent backup exists |
| Backup age | `calculator_backup_age_seconds` | Shows backup freshness |
| Remote write failures | `prometheus_remote_storage_failed_samples_total` | Shows whether Prometheus is failing to send data to Grafana Cloud |

### 3. Configure Backup Status Demo

Create a backup file:

```powershell
cd "G:\first PC\BSSE\Semester 7\DevOps\Project1\Calculator"
New-Item -ItemType Directory -Force backups
Copy-Item db.sqlite3 backups\db.sqlite3.bak -Force
```

Refresh:

```text
http://localhost:8000/app/backup-status/
```

Then check:

```promql
calculator_backup_status
```

Expected value:

```text
1
```

### 4. Simulate a System Failure

Stop the Django application with `Ctrl + C`.

After Prometheus scrapes again, check:

```promql
up{job="calculator-local"}
```

Expected value:

```text
0
```

Start the app again:

```powershell
python manage.py runserver 0.0.0.0:8000
```

When the value returns to `1`, the service has recovered.

### 5. Simulate a Backup Failure

Rename or remove the backup file:

```powershell
Rename-Item backups\db.sqlite3.bak db.sqlite3.bak.failed
```

Open:

```text
http://localhost:8000/app/backup-status/
```

Then check:

```promql
calculator_backup_status
```

Expected value:

```text
0
```

Restore the backup:

```powershell
Rename-Item backups\db.sqlite3.bak.failed db.sqlite3.bak
```

### 6. RPO and RTO Report

Example thresholds for this project:

| Metric | Target |
| --- | --- |
| RPO | 24 hours maximum acceptable data loss |
| RTO | 5 minutes maximum acceptable recovery time |

Example result:

| Scenario | Measured Result | Meets Target? |
| --- | --- | --- |
| Service downtime | App recovered in approximately 1 minute after restart | Yes, under 5 minutes |
| Backup failure | Backup status detected as failed on the next scrape interval | Yes for detection |
| Data loss risk | Backup file is expected to be updated daily | Yes if backup age stays below 24 hours |

### 7. Suggested Improvements

- Automate database backups instead of copying files manually.
- Add Grafana alerts for `up == 0`, `calculator_app_health_status == 0`, and `calculator_backup_status == 0`.
- Reduce Prometheus scrape interval for faster detection in production.
- Use persistent storage and scheduled backups for PostgreSQL.
- Add high availability for the application and database to reduce RTO.
