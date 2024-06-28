import csv
import json

# List to hold compromised usernames
compromised_users = []

# Read usernames from the CSV file and append them to compromised_users list
try:
    with open("passwords.csv", "r") as password_file:
        password_csv = csv.DictReader(password_file)
        for password_row in password_csv:
            username = password_row['Username']
            compromised_users.append(username)
except FileNotFoundError:
    print("Error: 'passwords.csv' file not found.")
except Exception as e:
    print(f"An error occurred while reading the passwords: {e}")

# Write compromised usernames to a text file
try:
    with open("compromised_users.txt", "w") as compromised_user_file:
        for compromised_user in compromised_users:
            compromised_user_file.write(compromised_user + "\n")
except Exception as e:
    print(f"An error occurred while writing the compromised users: {e}")

# Create a dictionary with the boss message
boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
}

# Write the boss message to a JSON file
try:
    with open("boss_message.json", "w") as boss_message:
        json.dump(boss_message_dict, boss_message)
except Exception as e:
    print(f"An error occurred while writing the boss message: {e}")

# Scrambled password art
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

# Write the scrambled password art to a new CSV file
try:
    with open("new_passwords.csv", "w") as new_passwords_obj:
        new_passwords_obj.write(slash_null_sig)
except Exception as e:
    print(f"An error occurred while writing the new passwords: {e}")
