import json
from moderator import moderate_text

def load_content(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

def run_moderation(filename="sample_content.txt"):
    content_list = load_content(filename)
    results = []

    for text in content_list:
        result = moderate_text(text)
        results.append(result)

        icon = "✅" if result["status"] == "APPROVED" else "⚠️" if result["status"] == "FLAGGED" else "❌"
        print(f"{icon} {result['status']} - \"{text}\"")
        if result["reasons"]:
            print(f"   Reasons: {', '.join(result['reasons'])}")

    with open("report.json", "w") as report_file:
        json.dump(results, report_file, indent=2)

    print("\n📄 Report saved to report.json")

if __name__ == "__main__":
    run_moderation()
    