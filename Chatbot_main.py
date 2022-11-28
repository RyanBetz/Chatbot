#create python class for chatbot
def Chatbot():
    def __init__(question, answer, self=None):
        self.question = question
        self.answer = answer
    def get_question(self):
        return self.question
    def get_answer(self):
        return self.answer
    def set_question(self, question):
        self.question = question
    def set_answer(self, answer):
        self.answer = answer
    def __str__(self):
        return "Question: " + self.question + " Answer: " + self.answer
#main function
def main():
    #create a list of chatbot objects
    chatbot_list = []
    #open the file
    chatbot_file = open("chatbot.txt", "r")
    #read the file
    for line in chatbot_file:
        #split the line into question and answer
        question, answer = line.split(",")
        #create a chatbot object
        chatbot = Chatbot(question, answer)
        #add the chatbot object to the list
        chatbot_list.append(chatbot)
    #close the file
    chatbot_file.close()
    #get user input
    user_question = input("Enter a question: ")
    #search for the question in the list
    for chatbot in chatbot_list:
        if user_question == chatbot.get_question():
            print(chatbot.get_answer())
            break
    else:
        print("I don't know the answer to that question.")



