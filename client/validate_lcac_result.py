#!/usr/bin/env python3
"""
LCAC Benchmark Result Validator
--------------------------------
Validates benchmark result files against the official LCAC schema.

Usage:
    python3 validate_lcac_result.py path/to/lcac_benchmark_[timestamp].json
"""

import sys
import json
import pathlib
from jsonschema import validate, ValidationError

SCHEMA_PATH = pathlib.Path(__file__).parent.parent / "spec" / "lcac_metrics_schema.json"

def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[✗] Error reading JSON file: {e}")
        sys.exit(1)

def load_schema():
    try:
        with open(SCHEMA_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[✗] Error loading LCAC schema: {e}")
        sys.exit(1)

def validate_result(result_path):
    data = load_json(result_path)
    schema = load_schema()

    print(f"\n🔍 Validating {result_path} against LCAC schema...\n")

    try:
        validate(instance=data, schema=schema)
        print("✅ Validation successful — LCAC result file is valid and complete.\n")
        print(json.dumps(data, indent=2))
    except ValidationError as e:
        print(f"❌ Validation failed:\n\n{e.message}\n")
        print(f"At: {' → '.join(str(x) for x in e.path)}\n")
        sys.exit(1)

if __name__ == "__main__":
    results_dir = pathlib.Path("results")
    files = sorted(results_dir.glob("lcac_benchmark_*.json"))
    if len(sys.argv) < 2:
        if files:
            result_path = files[-1]
            print(f"[i] No file provided — validating latest: {result_path}")
        else:
            print("[✗] No LCAC result files found in results/")
            sys.exit(1)
    else:
        result_path = pathlib.Path(sys.argv[1])

    if not result_path.exists():
        print(f"[✗] File not found: {result_path}")
        sys.exit(1)

    validate_result(result_path)
