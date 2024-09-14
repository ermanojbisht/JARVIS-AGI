import tkinter as tk
from tkinter import ttk

from Julius import Julius

class JuliusUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Julius AI")

        # Create model selection dropdown
        self.model_label = tk.Label(root, text="Select Model:")
        self.model_label.pack()
        self.model_var = tk.StringVar()
        self.model_dropdown = ttk.Combobox(root, textvariable=self.model_var)
        self.model_dropdown['values'] = Julius.AVAILABLE_MODELS
        self.model_dropdown.current(Julius.AVAILABLE_MODELS.index('Gemini Flash'))  # Set default value

        self.model_dropdown.pack()

        # Create prompt input field
        self.prompt_label = tk.Label(root, text="Enter Prompt:")
        self.prompt_label.pack()
        self.prompt_entry = tk.Text(root, height=10, width=200)
        self.prompt_entry.pack()

        # Create stream checkbox
        self.stream_var = tk.BooleanVar()
        self.stream_checkbox = tk.Checkbutton(root, text="Stream Response", variable=self.stream_var)
        self.stream_checkbox.pack()

        # Create raw checkbox
        self.raw_var = tk.BooleanVar()
        self.raw_checkbox = tk.Checkbutton(root, text="Return Raw Response", variable=self.raw_var)
        self.raw_checkbox.pack()

        # Create chat button
        self.chat_button = tk.Button(root, text="Chat", command=self.chat)
        self.chat_button.pack()

        # Create response text field
        self.response_label = tk.Label(root, text="Response:")
        self.response_label.pack()
        self.response_text = tk.Text(root, height=10, width=200)
        self.response_text.pack()

    def chat(self):
        model = self.model_var.get()
        prompt = self.prompt_entry.get("1.0", "end-1c")
        stream = self.stream_var.get()
        raw = self.raw_var.get()

        ai = Julius(model=model)
        response = ai.chat(prompt, stream)

        if stream:
            for chunk in response:
                self.response_text.insert("end", chunk)
        else:
            self.response_text.insert("end", response)

if __name__ == "__main__":
    root = tk.Tk()
    ui = JuliusUI(root)
    root.mainloop()