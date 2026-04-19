import time
import random

class RealTimeMonitor:
    def __init__(self):
        self.data = []

    def fetch_data(self):
        # Simulate fetching data from an API
        new_data = random.uniform(0, 100)
        self.data.append(new_data)
        print(f"Fetched data: {new_data}")

    def monitor(self):
        print("Starting real-time monitoring...")
        try:
            while True:
                self.fetch_data()
                time.sleep(5)  # Wait for 5 seconds before fetching again
        except KeyboardInterrupt:
            print("Monitoring stopped.")

if __name__ == '__main__':
    monitor = RealTimeMonitor()
    monitor.monitor()