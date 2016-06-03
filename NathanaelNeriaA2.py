"""
Student ID: 13251882
Name : Nathanael Neria
Repository link: https://github.com/NathanaelNeria/NathanaelNeriaA2.git
Date submitted : 3/6/2016
"""
from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from itemlist import ItemList

class Main(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):

        """Initializer to construct the app"""

        super(Main, self).__init__(**kwargs)
        self.item_list = ItemList()
        storageitem = open("inventory.csv", "r+")
        for line in storageitem:
            self.item_list.store(line)

    def build(self):
        self.title = "Assignment2"
        self.root = Builder.load_file('layout.kv')
        return self.root

    def itemlist(self):

        """Function to show all the list item in the inventory.csv"""

        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.listitem.background_color = (1, 1, 0.5, 1)
        self.root.ids.hireitem.background_color = (1, 1, 1, 1)
        self.root.ids.returnitem.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 1, 1)
        item_count = 0
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            temp_button.bind(on_press=self.pressitem)
            self.root.ids.itemsBox.add_widget(temp_button)
            item_count += 1


    def itemhire(self):

        """Function to hire the items from inventory.csv, red color item mean the item is out"""

        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.listitem.background_color = (1, 1, 1, 1)
        self.root.ids.hireitem.background_color = (1, 1, 0.5, 1)
        self.root.ids.returnitem.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 1, 1)
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            temp_button.bind(on_press=self.pressitem)
            self.root.ids.itemsBox.add_widget(temp_button)

    def itemreturn(self):

        """Function to return the items that is out from the inventory.csv"""

        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.listitem.background_color = (1, 1, 1, 1)
        self.root.ids.hireitem.background_color = (1, 1, 1, 1)
        self.root.ids.returnitem.background_color = (1, 1, 0.5, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 1, 1)
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            temp_button.bind(on_press=self.pressitem)
            self.root.ids.itemsBox.add_widget(temp_button)


    def pressitem(self, instance):

        """Function will show the description of the selected item the label
        will also change when the item_return or item_hire button is being selected"""

        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if instance.text == name:
                if self.root.ids.listitem.background_color == [1, 1, 0.5, 1]:
                    self.root.ids.label.text = "{} ({}), ${:,.2f} is {}".format(name, item_desc, float(cost), status)
                elif self.root.ids.hireitem.background_color == [1, 1, 0.5, 1]:
                    if "in" in status:
                        self.root.ids.label.text = "Hiring: {} for ${:,.2f}".format(name, float(cost))
                    else:
                        self.root.ids.label.text = "Hiring: no items for $0.00"
                elif self.root.ids.returnitem.background_color == [1, 1, 0.5, 1]:
                    if "out" in status:
                        self.root.ids.label.text = "Returning: {}".format(name)
                    else:
                        self.root.ids.label.text = "Returning: no items"

    def confirm(self):

        """Function to make changes on the inventory.csv file"""

        item_count = 0
        with open("inventory.csv") as file:
            readitem = file.readlines()
        for line in readitem:
            name, item_desc, cost, status = line.split(",")
            if name in self.root.ids.label.text:
                if self.root.ids.hireitem.background_color == [1, 1, 0.5, 1]:
                    self.item_list.clear()
                    readitem[item_count] = readitem[item_count].replace("in", "out")
                    with open("inventory.csv", "w") as file:
                        file.writelines(readitem)
                    for line in readitem:
                        self.item_list.store(line)
                    file.close()
                    self.itemlist()
                elif self.root.ids.returnitem.background_color == [1, 1, 0.5, 1]:
                    self.item_list.clear()
                    readitem[item_count] = readitem[item_count].replace("out","in")
                    with open("inventory.csv", "w") as file:
                        file.writelines(readitem)
                    for line in readitem:
                        self.item_list.store(line)
                    file.close()
            item_count += 1 # add up everytime something is written
        self.itemlist()

    def additem(self):

        """Function to display the popup window"""

        self.root.ids.listitem.background_color = (1, 1, 1, 1)
        self.root.ids.hireitem.background_color = (1, 1, 1, 1)
        self.root.ids.returnitem.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 0.5, 1)
        additem = Builder.load_file('additempopup.kv')
        self.popup = Popup(title="Add Item", content=additem, size_hint=(.7, .7))
        self.popup.open()

    def press_save(self, name, item_desc, cost, instruction):

        """Function to save the input item to inventory.csv and dismiss the pop up window after saving"""

        error_mode = 0
        try: # error checking
            finalPrice = float(cost)
            if name == "":
                error_mode = 1
                error = "Error"
                check = float(error)
                print(check)
            elif item_desc == "":
                error_mode = 1
                error = "Error"
                check = float(error)
                print(check)
            elif finalPrice < 0:
                error_mode = 2
                error = "Error"
                check = float(error)
                print(check)
            else:
                newItem = "\n{},{},{},{}".format(name, item_desc, cost, "in")
                print(newItem)
                with open("inventory.csv", "a") as file:
                    file.writelines(newItem)
                self.item_list.store(newItem)
                self.cancel()
                self.status_text = "Choose action from the left menu, then select items on the right"
                self.itemlist()
        except ValueError:
            if error_mode == 0:
                if name == "" or item_desc == "" or cost == "":
                    instruction.text = "All fields must be completed"
                else:
                    instruction.text = "Please enter a valid number" # will appear if the finalprice is not a number
            elif error_mode == 1:
                instruction.text = "All fields must be completed" # will appear if one of the text input is blank
            elif error_mode == 2:
                instruction.text = "Price must not be negative" # will appear if the number is negative

    def cancel(self):

        """Function to dismiss pop up window"""

        self.popup.dismiss()

Main().run()
