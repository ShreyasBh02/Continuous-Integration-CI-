import psutil
import os

def test_cpu_usage_is_numeric():
    cpu = psutil.cpu_percent()
    assert isinstance(cpu, (int, float)), "CPU usage should be numeric"

def test_monitor_directory_exists():
    monitor_dir = "./monitor"
    if not os.path.exists(monitor_dir):
        os.makedirs(monitor_dir)
    assert os.path.isdir(monitor_dir), "Monitor directory should exist"

def test_env_variables_present():
    assert os.getenv("SENDER_EMAIL"), "SENDER_EMAIL must be set"
    assert os.getenv("SENDER_PASSWORD"), "SENDER_PASSWORD must be set"
    assert os.getenv("RECEIVER_EMAIL"), "RECEIVER_EMAIL must be set"
