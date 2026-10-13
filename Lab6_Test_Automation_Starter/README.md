# Lab 6 — Online Shopping System Test Automation

## What this project tests
The sample `calculate_discount` function applies example discount rules based on membership and cart total. The rules are illustrative; replace them with the exact conditions from your Lab 4 decision table if required.

## Run locally
1. Open this folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Run `python -m pip install -r requirements.txt`.
4. Run `python -m pytest -v`.

## GitHub Actions
The workflow at `.github/workflows/tests.yml` installs pytest and runs the tests on pushes, pull requests, and manual workflow dispatches.

## Suggested screenshots
- Project files visible in VS Code.
- Terminal showing the actual pytest result.
- GitHub Actions run showing the result after the repository is pushed.
- A failed test after a temporary intentional defect, followed by a passing run after restoring the code.

Do not claim a test passed until you have run it and captured your own result.
