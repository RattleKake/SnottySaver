import os.path
import tkinter as tk
from tkinter import messagebox

# Main window
win_root = tk.Tk()
win_root.geometry("280x100")
win_root.resizable(False, False)
win_root.title("Snotty Saver")

# Initialize variable
character = tk.StringVar(win_root)
character.set("")
save_file_number = tk.IntVar()
save_file_number.set(1)

# region Save type selector
label_character = tk.Label(text="Character")
radiobutton_peppino = tk.Radiobutton(win_root, text="Peppino", variable=character, value="Peppino")
radiobutton_peppino.deselect()
radiobutton_thenoise = tk.Radiobutton(win_root, text="The Noise", variable=character, value="The Noise")
radiobutton_thenoise.deselect()

label_save_file_number = tk.Label(text="Save file")
radiobutton_save1 = tk.Radiobutton(win_root, text="Save 1", variable=save_file_number, value=1)
radiobutton_save1.deselect()
radiobutton_save2 = tk.Radiobutton(win_root, text="Save 2", variable=save_file_number, value=2)
radiobutton_save3 = tk.Radiobutton(win_root, text="Save 3", variable=save_file_number, value=3)


# endregion


# region Save editing
def edit_save_file():
    path_to_appdata = os.getenv("APPDATA")

    if character.get() == "Peppino": characterPathName = ""
    elif character.get() == "The Noise": characterPathName = "N"

    path_to_pizza_tower_save = os.path.join(path_to_appdata, 'PizzaTower_GM2', 'saves', ) + "\\saveData" + str(save_file_number.get()) + str(characterPathName) + ".ini"

    # Check if the file exists before doing anything
    if os.path.exists(path_to_pizza_tower_save):

        # Read the save
        with open(path_to_pizza_tower_save, "r") as file:
            data = file.read()

        # Edit data
        if data.find("snotty=\"1.000000\"") != -1:
            data = data.replace("snotty=\"1.000000\"", "snotty=\"0.000000\"")

            # Write to file
            with open(path_to_pizza_tower_save, "w") as file:
                file.write(data)

            # Let the user know changes has been made
            tk.messagebox.showinfo("Snotty saved", "Snotty has been saved.\n\nRemember that unlike video games, you cannot undo your actions.")

        # No changes are to be made
        else:
            tk.messagebox.showwarning("Snotty not dead.","It looks like Snotty hasn't been killed.\n\nNo changes are kneaded. Thank you for being a law-abiding citizen.")



    else:
        tk.messagebox.showerror("Save file not found.", "Save file not found. Have you started a game with this save?")


button_edit_save = tk.Button(win_root, text="Save Snotty!", command=edit_save_file)

# endregion


# region Pack everything
label_character.place(relx=0.0, rely=0.0)
radiobutton_peppino.place(relx=0, rely=0.2)
radiobutton_thenoise.place(relx=0, rely=0.4)

label_save_file_number.place(relx=0.3, rely=0)
radiobutton_save1.place(relx=0.3, rely=0.2)
radiobutton_save2.place(relx=0.3, rely=0.4)
radiobutton_save3.place(relx=0.3, rely=0.6)

button_edit_save.place(relx=0.6, rely=0.3)
# endregion


# Start the main window
win_root.mainloop()
