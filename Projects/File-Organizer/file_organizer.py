"""
File Organizer
Reads all files in a chosen folder, categorizes them by extension,
moves them into category subfolders, and generates a summary report.
"""

import os
import shutil
from datetime import datetime

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".md"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Others": [],
}


def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder.")
        return

    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    counts = {category: 0 for category in CATEGORIES}
    failed = []
    total_processed = 0

    for filename in files:
        source_path = os.path.join(folder_path, filename)
        _, extension = os.path.splitext(filename)
        category = get_category(extension)

        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

        destination_path = os.path.join(category_folder, filename)

        total_processed += 1
        try:
            shutil.move(source_path, destination_path)
            counts[category] += 1
        except (shutil.Error, OSError) as e:
            failed.append((filename, str(e)))

    print_summary(counts, total_processed, failed)
    generate_report(folder_path, counts, total_processed, failed)


def print_summary(counts, total_processed, failed):
    print("\n--- Organization Summary ---")
    print(f"Total files processed: {total_processed}")
    for category, count in counts.items():
        print(f"  {category}: {count}")
    if failed:
        print(f"Files that couldn't be moved: {len(failed)}")
        for filename, error in failed:
            print(f"  - {filename}: {error}")
    else:
        print("Files that couldn't be moved: 0")


def generate_report(folder_path, counts, total_processed, failed):
    report_path = os.path.join(folder_path, "organization_report.txt")

    with open(report_path, "w") as report:
        report.write("File Organization Report\n")
        report.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.write("=" * 40 + "\n\n")
        report.write(f"Total files processed: {total_processed}\n\n")

        report.write("Files per category:\n")
        for category, count in counts.items():
            report.write(f"  {category}: {count}\n")

        report.write("\nFiles that couldn't be moved:\n")
        if failed:
            for filename, error in failed:
                report.write(f"  - {filename}: {error}\n")
        else:
            report.write("  None\n")

    print(f"\nReport generated at: {report_path}")


def main():
    folder_path = input("Enter the folder path to organize: ").strip()
    organize_folder(folder_path)


if __name__ == "__main__":
    main()
