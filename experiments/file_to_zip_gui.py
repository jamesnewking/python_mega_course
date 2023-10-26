import PySimpleGUI as sg
import zip_creator

compressLabel = sg.Text("Files to compress:")
compressInput = sg.Input(key="files")
compressButton = sg.FilesBrowse("Select", button_color="blue")

destinationLabel = sg.Text("Select destination folder:")
destinationInput = sg.Input(key="folder")
destinationButton = sg.FolderBrowse("Select", button_color="blue")
compressedFileNameLabel = sg.Text("Compressed File Name:")
compressedFileName = sg.Input(key="fileName")
actionButton = sg.Button("Compress", button_color="green")
window = sg.Window('Compress Files',
                   layout=[[compressLabel],
                           [compressInput, compressButton],
                           [destinationLabel],
                           [destinationInput, destinationButton],
                           [compressedFileNameLabel],
                           [compressedFileName, actionButton]]
                   )
event, values = window.read()
# print(f"event: {event}")
# print(f"values: {values}")
if values['files'] and values['folder'] and values['fileName']:
    filepaths = values['files'].split(";")
    destination = values['folder']
    fileName = values['fileName']+".zip"
    # print(f"filepaths: {filepaths}")
    # print(f"folder: {destination}")
    # print(f"compressed file name: {fileName}")
    zip_creator.make_archive(filepaths, destination, fileName)
window.close()
