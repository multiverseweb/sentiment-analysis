import tkinter as tk
from tkinter import ttk

class SentimentAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analysis")

        # Create a label for status
        self.status_label = tk.Label(root, text="Select an option from the dropdown menu.")
        self.status_label.pack(pady=10)

        # Create the dropdown menu
        self.dropdown = ttk.Combobox(root, values=["Select Option", "Positive Sentiment", "Negative Sentiment", "Neutral Sentiment"])
        self.dropdown.current(0)  # Set default value
        self.dropdown.bind("<<ComboboxSelected>>", self.on_dropdown_change)
        self.dropdown.pack(pady=10)

    def on_dropdown_change(self, event):
        # Get the selected option
        selected_option = self.dropdown.get()

        # Call the respective function based on the selection
        if selected_option == "Positive Sentiment":
            self.positive_sentiment()
        elif selected_option == "Negative Sentiment":
            self.negative_sentiment()
        elif selected_option == "Neutral Sentiment":
            self.neutral_sentiment()

    def positive_sentiment(self):
        self.status_label.config(text="Positive sentiment analysis selected.")

    def negative_sentiment(self):
        self.status_label.config(text="Negative sentiment analysis selected.")

    def neutral_sentiment(self):
        self.status_label.config(text="Neutral sentiment analysis selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalysisApp(root)
    root.mainloop()
