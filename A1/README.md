# Introduction to the Code

The code provided in this repository has the purpose of: given a certain file containing time in Julian Days, output three other files with the time in: UTC, UT1, and GPS, expressed in J2000 seconds. It will also output the conversion tables for UT1 and GPS if they are not in the directory.
For this purpose, there are two different functions:
- 'csv2array' is an auxiliary function that: given a certain file with a certain number of heading lines (maximum 2), outputs the array corresponding to the data on the CSV. This function has no intended use besides to support the main function ('time_conversion').
- 'time_conversion' is a function that: given a certain file containing time in Julian Days on its first column, outputs three different files changing the time column to be expressed in UTC, UT1, and GPS, always in J2000 seconds.  It will also output the conversion tables for UT1 and GPS if they are not in the directory.
Due to the fact that this code is only intended to provide the code for the reading and downloading of the time conversion tables, the actual conversion and writing of the output files is skipped.

# How to use the Code

Only the function 'time_conversion' has to be used. This function receives two inputs. The first one is the name of the data file containing the time in Julian Days, and the second one is the number of headings that this data file has (usually one).

# Working Example

Data file (contains 2 headings): orbit.dat

Then, the code can be used by adding one line at the end of it: time_conversion('orbit.dat',2)

~~~
def csv2array(csv_dat, nheadings):
	import csv
	import numpy as np
	# Read orbit data in CSV format
	with open(csv_dat, 'r') as file:
		csvreader = csv.reader(file)
		if nheadings == 2:
			name = next(csvreader)
			csv_headings = next(csvreader)
		elif nheadings == 1:
			csv_headings = next(csvreader)
		elif nheadings == 0:
			pass
		else:
			print('Maximum number of heading lines supported by the CSV reader is 2')
			exit()
		first_line = next(csvreader)
		first_line = [float(i) for i in first_line]
		data_array = np.array(first_line)
		for row in csvreader:
			row = [float(i) for i in row]
			data_array = np.vstack((data_array, row))
	return data_array

def time_conversion(orbit_dat, nheadings):
	import numpy as np
	import wget
	import os
	orbit_data = csv2array(orbit_dat, nheadings)
  	# Get time in MJD
	JD = orbit_data[:,0]
	MJD = JD - 2400000.5
	MJD_floored = np.floor(MJD)
	# Get time in UTC since J2000
	J2000 = JD - 2451545.0
	UTC = J2000*24*60*60
	# Convert the file
	orbit_UTC = orbit_data
	orbit_UTC[:,0] = UTC
	np.savetxt('orbit_UTC.dat', orbit_UTC,delimiter=',')
	# Conversion tables
	urls = {'UT1': 'https://maia.usno.navy.mil/ser7/gpsrapid.daily',
			    'GPS': 'https://maia.usno.navy.mil/ser7/tai-utc.dat'}
	# Conversions
	for type in ['UT1','GPS']:
		if os.path.isfile(f'{type}.dat'):
			pass
		else:
			url = urls[type]
			wget.download(url, f'{type}.dat')
		# Get data
		if type == 'UT1':
			with open(f'{type}.dat', 'r') as file:
				f = file.readlines()
				mjd_f = [float(f[i][1:6]) for i in range(0, len(f)-1)]
				delta = [float(f[mjd_f.index(MJD_floored[i])][38:45]) for i in range(0, len(MJD))]
      # Calculate the conversion and convert the file here!
      #
      #
      #
      #
		elif type == 'GPS':
			with open (f'{type}.dat', 'r') as file:
				f = file.readlines()
				delta = float(f[-1][37:40])
      # Calculate the conversion and convert the file here!
      #
      #
      #
      #

time_conversion('orbit.dat',2)
~~~

# Data type returned

*.dat files with data regarding the time conversion tables for UT1 and GPS. Completing the conversion and writing part, also *.dat files with the converted times will be present as an output.
