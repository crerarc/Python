def main():
    # Initialise variables
    import os
    import hashlib
    fh_invntry = {}
    rootdir = os.getcwd()
    fon = "doubles.txt"
    fo = open(fon, "w")
    
    """
    Limit read block size for md5 to improve efficiency, https://stackoverflow.com/questions/17731660/hashlib-optimal-size-of-chunks-to-be-used-in-md5-update
    """
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
    
    fo.close()
    


if __name__ == "__main__":
    """ Program Notes:
    Purpose:    Go through files in current folder, and its subfolders
                creating Hash for each and storing the hash and its title
                in a dictionary.  The dictionary is checked for each file,
                if a double is found, it is saved to a double file
    
    """
    main()


