import PySimpleGUI as sg
cycle = True
feetLabel = sg.Text("Enter feet:")
feetInput = sg.Input(key="feet")

inchLabel = sg.Text("Enter inches:")
inchInput = sg.Input(key="inches")
convertButton = sg.Button("Convert", button_color="green")
outputText = sg.Text("", key="output")
meterText = sg.Text("m", key="meter")
errorText = sg.Text("", key="error", text_color="red")
window = sg.Window('Inch Converter',
                   layout=[[feetLabel, feetInput],
                           [inchLabel, inchInput],
                           [convertButton, outputText, meterText],
                           [errorText]]
                   )
while cycle:
    event, values = window.read()
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

window.close()
