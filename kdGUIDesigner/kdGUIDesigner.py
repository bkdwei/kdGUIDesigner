'''
Created on 2019年6月2日

@author: bkd
'''
import json
from os.path import join, expanduser, exists
from tkinter import messagebox
from tkinter.constants import *
from tkinter.filedialog import LoadFileDialog, asksaveasfilename
import traceback

from kdGUI import *

from kdGUIDesigner.fileutil import check_and_create_file

from .DragManager import DragManager
from .exception_handler import *
from .python_exporter import parse_ui_json
from .widgetFactory import *


class kdGUIDesigner(ThemedWindow):

    def __init__(self):
        super().__init__()
        self.setTitle("kdGUIDesigner")
        self.setLayout(HORIZONTAL)
        self.setTheme("vista")
        self.initUI()
        self.bindWidgetBox()
        self.opened_file = None
        del_widget_property.connect(self.on_del_widget)
        show_widget_property.connect(
            self.show_widget_properties)
        edit_widget_property.connect(self.on_edit_widget)
        self.ui_content = {
            "Window": {"children": [], "properties": {"objectName": {
                "value": "MainWindow"}}}}

#         处理全局异常
        set_global_callback(self)

    def initUI(self):
        self.addWidgetBox()
        self.addLayouts()
        self.addSpacers()
        self.addButtons()
        self.addItemWidgets()
        self.addContainers()
        self.addInputWidgets()
        self.addDisplayWidgets()
        self.addMainWindow()
#         self.addObjectTree()
        self.addPropertyEditor()
#         self.addPropertyEditor()
        self.addMenuBar()

        # self.widgetBox
    def addWidgetBox(self):
        self.widgetBox = VerticalLayout("widget Box", self)
        print(type(self.widgetBox))
        self.addWidget(self.widgetBox)
        # 过滤
        le_filter = LineEdit("Filter", self.widgetBox)
        self.widgetBox.addWidget(le_filter)

    # layouts
    def addLayouts(self):
        vl_layouts = VerticalLayout(
            "Layouts", self.widgetBox)
        lb_verticalLayout = Label(
            "Vertical Layout", vl_layouts)
        lb_verticalLayout.setAnchor("w")
        vl_layouts.addWidget(lb_verticalLayout)

        lb_horizontal = Label(
            "Horizontal Layout", vl_layouts)
        lb_horizontal.setAnchor("w")
        vl_layouts.addWidget(lb_horizontal)

        lb_gridLayout = Label("Grid Layout", vl_layouts)
        lb_gridLayout.setAnchor("w")
        vl_layouts.addWidget(lb_gridLayout)
        self.widgetBox.addWidget(vl_layouts)

#         childs = vl_layouts.children()
        print("vl_layouts:", type(vl_layouts))

