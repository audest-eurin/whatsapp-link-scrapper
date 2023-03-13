import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WhatsApp Link Scrapper")

        self.networks = ['Facebook', 'Twitter', 'LinkedIn']
        self.themes = ['Sport', 'Musique', 'Cuisine']

        self.network_var = tk.StringVar(value=self.networks[0])
        self.theme_var = tk.StringVar(value=self.themes[0])

        self.network_dropdown = tk.OptionMenu(self.root, self.network_var, *self.networks)
        self.theme_dropdown = tk.OptionMenu(self.root, self.theme_var, *self.themes)
        self.start_button = tk.Button(self.root, text="Démarrer", command=self.start)

        self.network_dropdown.pack()
        self.theme_dropdown.pack()
        self.start_button.pack()

    def start(self):
        network = self.network_var.get()
        theme = self.theme_var.get()
        # call the scraping function with the chosen network and theme

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
