from tkinter import BOTH, LEFT
from typing import List

import ttkbootstrap as ttk
from PIL import Image

from core.model.ailiz_image import AilizImage


class Chooser:

    def __init__(self, images: List[AilizImage]):

        # Settaggio variabili di istanza
        self.images = images

        # Creazione finestra principale
        root = ttk.Window(
            title="Media organizer (Chooser)",
            themename="darkly",
            iconphoto="resources/logo1.png",
            size=(800, 680),
        )
        root.mainloop()
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=BOTH, expand=True)

        # Creazione variabili per GUI
        self.current_image_name = ttk.StringVar(value=None)
        self.current_image_path = ttk.StringVar(value=None)
        self.current_image_output_path = ttk.StringVar(value=None)
        self.current_image_index = ttk.IntVar(value=0)


        # Label per l'immagine (inizialmente vuota)
        self.image_label = ttk.Label(self.frame, textvariable=self.current_image_name, font=("Arial", 18))
        self.image_label.pack(pady=10)

        # Immagine
        self.image_preview = ttk.PhotoImage(
            name=self.current_image_name.get(),
            file=self.current_image_path.get(),
            height=480,
            width=854,
        )

        # Entry sotto l'immagine
        self.entry = ttk.Entry(self.frame)
        self.entry.pack(pady=10)

        # Tre pulsanti sotto l'entry
        self.button1 = ttk.Button(self.frame, text="Button 1", command=self.button1_action)
        self.button2 = ttk.Button(self.frame, text="Button 2", command=self.button2_action)
        self.button3 = ttk.Button(self.frame, text="Button 3", command=self.button3_action)

        self.button1.pack(side=LEFT, padx=10, pady=10)
        self.button2.pack(side=LEFT, padx=10, pady=10)
        self.button3.pack(side=LEFT, padx=10, pady=10)

    def next_image(self):
        image = Image.open("path/to/your/image.png")
        image = image.resize((200, 200), Image.ANTIALIAS)

    def button1_action(self):
        # Azione per il primo pulsante
        print("Button 1 pressed")

    def button2_action(self):
        # Azione per il secondo pulsante
        print("Button 2 pressed")

    def button3_action(self):
        # Azione per il terzo pulsante
        print("Button 3 pressed")