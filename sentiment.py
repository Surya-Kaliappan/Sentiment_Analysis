from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tkinter import *

def clearAll():
    negativeField.config(state=NORMAL)
    negativeField.delete(0, END)
    negativeField.config(state=DISABLED)
    neutralField.config(state=NORMAL)
    neutralField.delete(0, END)
    neutralField.config(state=DISABLED)
    positiveField.config(state=NORMAL)
    positiveField.delete(0, END)
    positiveField.config(state=DISABLED)
    textArea.delete(1.0, END)
    overall.config(text="")

def detect_sentiment():
    negativeField.config(state=NORMAL)
    negativeField.delete(0,END)
    negativeField.config(state=DISABLED)
    neutralField.config(state=NORMAL)
    neutralField.delete(0,END)
    neutralField.config(state=DISABLED)
    positiveField.config(state=NORMAL)
    positiveField.delete(0,END)
    positiveField.config(state=DISABLED)
    sentence = textArea.get("1.0", "end")
    sentiment_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_obj.polarity_scores(sentence)
    negative = sentiment_dict['neg'] * 100
    string = str(negative)
    negativeField.config(state=NORMAL)
    negativeField.insert(10, string)
    negativeField.config(state=DISABLED)
    neutral = sentiment_dict['neu'] * 100
    string = str(neutral)
    neutralField.config(state=NORMAL)
    neutralField.insert(10, string)
    neutralField.config(state=DISABLED)
    positive = sentiment_dict['pos'] * 100
    string = str(positive)
    positiveField.config(state=NORMAL)
    positiveField.insert(10, string)
    positiveField.config(state=DISABLED)
    if sentiment_dict['compound'] >= 0.05:
        string = "Positive"
    elif sentiment_dict['compound'] <= -0.05:
        string = "Negative"
    else:
        string = "Neutral"

    if(positive==0 and negative==0 and neutral==0):
        project = ""
    else:
        project = "Overall Sentence is "+string
        
    overall.config(text=project)

if __name__ == "__main__":
    gui = Tk()
    gui.config(background="#008ECC")
    gui.title("VADER Sentiment Analyzer")
    gui.geometry("400x650")
    enterText = Label(gui, text="Enter Your Sentence: ",font="arial 15 bold",bg="#008ECC")
    negative = Label(gui, text="Negative Percentage: ", font="arial 15",bg="#008ECC")
    neutral = Label(gui, text="Nuetral Percentage: ", font="arial 15",bg="#008ECC")
    positive = Label(gui, text="Positive Percentage: ", font="arial 15",bg="#008ECC")
    overall = Label(gui, font="arial 15",bg="#008ECC")
    textArea = Text(gui, height=5, width=30, font="arial 15",  bg="#57A0D2")
    check = Button(gui, text="Check Sentiment", bg="#0F52BA", font=("arial", 12, "bold"), command=detect_sentiment)
    clear = Button(gui, text="Clear", bg="#0F52BA", font=("arial", 12, "bold"), command=clearAll)
    Exit = Button(gui, text="Exit", bg="#0F52BA", font=("arial", 12, "bold"), command=exit)

    negativeField = Entry(gui, font="arial 15",state=DISABLED);
    neutralField = Entry(gui, font="arial 15",state=DISABLED)
    positiveField = Entry(gui, font="arial 15",state=DISABLED)

    
    enterText.grid(row=0, column=2,pady=15)
    textArea.grid(row=1, column=2, padx=35, pady=10, sticky=W)
    check.grid(row=2, column=2, pady=10)
    negative.grid(row=3, column=2, pady=10)
    neutral.grid(row=5, column=2, pady=10)
    positive.grid(row=7, column=2, pady=10)
    overall.grid(row=9, column=2,pady=(30,0))
    negativeField.grid(row=4, column=2)
    neutralField.grid(row=6, column=2)
    positiveField.grid(row=8, column=2)
    clear.grid(row=10, column=2,padx=(0,120),pady=(20,0))
    Exit.grid(row=10, column=2,padx=(100,0),pady=(20,0))
    gui.mainloop()
