#!/usr/bin/env python

"""
Problem: Find the number of islands and the largest island in a map.

Land has the value of 1 in the map (matrix). Non-land has the value 0.
Connected land is land adjacent to the current land.
This includes land directly above or below, or left or right.
Land diagonal to the current land is not connected. 
"""

def find_islands(imap, islands):
    """
    Iterate though all the locations in the map. When land is found,
    increase the number of islands and find all the connected land.
    parameters:
      imap - two dimensional matrix
      islands - list of island sizes 
    """
    for row in range(0, len(imap)):
        for col in range(0, len(imap[0])):
            if imap[row][col] == 1:
                islands.append(0)
                find_land(imap, islands, row, col)
        
def find_land(imap, islands, row, col):
    """
    Find all the connected land by checking if current location is land.
    If it is land, mark it as found using the value 2 and increase the size
    of the island, then determine all the possible adjacent locations and
    search recursively for adjacent land filtering out invalid locations
    that are outside the map.
    Note: the land data structure contains a list of adjacent location tuples
    which can be easily adjusted if the definition of adjacent location changes
    parameters:
      imap - two dimensional matrix
      islands - list of island sizes
      row - current row index
      col - current column index
    """
    if imap[row][col] == 1:
        imap[row][col] = 2
        islands[-1] += 1
        # create adjacent locations (above, below, left, right)
        land = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for r, c in land:
            if r >= 0 and r < len(imap) and c >= 0 and c < len(imap[0]):
                find_land(imap, islands, r, c)

def print_map(imap):
    """
    Print out the island map.
    parameters:
      imap - two dimensional matrix
    """
    for row in imap:
        print ' ', row

imaps = [
  [
  [0, 0, 1, 0],
  [0, 1, 1, 0], 
  [0, 1, 0, 0],
  [1, 1, 0, 1], 
  ],
  [
  [0, 0, 0, 0],
  [0, 1, 1, 0], 
  [0, 0, 0, 0],
  [0, 0, 0, 0], 
  ],
  [
  [1, 0, 0, 0],
  [0, 1, 0, 0], 
  [0, 0, 1, 0],
  [0, 0, 0, 1], 
  ],
  ]

# Iterate though all the maps finding all the islands and the largest
for inx, imap in enumerate(imaps):
    print 'map:', inx+1
    print_map(imap)
    islands = []       
    find_islands(imap, islands)
    print '  number of islands:', len(islands)
    max = 0
    for island in islands:
        if island > max:
            max = island
    print '  largest island:', max
