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
