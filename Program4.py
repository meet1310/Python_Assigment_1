import csv

def process_transactions(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    amount = float(row["amount"])

                    if amount <= 0:
                        raise ValueError("Amount must be positive")

                    print(f"{row['id']} -> {row['type']} -> ₹{amount}")

                except (ValueError, KeyError) as e:
                    print(f"Invalid transaction: {row} | Error: {e}")

    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("Error:", e)


# Main program
filename = input("Enter CSV file name: ")
process_transactions(filename)