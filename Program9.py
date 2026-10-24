import threading
import time

def run_job(job_name, seconds):
    print(job_name, "started")
    time.sleep(seconds)
    print(job_name, "completed")


n = int(input("Enter number of jobs: "))

threads = []

for i in range(n):
    name = input("Enter job name: ")
    seconds = int(input("Enter time: "))

    t = threading.Thread(
        target=run_job,
        args=(name, seconds)
    )

    threads.append(t)
    t.start()

# Wait for all jobs
for t in threads:
    t.join()

print("\nAll jobs completed.")