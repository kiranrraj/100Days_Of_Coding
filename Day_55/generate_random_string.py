# Title  : Generate random string
# Author : Kiran raj R.
# Date   : 24:10:2020

import secrets

print(f"Random secure Hexadecimal token is {secrets.token_hex(64)}")
print(f"Random secure URL is {secrets.token_urlsafe(64)}")
