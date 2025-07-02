## Log Monitoring System (Version 1.0)
A command-line based dynamic log analyzer built to parse `.log` files, extract key entries, categorize logs by level, and generate clean output reports.

## Features of 'dynamic_log_analyser.py'
- Takes `.log` file as input
- Parses and categorizes logs into:
  - DEBUG
  - INFO
  - ERROR/WARNING/CRITICAL
  - OTHER
- Generates clean, readable output:
  - Formatted log summaries
  - Saves logs to organized folders
  - Creates a report `summary.txt`
- Automatically names output folders and files
- Handles malformed lines and empty logs gracefully
---

# Project Structure
```
log_monitoring_system/
├── core_parser/
│   ├── dynamic_log_analyser.py # Main CLI log parser
│   ├── readme.md # Module-level doc
│   └── sample_logs/ # Sample test logs (cron & dnf)
├── ip_alert_module/
│   └── ip_tracker.py # (Upcoming) Suspicious IP tracker
├── dashboard/
│   └── live_web_ui.py # (Upcoming) Web UI (Flask-based)
├── docs/
│   └── architecture.md # Design plan & module notes
```
---
# Concepts Used
- File I/O
- String manipulation & log parsing
- Categorization logic
- Modular Python functions
- CLI interaction
- Exception handling
---
# Requirements
- Python 3.6 or higher
- Linux-based system (tested on CentOS/RHEL/Fedora)
- No external libraries required (pure Python)
---
# How to Use
+ **Make sure Python3 is installed on your system.**

1. **Run the script**  
   ```bash
   python3 dynamic_log_analyser.py
   ```	
2. **Enter full path of a log file**
   Example input:
   Enter full path of the log file to analyze: /var/log/cron

3. Output files will be saved:
   
   In a directory named based on the input file:
---


# Retrieving sample cron logs (sudo priviledge required)
```bash
$ sudo python3 dynamic_log_analyser.py 
```
Enter full path of the log file to analyze: /var/log/cron

# Retrieving sample dnf logs
```bash 
$ python3 dynamic_log_analyser.py 
```
Enter full path of the log file to analyze: /var/log/dnf.log

---
# Sample Generated logs
```
core_parser/
├── cron_logs
│   ├── cron_debug.log
│   ├── cron_error.log
│   ├── cron_info.log
│   ├── cron_other.log
│   └── cron_summary.txt
├── dnf_logs
│   ├── dnf_debug.log
│   ├── dnf_error.log
│   ├── dnf_info.log
│   ├── dnf_other.log
│   └── dnf_summary.txt
├── dynamic_log_analyser.py
├── readme.md
├── LICENSE

```
---

# Sample Summary of cron Logs
```
Summary of Logs
----------------------------------------------------------------------------------------------------
Analyzed Log File: /var/log/cron
Total Log Lines : 243
Debug Log Lines : 0
Info  Log Lines : 0
Error Log Lines : 0
Other Log Lines : 243
```
# Sample Summary of dnf Logs
```
Summary of Logs
----------------------------------------------------------------------------------------------------
Analyzed Log File: /var/log/dnf.log
Total Log Lines : 4229
Debug Log Lines : 3458
Info  Log Lines : 447
Error Log Lines : 11
Other Log Lines : 233
```
---
# Author
Md Nabil Hossain
Computer Engineer | Linux & Python Enthusiast
- Email: mdnabil.cse@gmail.com
- Portfolio: Coming Soon
- GitHub: [codebyperfect](https://github.com/codebyperfect)
---

## License
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

## Contributing
Feel free to fork the repo, suggest improvements, or open issues.
Your feedback and contributions are always welcome!
