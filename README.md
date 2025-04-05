# TVL Nuke Tools

[![copyright: TVL](https://img.shields.io/badge/Copyright-TVL-yellow.svg)](https://pluz21.itch.io/)

# Nuke TRS Tool

## Description

The **TRS Tool** adds commands to toggle the Tracker TRS (Translate, Rotate, Scale) settings for Tracker nodes in Nuke. This tool provides quick access to enable or disable the TRS settings for individual or all Tracker nodes.

## Setup

1. **Clone this repository** or download the `tracker_boolean.py` script.
2. **Place the `tracker_boolean.py` script**:
   - Option 1: In the `CustomScripts` folder inside your Nuke user directory (create the folder if it doesn't exist).
   - Option 2: Directly in the Nuke user directory (`~/.nuke`).

3. **Modify the `init.py` file** in your Nuke user directory to load the script:
   - For **Option 1** (CustomScripts folder):
     ```python
     custom_scripts_dir = os.path.expanduser(r'~\.nuke\CustomScripts')
     ```
   - For **Option 2** (directly in the Nuke user directory), add:
     ```python
     import sys
     import os
     sys.path.append(os.path.expanduser('~/.nuke'))  # Add the Nuke user directory to sys.path
     from tracker_boolean import toggleTrackerTRS, toggleAllTRS
     ```

4. Save the changes and restart Nuke.

---

## Usage

Once the tool is installed, you can access the following commands from the Nuke menu:

- **Toggle Tracker TRS**: Toggles the TRS (Translate, Rotate, Scale) settings for the selected Tracker node.
  - **Shortcut**: `Ctrl+Alt+Shift+T`
  
- **Toggle All TRS**: Toggles the TRS settings for all Tracker nodes in the script.
  - **Shortcut**: `Ctrl+Alt+Shift+0`

Additionally, you can call these methods from the **right-click context menu** in the **Tracker** node window. Simply right-click on the Tracker node in the node graph or properties panel, and you will see the following options under the **CustomTools/TrackerTools** menu:

- **Toggle Tracker TRS**: Toggles the TRS settings for the selected Tracker node.
- **Toggle All TRS**: Toggles the TRS settings for all Tracker nodes in the script.

---

## Notes

- Ensure Nuke is restarted after setting up the script to load the new commands.
- The tool is now ready to use from the Nuke menu and the right-click context menu with the assigned shortcuts.

