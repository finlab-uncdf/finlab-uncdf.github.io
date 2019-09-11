#coding=utf-8
import os.path
import gspread

test = []

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

from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('uncdf-doc.json', scope)
client = gspread.authorize(creds)
sheet = client.open('UNCDF Toolsite Backend').sheet1
test = sheet.get_all_values()

#print(test[5][2])
        
for index in range(2, len(test)):

        phase_t = test[index][1]
        subphase_t = test[index][2]
        name_t = test[index][3]
        about_t = test[index][4]
        limitation_t = test[index][5]
        time_t = test[index][6]
                
        usecase_t = test[index][7]
        usecase_t = usecase_t.split('\n')
        usecase_t = ulify(usecase_t)
        
        step_t = test[index][8]
        step_t = step_t.split('\n')
        step_t = nfhow(step_t)
        
        under_t = test[index][9]
        under_t = under_t.split('\n')
        under_t = nunder(under_t)
        
        
        fhow_t = test[index][10]
        fhow_t = fhow_t.split('\n')
        fhow_t = nfhow(fhow_t)
        
        fques_t = test[index][11]
        fques_t = fques_t.split('\n')
        fques_t = ulify(fques_t)
        
        
        prescheck_t = test[index][12]
        fdcheck_t = test[index][13]
        link_t = test[index][14]
        linkname_t = test[index][15]
                
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
                    <a class="linkin "href=" """+link_t+""" " target="_blank">"""+linkname_t+"""</a>

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
                    <a class="linkin "href=" """+link_t+""" " target="_blank">"""+linkname_t+"""</a>
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
				
				
                
			</div>
		</div>
	
	
</body>
</html>"""
            
        f.write(message)
        f.close()