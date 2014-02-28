XCassetsToDrawables
===================

Developers that are porting iOS apps to Android, have to convert many images. 
This file generates the new XCassets to Android Drawables.

It takes the @2x file, which is 200%, and converts it four sizes:
- xhdpi (200%)
- hdpi (150%)
- mdpi (100%)
- ldpi (50%)

The script requires the path of the iOS project.

New versions will: 
- Check for not accepted characters in file name.
- cleaner code.
