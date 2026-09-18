# 🐳 Docker Headless MetaTrader 5 (MT5) Server & 24/7 Watchdog

[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://www.docker.com/)
[![MetaTrader 5](https://img.shields.io/badge/MetaTrader-5-green.svg)](https://www.metatrader5.com/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-yellow.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Production](https://img.shields.io/badge/Status-24%2F7%20Active-success.svg)](https://github.com/themusafirr)

> Production-grade headless MetaTrader 5 VPS environment orchestrated with Docker, Wine, Web VNC/RDP, and an automated Python Watchdog daemon ensuring 100% uptime and automated algorithmic trading recovery.

---

## 🌟 Architecture & Highlights

- 🖥️ **Headless Linux Wine Virtualization:** Runs native Windows 64-bit MT5 seamlessly on Ubuntu/Debian x86_64 servers.
- 🌐 **Remote Web Access:** Connect to MT5 GUI via web browser on port `3000` (no native RDP client required).
- 🛡️ **Intelligent Python Watchdog Daemon (`watchdog.py`):**
  - Continuous health checks every 30 seconds.
  - Detects accidental MetaTrader terminal crashes and re-launches with pre-configured `startup.ini`.
  - Parses live Wine MT5 runtime execution logs.
  - **Auto-Enables Algo Trading:** Automatically simulates `Ctrl + E` via `xdotool` if automated trading becomes disabled or toggles off unexpectedly.

---

## 🚀 Quick Start

### 1. Prerequisites
- Docker & Docker Compose installed.
- Python 3.8+ for watchdog service.

### 2. Configure Environment
```bash
cp .env.example .env
# Customize PASSWORD and port mappings if required
```

### 3. Launch Docker MT5 Service
```bash
docker compose up -d
```
Access the web GUI at `http://<your-vps-ip>:3000`.

### 4. Start 24/7 Auto-Recovery Watchdog
```bash
nohup python3 watchdog.py > watchdog.log 2>&1 &
```

---

## 📁 Repository Structure

```
├── .env.example        # Environment variables configuration
├── .gitignore          # Excludes Wine prefixes, credentials, and screen captures
├── README.md           # Architecture overview & setup instructions
├── docker-compose.yml  # Multi-port container orchestration
└── watchdog.py         # Autonomous 24/7 process & algo-trading supervisor
```

---

## 💼 Custom Algorithmic Trading & FinTech Infrastructure

Need reliable 24/7 VPS deployment for Expert Advisors, low-latency execution engines, or bridge APIs?

- 💬 **Telegram:** [@the_musafir](https://t.me/the_musafir)
- 🌐 **GitHub:** [@themusafirr](https://github.com/themusafirr)

---

## 📄 License
MIT License. Built with ❤️ by [themusafirr](https://github.com/themusafirr).
