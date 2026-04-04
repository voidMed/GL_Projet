# 🏥 GL_Projet - Application de Prise de Rendez-vous Médicaux

## 📌 Description

Cette application permet aux patients de prendre des rendez-vous en ligne avec des médecins et aux médecins de gérer leur planning efficacement.

---

## 🎯 Objectif

Développer une plateforme moderne permettant :

* Aux patients de réserver facilement des rendez-vous
* Aux médecins de gérer leur agenda
* Une communication fluide entre les utilisateurs

---

## 🚀 Fonctionnalités principales

### 🔐 Authentification

* Inscription (patients / médecins)
* Connexion sécurisée
* Gestion des rôles

### 📅 Gestion des rendez-vous

* Prise de rendez-vous en ligne
* Modification des rendez-vous
* Annulation des rendez-vous
* Consultation de l’historique

### 📊 Tableau de bord

* Dashboard patient :

  * Voir les rendez-vous
  * Prendre un rendez-vous
* Dashboard médecin :

  * Gestion du planning
  * Liste des patients

### 🔔 Notifications

* Notifications internes
* Notifications par email

---

## 🧱 Architecture

Architecture basée sur les **microservices** :

* 🔑 Auth Service (Authentification)
* 📅 Appointment Service (Rendez-vous)
* 🔔 Notification Service (Notifications)

Communication via API REST.

---

## 🛠️ Technologies utilisées

### 🔙 Backend

* Java
* Spring Boot
* Spring Security (JWT)
* JPA / Hibernate

### 🎨 Frontend

* Interface conçue avec Figma
* (React recommandé pour l’implémentation)

### ⚙️ DevOps

* Docker
* Docker Compose
* GitHub Actions (CI/CD)
* JUnit (tests unitaires)
* SonarQube (qualité du code)

---

## 🐳 Conteneurisation avec Docker

Chaque microservice est conteneurisé.

```bash
docker-compose up --build
```

---

## 🔄 CI/CD (GitHub Actions)

Pipeline automatisé :

* Build du projet
* Exécution des tests
* Analyse SonarQube
* Déploiement (optionnel)

---

## 🧪 Tests

Tests unitaires réalisés avec :

* JUnit

Lancer les tests :

```bash
mvn test
```

---

## 📦 Installation

### Prérequis

* Java 17+
* Maven
* Docker

### Étapes

1. Cloner le projet

```bash
git clone <repo-url>
cd GL_Projet
```

2. Lancer les services

```bash
docker-compose up
```

3. Accéder à l’application

* Frontend : [http://localhost:3000](http://localhost:3000)
* Backend : [http://localhost:8080](http://localhost:8080)

---

## 📁 Structure du projet

```
GL_Projet/
│
├── auth-service/
├── appointment-service/
├── notification-service/
├── frontend/
├── docker-compose.yml
└── README.md
```

---

## ✨ Améliorations possibles

* Paiement en ligne
* Chat patient-médecin
* Intelligence artificielle pour recommandations
* Application mobile

---

## 👩‍💻 Auteur

Projet réalisé dans le cadre du module Génie Logiciel.
