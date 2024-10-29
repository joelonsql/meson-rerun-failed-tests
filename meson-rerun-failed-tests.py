#!/usr/bin/env python3

import json
import subprocess
import sys
import argparse
from pathlib import Path

def run_meson_tests(test_names=None, meson_args=None):
    """Run meson tests with the given test names and arguments"""
    if meson_args is None:
        meson_args = []
    
    meson_command = ["meson", "test"] + meson_args
    if test_names:
        meson_command.extend(test_names)

    command_str = ' '.join(f'"{arg}"' if ' ' in arg else arg for arg in meson_command)
    print("\n🐘🧪 Constructed Meson Test Command:")
    print(command_str)

    print("\n🐘🧪 Executing Meson Test Command...")
    try:
        result = subprocess.run(meson_command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n🐘💔 Meson tests failed with return code {e.returncode}.")
        return False
    except FileNotFoundError:
        print(f"\n🐘💔 Error: 'meson' command not found. Please ensure Meson is installed and in your PATH.")
        sys.exit(1)

def parse_test_log(test_log_path):
    """Parse the test log and return a list of failed tests"""
    failed_tests = []
    # Read and parse the test log (JSONL format - one JSON object per line)
    with test_log_path.open('r') as log_file:
        for line_num, line in enumerate(log_file, start=1):
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            try:
                test = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"🐘💔 Error: Invalid JSON on line {line_num}: {e}")
                sys.exit(1)

            if test.get('result') == "ERROR":
                full_test_name = test.get('name', '')
                if ' / ' in full_test_name:
                    _, test_name = full_test_name.split(' / ', 1)
                else:
                    test_name = full_test_name  # Fallback if format is unexpected
                failed_tests.append(test_name)
    return failed_tests

def main():
    # Parse just the logbase argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--logbase', default='testlog')
    
    # Parse known args to extract logbase
    args, _ = parser.parse_known_args()
    
    test_log_path = Path(f'./meson-logs/{args.logbase}.json')

    if not test_log_path.is_file():
        print(f"🐘🧪 Test log '{test_log_path}' does not exist. Assuming this is the first run.")
        failed_tests = []
    else:
        failed_tests = parse_test_log(test_log_path)

    # Pass all command line args except the script name through to meson as-is
    meson_args = sys.argv[1:]

    if not failed_tests:
        print(f"🐘✅ No previous failed tests found. Running all tests...")
        success = run_meson_tests(meson_args=meson_args)
        sys.exit(0 if success else 1)
    else:
        print(f"🐘💔 Failed Tests:")
        for test in failed_tests:
            print(f"   - {test}")

        print("\n🐘🧪 Running previously failed tests...")
        if run_meson_tests(failed_tests, meson_args):
            print(f"\n🐘✅ Previously failed tests now pass. Running all tests...")
            success = run_meson_tests(meson_args=meson_args)
            sys.exit(0 if success else 1)
        else:
            sys.exit(1)

if __name__ == "__main__":
    main()
