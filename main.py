import PySimpleGUI
from archive_extractor import archive_extract

PySimpleGUI.theme('DarkPurple4')

label1 = PySimpleGUI.Text("Select the file to extract: ")
input1 = PySimpleGUI.Input()
button1 = PySimpleGUI.FileBrowse('Choose', key='file')

label2 = PySimpleGUI.Text("Select destination folder: ")
input2 = PySimpleGUI.Input()
button2 = PySimpleGUI.FolderBrowse('Choose', key='folder')

extract_button = PySimpleGUI.Button("Extract")
output_label = PySimpleGUI.Text(key='output', text_color='green')

col1 = PySimpleGUI.Column([[label1], [label2]])
col2 = PySimpleGUI.Column([[input1], [input2]])
col3 = PySimpleGUI.Column([[button1], [button2]])

window = PySimpleGUI.Window('Archive Extractor. Created by - RJB', 
                            layout=[[col1, col2, col3],
                                    [extract_button, output_label]],
                                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    try:        
        file = values['file']
        folder = values['folder']
        archive_extract(file, folder)
        window['output'].update(value="Extraction Completed Succesfully.")
        window.read()
    except TypeError:
        break
    
    if PySimpleGUI.WIN_CLOSED:
        break
    
window.close()