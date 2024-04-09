import sqlite3
import pandas as pd

def get_table_data(table_name, conn):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    return df

db_file = 'ecommerce_platform1.db'
conn = sqlite3.connect(db_file)

# Display the selected table
df = get_table_data('ShippingDetails', conn)
print(f"df:{df}")

# Add new users
# import sqlite3
# import random
# from datetime import datetime, timedelta

# # Function to generate realistic and unique user data
# def generate_unique_users(existing_users, count, domain="example.com"):
#     base_names = ["Sophia", "Emma", "Olivia", "Ava", "Isabella", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn"]
#     last_names = ["Martinez", "Hernandez", "Lopez", "Gonzalez", "Sanchez", "Perez", "Garcia", "Rodriguez", "Lee", "Brown"]
#     existing_emails = {user[2] for user in existing_users}  # Extract existing emails from the current data
#     new_users = []
    
#     while len(new_users) < count:
#         first_name = random.choice(base_names)
#         last_name = random.choice(last_names)
#         email = f"{first_name.lower()}.{last_name.lower()}@{domain}"
#         # Ensure unique email
#         if email in existing_emails:
#             continue
#         existing_emails.add(email)

#         age = random.randint(22, 50)
#         registration_date = datetime.now() - timedelta(days=random.randint(1, 365 * 2))
#         address = f"{random.randint(100, 999)} {random.choice(['Oak', 'Maple', 'Pine', 'Elm', 'Cedar'])} St, {random.choice(['Springfield', 'Riverside', 'Greenfield', 'Hilltown', 'Lakeview'])}"
#         postal_code = f"011{random.randint(10, 99)}"
#         new_users.append((first_name + " " + last_name, email, age, registration_date.strftime('%Y-%m-%d'), address, postal_code))
    
#     return new_users

# # Function to insert users into the database
# def insert_users_into_db(db_path, new_users):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.executemany("INSERT INTO Users (Name, Email, Age, RegistrationDate, Address, PostalCode) VALUES (?, ?, ?, ?, ?, ?);", new_users)
#     conn.commit()
#     conn.close()

# # Main process
# def main():
#     db_path = 'ecommerce_platform1.db'  # Adjust this path to your database file location
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Users;")
#     existing_users = cursor.fetchall()
#     conn.close()

#     # Generate and insert new users
#     new_users_count = 30 - len(existing_users)  # Adjust the number as needed
#     new_users = generate_unique_users(existing_users, new_users_count)
#     insert_users_into_db(db_path, new_users)

#     print(f"Added {len(new_users)} new users to the database.")

# # Execute the program
# if __name__ == "__main__":
#     main()

# Add new orders
# import sqlite3
# import random
# from datetime import datetime, timedelta

# # Function to generate orders
# def generate_orders(user_ids, product_prices, count):
#     orders = []
#     for _ in range(count):
#         user_id = random.choice(user_ids)
#         order_date = datetime.now() - timedelta(days=random.randint(1, 365))
#         # Simulating order with 1 to 5 products
#         products = random.choices(list(product_prices.keys()), k=random.randint(1, 5))
#         total_amount = sum(product_prices[prod_id] for prod_id in products)
#         status = random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled'])
#         orders.append((user_id, order_date.strftime('%Y-%m-%d'), total_amount, status))
#     return orders

# # Function to insert orders into the database
# def insert_orders_into_db(db_path, orders):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.executemany("INSERT INTO Orders (UserID, OrderDate, TotalAmount, Status) VALUES (?, ?, ?, ?);", orders)
#     conn.commit()
#     conn.close()

# def main():
#     db_path = 'ecommerce_platform1.db'  # Adjust this path to your database file location

#     # Fetch existing user IDs and product prices
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute("SELECT UserID FROM Users;")
#     user_ids = [row[0] for row in cursor.fetchall()]
    
#     cursor.execute("SELECT ProductID, Price FROM Products;")
#     product_prices = {row[0]: row[1] for row in cursor.fetchall()}
#     conn.close()

#     # Generate and insert new orders
#     new_orders = generate_orders(user_ids, product_prices, 20)  # Number of orders to add
#     insert_orders_into_db(db_path, new_orders)

