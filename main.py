import tkinter as tk
windows = tk.Tk()
windows.title("Проверка корректности синтаксиса алгоритмов")
windows.geometry("1100x650")
windows.configure(bg="#171821")
windows.minsize(900, 550)
BG_COLOR = "#171821"
PANEL_COLOR = "#22232e"
TEXT_COLOR = "#eeeeff"
PURPLE = "#8050ed"
header = tk.Label(
    windows,
    text="</>  Проверка корректности синтаксиса алгоритмов",
    font=("Arial", 19, "bold"),
    bg=PANEL_COLOR,
    fg=TEXT_COLOR,
    pady=18
)
header.pack(fill="x")
main_frame = tk.Frame(windows, bg=BG_COLOR, padx=25, pady=25)
main_frame.pack(fill="both", expand=True)
input_label = tk.Label(
    main_frame,
    text="Введите алгоритм:",
    font=("Arial", 16, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
input_label.pack(anchor="w", pady=(0, 10))
editor_frame = tk.Frame(
    main_frame,
    bg=PANEL_COLOR,
    highlightbackground="#555568",
    highlightthickness=2
)
editor_frame.pack(fill="both", expand=True)
result_label = tk.Label(
    main_frame,
    text="Результат проверки появится здесь",
    font=("Arial", 13),
    bg=BG_COLOR,
    fg="#aaaaC8"
)
result_label.pack(anchor="w", pady=20)
windows.mainloop()