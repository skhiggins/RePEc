# This Python file uses the following encoding: utf-8

# AUTOMATE PREPARATION OF PAPER FOR WORKING PAPER SERIES
# Sean Higgins
# Created 16sep2015
# Edited  21jul2016

# INPUT INFORMATION ABOUT THE PAPER HERE #
# ########################## BEGIN USER INPUT ####################################
base = 'C:/Dropbox/RePEc' # change to the path of the shared RePEc folder 
						  #  if using a different computer
wpnum = '1604' # Working paper number
authors = 2 # Number of authors
Title = 'Towards an Understanding of the Political Economy of Multidimensional Poverty Measurement'
Month = 'May 2016' # DO NOT abbreviate month name
OriginalMonth = '' # LEAVE AS BLANK (i.e., '') unless revised verison of paper
# AUTHORS
# Add additional authors as necessary, and be sure to edit "authors =" above
# e.g. to add a third author change the line authors = 2 to authors = 3 and add here:
# Author3 = '...'
# Affiliation3 = '...'
# Email3 = '...'
# (removing the # which marks a comment)
Author1 = 'Stefano Barbieri'
FirstName1 = 'Stefano' # still need to automate this part
LastName1  = 'Barbieri'
Affiliation1 = 'Department of Economics, Tulane University'
Email1 = 'sbarbier@tulane.edu'
Author2 = 'Sean Higgins'
FirstName2 = 'Sean' # still need to automate this part
LastName2  = 'Higgins'
Affiliation2 = 'Department of Economics, Tulane University'
Email2 = 'shiggins@tulane.edu'
# ABSTRACT
# Use Latex syntax for special formatting: \emph{for italics}, \textbf{for bold}, etc.
Abstract = "Does adopting a multidimensional poverty index lead to higher government spending on the poor? If so, why? And how does it affect the allocation of government budgets across ministers? We answer these questions in a game-theoretic framework that accounts for the strategic interactions between government agents. Government ministers---such as the education, health, and housing ministers---share a common interest in reducing measured poverty; adopting a multidimensional measure may induce them to spend more on the poor since they can now directly impact measured poverty, whereas they have little short-run impact on, say, a unidimensional income poverty measure. Because an improvement in the scalar multidimensional poverty index is a public good for ministers, however, they can also free ride on each other's antipoverty spending. Despite introducing free riding, a multidimensional measure usually leads to an increase in total antipoverty spending. In addition to incentivizing ministers to spend resources to reduce measured poverty and thereby increase prestige for all government members, the multidimensional measure creates a new set of policy tools that serve as levers affecting total spending on the poor: dimension weights in the index and resource allocations across ministers. In the use of these tools, a conflict arises between maximizing reductions in measured poverty and maximizing equilibrium antipoverty spending; its resolution depends on whether the authority deciding weights and the authority allocating budgets have the same or opposing incentives. We illustrate using data from Mexico, the first country to adopt an official multidimensional poverty measure."
# KEYWORDS AND JEL CODES
# Will appear on cover page and in RePEc exactly as typed below
Keywords = 'Multidimensional poverty, free riding, public good games, poverty measurement'
JELcodes = 'C72, H41, I32'
# ######################### END USER INPUT #######################################

# ONLY EDIT THE REST IF YOU KNOW PYTHON 

# ##########
# PACKAGES #
# ##########
import re # regular expressions
import os # for shell commands like change directory
from time import strptime # to convert name of month to integer

# ########
# LOCALS #
# ########
if 'r' in wpnum:
	is_revised = 1
	month_ = "OriginalMonth"
else:
	is_revised = 0
	month_ = "Month"
years = re.match(r'.*([0-9]{4})',locals()[month_])
myyear = years.group(1)
wpnum_nor = re.sub('r','',wpnum)
if is_revised==1:
	revyears = re.match(r'.*([0-9]{4})',Month)
	revyear = revyears.group(1)

# #############
# DIRECTORIES #
# #############
inputs = base + '/pdf/' + myyear + '/inputs'
outputs = base + '/python_code/outputs'
scrape = base + '/tul/wpaper'
pdfs = base + '/pdf'