#     print(f"Added {len(new_orders)} new orders to the database.")

# # Execute the program
# if __name__ == "__main__":
#     main()


# import sqlite3

# # Replace 'your_database.db' with the path to your .db file
# db_path = 'ecommerce_platform1.db'

# # Connect to the SQLite database
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Get a list of all tables in the database
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()

# # Iterate through all tables
# for table_name in tables:
#     print(f"Table: {table_name[0]}")
#     cursor.execute(f"SELECT * FROM `{table_name[0]}`")

#     # Get all columns in the table
#     columns = [description[0] for description in cursor.description]
#     print(f"Columns: {', '.join(columns)}")

#     # Fetch and print all rows of the table
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

#     print()  # Print a newline for better readability between tables

# # Close the connection to the database
# conn.close()


# import sqlite3

# # Connect to your SQLite database
# conn = sqlite3.connect('ecommerce_platform1.db')  # Replace 'your_database.db' with the path to your database file
# cursor = conn.cursor()

# # SQL statement to delete rows
# delete_query = "DELETE FROM Orders WHERE OrderID > 20;"

# # Execute the SQL statement
# cursor.execute(delete_query)

# # Commit the transaction
# conn.commit()

# # Close the database connection
# conn.close()

# import sqlite3

# # Connect to your SQLite database
# conn = sqlite3.connect('ecommerce_platform1.db')  # Replace 'your_database.db' with the path to your database file
# cursor = conn.cursor()

# # SQL statement for inserting data
# insert_query = """
# INSERT INTO Orders (UserID, OrderDate, TotalAmount, Status)
# VALUES
# (13, '2022-06-03', 105.97, 'Delivered'),
# (19, '2022-06-05', 24.98, 'Shipped'),
# (24, '2022-06-07', 179.98, 'Processing'),
# (11, '2022-06-10', 28.98, 'Delivered'),
# (26, '2022-06-12', 194.98, 'Processing'),
# (15, '2022-06-15', 55.98, 'Shipped'),
# (21, '2022-06-17', 44.98, 'Delivered'),
# (17, '2022-06-19', 98.98, 'Processing'),
# (22, '2022-06-22', 124.97, 'Shipped'),
# (14, '2022-06-24', 22.99, 'Delivered'),
# (29, '2022-06-26', 1499.99, 'Processing'),
# (20, '2022-06-29', 34.98, 'Shipped'),
# (25, '2022-07-01', 114.97, 'Delivered'),
# (18, '2022-07-03', 64.98, 'Processing'),
# (27, '2022-07-06', 210.98, 'Shipped'),
# (23, '2022-07-08', 34.98, 'Delivered'),
# (16, '2022-07-11', 135.97, 'Processing'),
# (30, '2022-07-13', 254.97, 'Shipped'),
# (28, '2022-07-16', 18.98, 'Delivered'),
# (12, '2022-07-18', 45.99, 'Processing');
# """

# # Execute the SQL statement
# cursor.execute(insert_query)

# # Commit the transaction
# conn.commit()

# # Close the database connection
# conn.close()


#Add orderdetails
# import sqlite3

# # Connect to your SQLite database
# conn = sqlite3.connect('ecommerce_platform1.db')  # Replace 'your_database.db' with the path to your database file
# cursor = conn.cursor()

# # SQL statement for inserting data
# insert_query = """
# INSERT INTO OrderDetails (OrderID, ProductID, Quantity, PricePerUnit)
# VALUES
# (21, 14, 5, 2.99),
# (21, 13, 3, 5.99),
# (22, 26, 2, 12.99),
# (23, 21, 1, 199.99),
# (23, 12, 1, 15.99),
# (24, 15, 1, 12.99),
# (24, 16, 1, 8.99),
# (25, 5, 5, 19.99),
# (25, 6, 3, 49.99),
# (26, 29, 2, 15.99),
# (26, 30, 1, 17.99),
# (27, 20, 4, 9.99),
# (28, 25, 2, 29.99),
# (28, 26, 1, 12.99),
# (29, 27, 1, 89.99),
# (29, 28, 1, 24.99),
# (30, 18, 1, 22.99),
# (31, 1, 1, 1499.99),
# (32, 29, 2, 15.99),
# (33, 14, 4, 2.99),
# (33, 13, 3, 5.99),
# (34, 24, 4, 9.99),
# (34, 23, 1, 45.99),
# (35, 4, 3, 29.99), 
# (35, 3, 2, 14.99), 
# (36, 15, 1, 12.99), 
# (36, 16, 1, 8.99), 
# (37, 7, 1, 99.99),
# (37, 8, 1, 149.99),
# (38, 22, 1, 499.99),
# (38, 19, 1, 19.99),
# (39, 16, 2, 8.99),
# (40, 23, 1, 45.99);
# """

