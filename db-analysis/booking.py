
import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('hotel_booking.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Retrieve and print the first row from the booking_summary table
cursor.execute("SELECT * FROM booking_summary LIMIT 1")
first_row = cursor.fetchone()
print("First row of booking_summary:")
print(first_row)

# Retrieve and print the first ten rows from the booking_summary table
cursor.execute("SELECT * FROM booking_summary LIMIT 10")
first_ten_rows = cursor.fetchall()
print("First ten rows of booking_summary:")
for row in first_ten_rows:
    print(row)

# Retrieve and print the first five rows where the country is 'BRA' from the booking_summary table
cursor.execute("SELECT * FROM booking_summary WHERE country = 'BRA' LIMIT 5")
bra = cursor.fetchall()
print("BRA bookings (first 5 rows):")
for row in bra:
    print(row)

# Create a new table named bra_customers with specified fields if it does not already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS bra_customers
                  (num INTEGER, hotel TEXT, is_cancelled INTEGER, lead_time INTEGER,
                  arrival_date_year INTEGER, arrival_date_month TEXT, arrival_date_day_of_month INTEGER,
                  adults INTEGER, children INTEGER, country TEXT, adr REAL, special_requests INTEGER)''')

# Insert the retrieved 'BRA' bookings into the bra_customers table
cursor.executemany("INSERT INTO bra_customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", bra)

# Retrieve and print the first ten rows from the bra_customers table
cursor.execute("SELECT * FROM bra_customers LIMIT 10")
bra_customers_rows = cursor.fetchall()
print("First 10 rows of bra_customers:")
for row in bra_customers_rows:
    print(row)

# Retrieve the lead time for bookings that were canceled from the bra_customers table
cursor.execute("SELECT lead_time FROM bra_customers WHERE is_cancelled = 1")
lead_time_cancelled = cursor.fetchall()

# Calculate and print the average lead time for canceled bookings
average_lead_time_cancelled = sum([row[0] for row in lead_time_cancelled]) / len(lead_time_cancelled)
print("Average lead time for cancelled bookings:", average_lead_time_cancelled)

# Retrieve the lead time for bookings that were not canceled from the bra_customers table
cursor.execute("SELECT lead_time FROM bra_customers WHERE is_cancelled = 0")
lead_time_not_cancelled = cursor.fetchall()

# Calculate and print the average lead time for non-canceled bookings
average_lead_time_not_cancelled = sum([row[0] for row in lead_time_not_cancelled]) / len(lead_time_not_cancelled)
print("Average lead time for not cancelled bookings:", average_lead_time_not_cancelled)

# Retrieve the special requests for bookings that were canceled from the bra_customers table
cursor.execute("SELECT special_requests FROM bra_customers WHERE is_cancelled = 1")
special_requests_cancelled = cursor.fetchall()

# Calculate and print the total special requests for canceled bookings
total_special_requests_cancelled = sum([row[0] for row in special_requests_cancelled])
print("Total special requests for cancelled bookings:", total_special_requests_cancelled)

# Retrieve the special requests for bookings that were not canceled from the bra_customers table
cursor.execute("SELECT special_requests FROM bra_customers WHERE is_cancelled = 0")
special_requests_not_cancelled = cursor.fetchall()

# Calculate and print the total special requests for non-canceled bookings
total_special_requests_not_cancelled = sum([row[0] for row in special_requests_not_cancelled])
print("Total special requests for not cancelled bookings:", total_special_requests_not_cancelled)

# Commit the changes and close the connection to the database
conn.commit()
conn.close()
