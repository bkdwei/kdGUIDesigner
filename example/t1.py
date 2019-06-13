
from kdGUI import *


class kdGUIDesigner(Window):

    def __init__(self):
        super().__init__()

        self.HorizontalLayout_0 = HorizontalLayout(
            'HorizontalLayout_0', self)
        self.addWidget(self.HorizontalLayout_0)
        self.PushButton_0 = PushButton(
            'PushButton_0', self.HorizontalLayout_0)
        self.HorizontalLayout_0.addWidget(self.PushButton_0)
        self.RadioButton_0 = RadioButton(
            'RadioButton_0', self.HorizontalLayout_0)
        self.HorizontalLayout_0.addWidget(
            self.RadioButton_0)
        self.CheckButton_0 = CheckButton(
            'CheckButton_0', self.HorizontalLayout_0)
        self.HorizontalLayout_0.addWidget(
            self.CheckButton_0)
        self.HorizontalLayout_1 = HorizontalLayout(
            'HorizontalLayout_1', self)
        self.addWidget(self.HorizontalLayout_1)
        self.ListWidget_0 = ListWidget(
            self.HorizontalLayout_1)
        self.HorizontalLayout_1.addWidget(self.ListWidget_0)
        self.TreeWidget_0 = TreeWidget(
            self.HorizontalLayout_1)
        self.HorizontalLayout_1.addWidget(self.TreeWidget_0)
        self.HorizontalLayout_2 = HorizontalLayout(
            'HorizontalLayout_2', self)
        self.addWidget(self.HorizontalLayout_2)
        self.ComboBox_0 = ComboBox(self.HorizontalLayout_2)
        self.HorizontalLayout_2.addWidget(self.ComboBox_0)
        self.LineEdit_22 = LineEdit(
            'LineEdit_22', self.HorizontalLayout_2)
        self.HorizontalLayout_2.addWidget(self.LineEdit_22)


app = kdGUIDesigner()
app.run()
