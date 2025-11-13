# 🧠 ML Model Deployment with CI/CD

## 🚀 Overview  
This project demonstrates **end-to-end Machine Learning Model Deployment** using modern DevOps practices — **Docker**, **Kubernetes**, and **CI/CD pipelines** with **GitHub Actions**.  

It automates the entire workflow:  
> Train → Containerize → Deploy → Scale  

showcasing how an ML model can be moved from development to production reliably and efficiently.

---

## 🧩 Features  
- **Machine Learning Model** built with Python (`model.py`)  
- **Flask API** (`app.py`) for serving predictions  
- **Containerization** using **Docker**  
- **Kubernetes Deployment** (`k8s/`) for scalable model serving  
- **CI/CD Pipeline** via **GitHub Actions** (`.github/workflows/`)  
- **Automatic build, test, and deployment** on every commit  

---

## 🛠️ Tech Stack  
| Component | Technology |
|------------|-------------|
| Language | Python |
| Framework | Flask |
| Containerization | Docker |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Dependencies | Listed in `requirements.txt` |

---

## ⚙️ Project Structure  
ML-Deployment-CI-CD/
│
├── app.py
├── model.py 
├── requirements.txt
├── Dockerfile 
├── k8s/ # Kubernetes manifests (deployment, service)
├── .github/workflows/ # CI/CD pipeline definition
└── .gitignore


---

## 🚀 Deployment Flow  
1. **Push Code to GitHub** → GitHub Actions triggers automatically  
2. **CI/CD Workflow** builds the Docker image  
3. **Image is deployed** to the Kubernetes cluster  
4. **Pod starts running** and serves predictions through Flask API  

Example:  
```bash
kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
ml-deployment-5448578f7d-gnx8w   1/1     Running   0          2m41s

## 📈 Results

After deployment, the application is accessible via browser or API endpoint.  
You’ll see your ML model running live in a production-grade environment managed by Kubernetes.

---

## 🌟 Key Learning Outcomes

- Complete **MLOps pipeline** from model to production  
- Hands-on experience with **CI/CD automation**  
- Understanding of **container orchestration with Kubernetes**  
- Exposure to **real-world ML deployment challenges**

---

## 👨‍💻 Author

**Mohsin Khan**  
📍 AI & ML Student | Aspiring SDE/ML Engineer  
🔗 [GitHub](https://github.com/mohsinkhan85090)
