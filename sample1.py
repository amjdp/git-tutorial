
list1 = [];


while True :    
    print("A. Add\n D. Delete \n E. Exit")
    choice = input("Please enter your choice: ")
    
    if choice == 'A':
        print('Add')
    elif choice == 'D':
        print('Delete')
    elif choice == 'E':
        print('Exit')
    x = input("Enter a product:  ")
    list1.append(x);
    print(list1);

   

    

    