#         for c in childs:
#             print("childs" + c.text())

        # spacers
    def addSpacers(self):
        vl_spacers = VerticalLayout(
            "Spacers", self.widgetBox)

        lb_horizontalSpacer = Label(
            "Horizontal Spacer", vl_spacers)
        lb_horizontalSpacer.setAnchor("w")
        vl_spacers.addWidget(lb_horizontalSpacer)

        lb_verticalSpacer = Label(
            "Vertical Spacer", vl_spacers)
        lb_verticalSpacer.setAnchor("w")
        vl_spacers.addWidget(lb_verticalSpacer)

        self.widgetBox.addWidget(vl_spacers)

    # buttons
    def addButtons(self):
        vl_buttons = VerticalLayout(
            "Buttons", self.widgetBox)

        lb_pushbutton = Label("Push Button", vl_buttons)
        lb_pushbutton.setAnchor("w")
        vl_buttons.addWidget(lb_pushbutton)

        lb_radiobutton = Label("Radio Button", vl_buttons)
        lb_radiobutton.setAnchor("w")
        vl_buttons.addWidget(lb_radiobutton)

        lb_checkbutton = Label("Check Button", vl_buttons)
        lb_checkbutton.setAnchor("w")
        vl_buttons.addWidget(lb_checkbutton)

        self.widgetBox.addWidget(vl_buttons)

    # item widgets
    def addItemWidgets(self):
        vl_item_widgets = VerticalLayout(
            "Item Widgets", self.widgetBox)

        lb_list_widget = Label(
            "List Widget", vl_item_widgets)
        lb_list_widget.setAnchor("w")
        vl_item_widgets.addWidget(lb_list_widget)

        lb_tree_widget = Label(
            "Tree Widget", vl_item_widgets)
        lb_tree_widget.setAnchor("w")
        vl_item_widgets.addWidget(lb_tree_widget)

        lb_table_widget = Label(
            "Table Widget", vl_item_widgets)
        lb_table_widget.setAnchor("w")
        vl_item_widgets.addWidget(lb_table_widget)

        self.widgetBox.addWidget(vl_item_widgets)

    # containers
    def addContainers(self):
        vl_containers = VerticalLayout(
            "Containers", self.widgetBox)

        lb_scroll_area = Label("Scroll Area", vl_containers)
        lb_scroll_area.setAnchor("w")
        vl_containers.addWidget(lb_scroll_area)

        lb_tab_widget = Label("Tab Widget", vl_containers)
        lb_tab_widget.setAnchor("w")
        vl_containers.addWidget(lb_tab_widget)

        self.widgetBox.addWidget(vl_containers)

    # input widget
    def addInputWidgets(self):
        vl_input_widgets = VerticalLayout(
            "Input Widgets", self.widgetBox)

        lb_combobox = Label("Combo Box", vl_input_widgets)
        lb_combobox.setAnchor("w")
        vl_input_widgets.addWidget(lb_combobox)

        lb_lineedit = Label("Line Edit", vl_input_widgets)
        lb_lineedit.setAnchor("w")
        vl_input_widgets.addWidget(lb_lineedit)

        lb_textedit = Label("Text Edit", vl_input_widgets)
        lb_textedit.setAnchor("w")
        vl_input_widgets.addWidget(lb_textedit)

        lb_plaintextedit = Label(
            "Plain Text Edit", vl_input_widgets)
        lb_plaintextedit.setAnchor("w")
        vl_input_widgets.addWidget(lb_plaintextedit)

        lb_spinbox = Label("Spin Box", vl_input_widgets)
        lb_spinbox.setAnchor("w")
        vl_input_widgets.addWidget(lb_spinbox)

        lb_dateedit = Label("Date Edit", vl_input_widgets)
        lb_dateedit.setAnchor("w")
        vl_input_widgets.addWidget(lb_dateedit)

        lb_timeedit = Label("Time Edit", vl_input_widgets)
        lb_timeedit.setAnchor("w")
        vl_input_widgets.addWidget(lb_timeedit)

        self.widgetBox.addWidget(vl_input_widgets)

    # display widgets
    def addDisplayWidgets(self):
        vl_display_widgets = VerticalLayout(
            "Display Widgets", self.widgetBox)

        lb_label = Label("Label", vl_display_widgets)
        lb_label.setAnchor("w")
        vl_display_widgets.addWidget(lb_label)

        lb_text_browser = Label(
            "Text Browser", vl_display_widgets)
        lb_text_browser.setAnchor("w")
        vl_display_widgets.addWidget(lb_text_browser)

        lb_progress_bar = Label(
            "Prograss Bar", vl_display_widgets)
        lb_progress_bar.setAnchor("w")
        vl_display_widgets.addWidget(lb_progress_bar)
        self.widgetBox.addWidget(vl_display_widgets)

    # main windows
    def addMainWindow(self):
        self.gl_main = Container(
            "MainWindos - untitle", self)
        self.gl_main.setLayout("grid")
        self.gl_main.objectName = "MainWindow"
#         self.gl_main = GridLayout("MainWindos - untitle", self)
        self.addWidget(self.gl_main, expand=YES)
        menu_layout = Menu(False, self.gl_main)

        menu_sub_layout = Menu(False, menu_layout)
        menu_sub_layout.addAction(
            "Vertical Layout", lambda: self.setMainWindowLayout(VERTICAL))
        menu_sub_layout.addAction(
            "Horizontal Layout", lambda: self.setMainWindowLayout(HORIZONTAL))
        menu_sub_layout.addAction(
            "Grid Layout", lambda: self.setMainWindowLayout(Window.GRID))
        menu_layout.addMenu("layout1", menu_sub_layout)
        addContextMenu(self.gl_main, menu_layout)
        print(self.get_variable_name(self.gl_main))

    # object tree
    def addObjectTree(self):
        tr_widget = TreeWidget(self)
        self.addWidget(tr_widget)

    def addPropertyEditor(self):
        self.tw_properties = PropertyEditor(self)
        self.addWidget(self.tw_properties)
        self.cur_widget = None
        self.tw_properties.value_change_signal.connect(
            self._on_properties_value_change)

    def _on_properties_value_change(self, key, value):
        if not self.cur_widget:
            return
        self.cur_widget.properties[key]["value"] = value
        update_widget_properties(self.cur_widget)

    def addPropertyEditor1(self):
        self.tw_properties = TreeWidget(self)
        self.addWidget(self.tw_properties)
        self.tw_properties["columns"] = (
            "properties", "values")
