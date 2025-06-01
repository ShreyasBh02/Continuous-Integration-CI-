import time
import os
import smtplib
import psutil
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Thread

## Config
MONITOR_DIR = "./monitor" # Directory to watch
CPU_THRESHOLD = 75 # %
CHECK_INTERVAL = 2 # sec
MONITOR_DURATION = 10 # seconds for monitoring duration
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


## Alert
def send_Mail(subject, body):
    


    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        print(f"Sending email from: {SENDER_EMAIL}")
        print(f"Sending to: {RECEIVER_EMAIL}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,msg.as_string())
        server.quit()
        print(f"[EMAIL SENT] {subject}")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")

## Helth Monitor
def monitor_health():
    start_time = time.time()
    while (time.time() - start_time) < MONITOR_DURATION:
        cpu = psutil.cpu_percent()
        if cpu > CPU_THRESHOLD:
            msg = f"[ALERT] High CPU Usage Detected: {cpu} % at {datetime.now()}"
            print(msg)
            send_Mail("CPU Usage Alert", msg)
        time.sleep(CHECK_INTERVAL)


# -------- MAIN -------- #
if __name__ == "__main__":
   ## Email Message
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subject = f"GitHub Workflow: {os.getenv('WORKFLOW_NAME', 'Unknown')} Completed"
    
    body = (
        f"Hello,\n\n"
        f"The following GitHub workflow has completed:\n\n"
        f"- Workflow Name: {os.getenv('WORKFLOW_NAME', 'Unknown')}\n"
        f"- Repository: {os.getenv('REPO_NAME', 'Unknown')}\n"
        f"- Run ID: {os.getenv('WORKFLOW_RUN_ID', 'Unknown')}\n"
        f"- Status: Completed\n"
        f"- Timestamp: {current_time}\n\n"
        f"For more details, please visit the repository: [GitHub Repository]({os.getenv('REPO_URL', 'https://github.com')})\n\n"
        f"Best regards,\n"
        f"Your Monitoring System"
    )
    send_Mail(subject, body)

    if not os.path.exists(MONITOR_DIR):
        os.makedirs(MONITOR_DIR)

    print("[SYSTEM MONITORING STARTED]")
    monitor_thread = Thread(target=monitor_health)
    monitor_thread.start()
    monitor_thread.join()  # Wait for monitoring to finish
    print("[SYSTEM MONITORING ENDED]") 

        
