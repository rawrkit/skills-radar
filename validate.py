#!/usr/bin/env python3
"""Validate catalog.json.

The catalog is consumed by agents that fetch it over HTTP and parse it with a
strict JSON parser, so a stray byte-order mark or a duplicate id breaks real
users rather than just looking untidy.

Checks:
  1. no UTF-8 BOM (a BOM makes json.load and many other parsers fail outright)
  2. valid JSON
  3. required fields present on every entry
  4. status is one of the four known values
  5. roles come from the known set
  6. no duplicate ids

Exit code 0 = clean, 1 = problems. Run: python validate.py
"""
import json
import pathlib
import sys

CATALOG = pathlib.Path(__file__).parent / "catalog.json"
REQUIRED = ("id", "source", "url", "category", "roles", "status", "description_en")
STATUSES = {"approved", "in-kit", "new", "rejected"}
ROLES = {"BA", "PO", "SM", "DEV", "QA", "ALL"}

errors: list[str] = []

raw = CATALOG.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    errors.append("catalog.json starts with a UTF-8 BOM — strict JSON parsers reject it")
    raw = raw[3:]

entries = []
try:
    entries = json.loads(raw.decode("utf-8")).get("entries", [])
except json.JSONDecodeError as exc:
    errors.append(f"invalid JSON — {exc}")

seen: dict[str, int] = {}
for i, e in enumerate(entries):
    where = e.get("id") or f"entries[{i}]"
    for field in REQUIRED:
        if not e.get(field):
            errors.append(f"{where}: missing or empty '{field}'")
    status = e.get("status")
    if status and status not in STATUSES:
        errors.append(f"{where}: unknown status '{status}' (expected one of {sorted(STATUSES)})")
    for role in e.get("roles", []):
        if role not in ROLES:
            errors.append(f"{where}: unknown role '{role}'")
    if e.get("id"):
        seen[e["id"]] = seen.get(e["id"], 0) + 1

for eid, count in seen.items():
    if count > 1:
        errors.append(f"duplicate id '{eid}' appears {count}x")

for e in errors:
    print(f"ERROR {e}")
print(f"\n{len(entries)} entries, {len(errors)} errors")
sys.exit(1 if errors else 0)
