# ==========================================
# Week 7 Assignment: My Notes & The Report Builder
# ==========================================

def manage_notes():
    """Part 1: My Notes - Writing and reading notes from a file."""
    print("--- Part 1: My Notes ---")
    
    # Prompt the user for input
    user_note = input("Enter a note you would like to save: ")
    
    # Write the note to 'notes.txt' using 'w' (or 'a' if appending)
    # Using 'with' ensures the file closes automatically and safely
    with open("notes.txt", "w") as file:
        file.write(user_note + "\n")
    print("✓ Note successfully written to 'notes.txt'.\n")
    
    # Read the contents back from 'notes.txt' and display them
    print("Reading contents from 'notes.txt':")
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file 'notes.txt' was not found.")


def report_builder():
    """Part 2: The Report Builder - Generating and formatting a text report."""
    print("--- Part 2: The Report Builder ---")
    
    # Define report details and data
    report_title = "Python File Handling Progress Report"
    author_name = "PLP Student"
    status = "Completed Successfully"
    
    report_filename = "report.txt"
    
    # Writing a structured report to a file
    with open(report_filename, "w") as report_file:
        report_file.write("=" * 45 + "\n")
        report_file.write(f"{report_title.center(45)}\n")
        report_file.write(f"Author: {author_name}\n")
        report_file.write(f"Status: {status}\n")
        report_file.write("=" * 45 + "\n\n")
        report_file.write("Report Summary:\n")
        report_file.write("- Successfully practiced file creation and writing.\n")
        report_file.write("- Implemented safe resource management using context managers ('with').\n")
        report_file.write("- Parsed and displayed file content back to the user.\n\n")
        report_file.write("=" * 45 + "\n")
        
    print(f"✓ Report successfully generated and saved to '{report_filename}'.\n")
    
    # Verify by reading the generated report back out
    print(f"Displaying contents of '{report_filename}':")
    with open(report_filename, "r") as report_file:
        print(report_file.read())


if __name__ == "__main__":
    # Execute both parts of the assignment
    manage_notes()
    print("\n" + "="*50 + "\n")
    report_builder()
