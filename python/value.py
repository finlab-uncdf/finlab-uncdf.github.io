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
ref_t = ""
prescheck_t = ""
fdcheck_t = ""
css = ""

def ulify(elements):
    string = "<ul>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ul>"
    return string

#def nstep(elements):
#    string = "<ul>\n"
#    for s in elements:
#        string += "<li>" + str(s) + "</li>\n"
#    string += "</ul>"
#    return string

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


def nstep(elements):
    string = ""
    for s in elements:
        string += """<div class="tool-step-segment">""" + str(s) + "</div>\n"
    string += ""
    string = string.replace('segment">', 'segment"> <span>')
    string = string.replace(':', ': </span>')
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
        ref_n = row[12]
        prescheck_n = row[13]
        fdcheck_n = row[14]

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
        ref.append(ref_n)
        prescheck.append(prescheck_n)
        fdcheck.append(fdcheck_n)
    
for index in range(1, len(name)):
#        print(step[index])
#        title_t = fques[index]
#        splitty = title_t.split('\n')
#        print(ulify(splitty))
        phase_t = phase[index]
        subphase_t = subphase[index]
        name_t = name[index]
        time_t = time[index]
        about_t = about[index]
        
        usecase_t = usecase[index]
        usecase_t = usecase_t.split('\n')
        usecase_t = ulify(usecase_t)
        
        limitation_t = limitation[index]
        
        under_t = under[index]
        under_t = under_t.split('\n')
        under_t = nunder(under_t)
        
        step_t = step[index]
        step_t = step_t.split('\n')
        step_t = nfhow(step_t)
        
        fhow_t = fhow[index]
        fhow_t = fhow_t.split('\n')
        fhow_t = nfhow(fhow_t)
        
        fques_t = fques[index]
        fques_t = fques_t.split('\n')
        fques_t = ulify(fques_t)
        
        ref_t = ref[index]
        ref_t = ref_t.split('\n')
        ref_t = ulify(ref_t)
        
        prescheck_t = prescheck[index]
        fdcheck_t = fdcheck[index]
        
        if phase_t == "STRATEGY, INNOVATION & IMPACT":
            css = "toolblue"
        elif phase_t == "HUMAN CENTERED DESIGN":
            css = "toolpurple"
        elif phase_t == "BEHAVIOURS & DESIGN":
            css = "toolgreen"
        elif phase_t == "NETWORK BUILDING":
            css = "toolred"
        
        f = open("../tools/"+name_t+".html",'w')
        
        if prescheck_t == "1":
            message = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	
	<meta http-equiv="x-ua-compatible" content="ie=edge">
	
	<title>UNCDF Toolkit | """+name_t+"""</title>
	
	<meta name="description" content="">
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<link rel="stylesheet" href="../css/"""+css+""".css">
</head>
<body>
	<div class="header-section">
		<div class="header-container">
			<h1><a href="../index.html">UNCDF Toolkit</a></h1>
			
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
						<h3><span>"""+phase_t+"""</span> | """+subphase_t+"""</h3>
						
						<h1>"""+name_t+"""</h1>
					</div>
					
					<div class="tool-about">
						<h2>About</h2>
						
						<p>"""+about_t+"""</p>
					</div>
					
					<div class="tool-use-case">
						<h2>Use Cases</h2>
						
						"""+usecase_t+"""
					</div>
					
					<div class="tool-limitations">
						<h2>Limitations</h2>
						
						<p>"""+limitation_t+"""</p>
					</div>
				</div>
				
				<div class="pres-down-grid">
					<div class="tool-card-image">
						<img src="../images/toolcard.png" alt="" />
					</div>
					
					<div class="download-buttons">
						<div class="download-link"><a href="/#" download="#">
												<button class="download-button">Download Tool!</button>
											</a></div>
										</div>
					</div>
				</div>
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
	
	<title>UNCDF Toolkit | """+name_t+"""</title>
	
	<meta name="description" content="">
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<link rel="stylesheet" href="../css/"""+css+""".css">
</head>
<body>
	<div class="header-section">
		<div class="header-container">
			<h1><a href="../index.html">UNCDF Toolkit</a></h1>
			
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
						<h3><span>"""+phase_t+"""</span> | """+subphase_t+"""</h3>
						
						<h1>"""+name_t+"""</h1>
						
						<p class="time">"""+time_t+"""</p>
					</div>
					
					<div class="tool-about">
						<h2>About</h2>
						
						<p>"""+about_t+"""</p>
					</div>
					
					<div class="tool-use-case">
						<h2>Use Cases</h2>
						
						"""+usecase_t+"""
					</div>
					
					<div class="tool-limitations">
						<h2>Limitations</h2>
						
						<p>"""+limitation_t+"""</p>
					</div>
				</div>
				
				<div class="tool-image-illustration">
					<img src="../images/"""+name_t+"""_illust.jpg" alt="" />
				</div>
			</div>
		</div>
	</div>
	
	<div class="under-section">
		<div class="under-container">
			<div class="under-grid">
				<div class="tool-under-image">
					<img src="../images/tool_small.png" alt="" />
				</div>
				
				<div class="tool-understand">
					<h2>Understand</h2>
					
					"""+under_t+"""
				</div>
				
				
				<div class="tool-steps">
					<div class="tool-step-grid">
						<div class="tool-step-segment-title">
							<h2>Step by Step</h2>
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
				<div class="f-intro-text">
					<h2>Facilitators Section</h2>
				</div>
				
				<div class="f-how-to">
					<h2>How to for Facilitators</h2>
					
					"""+fhow_t+"""
				</div>
				
				<div class="f-question-bank">
					<h2>Facilitators Question Bank</h2>
					
					"""+fques_t+"""
				</div>
			</div>
		</div>
	</div>
	<div class="down-section">
		<div class="down-container">
			<div class="down-grid">
				<div class="tool-card-image">
											<img src="../images/toolcard.png" alt="" />
											
											<div class="download-link"><a href="/#" download="#">
												<button class="download-button">Download Tool!</button>
											</a></div>
											
										</div>
										
										<div class="f-deck-image">
											<img src="../images/f-deck-image.jpg" alt="" />
											
											<div class="download-link"><a href="/#" download="#">
													<button class="download-button">Download Facilitation Slides!</button>
												</a></div>
											
										</div>
				
				<div class="reference-section">
					<h2>References</h2>
					
					"""+ref_t+"""
				</div>
			</div>
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
	
	<title>UNCDF Toolkit | """+name_t+"""</title>
	
	<meta name="description" content="">
	
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<link rel="stylesheet" href="../css/"""+css+""".css">
</head>
<body>
	<div class="header-section">
		<div class="header-container">
			<h1><a href="../index.html">UNCDF Toolkit</a></h1>
			
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
						<h3><span>"""+phase_t+"""</span> | """+subphase_t+"""</h3>
						
						<h1>"""+name_t+"""</h1>
						
						<p class="time">"""+time_t+"""</p>
					</div>
					
					<div class="tool-about">
						<h2>About</h2>
						
						<p>"""+about_t+"""</p>
					</div>
					
					<div class="tool-use-case">
						<h2>Use Cases</h2>
						
						"""+usecase_t+"""
					</div>
					
					<div class="tool-limitations">
						<h2>Limitations</h2>
						
						<p>"""+limitation_t+"""</p>
					</div>
				</div>
				
				<div class="tool-image-illustration">
					<img src="../images/"""+name_t+"""_illust.jpg" alt="" />
				</div>
			</div>
		</div>
	</div>
	
	<div class="under-section">
		<div class="under-container">
			<div class="under-grid">
				<div class="tool-under-image">
					<img src="../images/tool_small.png" alt="" />
				</div>
				
				<div class="tool-understand">
					<h2>Understand</h2>
					
					"""+under_t+"""
				</div>
				
				
				<div class="tool-steps">
					<div class="tool-step-grid">
						<div class="tool-step-segment-title">
							<h2>Step by Step</h2>
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
				<div class="f-intro-text">
					<h2>Facilitators Section</h2>
				</div>
				
				<div class="f-how-to">
					<h2>How to for Facilitators</h2>
					
					"""+fhow_t+"""
				</div>
				
				<div class="f-question-bank">
					<h2>Facilitators Question Bank</h2>
					
					"""+fques_t+"""
				</div>
			</div>
		</div>
	</div>
	<div class="down-section">
		<div class="down-container">
			<div class="down-grid">
				
				<div class="tool-card-image" style="grid-column-start: 1;
										grid-column-end: 3;">
											<img src="../images/toolcard.png" alt="" />
											
											<div class="download-link"><a href="/#" download="#">
												<button class="download-button">Download Tool!</button>
											</a></div>
										</div>
											
										</div>
				
				</div>
				
				<div class="reference-section">
					<h2>References</h2>
					
					"""+ref_t+"""
				</div>
			</div>
		</div>
	
	

</body>
</html>"""
            
        f.write(message)
        f.close()
