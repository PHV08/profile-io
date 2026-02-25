import sys
from analyzer import analyze_code
from profiler import generate_profile

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <python_file>")
        return

    filepath = sys.argv[1]
    metrics = analyze_code(filepath)
    profile = generate_profile(metrics)

    print("\n🧬 CodeDNA Profile")
    print("-" * 40)
    for key, value in profile.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
