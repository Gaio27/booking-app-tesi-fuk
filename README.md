Aplikasaun **PWA (Progressive Web App)** simpátiku no lalais hodi maneja agendamentu tesi fuk iha Timor-Leste. Aplikasaun ne'e kria uza **Python (Flask)**, **SQLite**, **HTML/CSS/JS**, no bele mehalai uza **Docker**.

---

## 🚀 Fitur Hotu-Hotu

* **PWA Support**: Bele instala diretu iha telemóvel (Android / iOS) no mehalai offline ho Service Worker.
* **Agendamentu Cliente**: Cliente bele hili servisu, data, no oras tesi fuk nian.
* **Admin Dashboard Seguru**: 
  * Proteje ho login session no password hashing (`werkzeug.security`).
  * Admin bele troka status agendamentu (*Pendente*, *Konfirmadu*, *Kansela*) ka hamos (*delete*).
* **Database SQLite**: Rai dadus agendamentu iha forma permanente.
* **Docker & CI/CD**: Inklui `Dockerfile` no GitHub Actions workflow hodi halo build image automatikamente.

---

## 🛠️ Teknolojia (Tech Stack)

* **Backend**: Python 3.9+ / Flask
* **Database**: SQLite3
* **Frontend**: HTML5, CSS3, JavaScript (Vanilla JS), Web App Manifest, Service Worker
* **DevOps**: Docker, GitHub Actions (CI/CD)
* **Testing**: Pytest

---

## 🔑 Credensiál Default Admin

* **Username**: `admin`
* **Password**: `password123`
