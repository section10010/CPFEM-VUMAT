# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_15-19.56.28 126354
# Run by yzhang951 on Wed Dec 15 16:13:30 2021
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=260.085388183594, 
    height=201.259262084961)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
o1 = session.openOdb(name='/home/yzhang951/AlHEA/response/lam/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/yzhang951/AlHEA/response/lam/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    COMPONENT, 'LE11'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-1', frame=13)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, 
    title=OFF, state=OFF, annotations=OFF, compass=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316.697, 
    farPlane=367.357, width=162.427, height=128.649, viewOffsetX=5.57259, 
    viewOffsetY=-1.83516)
session.viewports['Viewport: 1'].view.setValues(nearPlane=316.265, 
    farPlane=367.789, width=162.205, height=128.473, viewOffsetX=-8.81426, 
    viewOffsetY=-1.48164)
session.printToFile(fileName='strain', format=TIFF, canvasObjects=(
    session.viewports['Viewport: 1'], ))