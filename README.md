# 🛡️ Real-Time System Monitor with Alerts

A Python-based real-time monitoring tool for system CPU health, directory changes, and API/service availability with email alerts.

## 🚀 Features

- CPU usage monitoring and alerts
- Environment-based configuration
- Email notifications for threshold breaches
- Unit tested with GitHub Actions CI pipeline

## 🗂️ Project Structure

project-root/
│
├── app.py # Main monitoring script
├── requirements.txt # Python dependencies
├── tests/
│  └── test_app.py # Unit tests
└── .github/
   └── workflows/
      └── python-ci.yml # CI Workflow for GitHub Actions


## 🔧 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/system-monitor.git
   cd system-monitor

2. Set environment variables (e.g. in .env or terminal):
export SENDER_EMAIL=your_email@gmail.com
export SENDER_PASSWORD=your_password
export RECEIVER_EMAIL=receiver_email@gmail.com

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
pip install -r requirements.txt
