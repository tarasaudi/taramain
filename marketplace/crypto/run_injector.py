# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MpDbQhYOO3_gqQmkZ5GSsxgh3QkUXQ44
"""

from affiliate_manager import inject_global_affiliates, list_affiliates, get_affiliate_count

def main():
    agent_id = "A001"
    csv_file = "global_affiliate_platforms.csv"

    affiliate_codes = {
        "Binance": "CPA_00EDS8MQJG",
        "Coinbase": "YOUR_COINBASE_CODE",
        "Crypto.com": "YOUR_CRYPTO_COM_CODE",
    }

    print(f"Injecting global affiliates into agent '{agent_id}' from '{csv_file}' ...")

    inject_global_affiliates(agent_id, csv_file, affiliate_codes)

    total = get_affiliate_count(agent_id)
    print(f"Injection complete! Total affiliates under '{agent_id}': {total}")

    affiliates = list_affiliates(agent_id)
    for aff in affiliates:
        print(f"{aff['name']}: {aff['referral_link']}")

if __name__ == "__main__":
    main()