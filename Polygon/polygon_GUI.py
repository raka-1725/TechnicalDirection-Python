import math
import sys
from typing import List, Tuple
#imports to use later


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
    #A class representing a polygon with vertices in 2D space.
    #A Tuple is a collection of elemets and used to store data
    def __init__(self, vertices: List[Tuple[float, float]]):
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices")
        
        self.vertices = vertices
    
    @property
    #defines a method but you can access it like an attribute
    def num_sides(self) -> int:
        #Return the number of sides in the polygon
        return len(self.vertices)
    
    @property
    def perimeter(self) -> float:
        #Calculate and return the perimeter of the polygon
        total = 0
        for i in range(self.num_sides):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_sides]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            total += distance
        return total
    
    @property
    def area(self) -> float:
        #Calculate the area of the polygon using the Shoelace formula.
        total = 0
        for i in range(self.num_sides):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_sides]
            total += x1 * y2 - x2 * y1
        return abs(total) / 2

class PolygonWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #title
        self.setWindowTitle("Polygon Graphic Builder")
        self.setMinimumSize(1200,750)

        #ceneter window
        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QHBoxLayout(central)

        controls = QWidget()
        controls_layout = QVBoxLayout(controls)
        self.setMaximumWidth(300)

        #create row for the number of sides input
        sides_row = QHBoxLayout()
        sides_row.addWidget(QLabel("Number of Sides:"))
        self.sides_spin = QSpinBox()
        self.sides_spin.setMinimum(3)
        self.sides_spin.setMaximum(100)
        self.sides_spin.setValue(4)
        self.sides_spin.valueChanged.connect(self.build_vertex_table)
        sides_row.addWidget(self.sides_spin)
        controls_layout.addLayout(sides_row)

        #creates vertex table
        self.vertex_table = QTableWidget()
        self.vertex_table.setColumnCount(2)
        self.vertex_table.setHorizontalHeaderLabels(["X", "Y"])
        self.vertex_table.verticalHeader().setVisible(True)
        self.vertex_table.horizontalHeader().setStretchLastSection(True)
        controls_layout.addWidget(QLabel("Vertices (one row per point):"))
        controls_layout.addWidget(self.vertex_table)

        #create draw button and connect vertecies
        self.draw_btn = QPushButton("Draw Polygon")
        self.draw_btn.clicked.connect(self.draw_polygon)
        controls_layout.addWidget(self.draw_btn)

        #status label
        self.status_label = QLabel("Set sides, fill coordinates, then click Draw Polygon.")
        self.status_label.setWordWrap(True)
        controls_layout.addWidget(self.status_label)
        controls_layout.addStretch()

        #creates graph for drawing polygon
        self.scene = QGraphicsScene(self)
        self.graph_view = QGraphicsView(self.scene)
        self.graph_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.graph_view.setBackgroundBrush(QBrush(QColor("#00000000")))

        #add to main window
        root_layout.addWidget(controls)
        root_layout.addWidget(self.graph_view, stretch=3)

        self.build_vertex_table()

    #
    def build_vertex_table(self, num_sides=None):
        if num_sides is None:
            num_sides = self.sides_spin.value()
        # Adjust vertex to have same val of row and side
        self.vertex_table.setRowCount(num_sides)
        for row in range(num_sides):
            self.vertex_table.setVerticalHeaderItem(row, QTableWidgetItem(f"V{row + 1}"))
            if self.vertex_table.item(row, 0) is None:
                self.vertex_table.setItem(row, 0, QTableWidgetItem("0"))
            if self.vertex_table.item(row, 1) is None:
                self.vertex_table.setItem(row, 1, QTableWidgetItem("0"))
        self.status_label.setText(f"Coordinate box ready for {num_sides} sides.")

    def read_vertices(self) -> List[Tuple[float, float]]:
        #Read vertecies
        vertices: List[Tuple[float, float]] = []
        #for each row check value error
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
        #Read vertices from the table and create Polygon
        try:
            vertices = self.read_vertices()
            polygon = Polygon(vertices)
        except ValueError as err:
            self.status_label.setText(f"Error: {err}")
            return

        #Draw polygon using QGraphicsScene
        qt_polygon = QPolygonF([QPointF(x, -y) for x, y in vertices])
        pen = QPen(QColor("#1f4e79"), 1)
        fill = QBrush(QColor("#1f6f79c7"))
        self.scene.addPolygon(qt_polygon, pen, fill)

        #Draw vertices with colors
        vertex_pen = QPen(QColor("#aa3a3a"), 0.5)
        vertex_fill = QBrush(QColor("#d9534f"))
        radius = 0.5
        for x, y in vertices:
            px = x - radius
            py = -y - radius
            self.scene.addEllipse(px, py, radius * 2, radius * 2, vertex_pen, vertex_fill)

        # add graph lines
        bounds = self.scene.itemsBoundingRect()
        pad = max(bounds.width(), bounds.height(), 10) * 0.15 + 10
        self.scene.addLine(bounds.left() - pad, 0, bounds.right() + pad, 0, QPen(QColor("#2F00FF"), 0.5))
        self.scene.addLine(0, bounds.top() - pad, 0, bounds.bottom() + pad, QPen(QColor("#2F00FF"), 0.5))

        # fit padding
        all_bounds = self.scene.itemsBoundingRect()
        self.graph_view.setSceneRect(all_bounds.adjusted(-pad, -pad, pad, pad))
        self.graph_view.fitInView(self.graph_view.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

        #Update label with info
        self.status_label.setText(
            f"Polygon created: {polygon.num_sides} sides | Perimeter: {polygon.perimeter:.2f} | Area: {polygon.area:.2f}"
        )


# Example usage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PolygonWindow()
    window.show()
    sys.exit(app.exec())