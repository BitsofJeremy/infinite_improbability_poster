import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import random
from dotenv import load_dotenv
import twit_it
import cast_it

load_dotenv()

class InfiniteImprobabilityPoster:
    def __init__(self, master):
        self.master = master
        master.title("Infinite Improbability Poster")
        master.geometry("600x500")
        self.set_theme()
        self.create_widgets()

    def set_theme(self):
        self.master.configure(bg='#1e1e1e')
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', foreground='#00ff00', background='#1e1e1e')
        style.configure('TButton', foreground='#00ff00', background='#3e3e3e')
        style.configure('TCheckbutton', foreground='#00ff00', background='#1e1e1e')
        style.map('TButton', background=[('active', '#4e4e4e')])

    def create_widgets(self):
        self.create_starfield()
        self.add_title()

        self.message_label = ttk.Label(self.master, text="Message:")
        self.message_label.pack(pady=5)
        self.message_input = tk.Text(self.master, height=5, width=60, bg='#2e2e2e', fg='#00ff00', insertbackground='#00ff00')
        self.message_input.pack(pady=5)

        self.char_count = ttk.Label(self.master, text="0/280")
        self.char_count.pack()
        self.message_input.bind('<KeyRelease>', self.update_char_count)

        self.platforms_frame = ttk.Frame(self.master, style='TLabel')
        self.platforms_frame.pack(pady=10)
        self.twitter_var = tk.BooleanVar()
        self.warpcast_var = tk.BooleanVar()
        ttk.Checkbutton(self.platforms_frame, text="Twitter", variable=self.twitter_var, style='TCheckbutton').pack(side=tk.LEFT)
        ttk.Checkbutton(self.platforms_frame, text="Warpcast", variable=self.warpcast_var, style='TCheckbutton').pack(side=tk.LEFT)

        self.image_button = ttk.Button(self.master, text="Add Image", command=self.select_image)
        self.image_button.pack(pady=5)
        self.image_label = ttk.Label(self.master, text="No image selected")
        self.image_label.pack()

        self.post_button = ttk.Button(self.master, text="Post", command=self.post_message)
        self.post_button.pack(pady=10)

        self.status_output = tk.Text(self.master, height=5, width=60, bg='#2e2e2e', fg='#00ff00', state='disabled')
        self.status_output.pack(pady=5)

    def create_starfield(self):
        self.canvas = tk.Canvas(self.master, bg='#1e1e1e', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_rectangle(0, 0, 600, 500, fill='#1e1e1e', outline='#1e1e1e')

        width = 600
        height = 500

        for _ in range(100):
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = 1 if random.random() > 0.1 else 2
            self.canvas.create_oval(x, y, x+size, y+size, fill='white', outline='white')

    def add_title(self):
        title_font = ('Courier', 24, 'bold')  # You can replace 'Courier' with a more sci-fi font if available
        self.canvas.create_text(300, 50, text="Infinite Improbability Poster",
                                font=title_font, fill='#00ff00')

    def update_char_count(self, event):
        count = len(self.message_input.get("1.0", 'end-1c'))
        self.char_count.config(text=f"{count}/280")

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
        if self.image_path:
            self.image_label.config(text=os.path.basename(self.image_path))
        else:
            self.image_label.config(text="No image selected")

    def post_message(self):
        message = self.message_input.get("1.0", 'end-1c')
        if not message:
            messagebox.showerror("Error", "Please enter a message to post.")
            return

        if self.twitter_var.get():
            self.post_to_twitter(message)
        if self.warpcast_var.get():
            self.post_to_warpcast(message)

    def post_to_twitter(self, message):
        print("Attempting to post to Twitter...")
        try:
            success = twit_it.send_tweet(message)
            if success:
                self.update_status("Posted to Twitter successfully!")
            else:
                self.update_status("Failed to post to Twitter.")
        except Exception as e:
            print(f"Error posting to Twitter: {str(e)}")
            self.update_status(f"Error posting to Twitter: {str(e)}")

    def post_to_warpcast(self, message):
        print("Attempting to post to Warpcast...")
        try:
            success = cast_it.send_cast(status=message)
            if success:
                self.update_status("Posted to Warpcast successfully!")
            else:
                self.update_status("Failed to post to Warpcast.")
        except Exception as e:
            print(f"Error posting to Warpcast: {str(e)}")
            self.update_status(f"Error posting to Warpcast: {str(e)}")

    def update_status(self, message):
        self.status_output.config(state='normal')
        self.status_output.insert(tk.END, message + "\n")
        self.status_output.config(state='disabled')
        self.status_output.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InfiniteImprobabilityPoster(root)
    root.mainloop()
