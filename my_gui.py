#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" My awesome GUI! """

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np

from PySide import QtCore, QtGui

import mpl


class MyGUI(QtGui.QDialog):

    def __init__(self, **kwargs):
        super(MyGUI, self).__init__(**kwargs)

        self.setGeometry(600, 480, 600, 480)
        self.move(QtGui.QApplication.desktop().screen().rect().center() \
            - self.rect().center())
        self.setWindowTitle("My awesome GUI")

        vertical_layout = QtGui.QVBoxLayout(self)
        self.figure_widget = mpl.MPLWidget(tight_layout=True)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figure_widget.sizePolicy().hasHeightForWidth())
        self.figure_widget.setSizePolicy(sizePolicy)
        vertical_layout.addWidget(self.figure_widget)

        horizontal_layout = QtGui.QHBoxLayout()
        self.btn_show_data = QtGui.QPushButton(self)
        self.btn_show_data.setText("Show data")
        horizontal_layout.addWidget(self.btn_show_data)

        self.btn_change_color = QtGui.QPushButton(self)
        self.btn_change_color.setText("Change color")
        horizontal_layout.addWidget(self.btn_change_color)
        spacer = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        horizontal_layout.addItem(spacer)
        self.btn_ok = QtGui.QPushButton(self)
        self.btn_ok.setText("OK")
        horizontal_layout.addWidget(self.btn_ok)
        vertical_layout.addLayout(horizontal_layout)

        # Create a matplotlib axes.
        ax = self.figure_widget.figure.add_subplot(111)
        ax.set_xlabel(r"$x$")
        ax.set_ylabel(r"$y$")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.scatter([], [])

        # Connect the signals.
        self.btn_ok.clicked.connect(self.close)
        self.btn_show_data.clicked.connect(self.show_data)
        self.btn_change_color.clicked.connect(self.change_color)

        # Create a matplotlib event listener.
        self.figure_widget.mpl_connect("button_press_event", self.button_press)

        return None


    def show_data(self):
        """ A function to show data. """

        x = np.random.uniform(size=100)
        y = np.random.uniform(size=100)

        self.figure_widget.figure.axes[0].collections[0].set_offsets(
            np.array([x, y]).T)
        self.figure_widget.draw()


    def change_color(self):
        """ Change the color of the data points. """

        colors = "rgbmky"
        self.figure_widget.figure.axes[0].collections[0].set_color(
            colors[np.random.randint(0, len(colors))])
        self.figure_widget.draw()

        return None


    def button_press(self, event):
        """ A function for when a button has been pressed in the figure. """

        print("Button press event!", event)


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyGUI()
    window.exec_()
