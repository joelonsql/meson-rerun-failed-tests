# Meson Rerun Failed Tests

## Introduction

When developing, you frequently run tests. If a test is failing, your main concern is whether your fix will make that specific test pass. If it does, running all other tests becomes necessary to ensure you haven't introduced new issues. However, if the failing test continues to fail, running all other tests is somewhat pointless since you haven't yet resolved the problem you're working on.

Currently, when you run `meson test` and encounter a failed test, executing `meson test` again will start all tests from the beginning. Unfortunately, Meson doesn't have a `--rerun-failed` option yet, but hopefully it will be introduced in the future.

The proposed command:

```bash
# Won't work, since this option doesn't exist (yet)
meson test --rerun-failed
```

would rerun only the tests that failed in the last run. This allows you to quickly check if your fix addresses the issue without waiting for all preceding tests to run. If the previously failed tests now pass, it could then proceed to run all other tests to ensure overall stability.

If/when Meson adds this functionality, this repository will be deprecated in favor of the official implementation, as that would provide a more integrated and maintainable solution. 

Until then, you can use a script to achieve similar functionality.

## How it Works

The script:

1. **Analyzes Test Log**:
   - Reads `./meson-logs/<logbase>.json` if it exists
   - Extracts failed test names from JSONL entries

2. **Executes Tests**:
   - Without failed tests: runs full suite
   - With failed tests: runs failed tests first
     - If they pass: runs full suite
     - If they fail: exits with error

The script is designed to be a drop-in replacement for `meson test`, accepting all standard Meson test arguments while adding the failed-test-first optimization.

## Prerequisites

- **Python 3**: Ensure Python 3.x is installed on your system.
- **Meson Build System**: Installed and configured for your project.
- **Meson in PATH**: The `meson` command should be accessible from the command line.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/meson-rerun-failed-tests.git
   ```

2. **Navigate to the directory**:
   ```bash
   cd meson-rerun-failed-tests
   ```

3. **Install to your user's bin directory**:
   ```bash
   mkdir -p ~/.local/bin
   cp meson-rerun-failed-tests.py ~/.local/bin/meson-rerun-failed-tests
   chmod +x ~/.local/bin/meson-rerun-failed-tests
   ```

   Note: Make sure `~/.local/bin` is in your PATH. If it isn't, add this line to your `~/.bashrc` or `~/.zshrc`:
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

## Usage

Run the script instead of `meson test` to utilize its functionality. 
