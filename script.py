import csv,string,os

deck_template=open("deck-template.html").read()
speaker_slide_template=open('speaker-slide-template.html').read()
slides = ""
with open('input.csv','r') as csvfile:
   reader = csv.reader(csvfile, delimiter=',', quotechar='"')
   for row in reader: 
      extraclass=""
      speakers =( row[0] + " " + row[1]).replace(',',"<br/>")
      if (type(row[3])==type("") and len(row[3]) > 70): extraclass="smallbody"
      row_d = {'title':row[3], 'speaker':speakers, 'starttime':row[8], 'room':row[5], 'group':row[7], 'img':row[4], 'extraclass': extraclass}
      slides += speaker_slide_template.format(row_d)

ad_slide_template=open('ad-slide-template.html').read()
for row in os.listdir("logos"):
   slides += ad_slide_template.replace("{{LOGO}}", "logos/"+row)

print string.replace(deck_template, "{REPLACEWITHSLIDES}", slides + open("ad-slides.html").read())
