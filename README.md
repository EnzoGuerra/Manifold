--FreeCAD workbench for designing hydraulic manifolds--
to install Manifold workbench: copy Manifold directory into FreeCAD Mod directory
to uninstall Manifold workbench: delete Manifold directory from FreeCAD Mod directory

use following guidelines to design a hydraulic manifold.  the hydraulic manifold is generated from a csv file; the csv file should be placed in an empty directory that will contain the hydraulic manifold.  use same name for the csv file as the hydraulic manifold file.  the first line of the csv file must be the block details, consisting of:  the string 'Block', and then the x, y, and z dimensions, of the block, all units are mm
ex: Block,63.5,31.75,41.14

then any of the following details can be added:
adding cavity: cavity, face, x, y coordinates
ex: T-10A,Front,25.0,150.0
adding din valve: din valve, face, x, y coordinates, rotation
ex: DIN24342 NG16,Front,80.0,80.0,0.0
adding din valve port: din valve port, face, x, y coordinates, rotation, depth
ex: DIN24342 NG16 X,Front,80.0,80.0,0.0,60.0
adding drill: 'Drillbit', face, x, y coordinates, diameter, depth
ex: Drillbit,Front,12.0,25.0,10.0,75.0
adding flange: flange, face, x, y coordinates, rotation
ex: ISO6162-1 2,Front,150.0,150.0,90.0
adding ng valve: ng valve, face, x, y coordinates, rotation
ex: NG6,Front,150.0,150.0,90.0
adding ng valve port: ng valve port, face, x, y coordinates, rotation, depth
ex: NG6 P,Front,150.0,150.0,90.0,55.0
adding oring: 'O-Ring', face, x, y coordinates, thickness, inside diameter
ex: O-Ring,Front,100.0,125.0,1.50,150.0
adding shcs: shcs, face, x, y coordinates	
ex: M20,Front,75.0,150.0
adding text: 'Text', face, x, y coordinates, rotation, string
ex: Text,Front,25.0,150.0,0.0,Tank

after the csv file has been written, start FreeCAD; then select 'Manifold' from the workbenches drop down box; a save dialog will appear; save file in same directory as csv file, using the same filename, the extension will be FCStd; after the save dialog ends, the hydraulic manifold will be generated according to the csv file; review the design and modify csv file accordingly.  FreeCAD must be restarted in order to run the Manifold workbench again.  reselect the hydraulic manifold file and overwrite the file in order to generated the modified hydraulic manifold from the csv file.  
a spreadsheet program would reduce the time to calculate/lookup many parameters required for designing a hydraulic manifold; use sheet 1 as the csv file output, then review csv file, it should not contain any empty lines and only the first column can have whitespaces.
the drawing feature is not avaliable yet.

notes:
use a text editor to read Manifold.py which will be in Manifold directory, so the contains of the dictionaries and lists can be read.
from details above:
for cavity, first add a 'Drillbit'; both must have the same face, x, y coordinates
cavity must be in CAVITIES dictionary;
for din valve, first add a 'Drillbit'; both must have the same face, x, y coordinates
din valve must be in DINVALVES dictionary;
for din valve that require ports;
both must have same face, x, y coordinates, and rotation
din valve port must be in DINPORTS dictionary
for din valve port, depth is the depth of the port
for 'Drillbit', diameter must be in DRILLBITS list
for 'Drillbit', depth is the depth of the 'Drillbit'
for flange, first add a 'Drillbit'; both must have the same face, x, y coordinates
flange must be in FLANGES dictionary;
ng valve must be in NGVALVES dictionary
for ng valve that require ports;
both must have same face, x, y coordinates, and rotation
ng valve port must be in NGPORTS dictionary
for ng valve port, depth is the depth of the port
for 'O-Ring', thickness must be in ORINGS dictionary;
for 'O-Ring', inside diameter must be in ORINGS[thickness] list
for shcs, first add a 'Drillbit'; both must have the same face, x, y coordinates
shcs must be in SHCS dictionary;
for 'Text', string is the text that will be placed on hydraulic manifold
face can only be 'Front', 'Top', 'Right', 'Rear', 'Bottom', 'Left' 
rotation can only be 0.0, 90.0, 180.0, 270.0
