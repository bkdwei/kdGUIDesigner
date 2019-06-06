'''
Created on 2019年6月4日

@author: bkd
'''

from kdGUI import *

del_widget_property = kdSignal()


def create_widget(widgetName, parent, properties):
    fn = factory.get(widgetName)
    if fn :
        widget = fn(parent, properties)
        if widget:
            menu_delete = Menu(False, parent)
            menu_delete.addAction("delete", lambda :deleteWidget(widget))
            addContextMenu(widget, menu_delete)
        return widget


def deleteWidget(widget):
    del_widget_property.emit(widget, None, widget.master)
    widget.destroy()


def create_buttton(parent, properties):
    btn = Button(properties["objectName"], parent)
    addWidget(parent, btn)
    return btn


def create_label(parent, properties):
    widget = None
    if "text" in properties:
        widget = Label(properties["text"], parent)
        addWidget(parent, widget)
    return widget  


def create_horizontal_layout(parent, properties):   
    widget = HorizotalLayout(properties["objectName"], parent)  
    addWidget(parent, widget)
    return widget


def create_radio_button(parent, properties):   
    widget = RadioButton(properties["objectName"], parent)  
    addWidget(parent, widget)
    return widget        


def create_list_widget(parent, properties):   
    widget = ListWidget(parent)  
    addWidget(parent, widget)
    return widget  


def create_tree_widget(parent, properties):   
    widget =TreeWidget(parent)  
    addWidget(parent, widget)
    return widget  
def create_Combo_box(parent, properties):   
    widget =ComboBox(parent)  
    addWidget(parent, widget)
    return widget  
# add widget
def addWidget(parent , child):
    if isinstance(parent, GridLayout):
        parent.addWidgetOnRow(child)
        print("add in GridLayout")
    if any([isinstance(parent, VerticalLayout), isinstance(parent, HorizotalLayout), isinstance(parent, HorizotalLayout), isinstance(parent, Container)]) :
        parent.addWidget(child)
        print("add in VerticalLayout or HorizotalLayout")


factory = {"Button":create_buttton, "Label":create_label, "HorizotalLayout":create_horizontal_layout, "RadioButton" :create_radio_button, "ListWidget":create_list_widget,"TreeWidget":   create_tree_widget,"ComboBox":create_Combo_box}
