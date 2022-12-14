from tkinter import ttk, Frame, Label, StringVar, HORIZONTAL, Text, RAISED, END
from PIL import Image, ImageTk


class Hard_core_writer(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.config(self, bg="#f8f9fa")
        self.session_duration = 5
        self.session_ongoing = 0
        self.prog_bar_var = 0
        self.col_id = 0
        self.timer = None
        self.user_input = None
        self.wirt_timer = None
        self.first_st = True
        self.session_seconds = 0
        self.master = master
        self.colors = ["#e7f5ff", "#d0ebff", "#a5d8ff", "#74c0fc", "#4dabf7", "#339af0", "#228be6", "#1c7ed6",
                       "#1971c2", "#1864ab"]
        # start menu
        self.title = Label(self, text="The most Dangerous Writing App\n\nDon't Stop Writing!",
                           font=("Arial", 20), bg="#f8f9fa")
        self.text_opt = [5, 5, 10, 15, 20, 30, 60]
        self.var = StringVar(self)
        self.var.set(self.text_opt[0])
        self.time_label = Label(self, text="Session length:", bg="#f8f9fa")
        self.min_label = Label(self, text="Minutes", bg="#f8f9fa")
        self.time_suggest = ttk.OptionMenu(self, self.var, *self.text_opt, command=self.set_duration)
        self.start_button = ttk.Button(self, text='Start Writing', command=self.start)
        # start menu

        # writing screen
        self.progressbar = None
        self.back_button = None
        # writing screen

        # menu grid
        self.title.grid(row=0, column=0, pady=100)
        self.time_label.grid(row=1, column=0, padx=(0, 150), pady=20)
        self.time_suggest.grid(row=1, column=0, pady=20)
        self.min_label.grid(row=1, column=0, padx=(120, 0), pady=20)
        self.start_button.grid(row=2, column=0)
        # menu grid

    def start_insert(self):
        self.title.grid(row=0, column=0, pady=100)
        self.time_label.grid(row=1, column=0, padx=(0, 150), pady=20)
        self.time_suggest.grid(row=1, column=0, pady=20)
        self.min_label.grid(row=1, column=0, padx=(120, 0), pady=20)
        self.start_button.grid(row=2, column=0)


    def calculate_seconds(self):
        self.session_seconds = self.session_duration * 60

    def insert_prog_bar(self):
        self.progressbar = ttk.Progressbar(self, orient=HORIZONTAL, length=790, mode='determinate')
        self.progressbar.grid(row=0, column=0)

    def insert_writing_board(self):
        self.user_input = Text(self, width=96, height=80, relief=RAISED, highlightthickness=1,
                               highlightbackground="black", fg="#1864ab", bg="#e7f5ff")
        self.user_input.tag_configure("center", justify='center', font=("bold", 20))
        self.user_input.insert(1.0, " ")
        self.user_input.tag_add("center", "1.0", "end")
        self.user_input.focus()
        self.back_button = ttk.Button(text="Back", command=self.clear_screen_write)
        self.back_button.grid(row=2, column=0, padx=(5, 0))
        self.user_input.grid(row=1, column=0, pady=(20, 2))

    def clear_board(self):
        if self.user_input is not None:
            self.user_input.configure(bg="#e7f5ff")
            self.user_input.delete("1.0", END)
            self.user_input.tag_configure("center", justify='center')
            self.user_input.insert(1.0, " ")
            self.user_input.tag_add("center", "1.0", "end")
            self.user_input.focus()

    def timer_tick(self):
        if self.session_ongoing != 0:
            self.progressbar["value"] = str(790 * (((self.session_ongoing / 10) / self.session_seconds) * 100) / 100)
        if self.session_seconds > self.session_ongoing:
            self.session_ongoing += 1
            self.timer = self.after(1000, self.timer_tick)
        else:
            self.clear_board()

    def next_color(self):
        if self.col_id == 9:
            self.clear_board()
            self.wrt_timer_reset()
        else:
            self.col_id += 1
            self.user_input.configure(bg=self.colors[self.col_id])
            self.wrt_timer(mode="inner")

    def wrt_timer(self, event='', mode=''):
        if mode == "inner":
            self.wirt_timer = self.after(400, self.next_color)
        if self.first_st is True:
            self.wirt_timer = self.after(400, self.next_color)
            self.first_st = False

    def wrt_timer_reset(self, event=''):
        if self.wirt_timer is not None:
            self.after_cancel(self.wirt_timer)
            self.col_id = 0
            self.user_input.configure(bg=self.colors[self.col_id])
            self.first_st = True

    def set_duration(self, duration):
        self.session_duration = int(duration)

    def bind_any_kay(self, gui):
        return gui.bind("<KeyPress>", self.wrt_timer_reset)

    def bind_any_kay_release(self, gui):
        return gui.bind("<KeyRelease>", self.wrt_timer)

    def clear_screen_start(self):
        self.title.grid_forget()
        self.time_label.grid_forget()
        self.time_suggest.grid_forget()
        self.min_label.grid_forget()
        self.start_button.grid_forget()

    def clear_screen_write(self):
        self.master.unbind("<KeyPress>")
        self.master.unbind("<KeyRelease>")
        self.after_cancel(self.wirt_timer)
        self.after_cancel(self.timer)
        self.progressbar.grid_forget()
        self.user_input.grid_forget()
        self.back_button.grid_forget()
        self.start_insert()

    def start(self):
        self.clear_screen_start()
        self.insert_prog_bar()
        self.insert_writing_board()
        self.calculate_seconds()
        self.timer_tick()
        self.bind_any_kay(self.master)
        self.bind_any_kay_release(self.master)


def ico(gui):
    icon = Image.open('data/red-circle.png')
    photo = ImageTk.PhotoImage(icon)
    return gui.wm_iconphoto(False, photo)
