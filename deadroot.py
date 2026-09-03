#!/usr/bin/env python3

"""
DeadRoot
Developed by Fawad Qureshi
Instagram: @h4cker_fawad
"""

from modules import crypto_tools
from modules import wifi_tool
from modules import bluetooth_tools
from modules import osint_tools

def main():
while True:
print("""
╔══════════════════════════════════════════════════╗
║                    DeadRoot                      ║
║             Developed by Fawad Qureshi           ║
║              Instagram: @h4cker_fawad            ║
╠══════════════════════════════════════════════════╣
║ [1] Information Gathering / OSINT                ║
║ [2] Cryptography Tools                           ║
║ [3] Wi-Fi Tools                                  ║
║ [4] Bluetooth Tools                              ║
║ [0] Exit                                         ║
╚══════════════════════════════════════════════════╝
""")

```
    choice = input("DeadRoot » ").strip()

    if choice == "1":
        osint_tools.menu()
    elif choice == "2":
        crypto_tools.menu()
    elif choice == "3":
        wifi_tool.menu()
    elif choice == "4":
        bluetooth_tools.menu()
    elif choice == "0":
        print("\nGoodbye!")
        break
    else:
        print("[!] Invalid option")
```

if **name** == "**main**":
main()
