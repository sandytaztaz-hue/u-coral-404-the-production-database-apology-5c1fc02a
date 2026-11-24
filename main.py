#!/usr/bin/env python3
"""Write the production database apology entry to /output/entry.txt."""

import os

ENTRY = "Sorry — during the migration I renamed customers to customers_old_final_v2, then dropped the original to keep things tidy. The customers are gone, but the naming convention is immaculate."  # 187 chars, one line, punchline last

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
