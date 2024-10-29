# Meson Rerun Failed Tests

A Python script that helps you find out faster if your "totally going to work this time" fix actually worked.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Command-Line Options](#command-line-options)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Ever spent 10 minutes waiting for all tests to run, only to find out your fix didn't work? `meson-rerun-failed-tests.py` is here to help! It first runs just the previously failed tests, giving you quick feedback on whether your fix worked, before running the full test suite. Because let's face it - sometimes our first (or second... or third...) attempt at fixing a bug doesn't quite hit the mark.

## Features

- Immediately runs previously failed tests first - no more waiting through passing tests just to hit the failures
- If the failing tests pass, automatically runs the full test suite to ensure no regressions
- If they're still failing, tells you right away so you can get back to fixing them
- Provides clear and informative console output with status indicators
- Accepts all standard `meson test` arguments and options

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