#         self.tw_properties.setColumns(
#             ("properties", "values"))
        self.tw_properties.setHeader("properties", 100)
        self.tw_properties.setHeader("values", 100)

    def bindWidgetBox(self):
        self.dm = DragManager()
        self.dm.add_widget_property.connect(
            self.on_add_widget)

        self.dm.show_mouse_info.connect(self.showMessage)

        _containers = self.widgetBox.childrens()
        for c in _containers:
            if isinstance(c, VerticalLayout):
                _lables = c.childrens()
                for l in _lables:
                    self.dm.add_dragable(l)

    def setMainWindowLayout(self, layout):
        self.gl_main.setLayout(layout)
        print(layout)

    def addMenuBar(self):
        menuBar = Menu(self)
        self.addMenu(menuBar)

        fileMenu = Menu(menuBar)
        fileMenu.addAction("new", self.new_file)
        fileMenu.addAction("open", self.open_file)
        fileMenu.addAction("save", self.save_file)
        fileMenu.addAction(
            "export python file", self.export_file)
        self.get_rencent_files()
        self.rencent_file_menu = Menu(fileMenu)
        fileMenu.addMenu(
            "rencent files", self.rencent_file_menu)
        if self.rencent_files:
            for f in self.rencent_files:
                self.rencent_file_menu.addAction(
                    f, self.open_rencent_file, True)
        menuBar.addMenu("file", fileMenu)

    def open_rencent_file(self, file_path):
        children = self.gl_main.childrens()
        for child in children:
            child.destroy()
        if not exists(file_path):
            self.rencent_file_menu.removeAction(file_path)
            self.rencent_files.remove(file_path)
            self.showMessage(file_path + "不存在")
            with open(self.rencent_files_path, "w") as f:
                f.write(json.dumps(self.rencent_files))
            return
        with open(file_path) as f:
            j = json.loads(f.read())
            self.ui_content = j
            self.initUIFromJson(self.gl_main, j)
        self.showMessage("你打开了文件" + file_path)

    def export_file(self):
        self.parse_text = []
        parse_ui_json(
            self.ui_content, "self", self.parse_text)
        messagebox.showinfo(
            "转换后的文件", "\n".join(self.parse_text))
        print("\n".join(self.parse_text))
        save_file = asksaveasfilename()
        if save_file:
            if not ".py" in save_file:
                save_file += ".py"
            with open(save_file, "w") as f:
                f.write("\n".join(self.parse_text))
        self.showMessage("转换文件成功" + save_file)

    def namestr(self, obj):
        ns = globals()
        for name in ns:
            if ns[name] is obj:
                print("name" + name)
                return name

    def get_variable_name(self, x):
        for k, v in locals().items():
            if v is x:
                return k

    def get_rencent_files(self):
        self.rencent_files_path = join(expanduser(
            "~"), "config/kdGUIDesigner/recent_fils.json")
        check_and_create_file(self.rencent_files_path)
        with open(self.rencent_files_path, "r") as f:
            content = f.read().strip()
            if content and content != "":
                self.rencent_files = json.loads(
                    content)
            else:
                self.rencent_files = []

    def show_widget_properties(self, widget):
        self.cur_widget = widget
        i = 0
        self.tw_properties.clear()
        for k, v in widget.properties.items():
            print("k:" + k)
            if not "type" in v or v["type"] == "text":
                self.tw_properties.addRow(
                    k, None, v["value"], None)
            else:
                self.tw_properties.addRow(
                    k, v["type"], v["value"], get_list_content(widget.__class__.__name__, k))
            i = i + 1

    def new_file(self):
        self.ui_content = {
            "Window": {"children": [], "properties": {"objectName": {
                "value": "MainWindow"}}}}
        self.gl_main.destroy()
        self.addMainWindow()

    def open_file(self):
        fd = LoadFileDialog(self)
        filename = fd.go()
        if filename:
            self.showMessage("你打开了文件" + filename)
            self.opened_file = filename
            with open(filename) as f:
                children = self.gl_main.childrens()
                for child in children:
                    child.destroy()
                j = json.loads(f.read())
                self.ui_content = j
                self.initUIFromJson(self.gl_main, j)
                if not filename in self.rencent_files:
                    self.rencent_files.append(filename)
                    self.rencent_file_menu.addAction(
                        filename, lambda: self.open_rencent_file(filename))
                with open(self.rencent_files_path, "w") as f:
                    f.write(json.dumps(self.rencent_files))