# ######################
# PRELIMINARY PROGRAMS #
# ######################
# Function to get rid of Latex formating
def delatexify(mystring):
	newstring = mystring
	newstring = re.sub('``','"',newstring)
	newstring = re.sub("''",'"',newstring)
	newstring = re.sub('---','--',newstring)
	newstring = re.sub('}','',newstring)
	newstring = re.sub('{','',newstring)
	newstring = re.sub(r'\\emph','',newstring)
	newstring = re.sub(r'\\textit','',newstring)
	newstring = re.sub(r'\\textbf','',newstring)
	return newstring

# ################### 
# LATEX COVER SHEET #
# ###################
os.chdir(inputs)
cover_file = 'tul' + wpnum + '_cover.tex'
cover = open(cover_file, 'w')

# Preliminaries
cover.write('\\documentclass[11pt,letterpaper,final]{article}\n')
cover.write('\\usepackage{pdfpages}\n')
cover.write('\\usepackage[top=1in, bottom=1in, left=1in, right=1in]{geometry}\n')
cover.write('\\usepackage[T1]{fontenc}\n')
cover.write('\\usepackage[utf8]{inputenc}\n')
cover.write('\\begin{document}\n')
cover.write('\\bigskip\\bigskip\n')

# Tulane working paper series
cover.write('\\begin{center}\\includegraphics[scale=0.25]{../../shieldword_black.pdf}\\\\{\\large Tulane Economics Working Paper Series}\n')
cover.write('\n')

# Paper title
cover.write('\\vspace{2\\baselineskip}\n')
# if title has colon or period or question mark put break after colon:
Title_latex = re.sub(':',r': \\\\ \\vspace{4pt}',Title)
cover.write('{\\LARGE ' + Title_latex + '}\n')
cover.write('\n')

# Authors
cover.write('\\vspace{1.5\\baselineskip}\n')
# if authors%2==0: #  even numbers: put 2 per line, hence boxsize = .5
	# boxsize = .45
# else: # odd numbers: put 3 per line, hence boxsize = .33
 	# boxsize = .33
boxsize = .3
authors_left = authors
i = 1
while i<=authors:
	cover.write('%Author ' + str(i) + '\n')
	cover.write('\\begin{minipage}[t]{' + str(boxsize) + '\\textwidth} \\centering\n')
	# to get Latex spacing right after periods in author name:
	author_latex = re.sub('\. ',r'.\\ ',locals()['Author' + str(i)])
	cover.write(author_latex + '\\\\ \n')
	affiliation_latex = re.sub(', ',r'\\\\ ',locals()['Affiliation' + str(i)])
	cover.write(affiliation_latex + '\\\\ \n')
	cover.write('\\mbox{' + locals()['Email' + str(i)] + '} \\\\ \n')
	cover.write('\\end{minipage}\n')
	cover.write('%\n')
	i += 1

# Working paper information
cover.write('\n')
cover.write('\\vspace{1.5\\baselineskip}\n')
cover.write('Working Paper ' + wpnum_nor + '\\\\ \n')
if is_revised==0:
	cover.write(Month + '\\vspace{\\baselineskip}\n')
else:
	cover.write('Original version: ' + OriginalMonth + '\\\\ \n')
	cover.write('This version: ' + Month + '\\vspace{\\baselineskip}\n')
	
cover.write('\n')

# Abstract
if Abstract != '':
	cover.write('\\textbf{Abstract}\\end{center}\n')
	cover.write('\\vspace{-\\baselineskip}\n')
	cover.write('\\noindent ' + Abstract + '\n')
	cover.write('\n')
	cover.write('\\vspace{\\baselineskip}\n')
else:
	cover.write('\\end{center}\n')

# Kewords and JEL codes
if Keywords !='':
	cover.write('\\noindent Keywords: ' + Keywords + '\\\\ \n')
if JELcodes !='':
	cover.write('\\noindent JEL codes: ' + JELcodes + '\n')
	
# End of .tex file
cover.write('\\thispagestyle{empty}\n')
cover.write('\\end{document}\n')
	
# Close the .tex file
cover.close()

# #################################### 
# FILE SCRAPED BY RePEc (wpaper.rdf) #
# ####################################
os.chdir(scrape)
wpaper = open('wpaper.rdf','a')

# Preliminaries
wpaper.write('\n')
wpaper.write('Template-Type: ReDIF-Paper 1.0\n')

