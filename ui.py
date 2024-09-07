import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text=f"Score: 0",foreground="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.question_canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            width=280,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true_button_clicked)
        self.true_button.grid(row=2, column=0)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.false_button_clicked)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.question_canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="End of the game")
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_clicked(self):
        self.give_feedback(self.quiz_brain.check_answer("true"))

    def false_button_clicked(self):
        self.give_feedback(self.quiz_brain.check_answer("false"))

    def give_feedback(self, answer_bool: bool):
        if answer_bool:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