#         self.showMessage("按钮的文本是" + self.btn1.text())

    def remove_type_and_content(self, content):
        for values in content.values():
            if isinstance(values, dict) and "properties" in values:
                for p in values["properties"].values():
                    if isinstance(p, dict) :
                        if "type" in p and p["type"] == "text":
                            del p["type"]
                        if "content" in p:
                            del p["content"]
            if isinstance(values, dict) and "children" in values:
                for child in values["children"]:
                    self.remove_type_and_content(child)

    def save_file(self):
        content = self.ui_content.copy()
        self.remove_type_and_content(content)
        if self.opened_file:
            with open(self.opened_file, "w") as f:
                f.write(json.dumps(content,
                                   indent=4, ensure_ascii=False))
                self.showMessage(
                    "保存文件成功" + self.opened_file)
        else:
            self.opened_file = asksaveasfilename()
            if self.opened_file:
                if not ".json" in self.opened_file:
                    self.opened_file += ".json"
                with open(self.opened_file, "w") as f:
                    f.write(json.dumps(
                        content, indent=4, ensure_ascii=False))
                    self.showMessage(
                        "保存文件成功" + self.opened_file)

    def initUIFromJson(self, parent, json):
        if isinstance(json, dict):
            widget, properties, children = self.get_widget(
                json)
            w = None
            if "row" in properties and "column" in properties:
                w = create_widget(widget, parent, properties, properties["row"], properties["column"])
            else:
                w = create_widget(widget, parent, properties)
            if not w:
                w = parent
            else:
                if "objectName" in properties:
                    w.objectName = properties["objectName"]["value"]
                    setattr(
                        self, properties["objectName"]["value"], w)
#                     print("yes:" + getattr(self, properties["objectName"]).text())
            if children:
                self.initUIFromJson(w, children)
        elif isinstance(json, list):
            for j in json:
                self.initUIFromJson(parent, j)

    def get_widget(self, json):
        clazz = None
        properties = None
        children = None
        for k, v in json.items():
            clazz = k
            if isinstance(v, dict):
                if "properties" in v:
                    properties = v["properties"]
                    print("properties:", v["properties"])
                if "children" in v:
                    children = v["children"]
                    print("children:", children)
        return clazz, properties, children

    def on_add_widget(self, widget, properties):
        parent_name = widget.parent.objectName
        parent_node = self.find_widget(
            parent_name, self.ui_content)
        if not parent_node:
            raise("can not find parent node")
            return

        prop = {}
        prop["properties"] = widget.properties
        prop["children"] = []
        item = {}
        item[widget.__class__.__name__] = prop
        parent_node["children"].append(item)
        print(self.ui_content)

    def find_widget(self, object_name, ui_content):
        for v in ui_content.values():
            if v["properties"]["objectName"]["value"] == object_name:
                return v
            elif len(v["children"]) != 0:
                for child in v["children"]:
                    parent_node = self.find_widget(
                        object_name, child)
                    if parent_node:
                        return parent_node
                    else:
                        continue

            else:
                continue

    def on_del_widget(self, widget, properties, parent):
        parent_name = widget.parent.objectName
        parent_node = self.find_widget(
            parent_name, self.ui_content)
        if not parent_node:
            raise("can not find parent node")
            return

        match = False
        for child in parent_node["children"]:
            if match:
                break
            for key, value in child.items():
                if key == widget.__class__.__name__ and value["properties"]["objectName"]["value"] == widget.objectName:
                    parent_node["children"].remove(child)
                    del child
                    match = True
                    break
                else:
                    continue
        print(self.ui_content)

    def on_edit_widget(self, widget):
        widget_node = self.find_widget(
            widget.objectName, self.ui_content)
        if widget_node:
            widget_node["properties"] = widget.properties

    def show_error(self, *args):
        a = traceback.format_exception(*args)
        messagebox.showerror(
            a[-1], "\n".join(a[:-1]), parent=self)


def drop(event):
    print("in drop", event.data)


def main():
    app = kdGUIDesigner()

    app.showMaximized()
    app.run()
