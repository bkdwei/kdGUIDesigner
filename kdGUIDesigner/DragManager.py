'''
Created on 2019年6月2日

@author: bkd
'''
from tkinter.simpledialog import askstring
from kdGUI import *
from .widgetFactory import create_widget


class DragManager():
    add_widget_property = kdSignal()
    del_widget_property = kdSignal()

    def __init__(self):
        self.wiget_index = {}

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
        x, y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x, y)

        # get parent
        print("get parent")
        if not any([isinstance(target, GridLayout), isinstance(target, VerticalLayout), isinstance(target, HorizontalLayout), isinstance(target, Container)]):
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
            print("add widget in GridLayout")
        if any([isinstance(target, VerticalLayout), isinstance(target, HorizontalLayout), isinstance(target, HorizontalLayout), isinstance(target, Container)]):
            target.addWidget(widget)
            print(
                "add widget in VerticalLayout or HorizontalLayout")

        self.add_widget_property.emit(widget, None, target)

    def create_widget(self, clazz, target):
        #         获取新组件的下标，生成id
        widget = None
        index = 0
        if not clazz in self.wiget_index:
            self.wiget_index[clazz] = 0
        else:
            index = self.wiget_index[clazz] + 1
            self.wiget_index[clazz] = index
        str_index = "_" + str(index)

        object_name = clazz.replace(" ", "") + str_index

        if clazz in ["Line Edit", "Check Button", "Radio Button", "Push Button", "Label", "Vertical Layout", "Horizontal Layout", "Grid Layout"]:
            properties = {}
            properties['text'] = {
                "value": object_name, "type": "text", "content": None}
            properties['objectName'] = {
                "value": object_name, "type": "text", "content": None}
            widget = create_widget(
                clazz.replace(" ", ""), target, properties)
        elif clazz in["List Widget", "Tree Widget", "Combo Box"]:
            properties = {}
            properties['objectName'] = {
                "value": object_name, "type": "text", "content": None}
            widget = create_widget(
                clazz.replace(" ", ""), target, properties)
        else:
            print("unknow widget class" + clazz)

        return widget

    def on_button_doubleClicked(self, event):
        print(event.widget.text())
        new_value = askstring(
            "input new value", "input new value for button")
        event.widget.setText(new_value)

    def deleteWidget(self, widget):
        self.del_widget_property.emit(
            widget, None, widget.master)
        widget.destroy()
