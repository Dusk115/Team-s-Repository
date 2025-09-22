import sys
import os
import src.utils.parse_input as pi

INPUT_DIR = "input"

if __name__ == "__main__":
    files = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]

    for idx, fname in enumerate(files, start=1):
        print(f"  {idx}. {fname}")
        try:
            input_file = os.path.join(INPUT_DIR, files[0])
            print(f"\nUsing input file: {input_file}\n")

            try:
                pi.demo(input_file)
            except Exception as e:
                print(f"Error running demo: {e}")

        except ValueError:
            print("Invalid input. Please enter a number.")
