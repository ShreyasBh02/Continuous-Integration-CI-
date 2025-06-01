# 🛡️ Real-Time System Monitor with Alerts

A Python-based real-time monitoring tool for system CPU health, directory changes, and API/service availability with email alerts.

## 🚀 Features

- Monitors CPU usage in real-time.
- Sends email alerts when CPU usage exceeds a defined threshold.
- Integrates with GitHub Actions for automated testing and deployment.
- Provides a structured email notification upon workflow completion.
- Email notifications for threshold breaches
- Unit tested with GitHub Actions CI pipeline


## Prerequisites

- Python 3.10 or higher
- GitHub account
- Access to a Gmail account for sending emails (or configure another SMTP server)
- Required Python packages listed in `requirements.txt`

## 🗂️ Project Structure
   ```
      project-root/
         │
         ├── app.py                 # Main monitoring script
         ├── requirements.txt       # Python dependencies
         ├── tests/
         │  └── test_app.py         # Unit tests
         └── .github/
            └── workflows/
               └── python-ci.yml    # CI Workflow for GitHub Actions
   ```


## 🔧 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/ShreyasBh02/Continuous-Integration-CI-.git
   cd system-monitor

2. Set up environment variables 
   
   SEND_EMAIL=your_email@gmail.com
   SEND_PASSWORD=your_password
   RECEIV_EMAIL=receiver_email@gmail.com

3. Install dependencies:
   ```bash
      python -m pip install --upgrade pip
      pip install -r requirements.txtt

## GitHub Actions Workflow
The project includes a GitHub Actions workflow defined in .github/workflows/python-ci.yml. This workflow will:

  - Trigger on pushes and pull requests to the main and master branches.
  - Checkout the code.
  - Set up Python and install dependencies.
  - Run tests using pytest.
  - Execute the monitoring script.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.