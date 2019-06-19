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
    show_mouse_info = kdSignal()

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
        #         you could use this method to move a floating window that
        #         represents what you're dragging
#         x, y = event.widget.winfo_pointerxy()
#         target = event.widget.winfo_containing(x, y)
# #         msg = "，y：" + str(event.y) + "source:" + str(event.widget.winfo_pointery()) + \
# #             ",target:" + str(target.winfo_pointery())
# 
#         if target and hasattr(target, "properties"):
#             print("in on on_drag",
#                   target.properties["text"]["value"])
# #             target["state"] = DISABLED
#             msg = "widget，x：" + str(x) + "，y：" + str(y) + \
#                 ",target:x" + str(target.winfo_rootx()) + ",y:" + str(target.winfo_rooty()) + ",bottom:" + \
#                 str(target.winfo_height())
#             msg += target.properties["text"]["value"]
#             self.show_mouse_info.emit(msg)
        pass

    def on_drop(self, event):
        x, y = event.widget.winfo_pointerxy()
        droped_widget = event.widget.winfo_containing(x, y)
        target = droped_widget

        if not target:
            return
        # get parent
        print("get parent")
        if not any([isinstance(target, GridLayout), isinstance(target, VerticalLayout), isinstance(target, HorizontalLayout), isinstance(target, Container)]):
            target = target.master

        new_row = None
        new_col = None
        print(droped_widget.grid_info())
        if target.getLayout() == "grid":
            grid_info = droped_widget.grid_info()
            if y - droped_widget.winfo_rooty() > droped_widget.winfo_height() * 2 / 3:
                if droped_widget.winfo_rootx() < x and x < droped_widget.winfo_rootx() + droped_widget.winfo_width():
                    if "row" in grid_info:
                        new_row = grid_info["row"] + 1
                        new_col = grid_info["column"]
                        print("new_row" + str(new_row))
            elif x - droped_widget.winfo_rootx() > droped_widget.winfo_width() * 2 / 3:
                if droped_widget.winfo_rooty() < y and y < droped_widget.winfo_rooty() + droped_widget.winfo_height():
                    if "row" in grid_info:
                        new_row = grid_info["row"]
                        new_col = grid_info["column"] + 1
                        print("new_col" + str(new_col))
        # create widget
        print("create widget")
        clazz = event.widget.text()
        widget = self.pre_create_widget(
            clazz, target, new_row, new_col)
        if not widget:
            print("无法创建组件" + clazz)
            return

        # add widget
#         if isinstance(target, GridLayout):
#             target.addWidgetOnRow(widget)
#             print("add widget in GridLayout")
#         if any([isinstance(target, VerticalLayout), isinstance(target, HorizontalLayout), isinstance(target, HorizontalLayout), isinstance(target, Container)]):
#             target.addWidget(widget)
#             print(
#                 "add widget in VerticalLayout or HorizontalLayout")
        self.add_widget_property.emit(widget, None)

    def pre_create_widget(self, clazz, target, row=None, col=None):
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
                "value": object_name}
            properties['objectName'] = {
                "value": object_name}
            widget = create_widget(
                clazz.replace(" ", ""), target, properties, row, col)
        elif clazz in["List Widget", "Tree Widget", "Combo Box"]:
            properties = {}
            properties['objectName'] = {
                "value": object_name, "type": "text", "content": None}
            widget = create_widget(
                clazz.replace(" ", ""), target, properties, row, col)
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
