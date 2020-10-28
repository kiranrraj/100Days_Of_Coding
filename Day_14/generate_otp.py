# Title  : Generate 6 digit number
# Author : Kiran raj R.
# Date   : 28:10:2020

import secrets

secretsGenerator = secrets.SystemRandom()
num = secretsGenerator.randrange(100000, 999999)

print(f"The generated number is {num}")
