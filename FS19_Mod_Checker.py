#  _______           __ ______ __                __               
# |   |   |.-----.--|  |      |  |--.-----.----.|  |--.-----.----.
# |       ||  _  |  _  |   ---|     |  -__|  __||    <|  -__|   _|
# |__|_|__||_____|_____|______|__|__|_____|____||__|__|_____|__|  

# Main Program

# (c) 2021 JTSage.  MIT License.

import gettext

from mod_checker.ui.tree import ModCheckTreeTab
from mod_checker.ui.canvas import ModCheckCanvasTab
from mod_checker.data.logger import ModCheckLog
from mod_checker.base import ModCheckRoot
from mod_checker.data.mods import FSMod

import mod_checker.data.conflict_mods as conflictMods
import mod_checker.data.script_mods as scriptMods
import mod_checker.data.util as ModCheckUtil


VERSION = "1.0.0.5"

# This might not be needed, python might just do this now.  But it probably 
# can't hurt.
ModCheckUtil.set_win32_lang()


gettext.install('fs19modcheck', ModCheckUtil.get_resource_path("./locale"))

# 
#  _______ _______ _____ __   _      _  _  _ _____ __   _ ______   _____  _  _  _
#  |  |  | |_____|   |   | \  |      |  |  |   |   | \  | |     \ |     | |  |  |
#  |  |  | |     | __|__ |  \_|      |__|__| __|__ |  \_| |_____/ |_____| |__|__|
#                                                                                
# 

rootWindow = ModCheckRoot(
	version      = VERSION,
	logger       = ModCheckLog(),
	icon         = ModCheckUtil.get_resource_path("./lib/") + 'mcicon.png',
	modClass     = FSMod,
	scriptMods   = scriptMods.mods,
	conflictMods = conflictMods.mods
)

rootWindow.makeMenuBar({
	"file-menu"     : _("File"),
	"save-log-file" : _("Save Log"),
	"exit-program"  : _("Exit")
})

rootWindow.addIOStrings({
	"error-open-settings" : _("Error Opening Settings File {filename}"),
	"error-not-settings"  : _("This is not a valid FS19 game settings file"),
	"xml-file-type"       : _("XML Settings File"),
	"txt-file-type"       : _("Text Document"),
	"YES"                 : _("YES"),
	"no"                  : _("no"),
	"OWNED"               : _("OWNED"),
	"save-log-title"      : _("Save Log File..."),
	"save-log-ok"         : _("Log File Saved Successfully"),
	"save-log-error"      : _("Unable to save the log file"),
	"save-log-filename"   : _("FS19_Mod_Checker_Log.txt")
})



#  _______  _____  __   _ _______ _____  ______      _______ _______ ______ 
#  |       |     | | \  | |______   |   |  ____         |    |_____| |_____]
#  |_____  |_____| |  \_| |       __|__ |_____|         |    |     | |_____]
#                                                                           

rootWindow.addTab("tabConfig",   underline=0, text=_('Configuration'))

rootWindow.makeConfigTab(strings = {
	"info-ask-for-file"    : _("First, you need to point Mod Checker to your gameSettings.xml file"),
	"load-button-label"    : _("Load Settings"),
	"info-game-settings"   : _("Game Settings File: {filename}"),
	"info-mod-folder"      : _("Mod Folder: {folder}"),
	"info-ask-process"     : _("Next, click \"{process_button_label}\" to scan your collection"),
	"process-button-label" : _("Check Mods"),
	"info-mods-found"      : _("Mods Found"),
	"info-mods-broken"     : _("Broken Mods"),
	"info-mods-folders"    : _("Folders Found"),
	"info-mods-missing"    : _("Missing Mods")
})




#  ______   ______  _____  _     _ _______ __   _      _______  _____  ______  _______
#  |_____] |_____/ |     | |____/  |______ | \  |      |  |  | |     | |     \ |______
#  |_____] |    \_ |_____| |    \_ |______ |  \_|      |  |  | |_____| |_____/ ______|
#                                                                                     

rootWindow.addTab("tabBroken",   underline=0, text=_('Broken Mods'))

