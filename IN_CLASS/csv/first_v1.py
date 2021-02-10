import csv

''' These constants hide the "magical numbers" for the columns
	of the CSV file. This is preferable to simply using the 
	nummbers because the numbers alone don't help you remember
	what each column holds. These symbols do.
'''
LAST_NAME = 1
FIRST_NAME = 2
GENDER = 3

''' For counting the number of each gender (which I do feel bad
    about not allowing for the diversity of gender), we are pre-
	populating a dictionary with the keys. In this way, we do not
	have to test for the presence of a key before adding to its
	value.
'''

gender_info = {'F': 0, 'M': 0}

''' We want to collect all the first names that share a particular
	last name. A dictionary has keys of last names...
	   From each key (last name), there is a set of first names.
'''
last_names = {}

''' Produce a simply "Gender Report".
'''

def GenderReport():
	print('Breakdown by self-identified gender')
	total = gender_info['M'] + gender_info['F']
	print('{:10s} {:<8d} {:.2f}'.format(
		'Female', gender_info['F'], gender_info['F'] / total * 100))
	print('{:10s} {:<8d} {:.2f}'.format(
		'Male', gender_info['M'], gender_info['M'] / total * 100))

def FirstNameReport(last_name):
	if last_name not in last_names:
		print('The name:', last_name, 'was not found')
	else:
		print('First name report:')
		print('Last name:', last_name, 'yields these first names:')
		fnames = sorted(list(last_names[last_name]))
		for fname in fnames:
			print(fname)

''' try / except is a way to prevent an error from causing a crash.
	Anything inside the try block that causes an error that would 
	otherwise crash can be caught in an except block.
'''

try:
	# The with block will close the file automatically.
	with open('studata.csv') as input_file:
		# "Wrap" the open file with a CSV reader.
		reader = csv.reader(input_file)
		for row in reader:
			# Even though this should never happen, it's good to put
			# in the test - this is an act of "defensive programming."
			if row[GENDER] not in gender_info:
				print('Unexpected value(gender):', row[GENDER])
				continue
			else:
				gender_info[row[GENDER]] += 1
			# If this is the first time we're seeing a last name,
			# we must construct an empty set for its value.
			if row[LAST_NAME] not in last_names:
				last_names[row[LAST_NAME]] = set()
			# Now we have a guarantee that the last name is already
			# a valid key and has a preexisting set to add to.
			last_names[row[LAST_NAME]].add(row[FIRST_NAME])

except FileNotFoundError:
	print('The file was not found')
	exit(0)

GenderReport()
FirstNameReport('Campos')
