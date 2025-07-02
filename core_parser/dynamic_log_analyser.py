import os
import sys

def extract_date_time(ts):
    """
    Extract date and time from a timestamp string.

    Args:
        ts (str): Timestamp string from log line.

    Returns:
        tuple: (date, time) extracted from the timestamp.
    """
    if 'T' in ts:
        # If timestamp format is like '2025-07-02T15:00:00'
        date_part, time_part = ts.split('T', 1)
        return date_part, time_part
    else:
        # For timestamps separated by spaces, e.g. 'Jul  2 15:00:00'
        parts = ts.split()
        if len(parts) >= 2:
            return parts[0], parts[1]
        # If cannot split properly, return full timestamp as date, and 'N/A' for time
        return ts, 'N/A'

def print_section(title, log_entries):
    """
    Print a formatted section of logs.

    Args:
        title (str): Section title (e.g., DEBUG, INFO).
        log_entries (list): List of log entries to print.
    """
    print(f"\n🔸 Printing {title} Logs")
    print("-" * 100)
    for i, (lineno, timestamp, log_type, message) in enumerate(log_entries, start=1):
        date, time = extract_date_time(timestamp)
        print(f"*{i}. Line:{lineno} -> {log_type} | Date:{date}, Time:{time} => {message}")
    print("=" * 100)

def save_to_file(output_dir, filename, log_entries):
    """
    Save log entries to a file in the specified directory.

    Args:
        output_dir (str): Directory path where file will be saved.
        filename (str): Name of the output file.
        log_entries (list): List of log entries to save.
    """
    with open(os.path.join(output_dir, filename), "w") as f:
        for i, (lineno, timestamp, log_type, message) in enumerate(log_entries, start=1):
            date, time = extract_date_time(timestamp)
            f.write(f"{i}. Line:{lineno} -> {log_type} | Date:{date}, Time:{time} => {message}\n")

def analyze_log_file(log_file):
    """
    Analyze the given log file, categorize lines by log level,
    print categorized logs, save categorized logs and summary to files.

    Args:
        log_file (str): Path to the log file to analyze.
    """
    # Counters for each log level
    all_line = 0
    debug_line = 0
    info_line = 0
    error_line = 0
    other_line = 0

    # Lists to hold log entries by category
    debug_list = []
    info_list = []
    error_list = []
    other_list = []

    # Try opening the file safely
    try:
        with open(log_file, "r") as logfile:
            for lineno, log in enumerate(logfile, start=1):
                line = log.strip()
                if not line:
                    # Skip empty lines
                    continue
                all_line += 1

                # Split line into at most 3 parts: timestamp, log_type, message
                parts = line.split(' ', 2)
                if len(parts) < 3:
                    # Malformed line; skip
                    continue

                timestamp, log_type, message = parts
                log_type_lower = log_type.lower()

                # Categorize logs based on log_type keywords
                if "debug" in log_type_lower:
                    debug_list.append((lineno, timestamp, log_type, message))
                    debug_line += 1
                elif "info" in log_type_lower:
                    info_list.append((lineno, timestamp, log_type, message))
                    info_line += 1
                elif any(x in log_type_lower for x in ["error", "warn", "crit"]):
                    error_list.append((lineno, timestamp, log_type, message))
                    error_line += 1
                else:
                    other_list.append((lineno, timestamp, log_type, message))
                    other_line += 1

    except FileNotFoundError:
        print(f"❌ Error: File '{log_file}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"❌ Error: Permission denied to read '{log_file}'.")
        sys.exit(1)

    # Create output directory named based on input file name
    base_name = os.path.basename(log_file)
    name_no_ext = os.path.splitext(base_name)[0]
    output_dir = f"{name_no_ext}_logs"
    os.makedirs(output_dir, exist_ok=True)

    # Print categorized logs
    print_section("DEBUG", debug_list)
    print_section("INFO", info_list)
    print_section("ERROR", error_list)
    print_section("OTHER", other_list)

    # Print summary to console
    print("\n📊 Summary of Logs")
    print("-" * 100)
    print(f"Analyzed Log File: {log_file}")
    print(f"Total Log Lines : {all_line}")
    print(f"Debug Log Lines : {debug_line}")
    print(f"Info  Log Lines : {info_line}")
    print(f"Error Log Lines : {error_line}")
    print(f"Other Log Lines : {other_line}")
    print("=" * 100)

    # Save categorized logs to files
    save_to_file(output_dir, f"{name_no_ext}_debug.log", debug_list)
    save_to_file(output_dir, f"{name_no_ext}_info.log", info_list)
    save_to_file(output_dir, f"{name_no_ext}_error.log", error_list)
    save_to_file(output_dir, f"{name_no_ext}_other.log", other_list)

    # Save summary report
    with open(os.path.join(output_dir, f"{name_no_ext}_summary.txt"), "w") as f:
        f.write("📊 Summary of Logs\n")
        f.write("-" * 50 + "\n")
        f.write(f"Analyzed Log File: {log_file}\n")
        f.write(f"Total Log Lines : {all_line}\n")
        f.write(f"Debug Log Lines : {debug_line}\n")
        f.write(f"Info Log Lines  : {info_line}\n")
        f.write(f"Error Log Lines : {error_line}\n")
        f.write(f"Other Log Lines : {other_line}\n")

    # Inform user about generated output files
    print(f"\n✅ Output files generated inside '{output_dir}':")
    print("-" * 80)
    print(f"-> {name_no_ext}_debug.log")
    print(f"-> {name_no_ext}_info.log")
    print(f"-> {name_no_ext}_error.log")
    print(f"-> {name_no_ext}_other.log")
    print(f"-> {name_no_ext}_summary.txt")
    print("=" * 100)

def main():
    print("=== Dynamic Log Analyzer v1.0 ===")
    log_file = input("🔍 Enter full path of the log file to analyze: ").strip()
    if not log_file:
        print("❌ No log file provided. Exiting.")
        sys.exit(1)
    analyze_log_file(log_file)

if __name__ == "__main__":
    main()

