from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from itemlist import ItemList

class Main(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):

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
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if instance.text == name:
                print(name)
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
            item_count += 1
        self.itemlist()

    def additem(self):
        self.root.ids.listitem.background_color = (1, 1, 1, 1)
        self.root.ids.hireitem.background_color = (1, 1, 1, 1)
        self.root.ids.returnitem.background_color = (1, 1, 1, 1)
        self.root.ids.confirm.background_color = (1, 1, 1, 1)
        self.root.ids.additem.background_color = (1, 1, 0.5, 1)
        additem = Builder.load_file('additempopup.kv')
        self.popup = Popup(title="Add Item", content=additem, size_hint=(.7, .7))
        self.popup.open()

    def press_save(self, name, item_desc, cost, instruction):
        def check(cost):
            try:
                float(cost)
                return True
            except ValueError:
                return False

        if len(name.strip()) == 0 or len(item_desc.strip()) == 0 or len(cost.strip()) == 0:
            instruction = "All fields must be completed"
        elif check(cost) == False:
            instruction = "Price must be valid number"
        elif check(cost) == True and float(cost) < 0:
            instruction = "Price cannot be negative"
        else:
            additem = "\n{},{},{},in".format(name, item_desc, float(cost))
            with open("inventory.csv", "a") as file:
                file.writelines(additem)
            self.item_list.store(additem)
            self.cancel()
            self.itemlist()

    def cancel(self):
        self.popup.dismiss()

Main().run()
