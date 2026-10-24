import pickle
import zipfile


# Take log entries from user
n = int(input("Enter number of log entries: "))

logs = []

for i in range(n):
    log = input("Enter log: ")
    logs.append(log)


# Save data using Pickle
with open("logs.pkl", "wb") as file:
    pickle.dump(logs, file)

# Compress Pickle file
with zipfile.ZipFile("logs.zip", "w") as zip_file:
    zip_file.write("logs.pkl")

print("\nLogs saved and compressed successfully.")


# Read data from ZIP
with zipfile.ZipFile("logs.zip", "r") as zip_file:
    with zip_file.open("logs.pkl") as file:
        data = pickle.load(file)

print("\nStored Logs:")
for log in data:
    print(log)