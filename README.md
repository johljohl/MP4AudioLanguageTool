# MP4AudioLanguageTool

Description
This application is designed to change the language code of audio tracks in MP4 video files. It's useful for adjusting the language metadata in MP4 files to the correct language, based on a selection of predefined languages and their ISO 639-2 codes.

Prerequisites
Python 3 must be installed on your computer.
The GPAC software, specifically the MP4Box tool, should be installed. It can be downloaded from the official GPAC website.
The program uses Tkinter for the GUI, which is typically included in the standard Python installation.

Installation and Configuration
Ensure Python 3 and GPAC are installed on your computer.
Copy the script code into a Python file, for example, language_changer.py.
Run the script by opening a terminal and typing python language_changer.py.

Usage
Launch the program; a GUI window should appear.
Click "Browse" to select an MP4 file whose language code you wish to change.
Choose the desired language from the dropdown menu.
Click "Change Language" to initiate the process. A progress window shows that the operation is underway.
A message will display once the language has been successfully changed.

Error Handling
If a non-MP4 file is selected, an error message will be displayed.
Any errors during the process will also be shown in an error message.

Extending the Program
You can add more languages to the languages dictionary. Make sure to use the correct ISO 639-2 codes.
Customize the path to MP4Box if necessary, depending on your installation.

Note
This tool only changes the language code of the audio track and does not affect the actual audio content.
Use the tool responsibly and only on files where you have the right to make changes.
