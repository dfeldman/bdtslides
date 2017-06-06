import csv,string

deck_template=open("deck-template.html").read()
speaker_slide_template=open('speaker-slide-template.html').read()
slides = ""
with open('input.csv','r') as csvfile:
   reader = csv.reader(csvfile, delimiter=',', quotechar='"')
   for row in reader: 
      row_d = {'title':row[3], 'speaker':row[5]+" "+row[6], 'starttime':row[9], 'room':row[8], 'group':row[7], 'img':row[2]}
      slides += speaker_slide_template.format(row_d)

print string.replace(deck_template, "{REPLACEWITHSLIDES}", slides + open("ad-slides.html").read())
