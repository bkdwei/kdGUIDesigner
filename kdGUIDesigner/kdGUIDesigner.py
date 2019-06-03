'''
Created on 2019年6月2日

@author: bkd
'''
from tkinter.constants import *

from kdGUI import *
from tkintertable import TableCanvas, TableModel
from .DragManager import DragManager


class kdGUIDesigner(Window):

    def __init__(self):
        super().__init__()
        self.setTitle("kdGUIDesigner")
        self.setLayout(HORIZONTAL)
        self.setTheme("clearlooks")
        self.initUI()
        self.bindWidgetBox()

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
        vl_layouts = VerticalLayout("Layouts", self.widgetBox)
        lb_verticalLayout = Label("Vertical Layout", vl_layouts)
        lb_verticalLayout.setAnchor("w")
        vl_layouts.addWidget(lb_verticalLayout)
        
        lb_horizontal = Label("Horizontal Layout", vl_layouts)
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
        vl_spacers = VerticalLayout("Spacers", self.widgetBox)
        
        lb_horizontalSpacer = Label("Horizontal Spacer", vl_spacers)
        lb_horizontalSpacer.setAnchor("w")
        vl_spacers.addWidget(lb_horizontalSpacer)
        
        lb_verticalSpacer = Label("Vertical Spacer", vl_spacers)
        lb_verticalSpacer.setAnchor("w")
        vl_spacers.addWidget(lb_verticalSpacer)
        
        self.widgetBox.addWidget(vl_spacers)
    
    # buttons
    def addButtons(self):
        vl_buttons = VerticalLayout("Buttons", self.widgetBox)
        
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
        vl_item_widgets = VerticalLayout("Item Widgets", self.widgetBox)
        
        lb_list_widget = Label("List Widget", vl_item_widgets)
        lb_list_widget.setAnchor("w")
        vl_item_widgets.addWidget(lb_list_widget)
        
        lb_tree_widget = Label("Tree Widget", vl_item_widgets)
        lb_tree_widget.setAnchor("w")
        vl_item_widgets.addWidget(lb_tree_widget)
        
        lb_table_widget = Label("Table Widget", vl_item_widgets)
        lb_table_widget.setAnchor("w")
        vl_item_widgets.addWidget(lb_table_widget)
        
        self.widgetBox.addWidget(vl_item_widgets)

    # containers
    def addContainers(self):
        vl_containers = VerticalLayout("Containers", self.widgetBox)
        
        lb_scroll_area = Label("Scroll Area", vl_containers)
        lb_scroll_area.setAnchor("w")
        vl_containers.addWidget(lb_scroll_area)
        
        lb_tab_widget = Label("Tab Widget", vl_containers)
        lb_tab_widget.setAnchor("w")
        vl_containers.addWidget(lb_tab_widget)
        
        self.widgetBox.addWidget(vl_containers) 
    
    # input widget
    def addInputWidgets(self):
        vl_input_widgets = VerticalLayout("Input Widgets", self.widgetBox)
        
        lb_combobox = Label("Combo Box", vl_input_widgets)
        lb_combobox.setAnchor("w")
        vl_input_widgets.addWidget(lb_combobox)
        
        lb_lineedit = Label("Line Edit", vl_input_widgets)
        lb_lineedit.setAnchor("w")
        vl_input_widgets.addWidget(lb_lineedit)
        
        lb_textedit = Label("Text Edit", vl_input_widgets)
        lb_textedit.setAnchor("w")
        vl_input_widgets.addWidget(lb_textedit)
        
        lb_plaintextedit = Label("Plain Text Edit", vl_input_widgets)
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
        vl_display_widgets = VerticalLayout("Display Widgets", self.widgetBox)
        
        lb_label = Label("Lable", vl_display_widgets)
        lb_label.setAnchor("w")
        vl_display_widgets.addWidget(lb_label)
        
        lb_text_browser = Label("Text Browser", vl_display_widgets)
        lb_text_browser.setAnchor("w")
        vl_display_widgets.addWidget(lb_text_browser)
    
        lb_progress_bar = Label("Prograss Bar", vl_display_widgets)
        lb_progress_bar.setAnchor("w")
        vl_display_widgets.addWidget(lb_progress_bar)    
        self.widgetBox.addWidget(vl_display_widgets)     
        
    # main windows
    def addMainWindow(self):
        self.gl_main = Container("MainWindos - untitle", self)
#         self.gl_main = GridLayout("MainWindos - untitle", self)
        self.addWidget(self.gl_main, expand=YES)
        menu_layout = Menu(False, self.gl_main)
        
        menu_sub_layout = Menu(False, menu_layout)
        menu_sub_layout.addAction("Vertical Layout", lambda :self.setMainWindowLayout(VERTICAL))
        menu_sub_layout.addAction("Horizontal Layout", lambda :self.setMainWindowLayout(HORIZONTAL))
        menu_sub_layout.addAction("Grid Layout", lambda :self.setMainWindowLayout(Window.GRID))
        menu_layout.addMenu("layout1", menu_sub_layout)
        addContextMenu(self.gl_main, menu_layout)
        print(self.get_variable_name(self.gl_main))

    # object tree
    def addObjectTree(self):
        tr_widget = TreeWidget(self)
        self.addWidget(tr_widget)

    def addPropertyEditor(self):
        c = Frame(self)
        data = {
            'rec1': {'Property': "ObjectName", 'Value': "Button"},
            'rec2': {'Property': "text", 'Value': "PushButton"}
       } 

        table_property = TableCanvas(c, data=data, rows=10, cols=2, width=260, cellwidth=130)
        self.addWidget(c)
        table_property.show()
        self.table_model = table_property.model
        self.table_property = table_property
    
    def bindWidgetBox(self):
        self.dm = DragManager()
        self.dm.show_widget_property.connect(self.show_widget_properties)
        
        _containers = self.widgetBox.childrens()
        for c in _containers :
            if  isinstance(c, VerticalLayout):
                _lables = c.childrens()
                for l in _lables:
                    self.dm.add_dragable(l)

    def setMainWindowLayout(self, layout):
        self.gl_main.setLayout(layout)
        print(layout)

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

    def show_widget_properties(self, clazz):
        print("clazz:" + clazz)
        self.table_model.createEmptyModel()
        self.table_property.redraw()
        
        if clazz == "Button" :
            self.table_property.addRow(None, Property='abc', Value='abc1')
            self.table_property.addRow(None, Property='abcd', Value='abdc1')


def drop(event):
    print("in drop", event.data)


def main():
    app = kdGUIDesigner()
   
    app.showMaximized()
    app.run()

