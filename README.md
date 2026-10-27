# BuildGuard-CI

An automated build validation and test analysis pipeline designed to support software build, test, and deployment workflows using CI/CD concepts.

## Project Details
Created to assist with development and validation activities by scanning execution logs, catching component defects, and automating software build verification.

## Implementation Summary
- **C++ Validator (`validator_core.cpp`):** Fast command-line parser that inspects test output logs, calculates pass/fail ratios, and returns proper exit codes for build verification.
- **Python CI Orchestrator (`ci_runner.py`):** Manages mock log generation, handles automatic binary compilation via `g++`, and formats execution status into structured summaries.

## Setup & Execution
Ensure `g++` and Python 3 are available in your environment, then run:

```bash
python3 ci_runner.py
