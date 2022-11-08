# Importing needed modules for phy

import os

# Conditions

# Files that end with these exstensions will be moved and renamed
Extension = (".m4a", ".M4a", ".M4A", ".mp3", ".Mp3", ".MP3")
# RootDir is a directory containing your current music library
RootDir = r'/Users/LukeSkywalker/Music/NewLibrary/Import'
# NewDir is a directory into which you want to move your music to
NewDir = r'/Users/LukeSkywalker/Music/NewLibrary/Export'

# Renaming Files

for root, dirs, files in os.walk((os.path.normpath(RootDir)), topdown=False):
    for f in files:  # for any file with a name in the dir
        if f.endswith(Extension):
            ArtistDirectory, AlbumDirectory = (root.split(os.sep)[-2:])  # Get Artist and Album from Folder Names
            RootPathAndName = os.path.join(root, f)  # Join Root Path and File Name
            NewFileName = (ArtistDirectory + " - " + f)  # Append new File Name
            NewPathAndName = os.path.join(NewDir, NewFileName)  # Append Path and File Name
            os.rename(RootPathAndName, NewPathAndName)  # Rename Root Path and File Name with New Root Path and File 
            # Name
            print(RootPathAndName, NewPathAndName)  # Print All Touched Files

print("Done")
