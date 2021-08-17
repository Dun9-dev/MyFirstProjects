current_users = ['user3', 'user2', 'user1', 'user4', 'user5', 'ADMin']
copy_current_users = [name.lower() for name in current_users]
new_users = ['carl', 'jon', 'Admin', 'uSEr2', 'sasha']
for new_users in new_users:
    if new_users.lower() in copy_current_users:
        print("The name is not available, select another")
    else:
        print("Good name!")
if current_users:
    for current_users in current_users:
        if current_users.lower() == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {current_users}, thank you for logging again.")
else:
    print("We need to ind some users!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numbers in numbers:
    if numbers == 1:
        print(f'{numbers}st')
    elif numbers == 2:
        print(f'{numbers}nd')
    elif numbers == 3:
        print(f'{numbers}rd')
    else:
        print(f'{numbers}th')

