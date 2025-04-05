import nuke
import nukescripts
import re

last_selected_node = None

def toggleTrackerTRS():
    # n = nuke.thisNode()
    n = nuke.selectedNode()  # This will grab the currently selected node

    if n.Class() == 'Tracker4':
        k = n['tracks']
        items = re.findall('{ [0-9, ]*}', k.toScript())[0]
        tracks = int(items.split(' ')[-2])
        
        p = nukescripts.panels.PythonPanel('TRS')

        p.setTooltip('Select the boxes to enable TRS respectively')
        
        t = nuke.Boolean_Knob('t', 'T')
        r = nuke.Boolean_Knob('r', 'R')
        s = nuke.Boolean_Knob('s', 'S')

        # set values of first Track
        t.setValue(k.getValue(6))
        r.setValue(k.getValue(7))
        s.setValue(k.getValue(8))

        p.addKnob(t)
        p.addKnob(r)
        p.addKnob(s)

        ret = p.showModalDialog()

        if ret == 1:
            # T
            for i in range(0, tracks):
                k.setValue(p.knobs()['t'].value(), 31*i+6)

            #R
            for i in range(0, tracks):
                k.setValue(p.knobs()['r'].value(), 31*i+7)

            #S
            for i in range(0, tracks):
                k.setValue(p.knobs()['s'].value(), 31*i+8)

    else:
        nuke.message('This is a Tracker4 feature, please select a Tracker.')

trs_toggle = {'state': True}

def toggleAllTRS():
    n = nuke.selectedNode()
    
    if n and n.Class() == 'Tracker4':
        k = n['tracks']
        
        items = re.findall(r'{ [0-9, ]*}', k.toScript())[0]
        tracks = int(items.split(' ')[-2])

        if tracks == 0:
            nuke.message('No tracks found in the selected Tracker4 node.')
            return

        new_value = 1 if trs_toggle['state'] else 0

        for i in range(tracks):
            k.setValue(new_value, 31*i+6)  # Translate
            k.setValue(new_value, 31*i+7)  # Rotate
            k.setValue(new_value, 31*i+8)  # Scale

        trs_toggle['state'] = not trs_toggle['state']

    else:
        nuke.message('Please select a Tracker4 node before using this feature.')

def setLastSelectedNode(node):
    last_selected_node = node

#Not used
#toggleAllTRS based on first track translate bool state
# def toggleAllTRS():
#     n = nuke.selectedNode()
    
#     if n and n.Class() == 'Tracker4':
#         k = n['tracks']
        
#         # Get the number of tracks from the serialized data
#         items = re.findall('{ [0-9, ]*}', k.toScript())[0]
#         tracks = int(items.split(' ')[-2])

#         t_value = 1  # Set Translate to True (1)
#         r_value = 1  # Set Rotate to True (1)
#         s_value = 1  # Set Scale to True (1)

#         for i in range(0, tracks):
#             k.setValue(t_value, 31*i+6)  # Translate
#             k.setValue(r_value, 31*i+7)  # Rotate
#             k.setValue(s_value, 31*i+8)  # Scale

#         # nuke.message('Successfully set T, R, and S for all tracks.')

#     else:
#         nuke.message('Please select a Tracker4 node before using this feature.')
# 
# def toggleAllTRS():