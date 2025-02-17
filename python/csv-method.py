#coding=utf-8
import os.path
import csv

phase_t = ""
subphase_t = ""
name_t = ""
about_t = ""
limitation_t = ""
time_t = ""
usecase_t = ""
step_t = ""
under_t = ""
fhow_t = ""
fques_t = ""
prescheck_t = ""
fdcheck_t = ""
css = ""
link_t = ""
linkname_t = ""

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def ulify(elements):
    string = "<ul>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ul>"
    return string

def nfhow(elements):
    string = "<ol>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ol>"
    string = string.replace('<li>', '<li><span>')
    string = string.replace(':', ':</span>')
    return string

def nunder(elements):
    string = "<ul>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ul>"
    string = string.replace('‘', '‘<span>')
    string = string.replace('’', '</span>’')
    return string

with open('uncdf.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    phase = []
    subphase = []
    name = []
    about = []
    limitation = []
    time = []
    usecase = []
    step = []
    under = []
    fhow = []
    fques = []
    ref = []
    prescheck = []
    fdcheck = []
    link = []
    linkname = []
    
    for row in readCSV:
        phase_n = row[1]
        subphase_n = row[2]
        name_n = row[3]
        about_n = row[4]
        limitation_n = row[5]
        time_n = row[6]
        usecase_n = row[7]
        step_n = row[8]
        under_n = row[9]
        fhow_n = row[10]
        fques_n = row[11]

        prescheck_n = row[12]
        fdcheck_n = row[13]
        link_n = row[14]
        linkname_n = row[15]

        phase.append(phase_n)
        subphase.append(subphase_n)
        name.append(name_n)
        about.append(about_n)
        limitation.append(limitation_n)
        time.append(time_n)
        usecase.append(usecase_n)
        step.append(step_n)
        under.append(under_n)
        fhow.append(fhow_n)
        fques.append(fques_n)

        prescheck.append(prescheck_n)
        fdcheck.append(fdcheck_n)
        
        link.append(link_n)
        linkname.append(linkname_n)
    
for index in range(2, len(name)):
        phase_t = phase[index]
        subphase_t = subphase[index]
        name_t = name[index]
        time_t = time[index]
        about_t = about[index]
        
        usecase_t = usecase[index]
        usecase_t = usecase_t.split('\n')
        usecase_t = nonblank_lines(usecase_t)
        usecase_t = ulify(usecase_t)
        
        limitation_t = limitation[index]
        
        under_t = under[index]
        under_t = under_t.split('\n')
        under_t = nonblank_lines(under_t)
        under_t = nunder(under_t)
        
        step_t = step[index]
        step_t = step_t.split('\n')
        step_t = nonblank_lines(step_t)
        step_t = nfhow(step_t)
        
        fhow_t = fhow[index]
        fhow_t = fhow_t.split('\n')
        fhow_t = nonblank_lines(fhow_t)
        fhow_t = nfhow(fhow_t)
        
        fques_t = fques[index]
        fques_t = fques_t.split('\n')
        fques_t = nonblank_lines(fques_t)
        fques_t = ulify(fques_t)
        
        prescheck_t = prescheck[index]
        fdcheck_t = fdcheck[index]
        
        link_t = link[index]
        linkname_t = linkname[index]
        
        if phase_t == "STRATEGY, INNOVATION & IMPACT":
            css = "toolblue"
        elif phase_t == "HUMAN CENTERED DESIGN":
            css = "toolpurple"
        elif phase_t == "BEHAVIOUR DESIGN":
            css = "toolgreen"
        elif phase_t == "NETWORK BUILDING":
            css = "toolred"
        
        f = open("../tool-pages/"+name_t+".html",'w')
        
        if prescheck_t == "1":
            message = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	
	<title>"""+name_t+"""</title>
	
	<meta name="description" content="">
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<link rel="stylesheet" href="../files/css/"""+css+""".css">
</head>
<body>
	<div class="header-section">
		<div class="header-container">
			<h1><a href="../index.html">The FinLab Toolkit</a></h1>
			
						<div class="header-links">
				<div class="header-link"><a href="../index.html">
					<button class="header-button">Back</button>
				</a></div>
			</div>
		</div>
	</div>
	
	<div class="tool-section">
		<div class="tool-container">
			<div class="tool-grid">
				<div class="tool-name">
					<div class="tool-name-text">
						<h3><span>"""+phase_t+""" |</span> """+subphase_t+"""</h3>
						
						<h1>"""+name_t+"""</h1>
					</div>
					
					<div class="tool-about">
						
						<p>"""+about_t+"""</p>
					</div>
					
					<div class="tool-use-case">
						<h2>USE CASES</h2>
						
						"""+usecase_t+"""
					</div>
					
					<div class="tool-limitations">
						<h2>LIMITATIONS</h2>
						
						<p>"""+limitation_t+"""</p>
					</div>
                     <a class="linkin "href=" """+link_t+""" " target="_blank" style="margin-left: 0;">"""+linkname_t+"""</a>
                   
				</div>
				
				<div class="pres-down-grid">
					<div class="tool-card-image">
					</div>
					
					<div class="download-buttons">
						<div class="download-link"><a href="../files/tools/decks/"""+name_t+"""_FacilitationDeck.pptx" download=" """+name_t+"""_FacilitationDeck.pptx">
												<button class="download-button">Download """+name_t+"""!</button>
											</a></div>
										</div>
					</div>
				</div>
			</div>
		</div>
        <div class="footer-section">
		<div class="header-container">
			<p>&copy; Copyright 2019, UNCDF. All rights reserved.</p>
		</div>
	</div>
</body>
</html>"""
        elif fdcheck_t == "1":
            message = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	
	<title>"""+name_t+"""</title>
	
	<meta name="description" content="">
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<link rel="stylesheet" href="../files/css/"""+css+""".css">
</head>
<body>
	<div class="header-section">
		<div class="header-container">
			<h1><a href="../index.html">The FinLab Toolkit</a></h1>
			
						<div class="header-links">
				<div class="header-link"><a href="../index.html">
					<button class="header-button">Back</button>
				</a></div>
			</div>
		</div>
	</div>
	
	<div class="tool-section">
		<div class="tool-container">
			<div class="tool-grid">
				<div class="tool-name">
					<div class="tool-name-text">
						<h3><span>"""+phase_t+""" |</span> """+subphase_t+"""</h3>
						
						<h1>"""+name_t+"""</h1>
						
						<p class="time">"""+time_t+"""</p>
					</div>
					
					<div class="tool-about">
						
						<p>"""+about_t+"""</p>
					</div>
					
					<div class="tool-use-case">
						<h2>USE CASES</h2>
						
						"""+usecase_t+"""
					</div>
					
					<div class="tool-limitations">
						<h2>LIMITATIONS</h2>
						
						<p>"""+limitation_t+"""</p>
					</div>
				</div>
				<div class="tool-image-illustration">
					<img src="../files/illustrations/"""+name_t+"""_illust.png" alt="" />
                    <a class="linkin "href=" """+link_t+""" " target="_blank">"""+linkname_t+"""</a>
				</div>
			</div>
		</div>
	</div>
	
	<div class="under-section">
		<div class="under-container">
			<div class="under-grid">
				<div class="tool-under-image">
<img src="../files/illustrations/"""+name_t+"""_toolcard.png" alt="" />
</div>
				
				<div class="tool-understand">
					<h2>UNDERSTANDING THE TOOL</h2>
					
					"""+under_t+"""
				</div>
				
				
				<div class="tool-steps">
					<div class="tool-step-grid">
						<div class="tool-step-segment-title">
							<h2>STEP BY STEP</h2>
						</div>
						
						"""+step_t+"""
					</div>
				</div>
			</div>
		</div>
	</div>
    <div class="f-section">
		<div class="f-container">
			<div class="f-grid">
				
				<div class="f-how-to">
					<h2><span>HOW TO</span> FOR FACILITATORS</h2>
					
					"""+fhow_t+"""
				</div>
				
				<div class="f-question-bank">
					<h2>FACILITATORS QUESTION BANK</h2>
					
					"""+fques_t+"""
				</div>
			</div>
		</div>
	</div>
	<div class="down-section">
		<div class="down-container">
			<div class="down-grid">
				<div class="tool-card-image">
											
											<div class="download-link"><a href="../files/tools/toolcards/"""+name_t+""".pptx" download=" """+name_t+""".pptx">
												<button class="download-button">Download """+name_t+"""!</button>
											</a></div>
											
										</div>
										
										<div class="f-deck-image">
											
											
											<div class="download-link"><a href="../files/tools/decks/"""+name_t+"""_FacilitationDeck.pptx" download=" """+name_t+"""_FacilitationDeck.pptx">
													<button class="download-button">Download Facilitation Slides!</button>
												</a></div>
											
										</div>	
			</div>
		</div>
	</div>
    <div class="footer-section">
		<div class="header-container">
			<p>&copy; Copyright 2019, UNCDF. All rights reserved.</p>
		</div>
	</div>
	
</body>
</html>"""
        else:
            message = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	
	<title>"""+name_t+"""</title>
	
	<meta name="description" content="">
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<link rel="stylesheet" href="../files/css/"""+css+""".css">
</head>
<body>
	<div class="header-section">
		<div class="header-container">
			<h1><a href="../index.html">The FinLab Toolkit</a></h1>
			
						<div class="header-links">
				<div class="header-link"><a href="../index.html">
					<button class="header-button">Back</button>
				</a></div>
			</div>
		</div>
	</div>
	
	<div class="tool-section">
		<div class="tool-container">
			<div class="tool-grid">
				<div class="tool-name">
					<div class="tool-name-text">
						<h3><span>"""+phase_t+""" |</span> """+subphase_t+"""</h3>
						
						<h1>"""+name_t+"""</h1>
						
						<p class="time">"""+time_t+"""</p>
					</div>
					
					<div class="tool-about">						
						<p>"""+about_t+"""</p>
					</div>
					
					<div class="tool-use-case">
						<h2>USE CASES</h2>
						
						"""+usecase_t+"""
					</div>
					
					<div class="tool-limitations">
						<h2>LIMITATIONS</h2>
						
						<p>"""+limitation_t+"""</p>
					</div>
				</div>
				<div class="tool-image-illustration">
					<img src="../files/illustrations/"""+name_t+"""_illust.png" alt="" />
                                        <a class="linkin "href=" """+link_t+""" " target="_blank">"""+linkname_t+"""</a>

				</div>
			</div>
		</div>
	</div>
	
	<div class="under-section">
		<div class="under-container">
			<div class="under-grid">
				<div class="tool-under-image">
<img src="../files/illustrations/"""+name_t+"""_toolcard.png" alt="" />
				</div>
				
				<div class="tool-understand">
					<h2>UNDERSTANDING THE TOOL</h2>
					
					"""+under_t+"""
				</div>
				
				
				<div class="tool-steps">
					<div class="tool-step-grid">
						<div class="tool-step-segment-title">
							<h2>STEP BY STEP</h2>
						</div>
						
						"""+step_t+"""
					</div>
				</div>
				
				
			</div>
		</div>
	</div>
    <div class="f-section">
		<div class="f-container">
			<div class="f-grid">
				
				<div class="f-how-to">
					<h2><span>HOW TO</span> FOR FACILITATORS</h2>
					
					"""+fhow_t+"""
				</div>
				
				<div class="f-question-bank">
					<h2>FACILITATORS QUESTION BANK</h2>
					
					"""+fques_t+"""
				</div>
			</div>
		</div>
	</div>
	<div class="down-section">
		<div class="down-container">
			<div class="down-grid">
				
				<div class="tool-card-image" style="grid-column-start: 1;
										grid-column-end: 2;">
											
											
											<div class="download-link"><a href="../files/tools/toolcards/"""+name_t+""".pptx" download=" """+name_t+""".pptx">
												<button class="download-button">Download """+name_t+"""!</button>
											</a></div>
										</div>
										</div>
				</div>
			</div>
		</div>
        <div class="footer-section">
		<div class="header-container">
			<p>&copy; Copyright 2019, UNCDF. All rights reserved.</p>
		</div>
	</div>
</body>
</html>"""
            
        f.write(message)
        f.close()