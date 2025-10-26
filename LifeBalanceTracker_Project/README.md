LifeBalance Tracker

**LifeBalance Tracker** is a personal productivity and wellness management system built with **Django** and **Django REST Framework**.  
It’s designed to help users find balance — by managing daily tasks, tracking habits, logging workouts, and planning meals — all in one place.

## 🧩 Project Overview

Many people struggle to balance productivity with personal wellness.  
LifeBalance Tracker aims to bridge that gap by combining tools for **task management**, **habit tracking**, **fitness logging**, and **meal planning** — providing a single, integrated platform that encourages consistency and self-care.

## 🚀 Tech Stack

- **Backend Framework:** Django 5 + Django REST Framework  
- **Authentication:** SimpleJWT (JSON Web Tokens)  
- **Database:** SQLite (for now)  
- **Language:** Python 3  
- **Testing Tool:** Postman  
- **Version Control:** Git & GitHub  


## ✅ Features Completed So Far

### 🧭 Phase 1: Project Setup
- Set up Django project and created three core apps:
  - `users` → Authentication and profiles
  - `productivity` → Tasks and habits (next)
  - `wellness` → Workouts and meals (later)
- Installed dependencies and configured project settings.

### 🔐 Phase 2: User Authentication (Completed)
- Custom **User Model** with extra fields:
  - `age`
  - `fitness_goal`
- Implemented **JWT authentication** with:
  - `POST /api/auth/register/` → Register a new user  
  - `POST /api/auth/login/` → Login and receive tokens  
  - `POST /api/token/refresh/` → Refresh expired access token  
  - `POST /api/auth/logout/` → Logout and blacklist refresh token  
- Added SimpleJWT token blacklisting for secure logout.
- Created and tested all endpoints successfully in Postman.
- Configured Django Admin and created a superuser for management.

✅ **Authentication System is fully functional and secure!**


 Lessons & Challenges

- **Migration conflicts:**  
  Encountered an `InconsistentMigrationHistory` error after introducing a custom User model.  
  Fixed by deleting the old database and regenerating all migrations.

- **JWT token issues:**  
  Faced `401 Unauthorized` and `Token expired` errors during testing.  
  Learned to properly handle access vs. refresh tokens, and added token blacklisting for clean logout sessions.

> These challenges were frustrating at first, but they helped me deeply understand Django’s authentication flow and token lifecycle.

---

## 📅 What’s Next (Phase 3: Productivity App)

Next up:
- Build **Task** and **Habit** models (linked to users).  
- Create serializers and CRUD endpoints.  
- Secure them so users can only access their own data.  
- Test all functionality in Postman.  

The goal:  
By the end of the next sprint, users should be able to add, view, update, and delete their **tasks** and **habits**, and track their streaks.

## 🧰 How to Run This Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mz-Akorkor/LifeBalanceTracker_Project.git
   cd LifeBalanceTracker_Project


   