import csv,string

deck_template=open("deck-template.html").read()
speaker_slide_template=open('speaker-slide-template.html').read()
slides = ""
with open('input.csv','r') as csvfile:
   reader = csv.reader(csvfile, delimiter=',', quotechar='"')
   for row in reader: 
      row_d = {'title':row[0], 'speaker':row[1], 'starttime':row[2], 'room':row[3], 'group':row[4], 'img':row[5]}
      slides += speaker_slide_template.format(row_d)

print string.replace(deck_template, "{REPLACEWITHSLIDES}", slides + open("ad-slides.html").read())
