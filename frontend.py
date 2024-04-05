import tkinter as tk

class SudokuSolverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        
        # Create GUI elements
        self.input_label = tk.Label(master, text="Enter Sudoku puzzle (use 0 for empty cells):")
        self.input_text = tk.Text(master, height=9, width=25)
        self.solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        self.output_label = tk.Label(master, text="Solved Sudoku:")
        self.output_text = tk.Text(master, height=9, width=25, state=tk.DISABLED)
        
        # Layout GUI elements
        self.input_label.grid(row=0, column=0)
        self.input_text.grid(row=1, column=0)
        self.solve_button.grid(row=2, column=0)
        self.output_label.grid(row=3, column=0)
        self.output_text.grid(row=4, column=0)

    def solve_sudoku(self):
        sudoku_input = self.input_text.get("1.0", tk.END)
        # Here you can call the backend function to solve the Sudoku puzzle
        # For simplicity, let's just display the input in the output area
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, sudoku_input)
        self.output_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
