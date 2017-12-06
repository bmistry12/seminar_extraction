import re

class Ontology():
    def __init__(self) :
        self.histWords = ['history']
        self.chemWords = ['chemistry', 'elements']
        self.phyWords = ['physics', 'nasa', 'superposition', 'space']
        self.bioWords = ['biology', 'human']
        self.mathsWords = ['maths', 'mathematical', 'graphs']
        self.robWords = ['robot', 'robots', 'robotics', 'robotic',  'autonomou']
        self.aiWords = ['ai', 'machine', 'arfiticial', 'intelligence']
        self.hciWords = ['hci', 'human']
        self.visWords = ['vision']
        self.techWords = ['computing', 'programming', 'apple', 'technology', 'computer science', 'computer', 'algorithms']
        self.pureWords = ['engineering']
        self.talkWords = ['talk', 'talks', 'environmental']
        self.miscWords = []
        self.ontology = {
            'Top' : {
                "Arts": {
                    "History": self.histWords, 'talks': list()
                 },
                 "Engineering": {
                     "Computing": {
                        "Robotics": self.robWords, 'talks': list(),
                        "AI": self.aiWords, 'talks': list(),
                        "HCI": self.hciWords, 'talks': list(),
                        "Vision": self.visWords, 'talks': list(),
                        "General_computing": self.techWords, 'talks': list(),
                      },    
                     "Pure": self.pureWords, 'talks': list()
                 },
                 "Science": {
                     "Physics": self.phyWords, 'talks': list(),
                     "Biology": self.bioWords, 'talks': list(),
                     "Chemistry": self.chemWords, 'talks': list(),
                     "Mathematics": self.mathsWords, 'talks': list()
                 },
                 "Other": {
                      "Talks": self.talkWords, 'talks': list(),
                      "Misc": self.miscWords, 'talks': list()
                 }
             }
        }

def check (self, word) :
    if word in self.histWords :
        print("history")
    elif word in self.chemWords :
        print ("chemistry")
    elif word in self.phyWords :
        print ("physics")
    elif word in self.bioWords :
        print ("biology")
    elif word in self.mathsWords :
        print ("maths")
    elif word in self.robWords :
        print ("robotics")
    elif word in self.aiWords :
        print ("AI")
    elif word in self.hciWords :
        print ("HCI")
    elif word in self.visWords :
        print ("Vision")
    elif word in self.techWords :
        print ("Tech")
    elif word in self.pureWords :
        print ("Pure")
    elif word in self.talkWords :
        print ("Talks")
    else :
        print ("Misc")

def trasverse(self, location=None, key=None):
    if location is None :
        location = self.ontology
    keys = location.keys()
    if 'topic_words' in keys :
        self.traversal_info[key] = location[key]
        return
    for key in keys :
        self.traverse(location[key], key)
    return

def returnSecond(a) :
    toReturn = ""
    for val in a :
        dis, thisOne, dis2 = val
        toReturn = thisOne
    return thisOne
        
def openTextFile(self, tfid):
    tags = ["stime", "/stime", "<stime>", "</stime>","etime", "/etime", "<etime>", "</etime>", "sentence", "paragraph",
            "speaker", "location", "/sentence", "/paragraph", "/speaker", "/location", ">", "<", "<speaker>", "</speaker>",
            "<location>", "</location>", "<paragraph>", "</paragraph>", "<sentence>", "</sentence>"]
    typeReg = 'Type\s:\s([A-z]*.?){3}'
    topicReg = 'Topic\s:(\s)*(([A-z]*\s)*)'
    path = "my_seminars_tagged/" + str(tfid) + ".txt"
    with open (path, "r") as f :
        corpus = f.read()
        #print(corpus)
        print("----------------- " +str(tfid)+ " -----------------")
        a = re.findall(topicReg, corpus)
        if (a == []):
            pass;
        else :
            a = returnSecond(a)
            print(a)
            words = a.split(" ")
            for  word in words :
                print(word) 
                check(self, word.lower())
                print("-----")
        b = re.findall(typeReg, corpus)
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        etype =  str(b[0]).strip()
        emailType = ""
        #strip any random punctuation
        for char in etype:
            if char not in punctuations:
                emailType = emailType + char

        print(emailType)
        check (self, emailType.lower())
        print("-------- end of  " + str(tfid) + " ---------------")
'''
        a = corpus.split(" ")
        for word in a:
            if word not in tags :
                print(word + "\n")
'''

def main() :
    ontology = Ontology()
    notTagged = True
    textFile = 301
    while(notTagged) :
        openTextFile(ontology, textFile)
        if (textFile == 484) :
            notTagged = False
        else :
            textFile = textFile + 1
        
