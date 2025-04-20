import tkinter as tk
from tkinter import Scrollbar, END, Canvas, Frame

# --- Bot Logic ---
def get_bot_response(msg):
    msg = msg.lower()
    responses = {
        "hi": "Hello there!",
        "hello": "Hi! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "what's your name": "I'm ChatBot, your virtual assistant.",
        "who made you": "I was created by a smart developer!",
        "what can you do": "I can answer simple questions and keep you company.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "bye": "Goodbye! Take care!",
        "thank you": "You're welcome!",
        "thanks": "Anytime!",
        "help": "Sure! Ask me anything, like 'what can you do' or 'tell me a joke'.",
        "what is the time": "I don't have a clock, but you can check your device 😉",
        "how does facial recognition work step by step": 
            "Facial recognition works by detecting a face in an image, analyzing its features (like eye spacing or jawline), converting these into a digital template, and comparing it to a database to find a match. It's like high-tech 'spot the difference'!",
        "what is machine learning": 
            "Machine learning is a type of AI where computers learn from data without being explicitly programmed. Think of it as teaching a child by showing examples instead of giving rigid rules!",
        "how many countries use facial recognition": 
            "Over 100 countries use facial recognition for security, law enforcement, or even payments. China and the U.S. are among the most active, but adoption varies widely.",
        "what is python programming": 
            "Python is a versatile, beginner-friendly programming language used for web development, data science, AI, and more. It's like the Swiss Army knife of coding!",
        "who created you": 
            "I was created by a team called team lossers"
    }
    return responses.get(msg, "Sorry, I didn't understand that.")

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern ChatBot")
        self.root.geometry("400x600")
        self.root.configure(bg="#ededed")

        # Header
        header = tk.Label(self.root, text="Chat me", bg="#075E54", fg="white", font=("Arial", 16, "bold"), pady=10)
        header.pack(fill=tk.X)

        # Chat area
        chat_frame = tk.Frame(self.root, bg="#f0f0f0")
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.chat_canvas = Canvas(chat_frame, bg="#f0f0f0", highlightthickness=0)
        scrollbar = Scrollbar(chat_frame, orient="vertical", command=self.chat_canvas.yview)
        self.chat_canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.messages_frame = Frame(self.chat_canvas, bg="#f0f0f0")
        self.chat_canvas.create_window((0, 0), window=self.messages_frame, anchor="nw")

        def on_configure(event):
            self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))

        self.messages_frame.bind("<Configure>", on_configure)

        # Entry
        entry_frame = tk.Frame(self.root, bg="#ededed")
        entry_frame.pack(fill=tk.X, pady=10, padx=10)

        self.entry_box = tk.Entry(entry_frame, font=("Arial", 13), width=25, bd=1, relief="flat")
        self.entry_box.pack(side=tk.LEFT, padx=(0, 10), ipady=6, fill=tk.X, expand=True)

        send_button = tk.Button(entry_frame, text="Send", command=self.send_message,
                                bg="#25D366", fg="white", font=("Arial", 11, "bold"), padx=10, pady=5)
        send_button.pack(side=tk.RIGHT)

        self.root.bind('<Return>', self.send_message)

    def add_message(self, msg, sender):
        msg_frame = Frame(self.messages_frame, bg="#f0f0f0")
        label = tk.Label(
            msg_frame,
            text=msg,
            bg="#DCF8C6" if sender == "user" else "#ffffff",
            font=("Arial", 12),
            wraplength=250,
            justify="left",
            anchor="w",
            padx=10,
            pady=5,
            bd=0,
            relief="solid"
        )
        label.pack(anchor="e" if sender == "user" else "w", padx=10, pady=2)
        msg_frame.pack(anchor="e" if sender == "user" else "w", fill="x", pady=2)
        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1.0)

    def send_message(self, event=None):
        msg = self.entry_box.get().strip()
        if msg == "":
            return
        self.entry_box.delete(0, END)
        self.add_message(msg, "user")
        self.root.after(500, lambda: self.add_message(get_bot_response(msg), "bot"))

# --- Run only if directly executed ---
if __name__ == "__main__":
    root = tk.Tk()
    app = Chatbot(root)
    root.mainloop()
