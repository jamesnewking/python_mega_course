import PySimpleGUI as sg

compressLabel = sg.Text("Files to compress:")
compressInput = sg.Input(key="files")
compressButton = sg.FilesBrowse("Select")

destinationLabel = sg.Text("Select destination folder:")
destinationInput = sg.Input(key="destination")
destinationButton = sg.FolderBrowse("Select")

actionButton = sg.Button("Compress")
window = sg.Window('Compress Files',
                   layout=[[compressLabel],
                           [compressInput, compressButton],
                           [destinationLabel],
                           [destinationInput, destinationButton],
                           [actionButton]]
                   )
event = window.read()
print(event)
window.close()