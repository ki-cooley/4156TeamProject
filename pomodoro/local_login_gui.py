import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Please login here')],
            [sg.Text("User id"), sg.InputText()],
            [sg.Text("Password"), sg.InputText(key='password', password_char='*')],
            [sg.Button('Login'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Login', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Login': # if user closes window or clicks cancel
        break

window.close()