# Inventory-Management
The Inventory Management System is designed to help businesses manage their stock levels efficiently and this system allows users to add, remove, update, search, and display inventory items

Inventory Management System
Project Overview:
The Inventory Management System is a Python-based application designed to help businesses efficiently manage their stock levels. This system provides functionalities to add, remove, update, search, and display inventory items. Additionally, it offers visual representations of the inventory through pie charts, aiding in the visualization of current stock and removed items.

## Key Features
### 1)Add New Items:
* Users can add new items to the inventory by specifying the item name and quantity.
* The new items are recorded in the main inventory file and the updated inventory file.

### 2)Remove Items:
* Users can remove specific quantities of items from the inventory by specifying the item name and the quantity to be removed.
* The system updates the inventory accordingly and logs the removed items in a separate file for tracking purposes.
### 3)Update Item Quantity:
* Users can update the quantity of existing items in the inventory.
* The system verifies the item and updates its quantity in the inventory files.
### 4)Search Inventory:
* Users can search for specific items in the inventory.
* The system displays the item name and its quantity if found.
### 5)Display Inventory:
* Users can view all items currently in the inventory.
* The system lists each item with its name and quantity.
### 6)Inventory Pie Chart:
* Users can view a pie chart representing the distribution of current inventory items.
* The pie chart provides a visual overview of the stock levels for each item.
### 7)Removed Items Pie Chart:
* Users can view a pie chart showing the distribution of removed items.
* This helps in tracking which items have been sold or discarded over time.

## File Structure
### Inventory.txt: Stores the current inventory items and their quantities.
### UpdatedInventory.txt: Stores the updated inventory after each modification.
### RemovedItems.txt: Logs the items that have been removed from the inventory.

## How to Use
### 1)Main Menu:
* The main menu offers various options for managing the inventory.
* Users can select an option by entering the corresponding number.
### 2)Input Validation:
* The system includes basic input validation to ensure proper data entry.
* Users are prompted to enter valid quantities and item names.

## Code Implementation
The project is implemented in Python and uses the matplotlib library for generating pie charts. The main functions include:
* mainmenu: Displays the main menu and handles user input.
* selectitems: Calls the appropriate function based on the user's choice.
* addInvent: Adds new items to the inventory.
* removeInvent: Removes specified quantities of items from the inventory.
* updateInvent: Updates the quantity of existing inventory items.
* searchInvent: Searches for specific items in the inventory.
* displayInvent: Displays all items currently in the inventory.
* display_Cur_PieChart: Generates a pie chart of current inventory items.
* display_soldinv_PieChart: Generates a pie chart of removed items.
