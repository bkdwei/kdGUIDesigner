'''
Created on 2019年6月2日

@author: bkd
'''
from tkinter.simpledialog import askstring
from kdGUI import *


class DragManager():
    show_widget_property = kdSignal()
    add_widget_property = kdSignal()

    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        print("in on start", event.widget["text"])
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
#         print("in on on_drag", event.widget["text"])
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)
#         print(x, y, target["text"])
      
        # get parent
        print("get parent")
        if not any([isinstance(target, GridLayout), isinstance(target, VerticalLayout), isinstance(target, HorizotalLayout), isinstance(target, Container)]):
            target = target.master
        
        # create widget 
        print("create widget")
        clazz = event.widget.text()
        widget = self.create_widget(clazz, target)  
        if not widget:
            print("无法创建" + clazz)
            return
                         
        # add widget
        if isinstance(target, GridLayout):
            target.addWidgetOnRow(widget)
            print("add in GridLayout")
        if any([isinstance(target, VerticalLayout), isinstance(target, HorizotalLayout), isinstance(target, HorizotalLayout), isinstance(target, Container)]) :
            target.addWidget(widget)
            print("add in VerticalLayout or HorizotalLayout")
            
        self.add_widget_property.emit(widget, None, target)

    def create_widget(self, clazz, target):
        widget = None
        if clazz == "Push Button" :
            widget = Button("button", target)
            widget.doubleClick(self.on_button_doubleClicked)
        elif clazz == "Lable" :
            widget = Label("label", target)
        elif clazz == "Vertical Layout":
            widget = VerticalLayout("Vertical Layout", target)
        elif clazz == "Horizontal Layout":
            widget = HorizotalLayout("Horizontal Layout", target)                        
        elif clazz == "Grid Layout":  
            widget = GridLayout("GridLayout", target)
        elif clazz == "Radio Button" :
            widget = RadioButton("RadioButton", target)
        elif clazz == "Check Button" :
            widget = CheckButton("CheckButton", target)
        elif clazz == "List Widget" :
            widget = ListWidget(target)            
        elif clazz == "Tree Widget" :
            widget = TreeWidget(target)  
        elif clazz == "Combo Box" :
            widget = ComboBox(target)  
        elif clazz == "Line Edit" :
            widget = LineEdit("LineEdit", target)  
        else :
            print("unknow widget class" + clazz)
        
        if widget:
            menu_delete = Menu(False, target)
            menu_delete.addAction("delete", lambda :self.deleteWidget(widget))
            addContextMenu(widget, menu_delete)
            
            widget.bind("<Button-1>", self.show_properties)
        return widget

    def on_button_doubleClicked(self, event):
        print(event.widget.text())
        new_value = askstring("input new value", "input new value for button")
        event.widget.setText(new_value)
    
    def deleteWidget(self, widget):
        widget.destroy()

    def show_properties(self, event):
        self.show_widget_property.emit(event.widget.__class__.__name__)
        
