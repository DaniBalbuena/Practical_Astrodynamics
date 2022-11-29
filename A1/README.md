Introduction to the Code

The code provided in this repository has the purpose of: given a certain file containing time in Julian Days, output three other files with the time in: UTC, UT1, and GPS, expressed in J2000 seconds. It will also output the conversion tables for UT1 and GPS if they are not in the directory.
For this purpose, there are two different functions:
- 'csv2array' is an auxiliary function that: given a certain file with a certain number of heading lines (maximum 2), outputs the array corresponding to the data on the CSV. This function has no intended use besides to support the main function ('time_conversion').
- 'time_conversion' is a function that: given a certain file containing time in Julian Days on its first column, outputs three different files changing the time column to be expressed in UTC, UT1, and GPS, always in J2000 seconds.  It will also output the conversion tables for UT1 and GPS if they are not in the directory.
Due to the fact that this code is only intended to provide the code for the reading and downloading of the time conversion tables, the actual conversion and writing of the output files is skipped.

How to use the Code

Only the function 'time_conversion' has to be used. This function receives two inputs. The first one is the name of the data file containing the time in Julian Days, and the second one is the number of headings that this data file has (usually one).

Working Example

Data file (contains 2 headings): orbit.dat

Then, the code can be used by adding one line at the end of it: time_conversion('orbit.dat',2)


Data type returned

*.dat files with data regarding the time conversion tables for UT1 and GPS. Completing the conversion and writing part, also *.dat files with the converted times will be present as an output.
