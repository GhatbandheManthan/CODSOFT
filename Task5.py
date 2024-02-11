import random
import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers with options
questions = {
    "What is the capital of France?": {
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    "Who wrote 'Romeo and Juliet'?": {
        "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"],
        "answer": "William Shakespeare"
    },
    "What is the chemical symbol for water?": {
        "options": ["H2O", "CO2", "O2", "CH4"],
        "answer": "H2O"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Mars", "Jupiter", "Saturn", "Venus"],
        "answer": "Mars"
    },
    "What is the tallest mammal in the world?": {
        "options": ["Giraffe", "Elephant", "Rhino", "Hippo"],
        "answer": "Giraffe"
    }
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.configure(bg="#e6e6e6")  # Set background color

        self.score = 0
        self.question_index = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#e6e6e6")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 12), bg="#4caf50", fg="white", padx=10, pady=5,
                               command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.question_index < len(questions):
            question, data = list(questions.items())[self.question_index]
            self.question_label.config(text=question)
            options = data["options"]
            random.shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
            self.correct_answer = data["answer"]
        else:
            self.display_final_results()

    def check_answer(self, choice_index):
        selected_option = self.option_buttons[choice_index].cget("text")
        if selected_option == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is: {self.correct_answer}")
        self.question_index += 1
        self.next_question()

    def display_final_results(self):
        messagebox.showinfo("Quiz Complete", f"Your score: {self.score} out of {len(questions)}")
        percentage = (self.score / len(questions)) * 100
        if percentage >= 70:
            messagebox.showinfo("Congratulations!", "Congratulations! You did a great job!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
