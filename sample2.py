
list1 = [];


while True :
    
    print("\n A. Add\n D. Delete \n E. Exit \n U. Update")
    choice = input("Please enter your choice: ")
    
    if choice == 'A':
        print('ADD')
        x = input("Enter a product: ")
        list1.append(x)

    elif choice == 'D':
        print('DELETE')
        delete = input('enter product to remove')
        list1.remove(delete)

    elif choice == 'U':
        print('UPDATE')
        item = input("Enter product to update")
        i = list1.index(item)
        list1[i] = input("Enter new value ")
       
    elif choice == 'E':
        break;
    print(list1)
    
   

   

    

    
