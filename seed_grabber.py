import os

def get_most_recent_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        return None
    return max(files, key=os.path.getmtime)

def extract_latest_seed_and_count(filepath):
    target_prefix = "Log: Setting bee random seed: "
    latest_seed = None

    # Find the latest seed for beea at the bottom of the file
    with open(filepath, "r") as file:
        for line in file:
            if line.startswith(target_prefix):
                seed_str = line[len(target_prefix):].strip()
                latest_seed = seed_str

    # If no seed found, return None, 0
    if latest_seed is None:
        return None, 0

    count = 0
    # Count the lines containing the seed bees use
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(target_prefix) and line.endswith(latest_seed):
                count += 1

    return int(latest_seed) - 1314 - int(count), count