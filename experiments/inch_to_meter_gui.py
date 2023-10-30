import PySimpleGUI as sg
sg.theme("Black")
feetLabel = sg.Text("Enter feet:")
feetInput = sg.Input(key="feet")
inchLabel = sg.Text("Enter inches:")
inchInput = sg.Input(key="inches")
convertButton = sg.Button("Convert", key="convert", button_color="green")
outputText = sg.Text("", key="output")
meterText = sg.Text("m", key="meter")
errorText = sg.Text("", key="error", text_color="red")
exitButton = sg.Button("Exit", key="exit", button_color="red")
window = sg.Window('Inch Converter',
                   layout=[[feetLabel, feetInput],
                           [inchLabel, inchInput],
                           [convertButton, exitButton, outputText, meterText],
                           [errorText]
                           ]
                   )
while True:
    event, values = window.read()
    match event:
        case "convert":
            convertFeet = values['feet']
            convertInches = values['inches']
            if convertFeet.isnumeric() and convertInches.isnumeric():
                totalInches = float(convertFeet) * 12 + float(convertInches)
                totalMeters = totalInches / 39.37
                window['output'].update(value=round(totalMeters,3))
                window['error'].update(value='')

            else:
                window['feet'].update(value='')
                window['inches'].update(value='')
                window['output'].update(value='')
                window['error'].update(value='* Must be whole numbers *')
        case "exit" | sg.WIN_CLOSED:
            break

window.close()
