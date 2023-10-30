import tkinter as tk
from tkinter import ttk
import pandas as pd

class CSVViewer(tk.Tk):
    def __init__(self, csv_path):
        super().__init__()

        self.csv_path = csv_path
        self.last_content = None  # store the last content we've read

        # Window properties
        self.title("CSV Viewer - Excel Lookalike")
        self.geometry("800x600")

        # Create a frame for the Treeview
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create and set the Treeview style
        style = ttk.Style(self)
        style.configure("Treeview",
                        background="#D1D1D2",
                        alternatebackground="#E5E5E5",
                        fieldbackground="#D1D1D2",
                        rowheight=25)
        style.map('Treeview',
                  background=[('selected', '#4a6984')])

        # Scrollbar style
        style.configure("Vertical.TScrollbar", gripcount=0, background='#9b9d9d', darkcolor='#5b5e5e', lightcolor='#5b5e5e', troughcolor='#5b5e5e', bordercolor='#5b5e5e', arrowcolor='white')
        
        # Enabling alternating row colors
        self.tree = ttk.Treeview(self.frame, columns=[], show="headings", selectmode="none", style="Treeview")
        self.tree.tag_configure('odd', background='#E5E5E5')
        self.tree.tag_configure('even', background='#D1D1D2')
        
        # Scrollbar for the Treeview
        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview, style="Vertical.TScrollbar")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Packing the treeview after scrollbar configuration
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Periodically refresh the data
        self.after(100, self.load_data)

    def load_data(self):
        # Load the CSV into a DataFrame
        df = pd.read_csv(self.csv_path)

        # Check if content has changed
        if not self.last_content or self.last_content != df.to_string():
            # Update last content
            self.last_content = df.to_string()

            # Clear previous content in tree
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Define columns and headings
            self.tree["columns"] = list(df.columns)
            for col in df.columns:
                max_width = max([len(str(val)) for val in df[col]]) * 10  # Calculate max width based on content
                max_width = min(max_width, 200)  # Set a maximum width limit
                self.tree.heading(col, text=col, anchor=tk.W)
                self.tree.column(col, anchor=tk.W, width=max_width)

            # Insert data with alternating colors
            for index, (_, row) in enumerate(df.iterrows()):
                tag = 'even' if index % 2 == 0 else 'odd'
                self.tree.insert("", tk.END, values=tuple(row), tags=(tag,))

        # Refresh data every 100 ms (0.1 second)
        self.after(100, self.load_data)

if __name__ == "__main__":
    app = CSVViewer("gh.csv")
    app.mainloop()
