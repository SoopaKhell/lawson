# generates slide info from HOA.pdf via pdftotext

import re
from os import system
from os import remove
from os.path import exists

def get_text():
    if not exists("HOA.md"):
        #print("HOA.txt is missing, creating with pdftotext...")
        system("./pptx-convert")
        text = ""
        with open("HOA.md", "r") as f:
            text = f.read()
        return text
    else:
        #print("HOA.md found, using it")
        text = ""
        with open("HOA.md", "r") as f:
            text = f.read()
        return text


def get_slide(page, summarize=True):
    text = get_text()

    slides = text.split("\n\n---\n\n")

    try:
        slideText = slides[page-1]
    except IndexError:
        print("Slide {} does not exist.".format(page))
        exit()

    if len(slideText.split(" ")) <= 8:
        return "IMAGE SLIDE"

    #slideText = slideText.split("\n")
    
    slideText = "### " + slideText
    slideText = slideText.replace("\n", "\n\n", 1)

    slideText = re.sub("\d+ *$", "", slideText)

    if summarize:
        slideText = slideText.replace("United States", "US")
        slideText = slideText.replace("Great Britain", "GB")
        slideText = slideText.replace("Britain", "GB")

        slideText = slideText.replace("Confederacy", "CSA")
        slideText = slideText.replace("Confederate ", "CSA ")

        slideText = slideText.replace("Robert E. Lee", "Lee")
        slideText = slideText.replace("Jefferson Davis", "Davis")
        slideText = slideText.replace("Abraham Lincoln", "Lincoln")

        slideText = re.sub("(?i)America( |\.|$)", "the US ", slideText)
        slideText = re.sub("(?i)American troops", "US troops", slideText)
        slideText = slideText.replace(" U.S.", " US")
        slideText = slideText.replace(" U.S.A.", " US")
        slideText = slideText.replace(" USA", " US")
        
        slideText = slideText.replace("twice as many as", "2x")
        
        slideText = slideText.replace("had been", "was")
        slideText = slideText.replace("they was", "they were")

        slideText = slideText.replace("was not allowed to ", "couldn't ")
        slideText = slideText.replace("were not allowed to ", "couldn't ")
        
        slideText = slideText.replace(" number", " #")
        slideText = slideText.replace("number ", "# ")
        slideText = slideText.replace("Number ", "# ")

        slideText = slideText.replace("for example", "e.g.")
        slideText = slideText.replace("For example", "E.g.")
        
        slideText = slideText.replace("without", "w/o")
        slideText = slideText.replace("Without", "W/o")
        
        slideText = slideText.replace(" with ", " w/ ")
        slideText = slideText.replace("With ", "w/ ")

        slideText = slideText.replace("within", "w/i")
        slideText = slideText.replace("Within", "W/i")
        
        slideText = slideText.replace("although", "though")
        slideText = slideText.replace("Although", "Though")

        slideText = slideText.replace("first", "1st")
        slideText = slideText.replace("second", "2nd")
        slideText = slideText.replace("third", "3rd")
        slideText = slideText.replace("fourth", "4th")

        slideText = slideText.replace("First", "1st")
        slideText = slideText.replace("Second", "2nd")
        slideText = slideText.replace("Third", "3rd")
        slideText = slideText.replace("Fourth", "4th")
        
        slideText = slideText.replace("equal", "=")
        slideText = slideText.replace("Equal", "=")

        slideText = slideText.replace("continued", "cont.")
        
        slideText = slideText.replace("that would", "that'd")

        slideText = slideText.replace("estimated", "est.")
        
        slideText = slideText.replace("a series of", "many")
        slideText = slideText.replace("A series of", "Many")
        
        slideText = slideText.replace("largely", "")
        slideText = slideText.replace("Largely", "")

        slideText = slideText.replace("overly", "too")
        slideText = slideText.replace("far too", "too")

        slideText = slideText.replace("less than ", "<")
        slideText = slideText.replace(" Less than ", " <")

        slideText = slideText.replace("fewer than ", "<")
        slideText = slideText.replace(" Fewer than ", " <")

        slideText = slideText.replace("more than ", ">")
        slideText = slideText.replace(" More than ", " >")
        
        slideText = slideText.replace("greater than ", ">")
        slideText = slideText.replace(" Greater than ", " >")
        
        slideText = slideText.replace("they seemed to be", "were")
        slideText = slideText.replace("seemed to be", "was")
        
        slideText = slideText.replace("population", "pop.")
        slideText = slideText.replace("Population", "Pop.")
    
        slideText = slideText.replace("That is, ", "i.e. ")
        
        slideText = slideText.replace("because", "b/c")
        slideText = slideText.replace("Because", "b/c")

        slideText = re.sub("(?i)whether or not ", "whether ", slideText)

        slideText = re.sub("(?i)could not( |\.|$)", "couldn't ", slideText)
        slideText = re.sub("(?i)in order to( |\.|$)", "to ", slideText)
        slideText = re.sub("(?i)do not( |\.|$)", "don't ", slideText)
        slideText = re.sub("(?i)did not( |\.|$)", "didn't ", slideText)
        slideText = re.sub("(?i)cannot( |\.|$)", "can't ", slideText)
        slideText = re.sub("(?i)had the right to( |\.|$)", "could ", slideText)
        slideText = re.sub("(?i)didn't have the right to( |\.|$)", "couldn't ", slideText)
        slideText = re.sub("(?i)was able to( |\.|$)", "could ", slideText)
        slideText = re.sub("(?i)were able to( |\.|$)", "could ", slideText)
        slideText = re.sub("(?i)wasn't able to( |\.|$)", "couldn't ", slideText)
        slideText = re.sub("(?i)should not( |\.|$)", "shouldn't ", slideText)
        slideText = re.sub("(?i)should not( |\.|$)", "shouldn't ", slideText)
        
        slideText = re.sub("(?i)no one( |\.|$)", "nobody ", slideText)

        #slideText = re.sub(" \((.+?)\)", "", slideText)
        
        slideText = slideText.replace(" assisted ", " helped ")
        slideText = slideText.replace(" assist in ", " help ")

        slideText = slideText.replace("did damage to ", "damaged ")
        slideText = slideText.replace("did harm to ", "harmed ")
        slideText = slideText.replace("did harm to ", "harmed ")

        slideText = slideText.replace("Did damage to ", "damaged ")
        slideText = slideText.replace("Did harm to ", "harmed ")
        slideText = slideText.replace("Did harm to ", "harmed ")

        slideText = slideText.replace("In the course of ", "During ")
        slideText = slideText.replace(" in the course of ", "during ")

        slideText = slideText.replace("Within the course of ", "Over ")
        slideText = slideText.replace(" within the course of ", " over ")

        slideText = slideText.replace("In the process of ", "")
        slideText = slideText.replace(" in the process of ", " ")
        
        slideText = slideText.replace(" He would ", " He'd ")
        slideText = slideText.replace(" he would", " he'd")

        slideText = slideText.replace("would not", "wouldn't")

        slideText = slideText.replace(" he'd\n", " he would\n")
       
        slideText = slideText.replace(" made an effort", " tried")

        slideText = slideText.replace("Prior to ", "Before ")
        slideText = slideText.replace(" prior to ", " before ")

        slideText = slideText.replace("as a means to", "")

        slideText = slideText.replace(" as a matter of fact, ", " ")
        slideText = slideText.replace("As a matter of fact, ", "")

        slideText = slideText.replace("In fact, ", "")

        slideText = slideText.replace("As a result of", "Because of")
        slideText = slideText.replace("as a result of", "because of")

        slideText = slideText.replace("With the exception of ", "Except ")
        slideText = slideText.replace(" with the exception of ", " except ")

        slideText = slideText.replace("A large number of ", "Many ")
        slideText = slideText.replace(" a large number of ", "many ")

        slideText = slideText.replace("A majority of ", "Most ")
        slideText = slideText.replace(" a majority of ", "most ")
        
        slideText = slideText.replace("In the event that ", "If ")
        slideText = slideText.replace(" in the event that ", "if ")
        
        slideText = slideText.replace(" had the power to", " could")
        slideText = slideText.replace(" Had the power to", " Could")

        slideText = slideText.replace("in itself", "")
        slideText = slideText.replace("in and of itself", "")
        slideText = slideText.replace("In itself", "")
        slideText = slideText.replace("In and of itself", "")
        
        slideText = slideText.replace(" and ", " & ")

        slideText = slideText.replace("in light of the fact that", "because")
        slideText = slideText.replace("In light of the fact that", "Because")

        slideText = slideText.replace("in actuality, ", "")
        slideText = slideText.replace("In actuality, ", "")
        
        slideText = slideText.replace("in actuality ", "")
        slideText = slideText.replace("In actuality ", "")
        
        slideText = slideText.replace("can be seen as", "is")
        slideText = slideText.replace("Can be seen as", "Is")

        slideText = slideText.replace(" declared that ", " said ")
        slideText = slideText.replace(" stated that ", " said ")
        slideText = slideText.replace(" said that ", " said ")
        slideText = slideText.replace(" proclaimed that ", " said ")
        slideText = slideText.replace(" claimed that ", " said ")
        slideText = slideText.replace(" asserted that ", " said ")
        slideText = slideText.replace(" affirmed that ", " said ")
        slideText = slideText.replace(" states that ", " says ")
        
        slideText = slideText.replace("largely", "")
        slideText = slideText.replace("Largely, ", "")
        
        slideText = slideText.replace(" miles", " mi")
        
        slideText = slideText.replace(" not very many ", " few ")
        slideText = slideText.replace("Not very many ", "Few ")
        
        slideText = slideText.replace("was successful", "succeeded")
        
        slideText = slideText.replace("result in", "mean")
        
        slideText = slideText.replace("However, ", "")
        slideText = slideText.replace("At the least, ", "")
        slideText = slideText.replace("Although, ", "")
        slideText = slideText.replace("Nevertheless, ", "")
        slideText = slideText.replace("Still, ", "")
        
        slideText = slideText.replace("difficult ", "hard ")
        slideText = slideText.replace("difficult,", "hard,")
        slideText = slideText.replace("Difficult ", "Hard ")
        
        slideText = slideText.replace("somewhat", "kind of")
        
        slideText = slideText.replace("government", "gov")
        slideText = slideText.replace("Government", "Gov")
        
        slideText = slideText.replace("US Constitution", "Constitution")
        
        slideText = slideText.replace(" simply ", " ")
        slideText = slideText.replace(" simply ", " ")
        
        slideText = slideText.replace(" rapidly ", " quickly ")

        slideText = slideText.replace("approximately", "approx.")
        slideText = slideText.replace("as soon as possible", "ASAP")

        slideText = slideText.replace("As a whole, ", "")
        slideText = slideText.replace("as a whole ", "")
        
        slideText = slideText.replace(",000,000", " mil")
        slideText = slideText.replace(",000", "k")
        slideText = slideText.replace(",500", ".5k")
        slideText = slideText.replace("0000", "0k")
        slideText = slideText.replace("000", "k")

        slideText = slideText.replace("Supreme Court", "SCOTUS")
        
        slideText = re.sub("(b|B)y (January|February|March|April|May|June|July|August|Septempber|October|November|December) \d\d\d\d,?","",slideText)
        slideText = re.sub("(b|B)y (January|February|March|April|May|June|July|August|Septempber|October|November|December),?","",slideText)
        slideText = re.sub("(b|B)y \d\d\d\d,?","",slideText)
        
        slideText = re.sub("(i|I)n (January|February|March|April|May|June|July|August|Septempber|October|November|December) \d\d\d\d,?","",slideText)
        slideText = re.sub("(i|I)n (January|February|March|April|May|June|July|August|Septempber|October|November|December),?","",slideText)
        slideText = re.sub("(i|I)n \d\d\d\d,?","",slideText)

        slideText = re.sub("(o|O)n (January|February|March|April|May|June|July|August|Septempber|October|November|December) \d+,? (\d\d\d\d)?,?","",slideText)

        slideText = re.sub("\.$", "", slideText)

    slideText = slideText.replace(" * ", "\n* ")

    slideText = slideText.replace(" \n", "\n")

    slideText = slideText.replace(" .", ".")

    slideText = re.sub("[ \.\w]\*", "\n* ", slideText)

    slideText = slideText.replace(" *  ", " * ")
    slideText = re.sub(" +", " ", slideText)
    slideText = re.sub("\d{1,3}$", "", slideText)

    slideText = slideText.replace("\t*  ", "\t* ")

    slideText = slideText.replace("*", "* ")
    slideText = slideText.replace("  ", " ")

    lines = slideText.split("\n")
    newLines = []

    for line in lines:
        if not line.startswith("#"):
            newLine = re.sub(" \((.+?)\)", "", line)
            newLines.append(newLine)
        else:
            newLines.append(line)

    slideText = '\n'.join(newLines)

    return slideText.strip("\n")

def get_full_slides(summarize=True):
    fullText = ""
    for slideNum in range(1,get_text().count("\n---\n")+1):
        slideText = get_slide(slideNum, summarize)
        slideText = slideText.replace("### ", "")
        slideText = "### Slide "+str(slideNum)+": "+slideText+"\n\n---\n\n"
        fullText += slideText
    return fullText.strip("\n\n---\n\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "all":
            if len(sys.argv) == 3:
                if sys.argv[2].lower() == "false":
                    print(print_full_slides(False))
                else:
                    print(print_full_slides(True))
            else:
                print(print_full_slides(True))
        else:
            slideNum = int(sys.argv[1])
            if len(sys.argv) == 3:
                if sys.argv[2].lower() == "false":
                    print(get_slide(slideNum, False))
                else:
                    print(get_slide(slideNum, True))
            else:
                print(get_slide(slideNum, True))