# Authors
i = 1
while i<=authors:
	wpaper.write('Author-Name: ' + locals()['Author' + str(i)] + '\n')
	wpaper.write('Author-X-Name-First: ' + locals()['FirstName' + str(i)] + '\n')
	wpaper.write('Author-X-Name-Last: ' + locals()['LastName' + str(i)] + '\n')
	wpaper.write('Author-Email: ' + locals()['Email' + str(i)] + '\n')
	wpaper.write('Author-Workplace-Name: ' + locals()['Affiliation' + str(i)] + '\n')
	i += 1


	
# Title
title_repec = delatexify(Title)
wpaper.write('Title: ' + title_repec + '\n')

# Abstract
abstract_repec = delatexify(Abstract)
wpaper.write('Abstract: ' + abstract_repec + '\n')
	
# Additional info
month_abbr = locals()[month_][0:3]
month_num = str(strptime(month_abbr,'%b').tm_mon)
if len(month_num)==1:
	month_num = '0' + month_num
wpaper.write('Creation-Date: ' + myyear + '-' + month_num + '\n')
if is_revised==1:
	revmonth_abbr = Month[0:3]
	revmonth_num = str(strptime(revmonth_abbr,'%b').tm_mon)
	if len(revmonth_num)==1:
		revmonth_num = '0' + revmonth_num
	wpaper.write('Revision-Date: ' + revyear + '-' + revmonth_num + '\n')
wpaper.write('File-URL: http://econ.tulane.edu/RePEc/pdf/tul' + wpnum + '.pdf' + '\n')
wpaper.write('File-Format: Application/pdf\n')
if is_revised==0:
	wpaper.write('File-Function: First Version, ' + Month + '\n')
else:
	wpaper.write('File-Function: Revised Vresion, ' + Month + '\n')
wpaper.write('Number: ' + wpnum_nor + '\n')
wpaper.write('Classification-JEL: ' + JELcodes + '\n')
wpaper.write('Keywords: ' + Keywords + '\n')
wpaper.write('Handle: RePEc:tul:wpaper:' + wpnum_nor + '\n')

# Close the .rdf file
wpaper.close()

# ############################# 
# FOR WEBSITE (tulXXXX.shtml) #
# #############################
# Note the text added to tulXXXX.html must then be manually copied and pasted to
#  workingpapers.html to get it in the right place (since append only appends to the end of a file,
#  later see if possible to automate the copy and paste to a specific line of workingpapers.html)
os.chdir(base) 
shtml_file = outputs + '/tul' + wpnum + '.shtml'
shtml = open(shtml_file, 'w')

shtml_authors = []
i = 1
while i<=authors:
	if 'Tulane University' in locals()['Affiliation' + str(i)]:
		shtml_authors.append('<strong>' + locals()['Author' + str(i)] + '</strong>')
	else:
		shtml_authors.append(locals()['Author' + str(i)])
	i += 1

i = 0 # since python indexes at 0
while i<=authors-1:
	if i==0:
		author_list = shtml_authors[i]
	elif i>0 and authors==2:
		author_list = author_list + ' and ' + shtml_authors[i]
	elif i>0 and authors>2:
		if i<authors-1:
			author_list = author_list + ', ' + shtml_authors[i]
		else:
			author_list = author_list + ', and ' + shtml_authors[i]
	i += 1
	
title_shtml = delatexify(Title)
if title_shtml.endswith('\?') or title_shtml.endswith('\.'):
	eol = '' # end of line with title
else:
	eol = '.'

shtml.write('<li>\n')
shtml.write(author_list + '.\n')
shtml.write(myyear + '.\n')
shtml.write('<a href="https://ideas.repec.org/p/tul/wpaper/' + wpnum + '.html">\n')
shtml.write(title_repec + '</a>' + eol + '\n')
shtml.write('Tulane University Economics Working Paper\n')
shtml.write(wpnum_nor + '.\n')
shtml.write('<br /></li><br />\n')

shtml.close()

# ########################## 
# FOR WEBSITE (index.html) #
# ##########################
myhtml_file = pdfs + '/index.html'
myhtml = open(myhtml_file, 'r')
lines = myhtml.readlines()
myhtml.close()

newhtml = open(myhtml_file, 'w')
newhtml.writelines([item for item in lines[:-1]])
newhtml.write('<BR><A HREF=tul' + wpnum + '.pdf>tul' + wpnum + '.pdf</A>\n')
newhtml.write('</HTML>')

newhtml.close()


