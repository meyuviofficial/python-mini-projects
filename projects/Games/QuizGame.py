class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "What is CPU stands for?",
                "answer": "central processing unit",
            },
            {
                "question": "What is GPU stands for?",
                "answer": "graphical processing unit",
            },
            {"question": "What is RAM stands for?", "answer": "random access memory"},
            {"question": "What is ROM stands for?", "answer": "read only memory"},
            {
                "question": "Mouse is an input device or output device?",
                "answer": "input device",
            },
        ]

    def start(self):
        print
        print("Welcome To My Quiz Game")
        print("Interesting Game to Play")
        print

        player = input("Do you want to play the game? ")
        if player.lower() != "yes":
            print("Good Bye")
            quit()

        name_player = input("Enter Your Name: ")
        print("Let's Start the Game :) ", name_player)

        for question in self.questions:
            answer = input(question["question"] + "\n")
            if answer.lower() == question["answer"]:
                print("Correct")
                self.score += 1
            else:
                print("Wrong")

        print("You got the " + str(self.score) + " correct answers")
        print("You got the " + str((self.score / 5) * 100) + " correct answers")
        print("Good Bye")


if __name__ == "__main__":
    quiz = QuizGame()
    quiz.start()
