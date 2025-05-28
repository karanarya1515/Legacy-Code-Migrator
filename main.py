import os
import ollama

INPUT_DIR = "inputs"
OUTPUT_DIR = "outputs"

def detect_language(filename):
    ext = os.path.splitext(filename)[1]
    language_map = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.cs': 'C#',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.go': 'Go',
        '.rs': 'Rust'
    }
    return language_map.get(ext, "unknown")

def migrate_code(file_path):
    with open(file_path, "r") as f:
        legacy_code = f.read()

    filename = os.path.basename(file_path)
    language = detect_language(filename)

    print(f"🛠️ Processing: {filename} as {language}...")

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": f"Modernize this legacy {language} code and explain the changes step by step:\n\n{legacy_code}"}
        ]
    )

    migrated_code = response["message"]["content"]

    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, "w") as f:
        f.write(migrated_code)

    print(f"✅ Migrated code saved to {output_path}")

def list_input_files():
    files = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
    if not files:
        print("❌ No input files found.")
        return []
    print("\n📁 Available input files:")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    return files

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    while True:
        print("\n===== Legacy Code Migration Assistant =====")
        print("1. List input files")
        print("2. Migrate a specific file")
        print("3. Migrate all files")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_input_files()

        elif choice == "2":
            files = list_input_files()
            if not files:
                continue
            try:
                selection = int(input("Enter file number to migrate: ")) - 1
                if 0 <= selection < len(files):
                    file_path = os.path.join(INPUT_DIR, files[selection])
                    migrate_code(file_path)
                else:
                    print("❌ Invalid file number.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            files = list_input_files()
            if not files:
                continue
            for file in files:
                file_path = os.path.join(INPUT_DIR, file)
                migrate_code(file_path)

        elif choice == "4":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()