rootWindow.addBrokenStrings({
	"default"         : _("This File or Folder is invalid"),
	"unzip-folder"    : _("This folder appears to be the contents of a zipped modpack.  The contents should be moved into the main mods folder, and this folder removed"),
	"unzip-zipfile"   : _("This file appears to be a zipped modpack.  The contents should be extracted to the main mod folder, and this file removed."),
	"digit-folder"    : _("Mod Folders cannot start with a digit.  Is this a collection of mods that should be moved to the root mods folder and then removed?"),
	"digit-zipfile"   : _("Zip files cannot start with a digit.  Is this perhaps a collection of mods? If it is, extract the contents and delete this file."),
	"duplicate-have"  : _("This looks like a copy of the {guessedModName} mod and can probably be deleted."),
	"duplicate-miss"  : _("This looks like a copy, but the original wasn't found. Rename it?"),
	"unknown-folder"  : _("This folder is named incorrectly, but we didn't figure out what is wrong."),
	"unknown-zipfile" : _("This ZIP file is named incorrectly, but we didn't figure out what is wrong."),
	"must-be-zipped"  : _("Unzipped mods cannot be used in multiplayer, you should zip this folder"),
	"garbage-default" : _("This file should not exist here, delete or move it."),
	"garbage-archive" : _("This is an archive file.  It might be a mod pack which should be unpacked and then removed.")
})

rootWindow.tabContent["tabBroken"] = ModCheckCanvasTab(
	parent      = rootWindow.tabFrame["tabBroken"],
	title       = _("Broken Mods"),
	description = _("These mods have been detected to be a possible problem.  ZIP Files or Folders with any non-alphanumeric character other than \"_\" will not be loaded by the game.  Mods that are not compressed as a ZIP file cannot be used in multiplayer games.  Finally, the mod folder should only contain mods, no other files.  Below, there is a list of problem files, and a suggested solution")
)




#  _______ _____ _______ _______ _____ __   _  ______      _______  _____  ______  _______
#  |  |  |   |   |______ |______   |   | \  | |  ____      |  |  | |     | |     \ |______
#  |  |  | __|__ ______| ______| __|__ |  \_| |_____|      |  |  | |_____| |_____/ ______|
#                                                                                         

rootWindow.addTab("tabMissing",  underline=0, text=_('Missing Mods'))

rootWindow.tabContent["tabMissing"] = ModCheckTreeTab(
	parent = rootWindow.tabFrame["tabMissing"],
	title  = _("Missing Mods"),
	description = _("The scanner failed to find the mods below, however they are referenced in one or more savegames. For mods that have not been purchased, this is usually harmless.  For mods you have purchased, missing the mod file could cost you in-game money.  To correct this, re-download the mod from where you originally got it and place it in the mod folder."),
	columns = [
		_("Name"),
		_("Title"),
		_("Purchased"),
		_("Savegame")
	],
	columnExtra = {
		"#3": {"minwidth": 0, "width": 75, "stretch": 0},
		"#4": {"minwidth": 0, "width":100, "stretch": 0}
	}
)




#  _______  _____  __   _ _______        _____ _______ _______      _______  _____  ______  _______
#  |       |     | | \  | |______ |        |   |          |         |  |  | |     | |     \ |______
#  |_____  |_____| |  \_| |       |_____ __|__ |_____     |         |  |  | |_____| |_____/ ______|
#                                                                                                  

rootWindow.addTab("tabConflict", underline=0, text=_('Possible Conflicts'))

rootWindow.tabContent["tabConflict"] = ModCheckCanvasTab(
	parent      = rootWindow.tabFrame["tabConflict"],
	title       = _("Possible Conflicts"),
	description = _("These mods were detected in your mod folder.  In some specific cases, they can cause conflicts with other mods, causing your game to either not work or behave strangely. This display is for informational purposes, and should not be taken a suggestion not to use anything listed here"),
	extraText   = [
		"\u2022 " + _("This should not be taken as a suggestion that these mods do not work."),
		"\u2022 " + _("This is also not intended as a slight against the mod or author."),
		"\u2022 " + _("Many (most) times these mods will work as intended."),
		"\u2022 " + _("If you do experience in-game problems, this may be a good place to start testing.")
	]
)




