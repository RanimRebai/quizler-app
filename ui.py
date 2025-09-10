from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface :
    def __init__(self,quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizler")
        self.quiz_brain = quiz_brain


        self.window.configure(background=THEME_COLOR)

        self.score = Label(self.window, text=f"Score:{self.quiz_brain.score}", fg="white", bg=THEME_COLOR,font=("Arial", 17))
        self.score.grid(row=0, column=1,pady=20)


        self.canvas = Canvas(self.window ,bg="white",width=300,height=250 )
        self.canvasText = self.canvas.create_text(150,125, width=280, text="Question goes here", fill=THEME_COLOR, font=("Arial", 20, "bold"))

        self.canvas.grid(row=1, column=0,columnspan=2,padx=20,sticky="ew")

        self.image1 = PhotoImage(file="images/true.png")
        self.true = Button(self.window, image=self.image1,bg=THEME_COLOR,highlightthickness=0,
                           activebackground=THEME_COLOR,activeforeground=THEME_COLOR,
                           command=self.checkanswerTrue)
        self.true.grid(row=2, column=0,padx=20,pady=20)

        self.image = PhotoImage(file="images/false.png")
        self.false = Button(self.window, image=self.image,bg=THEME_COLOR,
                            highlightthickness=0,activebackground=THEME_COLOR,activeforeground=THEME_COLOR,
                            command=self.checkanswerFalse)
        self.false.grid(row=2, column=1,padx=20,pady=20)

        self.next_question()

        self.window.mainloop()
    def next_question(self):
        self.score.configure(text=f"Score:{self.quiz_brain.score}")
        self.canvas.config(bg="white")
        nextQuestion = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.canvasText, text=nextQuestion)
    def checkanswerTrue(self):
        trueOrFalse=self.quiz_brain.check_answer("True")
        self.answer(trueOrFalse)
    def checkanswerFalse(self):
        trueOrFalse=self.quiz_brain.check_answer("False")
        self.answer(trueOrFalse)
    def answer(self,answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

