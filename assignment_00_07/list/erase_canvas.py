import tkinter as tk

CELL_SIZE = 40
ROWS = 10
COLS = 10
ERASER_SIZE = 60

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
        self.canvas.pack()
        self.rectangles = []
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = j * CELL_SIZE
                y2 = i * CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
                row.append(rect)
            self.rectangles.append(row)   

        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="black", fill="gray", stipple="gray25")
        self.canvas.bind("<B1-Motion>", self.move_eraser)  

    def move_eraser(self, event):
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE
        self.canvas.coords(self.eraser, x1, y1, x2, y2)
        for i in range(ROWS):
            for j in range(COLS):
                rect = self.rectangles[i][j]
                rx1, ry1, rx2, ry2 = self.canvas.coords(rect)
                if not (x2 < rx1 or x1 > rx2 or y2 < ry1 or y1 > ry2):
                    self.canvas.itemconfig(rect, fill="white") 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Eraser Canvas Example")
    app = EraserCanvas(root)
    root.mainloop()     
