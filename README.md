# 🚀 End-to-End CI/CD Pipeline Project

A fully automated CI/CD pipeline built using Flask, Docker, Kubernetes, and GitHub Actions.

---

## 📌 Project Overview

This project demonstrates a complete DevOps pipeline where a single `git push` triggers an automated workflow that builds, pushes, and deploys the application automatically.

---

## 🔄 Pipeline Flow

```
Push Code to GitHub
        ↓
GitHub Actions Triggers
        ↓
Docker Image Built Automatically
        ↓
Image Pushed to Docker Hub
        ↓
Kubernetes Deploys with 2 Replicas
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python Flask | Web Application |
| Docker | Containerization |
| Kubernetes | Container Orchestration |
| GitHub Actions | CI/CD Automation |
| Docker Hub | Image Registry |
| Prometheus & Grafana | Monitoring |

---

## 📁 Project Structure

```
flask-app/
  ├── app.py                          # Flask application
  ├── Dockerfile                      # Container configuration
  ├── deployment.yaml                 # Kubernetes deployment
  ├── service.yaml                    # Kubernetes service
  └── .github/
        └── workflows/
              └── deploy.yml          # GitHub Actions workflow
```

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/pramesh-1994/flask-app.git
cd flask-app
```

**2. Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

**3. Run the app**
```bash
flask run
```

**4. Open browser**
```
http://127.0.0.1:5000
http://127.0.0.1:5000/health
```

---

## 🐳 Run with Docker

```bash
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app
```

---

## ☸️ Deploy on Kubernetes

```bash
minikube start
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service flask-app-service
```

---

## ⚙️ GitHub Actions CI/CD

Every push to `main` branch automatically:
- Builds Docker image
- Pushes to Docker Hub

---

## 📊 Monitoring

Prometheus and Grafana used for monitoring application health and performance.

---

## 👨‍💻 Author

**Pramesh** — Server Engineer | DevOps Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/pramesh-maurya-55823814a/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/pramesh-1994)
