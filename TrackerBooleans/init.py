custom_scripts_dir = os.path.expanduser(r'~\.nuke\CustomScripts')
if custom_scripts_dir not in sys.path:
    sys.path.append(custom_scripts_dir)

# Import functions from tracker_boolean script
from tracker_boolean import toggleTrackerTRS, toggleAllTRS

nuke_initialized = False

def set_nuke_initialized():
    global nuke_initialized
    if nuke.GUI:
        nuke_initialized = True
    else:
        print("Still waiting for the UI to be initialized...")

def on_nuke_initialized():
    set_nuke_initialized()
    if nuke_initialized:
        custom_init()

def custom_init():
    init_tracker_boolean()

def init_tracker_boolean():
    animM = nuke.menu('Animation')
    animM.addCommand('Toggle Tracker TRS', 'toggleTrackerTRS()', 'ctrl+alt+shift+t')  # Change shortcut here to open the Tracker custom menu for TRS
    animM.addCommand('Toggle All TRS', 'toggleAllTRS()')
    
    nuke.menu('Nuke').addCommand('CustomTools/TrackerTools/Toggle All TRS', 'toggleAllTRS()', 'ctrl+alt+shift+0')  # Change shortcut here to set all TRS for all tracks to true
    nuke.menu('Nuke').addCommand('CustomTools/TrackerTools/Toggle Tracker TRS', 'toggleTrackerTRS()', 'ctrl+alt+shift+t')  # Change shortcut here to open the Tracker custom menu for TRS

nuke.addUpdateUI(on_nuke_initialized)