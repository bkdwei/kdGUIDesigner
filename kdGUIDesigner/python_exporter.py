'''
Created on 2019年6月9日

@author: bkd
'''
from PIL._imagingmath import add_F
from string import Template

from kdGUI import *


def create_buttton(parent_name, properties):
    btn_temp = Template(
        """
        self.${objectName} = PushButton('${text}',${parent})
        ${parent}.addWidget(self.${objectName})
""")
    return btn_temp.substitute(objectName=properties["objectName"]["value"], text=properties["text"]["value"], parent=parent_name)


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


def export_to_python(ui_json, parse_text, parent=None):
    for clazz, v in ui_json.items():
        fn = factory.get(clazz)
        if fn:
            widget_text = fn(parent, v["properties"])
            parse_text.append(widget_text)
        if "children" in v:
            for child in v["children"]:
                export_to_python(
                    child, parse_text, "self." + v["properties"]["objectName"]["value"])


def parse_ui_json(ui_json, parent, parse_text):
    parse_text.append(add_header())
    export_to_python(ui_json, parse_text, parent)
    parse_text.append(add_footer())
    return parse_text


def add_header():
    return """
from kdGUI import *
    
class kdGUIDesigner(Window):

    def __init__(self):
        super().__init__()
"""


def add_footer():
    return """
app = kdGUIDesigner()
app.run()
"""


factory = {"LineEdit": create_line_edit, "CheckButton": create_check_button, "PushButton": create_buttton, "Label": create_label, "HorizontalLayout": create_horizontal_layout, "VerticalLayout": create_vertical_layout,
           "RadioButton": create_radio_button, "ListWidget": create_list_widget, "TreeWidget":   create_tree_widget, "ComboBox": create_combo_box}
