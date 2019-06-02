'''
Created on 2019年6月2日

@author: bkd
'''
from tkinter.constants import *

from kdGUI import *


class kdGUIDesigner(Window):

    def __init__(self):
        super().__init__()
        pass


def main():
    app = Window("kdGUIDesigner")
    app.setLayout(HORIZONTAL)
    app.setTheme("clearlooks")
    
    # widgetBox
    widgetBox = VerticalLayout("widget Box", app)
    app.addWidget(widgetBox)
    lb = Label("标签", widgetBox)
    widgetBox.addWidget(lb)
    le_filter = LineEdit(None, widgetBox)
    widgetBox.addWidget(le_filter)
    
    # main windows
    gl_main = GridLayout("MainWindos - untitle", app)
    bt_test = Button("good", gl_main)
    gl_main.addWidget(bt_test, 0, 0)
    app.addWidget(gl_main)
    
    # object tree
    tr_widget = TreeWidget(app)
    app.addWidget(tr_widget)
    bkd = tr_widget.addTopLevelItem("bkd")
#     tr_widget.addChildren(bkd, ("a", "b"))
    
    # layouts
    vl_layouts = VerticalLayout("Layouts", widgetBox)
    
    lb_verticalLayout = Label("Vertical Layout", vl_layouts)
    lb_verticalLayout.setAnchor("w")
    vl_layouts.addWidget(lb_verticalLayout)
    
    lb_horizontal = Label("Horizontal Layout", vl_layouts)
    lb_horizontal.setAnchor("w")
    vl_layouts.addWidget(lb_horizontal)
    
    lb_gridLayout = Label("Grid Layout", vl_layouts)
    lb_gridLayout.setAnchor("w")
    vl_layouts.addWidget(lb_gridLayout)
    widgetBox.addWidget(vl_layouts)
    
    # spacers
    vl_spacers = VerticalLayout("Spacers", widgetBox)
    
    lb_horizontalSpacer = Label("Horizontal Spacer", vl_spacers)
    lb_horizontalSpacer.setAnchor("w")
    vl_spacers.addWidget(lb_horizontalSpacer)
    
    lb_verticalSpacer = Label("Vertical Spacer", vl_spacers)
    lb_verticalSpacer.setAnchor("w")
    vl_spacers.addWidget(lb_verticalSpacer)
    
    widgetBox.addWidget(vl_spacers)
    
    # buttons
    vl_buttons = VerticalLayout("Buttons", widgetBox)
    
    lb_pushbutton = Label("Push Button", vl_buttons)
    lb_pushbutton.setAnchor("w")
    vl_buttons.addWidget(lb_pushbutton)
    
    lb_radiobutton = Label("Radio Button", vl_buttons)
    lb_radiobutton.setAnchor("w")
    vl_buttons.addWidget(lb_radiobutton)
    
    lb_checkbutton = Label("Check Button", vl_buttons)
    lb_checkbutton.setAnchor("w")
    vl_buttons.addWidget(lb_checkbutton)
    
    widgetBox.addWidget(vl_buttons)
    
    # item widgets
    vl_item_widgets = VerticalLayout("Item Widgets", widgetBox)
    
    lb_list_widget = Label("List Widget", vl_item_widgets)
    lb_list_widget.setAnchor("w")
    vl_item_widgets.addWidget(lb_list_widget)
    
    lb_tree_widget = Label("Tree Widget", vl_item_widgets)
    lb_tree_widget.setAnchor("w")
    vl_item_widgets.addWidget(lb_tree_widget)
    
    lb_table_widget = Label("Table Widget", vl_item_widgets)
    lb_table_widget.setAnchor("w")
    vl_item_widgets.addWidget(lb_table_widget)
    
    widgetBox.addWidget(vl_item_widgets)
   
    # containers
    vl_containers = VerticalLayout("Containers", widgetBox)
    
    lb_scroll_area = Label("Scroll Area", vl_item_widgets)
    lb_scroll_area.setAnchor("w")
    vl_item_widgets.addWidget(lb_scroll_area)
    
    lb_tab_widget = Label("Tab Widget", vl_item_widgets)
    lb_tab_widget.setAnchor("w")
    vl_item_widgets.addWidget(lb_tab_widget)
    
    widgetBox.addWidget(vl_containers) 
    
        # input widget
    vl_input_widgets = VerticalLayout("Input Widgets", widgetBox)
    
    lb_combobox = Label("Combo Box", vl_input_widgets)
    lb_combobox.setAnchor("w")
    vl_item_widgets.addWidget(lb_combobox)
    
    lb_lineedit = Label("Line Edit", vl_input_widgets)
    lb_lineedit.setAnchor("w")
    vl_item_widgets.addWidget(lb_lineedit)
    
    lb_textedit = Label("Text Edit", vl_input_widgets)
    lb_textedit.setAnchor("w")
    vl_item_widgets.addWidget(lb_textedit)
    
    lb_plaintextedit = Label("Plain Text Edit", vl_input_widgets)
    lb_plaintextedit.setAnchor("w")
    vl_item_widgets.addWidget(lb_plaintextedit)
    
    lb_spinbox = Label("Spin Box", vl_input_widgets)
    lb_spinbox.setAnchor("w")
    vl_item_widgets.addWidget(lb_spinbox)
    
    lb_dateedit = Label("Date Edit", vl_input_widgets)
    lb_dateedit.setAnchor("w")
    vl_item_widgets.addWidget(lb_dateedit)
    
    lb_timeedit = Label("Time Edit", vl_input_widgets)
    lb_timeedit.setAnchor("w")
    vl_item_widgets.addWidget(lb_timeedit)
    
    widgetBox.addWidget(vl_input_widgets)
    
        # display widgets
    vl_display_widgets = VerticalLayout("Display Widgets", widgetBox)
    
    lb_label = Label("Lable", vl_display_widgets)
    lb_label.setAnchor("w")
    vl_display_widgets.addWidget(lb_label)
    
    lb_text_browser = Label("Text Browser", vl_display_widgets)
    lb_text_browser.setAnchor("w")
    vl_display_widgets.addWidget(lb_text_browser)

    lb_progress_bar = Label("Prograss Bar", vl_display_widgets)
    lb_progress_bar.setAnchor("w")
    vl_display_widgets.addWidget(lb_progress_bar)    
    widgetBox.addWidget(vl_display_widgets)     
    app.run()
