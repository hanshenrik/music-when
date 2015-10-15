#!/usr/bin/env python
# coding: utf-8

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
Script for parsing the exported tracks file created by lastexport.py in order
to figure out which hours of the day you listen to music the most.
Usage: musicwhen.py -i FILENAME (of file created by lastexport.py)
"""

__version__ = '0.0.1'

from optparse import OptionParser
import sys
import matplotlib.pyplot as plt
import datetime

hours = range(24)
scrobblesPerHour = [0] * 24
totalScrobbles = 0
barColor = '#bb0000'

def get_options(parser):
  """ Define command line options."""
  parser.add_option("-i", "--input", dest="filename", default=None,
    help="Input file created by lastexport.py.")

  options, args = parser.parse_args()

  if not options.filename:
    sys.exit("Input file not specified, see --help")

  return options.filename

def parseTracks(filename):
  global scrobblesPerHour
  global totalScrobbles

  with open(filename, 'r') as f:
    for line in f:
      # Get the UNIX timestamp of each scrobbled track
      timestamp = int(line.split()[0])

      hour = int(datetime.datetime.fromtimestamp(timestamp).strftime('%H'))

      scrobblesPerHour[hour] += 1
      totalScrobbles += 1

def draw():
  plt.title('Music when?')
  plt.xlabel('Hour of day')
  plt.ylabel('# of scrobbles')
  plt.grid(True)
  plt.text(1, 4500, 'Total scrobbles: %d' % totalScrobbles, bbox={'facecolor': '#bb0000', 'alpha': 0.7, 'pad': 10})
  plt.bar(hours, scrobblesPerHour, color=barColor)

  # Set the x-axis range from 0 to 23, keep the y-axis as is
  x1, x2, y1, y2 = plt.axis()
  plt.axis((0, 23, y1, y2))
  
  plt.show()

def main(filename):
  parseTracks(filename)
  draw()
  
if __name__ == '__main__':
  parser = OptionParser()
  filename = get_options(parser)
  main(filename)
