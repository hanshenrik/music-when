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
Usage: musicwhen.py -u USERNAME (of last.fm user)
"""

__version__ = '0.0.1'

import os
import sys
import lastexport
import matplotlib.pyplot as plt
from optparse import OptionParser
from datetime import datetime

hours = range(24)
scrobblesPerHour = [0] * 24
totalScrobbles = 0
barColor = '#a2e877'
barColorDark = '#83c15d'
imgPath = 'img'
dataPath = 'data'

def get_options(parser):
  """ Define command line options."""
  parser.add_option("-u", "--username", dest="username", default=None,
    help="Username of the last.fm user.")

  options, args = parser.parse_args()

  if not options.username:
    sys.exit("Username not specified, see --help")

  return options.username.lower()

def parse_tracks(filename):
  global scrobblesPerHour
  global totalScrobbles

  filename = '{}.txt'.format(filename)

  with open(os.path.join(dataPath, filename), 'r') as f:
    for line in f:
      # Get the UNIX timestamp of each scrobbled track
      timestamp = int(line.split()[0])

      hour = int(datetime.fromtimestamp(timestamp).strftime('%H'))

      scrobblesPerHour[hour] += 1
      totalScrobbles += 1

def draw(username):
  plt.title("{}'s listening pattern".format(username))
  plt.xlabel('Hour of day')
  plt.ylabel('# of scrobbles')
  plt.grid(True)
  
  plt.bar(hours, scrobblesPerHour, color=barColor, edgecolor=barColorDark, linewidth=1)

  x1, x2, y1, y2 = plt.axis()
  plt.text(1, 0.9*y2, 'Total scrobbles: %d' % totalScrobbles,
    bbox={'facecolor': barColor, 'edgecolor': barColorDark, 'pad': 10})

  # Set the x-axis range from 0 to 23, keep the y-axis as is
  plt.axis((0, 23, y1, y2))

  save_as_image(username)

def save_as_image(filename):
  filename = '{}.png'.format(filename)

  if not os.path.exists(imgPath):
    os.makedirs(imgPath)

  plt.savefig(os.path.join(imgPath, filename), format='png')
  print "Saved figure to {}".format(os.path.join(imgPath, filename))

def get_time_of_latest_scrobble(username):
  filename = '{}.txt'.format(username)
  filepath = os.path.join(dataPath, filename)

  if not os.path.exists(filepath):
    return 0

  with file(filepath, 'r') as f:
    # Last line is newline, read last with text
    lastLine = f.readlines()[-2]
  
  lastScrobbleTimestamp = int(lastLine.split()[0])
  return lastScrobbleTimestamp + 30

def main(username):
  starttime = get_time_of_latest_scrobble(username)
  lastexport.main(username=username, starttime=starttime, dataPath=dataPath)
  parse_tracks(username)
  draw(username)

if __name__ == '__main__':
  parser = OptionParser()
  username = get_options(parser)
  main(username)
