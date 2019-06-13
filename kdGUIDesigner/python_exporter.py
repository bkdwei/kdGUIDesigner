'''
Created on 2019年6月9日

@author: bkd
'''
from kdGUI import *
from string import Template


def add_widget(parent_name, child_name, parent_class=None, child_properties=None):
    if not parent_class and (not child_properties):
        temp = Template(
            """        ${parent}.addWidget(self.${child})""")
        return temp.substitute(parent=parent_name, child=child_name)


def create_buttton(parent_name, properties):
    btn_temp = Template(
        """        self.${objectName} = PushButton('${text}',${parent})""")
    return btn_temp.substitute(objectName=properties["objectName"]["value"], text=properties["text"]["value"], parent=parent_name)


def create_label(parent_name, properties):
    label_temp = Template(
        """        self.${objectName} = Label('${text}',${parent})""")
    return label_temp.substitute(objectName=properties["objectName"]["value"], text=properties["text"]["value"], parent=parent_name)


def create_horizontal_layout(parent_name, properties):
    temp = Template(
        """        self.${objectName} = HorizontalLayout('${text}',${parent})""")
    return temp.substitute(objectName=properties["objectName"]["value"], text=properties["text"]["value"], parent=parent_name)


def create_vertical_layout(parent_name, properties):
    temp = Template(
        """        self.${objectName} = VerticalLayout('${text}',${parent})""")
    return temp.substitute(objectName=properties["objectName"]["value"], text=properties["text"]["value"], parent=parent_name)


def create_radio_button(parent_name, properties):
    temp = Template(
        """        self.${objectName} = RadioButton('${text}',${parent})""")
    return temp.substitute(objectName=properties["objectName"]["value"], text=properties["text"]["value"], parent=parent_name)


def create_check_button(parent_name, properties):
    temp = Template(
        """        self.${objectName} = CheckButton('${text}',${parent})""")
    return temp.substitute(objectName=properties["objectName"]["value"], text=properties["text"]["value"], parent=parent_name)


def create_list_widget(parent_name, properties):
    temp = Template(
        """        self.${objectName} = ListWidget(${parent})""")
    return temp.substitute(objectName=properties["objectName"]["value"], parent=parent_name)


def create_tree_widget(parent_name, properties):
    temp = Template(
        """        self.${objectName} = TreeWidget(${parent})""")
    return temp.substitute(objectName=properties["objectName"]["value"],  parent=parent_name)


def create_combo_box(parent_name, properties):
    temp = Template(
        """        self.${objectName} = ComboBox(${parent})""")
    return temp.substitute(objectName=properties["objectName"]["value"], parent=parent_name)


def create_line_edit(parent_name, properties):
    temp = Template(
        """        self.${objectName} = LineEdit('${text}',${parent})""")
    return temp.substitute(objectName=properties["objectName"]["value"], text=properties["text"]["value"], parent=parent_name)


def export_to_python(ui_json, parse_text, parent_name=None):
    if not parent_name:
        parent_name = "self"
    for clazz, v in ui_json.items():
        fn = factory.get(clazz)
        if fn:
            widget_text = fn(parent_name, v["properties"])
            parse_text.append(widget_text)
            parse_text.append(add_widget(
                parent_name, v["properties"]["objectName"]["value"]))
            parent_name = "self." + \
                v["properties"]["objectName"]["value"]
        if "children" in v:
            for child in v["children"]:
                export_to_python(
                    child, parse_text, parent_name)


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
