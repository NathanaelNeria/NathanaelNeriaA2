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
from itemlist import ItemList

class MainApp(App):

    stringproperty = StringProperty()

    def __init__(self, **kwargs):

        """Initializer to construct the app"""

        super(MainApp, self).__init__(**kwargs)
        self.item_list = ItemList()
        stock = open("inventory.csv", "r+")
        for items in stock:
            self.item_list.store(items)

    def build(self):
        self.title = "A2"
        self.root = Builder.load_file('layout.kv')
        return self.root

    def itemlist(self):

        """Function to show all the list item in the inventory.csv"""

        self.root.ids.itemlistbox.clear_widgets()
        self.root.ids.bottomlabel.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.listitem.background_color = (1, 1, 0.5, 1)
        self.root.ids.hireitem.background_color = (1, 1, 1, 1)
        self.root.ids.returnitem.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 1, 1)
        for items in self.item_list:
            name, desc, price, availability = items.split(",")
            if "in" in availability:
                tempbutton = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                tempbutton = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            tempbutton.bind(on_press=self.pressitem)
            self.root.ids.itemlistbox.add_widget(tempbutton)


    def itemhire(self):

        """Function to hire the items from inventory.csv, red color item mean the item is out"""

        self.root.ids.itemlistbox.clear_widgets()
        self.root.ids.bottomlabel.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.listitem.background_color = (1, 1, 1, 1)
        self.root.ids.hireitem.background_color = (1, 1, 0.5, 1)
        self.root.ids.returnitem.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 1, 1)
        for items in self.item_list:
            name, desc, price, availability = items.split(",")
            if "in" in availability:
                tempbutton = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                tempbutton = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            tempbutton.bind(on_press=self.pressitem)
            self.root.ids.itemlistbox.add_widget(tempbutton)

    def itemreturn(self):

        """Function to return the items that is out from the inventory.csv"""

        self.root.ids.itemlistbox.clear_widgets()
        self.root.ids.bottomlabel.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.listitem.background_color = (1, 1, 1, 1)
        self.root.ids.hireitem.background_color = (1, 1, 1, 1)
        self.root.ids.returnitem.background_color = (1, 1, 0.5, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 1, 1)
        for items in self.item_list:
            name, desc, price, availability = items.split(",")
            if "in" in availability:
                tempbutton = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                tempbutton = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            tempbutton.bind(on_press=self.pressitem)
            self.root.ids.itemlistbox.add_widget(tempbutton)


    def pressitem(self, instance):

        """Function will show the description of the selected item the bottomlabel
        will also change when the item_return or item_hire button is being selected"""

        for items in self.item_list:
            name, desc, price, availability = items.split(",")
            if instance.text == name:
                if self.root.ids.listitem.background_color == [1, 1, 0.5, 1]:
                    self.root.ids.bottomlabel.text = "{} ({}), ${:,.2f} is {}".format(name, desc, float(price), availability)
                elif self.root.ids.hireitem.background_color == [1, 1, 0.5, 1]:
                    if "in" in availability:
                        self.root.ids.bottomlabel.text = "Hiring: {} for ${:,.2f}".format(name, float(price))
                    else:
                        self.root.ids.bottomlabel.text = "Hiring: no items for $0.00"
                elif self.root.ids.returnitem.background_color == [1, 1, 0.5, 1]:
                    if "out" in availability:
                        self.root.ids.bottomlabel.text = "Returning: {}".format(name)
                    else:
                        self.root.ids.bottomlabel.text = "Returning: no items"

    def confirm(self):

        """Function to make changes on the inventory.csv file"""

        itemcount = 0
        with open("inventory.csv") as itemfile:
            read = itemfile.readlines()
        for items in read:
            name, desc, price, availability = items.split(",")
            if name in self.root.ids.bottomlabel.text:
                if self.root.ids.hireitem.background_color == [1, 1, 0.5, 1]:
                    self.item_list.clear()
                    read[itemcount] = read[itemcount].replace("in", "out")
                    with open("inventory.csv", "w") as itemfile:
                        itemfile.writelines(read)
                    for items in read:
                        self.item_list.store(items)
                    itemfile.close()
                    self.itemlist()
                elif self.root.ids.returnitem.background_color == [1, 1, 0.5, 1]:
                    self.item_list.clear()
                    read[itemcount] = read[itemcount].replace("out","in")
                    with open("inventory.csv", "w") as itemfile:
                        itemfile.writelines(read)
                    for items in read:
                        self.item_list.store(items)
                    itemfile.close()
                    self.itemlist()
            itemcount += 1

    def additem(self):

        """Function to display the popup window"""

        self.root.ids.listitem.background_color = (1, 1, 1, 1)
        self.root.ids.hireitem.background_color = (1, 1, 1, 1)
        self.root.ids.returnitem.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 0.5, 1)
        self.stringproperty = 'Enter new item'
        self.root.ids.popupbox.open()

    def error(self,price):  # error check
        try:
            float(price)
            return True
        except ValueError:
            return False

    def save(self, name, desc, price, instruction, error):

        """Function to save the input item to inventory.csv and dismiss the pop up window after saving"""

        if name.strip == '' or desc == '' or price == '':
            instruction.text = "All fields must be completed"
        elif error(price) == False:
            instruction.text = "Price must be valid number"
        elif error(price) == True and float(price) < 0:
            instruction.text = "Price cannot be negative"
        else:
            additems = "\n{},{},{},in".format(name, desc, float(price))
            with open("items.csv", "a") as itemfile:
                itemfile.writelines(additems)
            self.item_list.store(additems)
            self.cancel()
            self.itemlist()

    def cancel(self):

        """Function to dismiss pop up window"""

        self.popupbox.dismiss()

MainApp().run()
