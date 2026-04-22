import math
import sys
from typing import List, Tuple

from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QBrush, QColor, QPainter, QPen, QPolygonF
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

class Polygon:
    def __init__(self, vertices: List[Tuple[float, float]]):
        #A class representing a polygon with vertices in 2D space.
        #A Tuple is a collection of elemets and used to store data
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices")
        self.vertices = vertices

    @property
    #defines a method but you can access it like an attribute
    def num_sides(self) -> int:
        #Return the number of sides in the polygon
        return len(self.vertices)

    @property
    #Calculate and return the perimeter of the polygon
    def perimeter(self) -> float:
        total = 0.0
        for i in range(self.num_sides):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_sides]
            total += math.hypot(x2 - x1, y2 - y1)
        return total

    @property
    #Calculate and return the area of the polygon
    def area(self) -> float:
        total = 0.0
        for i in range(self.num_sides):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_sides]
            #changed math operation from using distance to having formula in total
            total += x1 * y2 - x2 * y1
        return abs(total) / 2


class PolygonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #title banner
        self.setWindowTitle("Polygon Builder")
        self.setMinimumSize(1200, 750)

        #centers window on screen
        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QHBoxLayout(central)

        controls = QWidget()
        controls_layout = QVBoxLayout(controls)
        controls.setMaximumWidth(300)

        #creates a row for the number of sides input
        sides_row = QHBoxLayout()
        sides_row.addWidget(QLabel("Number of sides:"))
        self.sides_spin = QSpinBox()
        self.sides_spin.setMinimum(3)
        self.sides_spin.setMaximum(100)
        self.sides_spin.setValue(4)
        self.sides_spin.valueChanged.connect(self.build_vertex_table)
        sides_row.addWidget(self.sides_spin)
        controls_layout.addLayout(sides_row)

        #creates the vertex table for inputting coordinates
        self.vertex_table = QTableWidget()
        self.vertex_table.setColumnCount(2)
        self.vertex_table.setHorizontalHeaderLabels(["X", "Y"])
        self.vertex_table.verticalHeader().setVisible(True)
        self.vertex_table.horizontalHeader().setStretchLastSection(True)
        controls_layout.addWidget(QLabel("Vertices (one row per point):"))
        controls_layout.addWidget(self.vertex_table)

        #creates the draw button and connects the verts together
        self.draw_btn = QPushButton("Draw Polygon")
        self.draw_btn.clicked.connect(self.draw_polygon)
        controls_layout.addWidget(self.draw_btn)

        #creates a status label to show the user what to do and the results of their polygon
        self.status_label = QLabel("Set sides, fill coordinates, then click Draw Polygon.")
        self.status_label.setWordWrap(True)
        controls_layout.addWidget(self.status_label)
        controls_layout.addStretch()

        #creates the graphics view for drawing the polygon
        self.scene = QGraphicsScene(self)
        self.graph_view = QGraphicsView(self.scene)
        self.graph_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.graph_view.setBackgroundBrush(QBrush(QColor("#00000000")))

        #adds the controls and graph view to the main layout
        root_layout.addWidget(controls)
        root_layout.addWidget(self.graph_view, stretch=3)

        self.build_vertex_table()

    def build_vertex_table(self, num_sides=None):
        if num_sides is None:
            num_sides = self.sides_spin.value()
        # Adjust the vertex table to have the correct number of rows for the specified number of sides.
        self.vertex_table.setRowCount(num_sides)
        for row in range(num_sides):
            self.vertex_table.setVerticalHeaderItem(row, QTableWidgetItem(f"V{row + 1}"))
            if self.vertex_table.item(row, 0) is None:
                self.vertex_table.setItem(row, 0, QTableWidgetItem("0"))
            if self.vertex_table.item(row, 1) is None:
                self.vertex_table.setItem(row, 1, QTableWidgetItem("0"))
        self.status_label.setText(f"Coordinate box ready for {num_sides} sides.")

    def read_vertices(self) -> List[Tuple[float, float]]:
        #Read the vertices from the vertex table and return them as a list of (x, y) cordinates
        vertices: List[Tuple[float, float]] = []
        for row in range(self.vertex_table.rowCount()):
            x_item = self.vertex_table.item(row, 0)
            y_item = self.vertex_table.item(row, 1)

            if x_item is None or y_item is None:
                raise ValueError(f"Row {row + 1} is missing coordinates.")

            x_text = x_item.text().strip()
            y_text = y_item.text().strip()
            if not x_text or not y_text:
                raise ValueError(f"Row {row + 1} is missing coordinates.")

            try:
                x = float(x_text)
                y = float(y_text)
            except ValueError as exc:
                raise ValueError(f"Row {row + 1} must contain valid numbers.") from exc

            vertices.append((x, y))

        return vertices

    def draw_polygon(self):
        self.scene.clear()
        #Read the vertices from the table and create a Polygon

        try:
            vertices = self.read_vertices()
            polygon = Polygon(vertices)
        except ValueError as err:
            self.status_label.setText(f"Error: {err}")
            return

        #Draw the polygon using QGraphicsScene
        qt_polygon = QPolygonF([QPointF(x, -y) for x, y in vertices])
        pen = QPen(QColor("#1f4e79"), 1)
        fill = QBrush(QColor("#1f6f79c7"))
        self.scene.addPolygon(qt_polygon, pen, fill)

        #Draw vertices on top of the polygon
        vertex_pen = QPen(QColor("#aa3a3a"), 0.5)
        vertex_fill = QBrush(QColor("#d9534f"))
        radius = 0.5
        for x, y in vertices:
            px = x - radius
            py = -y - radius
            self.scene.addEllipse(px, py, radius * 2, radius * 2, vertex_pen, vertex_fill)

        # Add axis lines around the polygon so the user has visual orientation.
        bounds = self.scene.itemsBoundingRect()
        pad = max(bounds.width(), bounds.height(), 10) * 0.15 + 10
        self.scene.addLine(bounds.left() - pad, 0, bounds.right() + pad, 0, QPen(QColor("#999999"), 0.5))
        self.scene.addLine(0, bounds.top() - pad, 0, bounds.bottom() + pad, QPen(QColor("#999999"), 0.5))

        # Adjust the view to fit the polygon with some padding.
        all_bounds = self.scene.itemsBoundingRect()
        self.graph_view.setSceneRect(all_bounds.adjusted(-pad, -pad, pad, pad))
        self.graph_view.fitInView(self.graph_view.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

        #Update the label with the polygon's area and perimeter
        self.status_label.setText(
            f"Polygon created: {polygon.num_sides} sides | Perimeter: {polygon.perimeter:.2f} | Area: {polygon.area:.2f}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PolygonWindow()
    window.show()
    sys.exit(app.exec())