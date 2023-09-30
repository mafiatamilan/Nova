import speech_recognition as sr

def Listen():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listensing...")
        r.pause_threshold=1
        audio = r.listen(source,0,2)

    try:
        print("reconizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said : {query}")

    except:
        return""

    query=str(query)
    return query.lower()

Listen() 
        