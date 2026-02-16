import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Member:
    def __init__(self, first_name, last_name, id, status):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.status = status

    def display_member(self):
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'ID: {self.id}')
        print(f'Status: {self.status}')
        print('='* 40)

def create_user():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    id = input('Enter your membership ID: ')
    status = input('Enter the membership status, or click enter: ').lower()
    if status == '':
        status = 'inactive'
    while status not in ('active', 'inactive'):
        status = input('Please type active, inactive or click enter: ').lower()
        continue
    print('User added successfully!\n')
    return Member(first_name, last_name, id, status)
        
members = []
while True:
    print('Welcome to Gym Membership Management!\n\n')
    print('choose an action:-')
    print('1) Add new member')
    print('2) Display all members')
    print('3) Search for a member')
    print('4) Exit\n ')
    choice = input('Enter your choice: ')
    while choice not in ('1','2','3','4'):
        choice = input('Please type only 1, 2, 3, or 4: ')
        continue

    if choice == '1':
        clear_screen()
        new_user = create_user()
        members.append(new_user)
        time.sleep(2)
        clear_screen()

    elif choice == '2':
        clear_screen()
        print('Displaying users ....\n')
        time.sleep(2)
        if not members:
            print('There are no users ....')
            time.sleep(2)
            clear_screen()
        else:
            for i, member in enumerate(members):
                print(f'Member {i+1}:-')
                member.display_member()
            time.sleep(2)
            input('Press enter to return to the main screen ...')
            clear_screen()
    elif choice == '3':
        if members:
            clear_screen()
            print('Search by:-')
            print('1) Membership ID')
            print('2) First Name')
            print('3) Membership Status')
            choice1 = input('Enter your choice: ')
            while choice1 not in ('1','2','3'):
                choice1 = input('Please type only 1, 2, or 3: ')
                continue
            if choice1 == '1':
                clear_screen()
                id_searched = input('Enter the ID: ')
                found = False
                for member in members:
                    if member.id == id_searched:
                        member.display_member()
                        found = True

                if not found:
                    print('Member not found, check the ID again')
                        
                time.sleep(2)
                input('Press enter to return to the main screen ...')
                clear_screen()
                
            elif choice1 == '2':
                clear_screen()
                name = input('Enter the First Name: ').lower()
                found = False
                for member in members:
                    if member.first_name.lower() == name:
                        member.display_member()
                        found = True
                if not found:
                    print('Member not found, check the Name again')
                    
                time.sleep(2)
                input('Press enter to return to the main screen ...')
                clear_screen()
                
            else:
                clear_screen()
                status = input('Enter the Membership Status: ').lower()
                found = False
                for  member in members:
                    if member.status.lower() == status:
                        member.display_member()
                        found = True
                if not found:
                    print('Member not found, check the status again')
                
                time.sleep(2)
                input('Press enter to return to the main screen ...')
                clear_screen()
        else:
            clear_screen()
            print('There are no members!')
            time.sleep(2)
            clear_screen()
    else:
        clear_screen()
        print('Thank you for using our application')
        time.sleep(1)
        print('Have a nice day .....')
        break



