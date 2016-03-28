# Manifold module

#***************************************************************************
#                                                                           
#    This file is part of the FreeCAD CAx development system.               
#                                                                           
#    This program is free software; you can redistribute it and/or modify   
#    it under the terms of the GNU Lesser General Public License (LGPL)     
#    as published by the Free Software Foundation; either version 2 of      
#    the License, or (at your option) any later version.                    
#    for detail see the LICENCE text file.                                  
#                                                                          
#    FreeCAD is distributed in the hope that it will be useful,             
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
#    GNU Lesser General Public License for more details.                    
#                                                                           
#    You should have received a copy of the GNU Library General Public     
#    License along with FreeCAD; if not, write to the Free Software        
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307   
#    USA                                                                    
#                                                                          
#***************************************************************************/

'''
InitGui.py
checked with pylint, to catch some errors
'''

# disabling import-error pylint warning
# pylint: disable=E0401
import FreeCAD as App
import FreeCADGui as Gui

__licence__ = 'GPL'
__title__ = 'InitGui.py'
__version__ = '0.9.2'

# disabling invalid-name pylint warning
# pylint: disable=C0103
# disabling undefined-variable pylint warning
# pylint: disable=E0602
# disabling no-self-use pylint warning
# pylint: disable=R0201
class ManfoldWorkbench(Workbench):
    '''
    Manfold workbench object
    '''
    MenuText = 'Manifold'
    ToolTip = 'Manifold Design for hydaulic circuits'
    Icon = 'freecad.svg'

    def Initialize(self):
        '''
        Manfold Design workbench Initialize
        '''
        try:
            # disabling wrong-import-position pylint warning
            # pylint: disable=C0413
            import Manifold
        except ImportError:
            App.Console.PrintMessage('workbench cannot be loaded')

    def Activated(self):
        '''
        this executes when workbench is activated
        '''
        App.Console.PrintMessage('ManfoldWorkbench.Activated')

    def Deactivated(self):
        '''
        this executes when workbench is deactivated
        '''
        App.Console.PrintMessage('ManfoldWorkbench.Deactivated')

    def GetClassName(self):
        '''
        Manfold Design workbench GetClassName
        '''
        return 'Gui::PythonWorkbench'

# disabling undefined-variable pylint warning
# pylint: disable=E0602
Gui.addWorkbench(ManfoldWorkbench())
