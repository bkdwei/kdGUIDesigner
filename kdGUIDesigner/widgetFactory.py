'''
Created on 2019年6月4日

@author: bkd
'''

import json
from kdGUI import *
from tkinter.simpledialog import askstring

from .fileutil import get_file_realpath


show_widget_property = kdSignal()
del_widget_property = kdSignal()
edit_widget_property = kdSignal()
wp = get_file_realpath("../data/widget_properties.json")
widget_properties = {}
with open(wp, "r") as f:
    widget_properties = json.loads(f.read())


def get_list_content(clazz, property):
    print("clazz:" + clazz + ",property:" + property)
    return widget_properties[clazz][property]["content"]


def show_properties(event):
    show_widget_property.emit(event.widget)


def create_widget(clazz, parent, properties, row=None, column=None):
    fn = factory.get(clazz)
    if fn:
        #         获取默认属性
        if clazz in widget_properties:
            new_prop = widget_properties[clazz].copy()
            new_prop.update(properties)
            properties = new_prop
#             创建组件
        widget = fn(parent, properties)

        if widget:
            #             添加到父容器
            addWidget(parent, widget, row, column)

#             绑定修改文本事件
            if clazz in ["LineEdit", "CheckButton", "RadioButton", "PushButton", "Label", "VerticalLayout", "HorizontalLayout", "GridLayout"]:
                bind_doubleClicked(
                    widget, on_widget_doubleClicked)

#             新增右键删除组件功能
            menu_delete = Menu(False, parent)
            menu_delete.addAction(
                "delete", lambda: deleteWidget(widget))
            addContextMenu(widget, menu_delete)

#             单击显示组件属性
            widget.bind("<Button-1>", show_properties)

#             设置组件的属性
            widget.objectName = properties["objectName"]["value"]
            widget.properties = properties
        return widget


def deleteWidget(widget):
    del_widget_property.emit(widget, None, widget.master)
    widget.destroy()


def on_widget_doubleClicked(event):
    print(event.widget.properties["text"]["value"])
    new_value = askstring(
        "input new value", "input new value for button")
    event.widget.setText(new_value)
    event.widget.properties["text"]["value"] = new_value
    show_widget_property.emit(event.widget)
    edit_widget_property.emit(event.widget)


def create_buttton(parent, properties):
    widget = PushButton(properties["text"]["value"], parent)

    return widget


def create_label(parent, properties):
    widget = Label(properties["text"]["value"], parent)
    return widget


def create_horizontal_layout(parent, properties):
    widget = HorizontalLayout(
        properties["objectName"]["value"], parent)

    return widget


def create_vertical_layout(parent, properties):
    widget = VerticalLayout(
        properties["objectName"]["value"], parent)

    return widget


def create_radio_button(parent, properties):
    widget = RadioButton(
        properties["objectName"]["value"], parent)
    return widget


def create_check_button(parent, properties):
    widget = CheckButton(
        properties["objectName"]["value"], parent)
    return widget


def create_list_widget(parent, properties):
    widget = ListWidget(parent)

    return widget


def create_tree_widget(parent, properties):
    widget = TreeWidget(parent)

    return widget


def create_combo_box(parent, properties):
    widget = ComboBox(parent)
    return widget


def create_line_edit(parent, properties):
    widget = LineEdit(properties["text"]["value"], parent)
    return widget


def addWidget(parent, child, row=None, column=None):
    child.parent = parent
    if isinstance(parent, GridLayout):
        parent.addWidgetOnRow(child)
        print("add in GridLayout")
    elif isinstance(parent, Container) and parent.getLayout() == "grid":
        parent.addWidget(child, row, column)
    elif any([isinstance(parent, VerticalLayout), isinstance(parent, HorizontalLayout), isinstance(parent, HorizontalLayout)]):
        parent.addWidget(child)
        print("add in VerticalLayout or  HorizontalLayout")
    else:
        parent.addWidget(child)


def bind_doubleClicked(widget, command):
    widget.bind("<Double-1>", command)


def update_widget_properties(widget):
    properties = widget.properties
    for k, v in properties.items():
        if k == "objectName":
            widget.objectName = v["value"]
#             setattr(self, widget.objectName, widget)
        elif k == "weight":
            pass
            #             widget.grid_configure(weight=v["value"])
        else:
            widget.config({k: v["value"]})


factory = {"LineEdit": create_line_edit, "CheckButton": create_check_button, "PushButton": create_buttton, "Label": create_label, "HorizontalLayout": create_horizontal_layout, "VerticalLayout": create_vertical_layout,
           "RadioButton": create_radio_button, "ListWidget": create_list_widget, "TreeWidget":   create_tree_widget, "ComboBox": create_combo_box}
