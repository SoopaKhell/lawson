import slides
import os

def write_summaries():

    summaryText = ""
    import readline
    readline.parse_and_bind('set editing-mode vi') 
    readline.parse_and_bind('set show-mode-in-prompt on')

    # for every slide
    for slideIndex, slide in enumerate(slides.get_full_slides().split("\n\n---\n\n")):
        for line in slide.split("\n"):
            if line.startswith("###"):
                summaryText += line+"\n\n"
            if not line.startswith("###") and not line.strip() == "":
                os.system("clear")
                print("Slide",slideIndex)
                print("---------\n")
                print(line.strip("\t").strip("* "))
                summaryText += line.split("* ")[0]+"* "+input("\nSummarize line: ") + "\n"
        summaryText += "\n\n---\n\n"

    with open("HOA_bullets.md", 'w') as f:
        f.write(summaryText.strip("\n\n---\n\n").replace("\n\n\n", "\n\n"))

def get_summary(slide):
    text = ""
    with open("HOA_bullets.md", 'r') as f:
        text = f.read()
    return text.split("\n\n---\n\n")[slide-1]

if __name__ == "__main__":
    write_summaries()
