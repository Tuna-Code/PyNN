import PySimpleGUI as sg

sg.theme('DarkBlue')

layout = [[sg.Text('Please Select a Network to Load')],
          [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse(file_types=(("NN Configuration Files", "*.conf"),))],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Network Loader', layout, location=(3439,343))

event, values = window.read()
window.close()
print(f'You chose Network: {values[0]}')