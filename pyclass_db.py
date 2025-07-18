import pyclass_def

db = pyclass_def.WriteDB()

if db.connect():
    db.create_table()
        
    # Insert individual users
    db.insert_user("Alice Johnson", "alice@email.com", 28)
    db.insert_user("Bob Smith", "bob@email.com", 34)
    db.insert_user("Carol Davis", "carol@email.com", 22)
    
    # Insert multiple users at once
    users_to_add = [
        ("David Wilson", "david@email.com", 29),
        ("Eva Brown", "eva@email.com", 31),
        ("Frank Miller", "frank@email.com", 27)
    ]
    db.insert_multiple_users(users_to_add)

    # Get all users
    all_users = db.get_all_users()
    print("\nAll users:")
    for user in all_users:
        print(user)

    # Update user age

    # Update user age
    # db.update_user_age(1, 30)

    # # Delete user
    # db.delete_user(2)

    # # Get all users again
    # all_users = db.get_all_users()
    # print("\nAll users after updates:")
    # for user in all_users:
    #     print(user)

    # Close the database connection
    db.close()  # Close the database connection