#  _____ __   _ _______ _______ _______ _____ _    _ _______      _______  _____  ______  _______
#    |   | \  | |_____| |          |      |    \  /  |______      |  |  | |     | |     \ |______
#  __|__ |  \_| |     | |_____     |    __|__   \/   |______      |  |  | |_____| |_____/ ______|
#                                                                                                

rootWindow.addTab("tabInactive", underline=0, text=_('Inactive Mods'))

rootWindow.tabContent["tabInactive"] = ModCheckTreeTab(
	parent = rootWindow.tabFrame["tabInactive"],
	title  = _("Inactive Mods"),
	description = _("These mods are not activated in any of your savegames.  If you would like to save space, and perhaps speed up FS19 starting, you could remove some or all of these."),
	columns = [
		_("Name"),
		_("Size"),
	],
	columnExtra = {
		"#2": {"minwidth": 0, "width":100, "stretch": 0, "anchor": "e"}
	}
)



#  _     _ __   _ _     _ _______ _______ ______       _______  _____  ______  _______
#  |     | | \  | |     | |______ |______ |     \      |  |  | |     | |     \ |______
#  |_____| |  \_| |_____| ______| |______ |_____/      |  |  | |_____| |_____/ ______|
#                                                                                     

rootWindow.addTab("tabUnused",   underline=0, text=_('Active, Un-Used Mods'))

rootWindow.tabContent["tabUnused"] = ModCheckTreeTab(
	parent = rootWindow.tabFrame["tabUnused"],
	title  = _("Active, Un-Used Mods"),
	description = _("These mods are active in a savegame, but do not seem to be in use. If you do not plan on using them, you could possible remove them.  Please note that some script only or pre-requisite mods may appear here by mistake, so please use this list carefully."),
	columns = [
		_("Name"),
		_("Title"),
		_("Savegame"),
		_("Size")
	],
	columnExtra = {
		"#3": {"minwidth": 0, "width":120, "stretch": 0},
		"#4": {"minwidth": 0, "width":100, "stretch": 0, "anchor": "e"}
	}
)



#  _______ ______   _____  _     _ _______
#  |_____| |_____] |     | |     |    |   
#  |     | |_____] |_____| |_____|    |   
#                                         

rootWindow.addTab("tabAbout",    text=_('About'))

rootWindow.tabContent["tabAbout"] = ModCheckCanvasTab(
	parent      = rootWindow.tabFrame["tabAbout"],
	hideCanvas  = True,
	title       = _("About FS19 Mod Checker"),
	description = _("This little program will take a look at your mod install folder and inform you of the following:"),
	extraText   = [
		"\u2022 " + _("If a mod file is named incorrectly and won't load in the game."),
		"\u2022 " + _("If a mod is not properly zipped."),
		"\u2022 " + _("If a mod is used in your save games, but does not appear to be installed."),
		"\u2022 " + _("If a mod is not loaded or used in any of your save games"),
		"\u2022 " + _("If a mod is loaded but unused in your save games."),
		" ",
		_("This program only offers suggestions, no files on your computer will be altered"),
		" ",
		_("For the latest version, see https://github.com/jtsage/FS19_Mod_Checker")
	]
	
)





# # 
# #  _______  _____  __   _ _______ _____  ______      _______ _______ ______ 
# #  |       |     | | \  | |______   |   |  ____         |    |_____| |_____]
# #  |_____  |_____| |  \_| |       __|__ |_____|         |    |     | |_____]
# #                                                                           
# # 
strings = {
	"info-ask-for-file"    : _("First, you need to point Mod Checker to your gameSettings.xml file"),
	"load-button-label"    : _("Load Settings"),
	"info-game-settings"   : _("Game Settings File: {filename}"),
	"info-ask-process"     : _("Next, click \"{process_button_label}\" to scan your collection"),
	"process-button-label" : _("Check Mods"),
	"info-mods-found"      : _("Mods Found"),
	"info-mods-broken"     : _("Broken Mods"),
	"info-mods-folders"    : _("Folders Found"),
	"info-mods-missing"    : _("Missing Mods")
}


#  _______ _______ _____ __   _              _____   _____   _____ 
#  |  |  | |_____|   |   | \  |      |      |     | |     | |_____]
#  |  |  | |     | __|__ |  \_|      |_____ |_____| |_____| |      
#                                                                  

rootWindow.mainloop()
