import PySimpleGUI as sg


class Gui:
    

    def file_select(self):
        sg.theme('DarkBlue')

        layout = [[sg.Text('Please Select a Network to Load')],
                [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FolderBrowse(initial_folder="Data",)],
                [sg.Submit(), sg.Cancel()]]

        window = sg.Window('Network Loader', layout, location=(3439,343))

        event, values = window.read()
        window.close()
        #print(f'You chose Network: {values[0]}')
        
        
        return values[0]
    
 