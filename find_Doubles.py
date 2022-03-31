#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  find_Doubles.py
#  
#  Copyright 2022 Crerar Christie <crerarc03@gmail.com>
#  
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>

"""Purpose:

Code walks through the directory this python file is run from and goes
through each subfolder. For each file in each folder, the code reads a
chuck of data and converts it to a hash key. A dictionary of hashkeys is
created with the first hashkey, thereafter, every subsequent hashkey is first
checked against existing hashkeys. If the key already exists, a double is
recorded in a "doubles.txt" file, if not, the hashkey and file path are
added to the dictionary. 

Limit read block size for md5 to improve efficiency,
https://stackoverflow.com/questions/17731660/hashlib-optimal-size-of-chunks-to-be-used-in-md5-update

"""

def main():
    # Initialise variables
    import os
    import hashlib
    fh_invntry = {}
    rootdir = os.getcwd()
    
    # Open output file and start traversing directory tree
    fon = "doubles.txt"
    with open(fon, "w") as fo:
    
        # Specify blocksize
        BLOCK_SIZE = 65536
        
        # Go through files and create dictionary of hashes 
        for subdir, dirs, files in os.walk(rootdir):
            for fi in files:
                
                # Create the hash object
                fh5 = hashlib.md5()
                
                # Save path to file as a string
                pth2fil = os.path.join(subdir, fi)
    
                # More efficient to read large files in chunks
                with open(pth2fil, 'rb') as f: # open the file to read bits
                    fb = f.read(BLOCK_SIZE)
                    while len(fb) > 0:
                        fh5.update(fb) # update the hash
                        fb = f.read(BLOCK_SIZE) # read the next block
                        
                # Store the hashed read blocks as a hexkey
                hxkey = fh5.hexdigest()
                
                # If the hashkey is already in the dictionary, report the current file as a double
                if hxkey in fh_invntry:
                    fo.write("Match\n")
                    fo.write("Existing: "+str(hxkey)+" "+str(fh_invntry[hxkey])+"\n")
                    fo.write("Current : "+str(hxkey)+" "+str(pth2fil)+"\n\n")
                    fo.write(" ")
                else:
                    fh_invntry[fh5.hexdigest()] = pth2fil
    
    
if __name__ == "__main__":
    main()


