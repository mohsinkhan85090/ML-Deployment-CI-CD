## ML Model Deployment with Docker, Kubernetes & CI/CD
The core purpose of this project is to bridge the gap between developing a Machine Learning model (which is done on a laptop) and getting that model used by real customers (which requires a stable, scalable production environment).

The project demonstrates two crucial concepts: Production Readiness and Automation (MLOps).

### project overview
 I built this project to demonstrate an end-to-end MLOps pipeline. The purpose was to show that I can take a trained ML model, containerize it with Docker for consistency, deploy it onto a scalable and resilient infrastructure using Kubernetes, and automate the entire testing and deployment process using CI/CD. This project proves my understanding of the best practices required to transition ML research into reliable production services.
This project demonstrates **end-to-end deployment of a Machine Learning model** using **Docker**, **Kubernetes**, and **CI/CD pipelines** via **GitHub Actions**.  
The ML model is containerized, deployed on a Kubernetes cluster, and automatically updated whenever code changes are pushed.  

---
## Project Architecture  
![Project Architecture](https://raw.githubusercontent.com/mohsinkhan85090/ML-Model-Deployment-with-Docker-Kubernetes-CI-CD/main/98.png)

---

## Features
- Containerized ML application using **Docker**
- Orchestrated deployment with **Kubernetes (kubeadm)**
- Automated **CI/CD pipelines** using **GitHub Actions**
- Continuous deployment: automatically updates running pods on new commits
- Unit testing integrated into the CI workflow
- Easy to extend for other ML models or applications

---

## Tech Stack
- **Programming Language:** Python 3.9  
- **Framework:** Flask  
- **Containerization:** Docker  
- **Orchestration:** Kubernetes (Single-node cluster via Docker Desktop)  
- **CI/CD:** GitHub Actions  
- **Libraries/Dependencies:** pandas, scikit-learn, flask  

---
```plaintext
ML-Deployment-CI-CD/
├── app.py # Flask app
├── model.py # ML model logic
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image build instructions
├── k8s/
│   ├── deployment.yaml # Kubernetes deployment definition
│   └── service.yaml # Kubernetes service definition
└── .github/
    └── workflows/
      └── ci-cd.yaml # GitHub Actions workflow
```

---

## Setup Instructions
```bash
1️⃣ Clone the Repository

git clone https://github.com/mohsinkhan85090/ML-Model-Deployment-with-Docker-Kubernetes-CI-CD.git
cd ML-Model-Deployment-with-Docker-Kubernetes-CI-CD


 2️⃣ Build Docker Image

docker build -t ml-deployment:latest .


 3️⃣ Run Docker Container Locally

docker run -d -p 5000:5000 ml-deployment:latest

4️⃣ Deploy on Kubernetes
Apply deployment and service YAML files:-

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Verify deployment:-

kubectl get pods
kubectl get services

Port-forward service to access locally:-

kubectl port-forward service/ml-service 5000:5000
```
##  CI/CD Pipeline (GitHub Actions)

The repository includes automated CI/CD workflows that:

- Checkout code from GitHub  
- Set up Python environment and install dependencies  
- Run unit tests (or skip if none exist)  
- Build Docker image  
- Push Docker image to Docker Hub  
- Update Kubernetes deployment automatically with the new image  

###  Example Workflow Steps

- Checkout code  
- Setup Python 3.9  
- Install dependencies  
- Run unit tests  
- Build and push Docker image  
- Deploy updated image to Kubernetes cluster  

---

## 🐳 Docker Hub Repository

**Docker image:** `mohsinkhan85090/ml-deployment:latest`  
Automatically updated on every push to **main** via GitHub Actions.

---

## 👨‍💻 Author

**Mohsin Khan**  
📍 AI & ML Student | Aspiring SDE/ML Engineer  
🔗 [GitHub](https://github.com/mohsinkhan85090)

