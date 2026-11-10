# report_builder.py
import os

csv_filename = "hubs.csv"
report_filename = "report.txt"

if not os.path.exists(csv_filename):
    print("hubs.csv not found")
else:
    total_learners = 0
    passes = 0
    failed = 0
    total_score = 0

    with open(csv_filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) == 3:
            total_learners += 1
            score = int(parts[2])
            total_score += score

            if score >= 50:
                passes += 1
            else:
                failed += 1

    average_score = total_score / total_learners if total_learners > 0 else 0

    report_content = (
        f"Total Learners: {total_learners}\n"
        f"Passes: {passes}\n"
        f"Failed: {failed}\n"
        f"Average Score: {average_score:.2f}\n"
    )

    with open(report_filename, "w", encoding="utf-8") as report_file:
        report_file.write(report_content)

    print(f"Report generated successfully in '{report_filename}':")
    print(report_content)