# # Execute the SQL statement
# cursor.execute(insert_query)

# # Commit the transaction
# conn.commit()

# # Close the database connection
# conn.close()

#add reviews

# import sqlite3

# # Connect to your SQLite database
# # conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with the path to your database file
# cursor = conn.cursor()

# # SQL statement for inserting data
# insert_query = """
# INSERT INTO Reviews (ProductID, UserID, Rating, Comment)
# VALUES 
# (5, 25, 4, 'The T-shirts are comfortable and fit well. Good value for the price.'),
# (6, 25, 5, 'Love these jeans! They''re stylish and well-made.'),
# (14, 21, 3, 'The bread is tasty but it does get stale quickly as others have mentioned.'),
# (13, 21, 5, 'This green tea is my new favorite! It''s so refreshing.'),
# (20, 27, 4, 'Cute and sturdy flower pots, perfect for my herbs.'), 
# (4, 27, 5, 'This book was a great help in my Python programming course!'),
# (23, 16, 4, 'My dog loves this food and it seems to be very healthy for him.'),
# (24, 16, 3, 'The cat toy is okay, but my cat got bored with it quickly.');
# """

# # Execute the SQL statement
# cursor.execute(insert_query)

# # Commit the transaction
# conn.commit()

# # Close the database connection
# conn.close()


# import sqlite3

# # Connect to your SQLite database
# # conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with the path to your database file
# cursor = conn.cursor()

# # SQL statement for inserting data
# insert_query = """
# INSERT INTO ShippingDetails (OrderID, ShippingAddress, EstimatedDeliveryDate, ActualDeliveryDate)
# VALUES 
# (21, '579 Willow Way, Cliffside', '2022-06-08', '2022-06-07'),
# (22, '965 Pine St, Springfield', '2022-06-10', '2022-06-09'),
# (23, '117 Cedar St, Lakeview', '2022-06-12', NULL),
# (24, '135 Oak Drive, Riverdale', '2022-06-15', '2022-06-14'),
# (25, '268 Maple St, Hilltown', '2022-06-17', NULL),
# (26, '902 Cedar Path, Mountainview', '2022-06-20', '2022-06-19'),
# (27, '863 Pine St, Lakeview', '2022-06-22', '2022-06-21'),
# (28, '217 Pine St, Hilltown', '2022-06-24', NULL),
# (29, '675 Maple St, Lakeview', '2022-06-27', '2022-06-26'),
# (30, '368 Elm Avenue, Lakeside', '2022-06-29', '2022-06-28'),
# (31, '389 Maple St, Springfield', '2022-07-02', NULL),
# (32, '376 Maple St, Greenfield', '2022-07-05', '2022-07-04'),
# (33, '135 Elm St, Lakeview', '2022-07-07', '2022-07-06'),
# (34, '887 Pine St, Lakeview', '2022-07-09', NULL),
# (35, '975 Pine St, Hilltown', '2022-07-12', '2022-07-11'),
# (36, '573 Elm St, Greenfield', '2022-07-14', '2022-07-13'),
# (37, '435 Cedar St, Lakeview', '2022-07-16', NULL),
# (38, '399 Maple St, Greenfield', '2022-07-18', '2022-07-17'),
# (39, '221 Maple St, Hilltown', '2022-07-20', '2022-07-19'),
# (40, '246 Pine Street, Brookside', '2022-07-22', NULL);
# """

# # Execute the SQL statement
# cursor.execute(insert_query)

# # Commit the transaction
# conn.commit()

# # Close the database connection
# conn.close()
