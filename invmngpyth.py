
import matplotlib.pyplot as plt 

File_Name = "Inventory.txt"
Updated_File_Name = "UpdatedInventory.txt"
Removed_Items_File = "RemovedItems.txt"

def mainmenu():
    print("<<==========================>>")
    print("   Inventory Management Menu  ")
    print("<<==========================>>")
    print(" 1)   Add new item to Inventory")
    print(" 2)   Remove items from Inventory")
    print(" 3)   Update Inventory item quantity")
    print(" 4)   Search Required Inventory")
    print(" 5)   Display Existing Inventory")
    print(" 6)   Display Existing Inventory Piechart")
    print(" 7)   Display Sold Items PieChart")
    print(" 999) Quit")
    option = int(input("Select an option: "))
    selectitems(option)

def selectitems(option):
    if option == 1:
        addInvent()
    elif option == 2:
        removeInvent()
    elif option == 3:
        updateInvent()
    elif option == 4:
        searchInvent()
    elif option == 5:
        displayInvent()
    elif option == 6:
        display_Curinv_PieChart()
    elif option == 7:
        display_soldinv_PieChart()
    elif option == 999:
        print("Exiting the program.")
        exit()
    else:
        print("Invalid option. Please try again.")
        mainmenu()

def addInvent():
    print(">>-------------------------<<")
    print("       Adding Inventory        ")
    print(">>-------------------------<<")
    item_desc = input("Enter the name of the item: ")
    item_qty = input("Enter the quantity of the item: ")
    with open(File_Name, 'a') as infile:
        infile.write(f"{item_desc},{item_qty}\n")
    with open(Updated_File_Name, 'a') as infile:
        infile.write(f"{item_desc},{item_qty}\n")
    option = int(input("Enter '1' to continue or '0' to Exit: "))
    if option == 1:
        mainmenu()
    else:
        print("Exiting the program.")
        exit()

