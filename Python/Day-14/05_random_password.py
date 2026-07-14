import random
import string

character_pool = string.ascii_letters + string.digits

password_length = random.randint(10, 12)

password = ''

for i in range(password_length):
    password += random.choice(character_pool)

print(f"Generated Password: {password}")