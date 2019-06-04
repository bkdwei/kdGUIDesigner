'''
Created on 2019年6月4日

@author: bkd
'''

from kdGUI import *


def create_widget(widgetName, parent, properties):
    fn = factory.get(widgetName)
    if fn :
        return fn(parent, properties)


def create_buttton(parent, properties):
    btn = None
    if not properties:
        return
    if "text" in properties:
        btn = Button(properties["text"], parent)
        addWidget(parent, btn)
    return btn


def create_label(parent, properties):
    widget = None
    if not properties:
        return
    if "text" in properties:
        btn = Label(properties["text"], parent)
        addWidget(parent, btn)
    return widget  

     
# add widget
def addWidget(parent , child):
    if isinstance(parent, GridLayout):
        parent.addWidgetOnRow(child)
        print("add in GridLayout")
    if any([isinstance(parent, VerticalLayout), isinstance(parent, HorizotalLayout), isinstance(parent, HorizotalLayout), isinstance(parent, Container)]) :
        parent.addWidget(child)
        print("add in VerticalLayout or HorizotalLayout")

        
factory = {"Button":create_buttton, "Label":create_label}