def removeInvent():
    print(">>-------------------------<<")
    print("       Removing Inventory      ")
    print(">>-------------------------<<")
    item_desc = input("Enter the item to remove: ")
    remove_qty = int(input("Enter the quantity to remove: "))
    item_found = False
    updated_inventory = []
    removed_items = []
    try:
        with open(File_Name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                current_item_name, current_item_qty = line.strip().split(',')
                current_item_qty = int(current_item_qty)
                if current_item_name == item_desc:
                    item_found = True
                    if remove_qty < current_item_qty:
                        updated_inventory.append(f"{current_item_name},{current_item_qty - remove_qty}\n")
                        removed_items.append(f"{current_item_name},{remove_qty}\n")
                    elif remove_qty == current_item_qty:
                        removed_items.append(line)
                    else:
                        print(f"Cannot remove {remove_qty} {item_desc}. Only {current_item_qty} available.")
                        updated_inventory.append(line)
                else:
                    updated_inventory.append(line)

        if item_found:
            with open(File_Name, 'w') as file:
                file.writelines(updated_inventory)
            with open(Updated_File_Name, 'w') as file:
                file.writelines(updated_inventory)
            with open(Removed_Items_File, 'a') as file:
                file.writelines(removed_items)
            print(f"'{remove_qty} {item_desc}' removed from the inventory.")
        else:
            print(f"'{item_desc}' is not found in the inventory.")
    except FileNotFoundError:
        print("Inventory file not found.")

    option = int(input("Enter '1' to continue or '0' to Exit: "))
    if option == 1:
        mainmenu()
    else:
        print("Exiting the program.")
        exit()


def updateInvent():
    print(">>-------------------------<<")
    print("       Updating Inventory      ")
    print(">>-------------------------<<")
    item_desc = input("Enter the name of the item to update: ")
    new_qty = input("Enter the new quantity: ")
    item_found = False
    updated_inventory = []
    try:
        with open(File_Name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                current_item_name, current_item_qty = line.strip().split(',')
                if current_item_name == item_desc:
                    updated_inventory.append(f"{current_item_name},{new_qty}\n")
                    item_found = True
                else:
                    updated_inventory.append(line)

        if item_found:
            with open(File_Name, 'w') as file:
                file.writelines(updated_inventory)
            with open(Updated_File_Name, 'w') as file:
                file.writelines(updated_inventory)
            print(f"'{item_desc}' quantity updated to {new_qty}.")
        else:
            print(f"'{item_desc}' is not found in the inventory.")
    except FileNotFoundError:
        print("Inventory file not found.")
    
    option = int(input("Enter '1' to continue or '0' to Exit: "))
    if option == 1:
        mainmenu()
    else:
        print("Exiting the program.")
        exit()


def searchInvent():
    print(">>-------------------------<<")
    print("      Searching Inventory      ")
    print(">>-------------------------<<")
    item_desc = input("Enter the name of the item to search: ")
    item_found = False
    try:
        with open(File_Name, 'r') as file:
            for line in file:
                current_item_name, current_item_qty = line.strip().split(',')
                if current_item_name == item_desc:
                    print(f"Item: {current_item_name}, Quantity: {current_item_qty}")
                    item_found = True
                    break

        if not item_found:
            print(f"'{item_desc}'is not found in the inventory.")
    except FileNotFoundError:
        print("Inventory file not found.")

    option = int(input("Enter '1' to continue or '0' to Exit: "))
    if option == 1:
        mainmenu()
    else:
        print("Exiting the program.")
        exit()

def displayInvent():
    print(">>-------------------------<<")
    print("       Current Inventory      ")
    print(">>-------------------------<<")
    try:
        with open(File_Name, "r") as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    item_desc, item_qty = line.strip().split(',')
                    print(f"Item: {item_desc}, Quantity: {item_qty}")
            else:
                print("Inventory is empty.")
    except FileNotFoundError:
        print("Inventory file not found.")
    
    option = int(input("Enter '1' to continue or '0' to Exit: "))
    if option == 1:
        mainmenu()
    else:
        print("Exiting the program.")
        exit()

def display_Curinv_PieChart():
    print(">>-------------------------<<")
    print("Displaying Inventory Pie Chart")
    print(">>-------------------------<<")
    try:
        inventory = {}
        with open(File_Name, "r") as file:
            lines = file.readlines()
            for line in lines:
                item_desc, item_qty = line.strip().split(',')
                inventory[item_desc] = int(item_qty)

        if not inventory:
            print("Inventory is empty. Cannot display pie chart.")
            return
        
        labels = list(inventory.keys())
        sizes = list(inventory.values())
        colors = plt.cm.Paired(range(len(labels)))

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=180, colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 0.35})
        plt.axis('equal')
        plt.title('Existing Inventory', fontsize=30)
        plt.legend(labels, title="Items", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        plt.show()
    except FileNotFoundError:
        print("Inventory file not found.")
    
    option = int(input("Enter '1' to continue or '0' to Exit: "))
    if option == 1:
        mainmenu()
    else:
        print("Exiting the program.")
        exit()

def display_soldinv_PieChart():
    print(">>-------------------------<<")
    print("Displaying Sold Items Pie Chart")
    print(">>-------------------------<<")
    try:
        inventory = {}
        with open(Removed_Items_File, "r") as file:
            lines = file.readlines()
            for line in lines:
                item_desc, item_qty = line.strip().split(',')
                if item_desc in inventory:
                    inventory[item_desc] += int(item_qty)
                else:
                    inventory[item_desc] = int(item_qty)

        if not inventory:
            print("No items have been sold. Cannot display pie chart.")
            return
        
        labels = list(inventory.keys())
        sizes = list(inventory.values())
        colors = plt.cm.Paired(range(len(labels)))

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=180, colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 0.35})
        plt.axis('equal')
        plt.title('Sold Inventory', fontsize=30)
        plt.legend(labels, title="Items", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        plt.show()
    except FileNotFoundError:
        print("Removed Items file not found.")
    
    option = int(input("Enter '1' to continue or '0' to Exit: "))
    if option == 1:
        mainmenu()
    else:
        print("Exiting the program.")
        exit()

if __name__ == "__main__":
    mainmenu()

