allInfo = {}

def write_resume_to_html():
    print("Type things in the format that you would like them on your resume!")
    yourname = input("What is your name? \n")
    allInfo["Your name"] = yourname
    new_section()

def new_section():
    print("\nNew section! \n")
    name = input("What section would you like to add to your resume?\n")
    name = name.strip()
    experiences = input("How many experiences would you like to put into this section? (input an intiger value) \n")
    try:
        experiences = int(experiences.strip())
    except:
        experiences = 1
    allInfo[name] = {}
    while experiences > 0:
        new_experience(name)
        experiences -= 1
    next()

def new_experience(section_name):
    print("\nNew experience! \n")
    name = input("What would you like to title this experience?\n")
    name = name.strip()
    allInfo[section_name][name] = {}
    allInfo[section_name][name]["Name"] = name
    company = input("What company/organization was this experience with? \n")
    company = company.strip()
    allInfo[section_name][name]["Company"] = company
    timeframe = input("What timeframe was this experience in? \n")
    timeframe = timeframe.strip()
    allInfo[section_name][name]["Timeframe"] = timeframe
    location = input("Where did this experience occur? \n")
    location = location.strip()
    allInfo[section_name][name]["Location"] = location
    descriptions = input("How many description bullet points would you like to put into this experience? (input an intiger value) \n")
    try:
        descriptions = int(descriptions.strip())
    except:
        descriptions = 1
    alist = []
    while descriptions > 0:
        alist.append(new_description())
        descriptions -= 1
    allInfo[section_name][name]["Descriptions"] = alist

def new_description():
    print("\nNew description! \n")
    description = input("What would you like this description of your experience to say? \n")
    return description

def to_html():
    #try:
        print(allInfo)
        file = input("What file would you like to put the html code into? (include .html at the end) \n")
        file = file.strip()
        with open(file, 'w') as outfile:
            outfile.write("<!DOCTYPE html>\n")
            outfile.write("<html>\n")
            outfile.write("    <BODY>\n")
            outfile.write("        <h1>" + allInfo["Your name"] + "</h1>\n")
            for section in allInfo:
                if section != "Your name":
                    outfile.write("        <h2>" + section + "</h2>\n")
                    for activity in allInfo[section]:
                        for part in allInfo[section][activity]:
                            if part == "Name":
                                outfile.write("        <h3>" + allInfo[section][activity][part] + "</h3>\n")
                            elif part == "Descriptions":
                                outfile.write("        <ol>\n")
                                for item in allInfo[section][activity][part]:
                                    outfile.write("            <li>" + item + "</li>\n")
                                outfile.write("        </ol>\n")
                            else:
                                outfile.write("        <p>" + allInfo[section][activity][part] + "</p>\n")
            outfile.write("    </body>\n")
            outfile.write("<html>\n")
    #except:
        #print("There may be an issue with your filename!")



def next():
    state = input("Would you like to add another section? (y/n) \n")
    state = state.strip().lower()
    if state == "y":
        new_section()
    else:
        to_html()
    

print(write_resume_to_html())