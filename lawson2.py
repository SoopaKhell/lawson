# lawson2.py
# script I do work HOA through
# takes slide info from slides.py, gets assignments from canvas API
#
# COMMAND LINE ARGS
# none = normal, get today's slides from canvas and send to DayX.md
# s = summarize bullet summary line individually (without vim, will compile into vim after all lines are complete)
# a = summarize the entire slides and send it to bullets.md
# p = pull from bullets.md, output to DayX.md and edit with vim
#

import textwrap
import os
import readline
import re
import requests
import webbrowser
import pyperclip
from summarize_bullets import get_summary

from sys import argv

from slides import get_slide

# deprecated
#def isAppLine(s):
#    return re.match("", s) != None

def write(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

appIDs = {
    1: "(single sentence summary)",
    2: "(illustration)",
    3: "(8 line poem)",
    4: "(4-2-1 summary)",
    5: "(top hat organizer)",
    6: "(episode organizer)",
    7: "(movie script)",
    8: "(eulogy)",
    9: "(window notes)",
    10: "(least important bullet/fact)",
    11: "(table)",
    12: "(bullet summarization)",
    13: "(single sentence summary & illustration)",
    14: "(newspaper page on the events in this unit)",
    15: "(two-page report on an event in this unit)"
}

args = [x.strip("-") for x in argv if x.startswith("-") or x.startswith("--")]

token = ""
with open("token") as f:
    token = "access_token="+f.read().strip()

modulesURL = "https://hallco.instructure.com/api/v1/courses/61222/modules?"+token
modules = reversed(requests.get(modulesURL).json())

moduleID = ""
for module in modules:
    if module['items_count'] != 0:
        moduleID = str(module["id"])
        break

itemsURL = "https://hallco.instructure.com/api/v1/courses/61222/modules/"+moduleID+"/items?per_page=400&"+token

moduleItems = requests.get(itemsURL).json()

dayNum = None
for i, arg in enumerate(argv):
    if arg == "-n":
        dayNum = argv[i+1]
        break

if dayNum == None:
    latestItem = moduleItems[-1]
else:
    for item in moduleItems:
        if "Day "+str(dayNum) in item["title"]:
            latestItem = item
            break

latestAssignmentURL = latestItem["url"]
latestAssignment = requests.get(latestAssignmentURL+"?"+token).json()

try:
    title = latestAssignment["name"].replace("--", "—")
    desc = latestAssignment["description"].replace("--", "—")
except:
    print("failed on:", latestAssignment["url"])
    exit()

desc = desc.replace("\xa0", "")
desc = desc.replace("\xc2", "")
desc = desc.replace("\r", "")
desc = desc.replace("<p>", "")
desc = desc.replace("</p>", "")

desc = desc.split("\n")

desc = [re.sub("<.*?>", "", line) for line in desc if not line.startswith("Unit")]
desc = [re.sub("\d\.\s*", "", line) for line in desc]

apps = [line for line in desc if re.match("Slide \d+ App \d+", line) != None]

apps = [line.replace("Slide ", "") for line in apps]
apps = [line.replace("App ", "") for line in apps]

apps = [x.split(" ") for x in apps]

apps = [[int(app[0]), int(app[1])] for app in apps] # [slide, app]

fileString = "# "+title+"\n\n---"
fileName = title.replace(" ", "") + ".md"

for app in apps:
    appNum = app[1]
    fileString += "\n\n"
    fileString += "## Slide " + str(app[0]) + " " + appIDs[app[1]] + "\n\n"
    if appNum == 4:
        slideContent = get_slide(app[0], True).split("\n")
        slideTitle = slideContent[0]
        slideBullets = '\n'.join(slideContent[2:])
        fileString += slideTitle+"""

The **4** most important facts:

"""+slideBullets+"""

The **2** most important facts of those:


* This fact is important because 

* This fact is important because 

**The** most important fact:


* This fact is the most important because """
    elif appNum == 7:
        fileString += "\n"+get_slide(app[0], True)+"""

| Aspect | Content |
| ---------------- |
| Title         |  |
| Protaganist   |  |
| Antagonist    |  |
| Setting       |  |
| Plot          |  |
| Conflict      |  |
| Resolution    |  |
| Genre         |  |"""
    elif appNum == 11:
        fileString += get_slide(app[0], True)
        fileString += """

|  |  |
| --- |
|  |  |
|  |  |
|  |  |
|  |  |
"""
    elif appNum == 12:
        if "p" in args:
            summ = get_summary(app[0])
            fileString += summ+"\n"
        elif "s" in args:
            for x in [x for x in get_slide(app[0]).split("\n") if not x.startswith("###") and not x.strip() == ""]:
                os.system("clear")
                print(textwrap.fill(x.strip("\t").strip("* ").replace("()", ""), width=75))
                print()
                pyperclip.copy(x.strip("\t").strip("* ").replace("()", ""))
                if x.startswith("* "):
                    fileString += "* "
                elif x.startswith("\t* "):
                    fileString += "\t* "
                elif x.startswith("\t\t* "):
                    fileString += "\t\t* "

                fileString += input("""Summarize line:

""")+"\n"
                
                write(fileName, fileString) # autosave after input
        else:
            fileString += get_slide(app[0], True)+"\n"
    elif appNum == 1:
        if "s" in args:
            lines = get_slide(app[0], True)
            os.system("clear")
            print(textwrap.fill(lines, width=75))
            pyperclip.copy(lines)
            fileString += input("""SINGLE SENTENCE summary:

""")+"\n"
            write(fileName, fileString) # autosave after input
        else:
            fileString += get_slide(app[0], True)
    fileString += "\n---"

for line in desc:
    if "summar" in line.lower():
        apAssignment = line.replace(" ::: ", " SEPARATOR ")
        apAssignment = apAssignment.replace(" : ", " TITLESEP ")


        apAssignment = re.split(": ", apAssignment)

        firstTwo = apAssignment[0]+apAssignment[1]
        apAssignment = apAssignment[-1]

        apAssignment = apAssignment.replace(" SEPARATOR ", " ::: ")
        apAssignment = apAssignment.replace(" TITLESEP ", " : ")

        apAssignment = apAssignment.split(" ::: ")

        print(apAssignment)

        if "document" in (firstTwo).lower():
            fileString += "\n\n## Document Summaries (3 sentences each)\n\n"
            for document in apAssignment:
                if "s" in args:
                    os.system("clear")
                    print(textwrap.fill("### "+document+"\n", width=75))
                    print()
                    fileString += "### "+document+"\n\n"+input("""3 sentence document summary:

""")+"\n\n"
                    write(fileName, fileString) # autosave after input
                else:
                    fileString += "### "+document+"\n\n\n\n"
        elif "timeline" in (firstTwo).lower():
            fileString += "\n\n## Timeline Summary\n\n"
            for timeline in apAssignment:
                if "s" in args:
                    os.system("clear")
                    print(textwrap.fill("### "+timeline+"\n", width=75))
                    print()
                    fileString += "### "+timeline+"\n\n"+input("""Timeline event summary:

""")+"\n\n"
                    write(fileName, fileString) # autosave after input
                else:
                    fileString += "### "+timeline+"\n\n\n\n"
            fileString = fileString[:-1]
        else:
            fileString += "\n\n## Could not find AP assignment"
if apps == []: # no assignment / study guide
    for item in moduleItems:
        if "guide" in item["title"].lower():
            webbrowser.open_new_tab(item["html_url"])
            exit()
    fileString += "\n\n"+desc[0]
else:
    write(fileName, fileString) # final output
    os.system("aspell -c /home/carter/HOA/"+fileName)

#if "s" in args:
#    os.system("clear")
print(fileName)
