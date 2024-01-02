import customtkinter as ctk

# APP LOGIC
def add_to_do():
  user_input = input_widget.get()
  added_todo = ctk.CTkLabel(master=scrollable_frame, text=user_input)
  added_todo.pack()
  input_widget.delete(0, ctk.END)

screen_mode = "dark"

def switch_theme():
  global screen_mode
  if screen_mode == "dark":
    ctk.set_appearance_mode("light")
    screen_mode = "light"

  else:
    ctk.set_appearance_mode("dark")
    screen_mode = "dark"
# WINDOW
root_window = ctk.CTk()

# DEFAULT SYSTEM SETTINGS
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root_window.geometry("720x480")
root_window.title("TODO APPLICATION")

# APP UI
title_label = ctk.CTkLabel(master=root_window, text="TODO APPLICATION",
                           font = ctk.CTkFont("AcmeFont", size=25))
title_label.pack(pady=20)

# SCROLLABLE FRAME
scrollable_frame = ctk.CTkScrollableFrame(master=root_window, width=500, height=300)
scrollable_frame.pack(pady=20)

# ENTRY WIDGET
input_widget = ctk.CTkEntry(master=scrollable_frame, placeholder_text="Add to do")
input_widget.pack(fill="x", padx=20)

# SUBMIT BUTTON
submit_button = ctk.CTkButton(master=root_window, text="ADD TO DO", command=add_to_do, width=200)
submit_button.pack(side="left", padx=100)

# SWITCH THEME BUTTON
switch_theme_button = ctk.CTkButton(master=root_window, text="SWITCH THEME", command=switch_theme, width=200)
switch_theme_button.pack(side="left")

# RUN APP
root_window.mainloop()