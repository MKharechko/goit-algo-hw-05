
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }

def load_logs(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        return [log for line in file if (log := parse_log_line(line))]
    
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log.get("level", "").lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log.get("level", "UNKNOWN") for log in logs if "level" in log))

def display_log_counts(counts: dict):
    print("\n=== Підрахунок логів за рівнями ===")
    for level, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{level:<10}: {count:>5} записів")
    print("=" * 35)

def main():
    file_path = "path\logfile.log" 
    logs = load_logs(file_path)
    
    if not logs:
        print("Файл логів порожній або не існує.")
        return
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

if __name__=="__main__":
    main()