import google_sheets
import seed_grabber
import time
import os

def main():
    directory = os.path.join(os.environ['USERPROFILE'], 'AppData', 'LocalLow', 'ZeekerssRBLX', 'Lethal Company', 'VLogs')
    directory = directory.replace('\\', '/')
    
    # Store previous values to detect changes
    last_seed = None
    last_count = None

    while True:
        latest_file = seed_grabber.get_most_recent_file(directory)

        if latest_file:
            latest_seed, seed_count = seed_grabber.extract_latest_seed_and_count(latest_file)
            print(f"Latest seed: {latest_seed}")
            print(f"Occurrences: {seed_count}")

            # Only update if seed or count has changed
            if latest_seed != last_seed or seed_count != last_count:
                google_sheets.update_sheet(latest_seed, seed_count)
                last_seed = latest_seed
                last_count = seed_count
            else:
                print("No changes detected. Skipping update.")
        else:
            print("No files found in the directory.")

        time.sleep(10)

main()