import PySimpleGUI as sg

sg.theme('DarkAmber')
# All the stuff inside your window.
layout = [  [sg.Text('Please login here')],
            [sg.Text("User id"), sg.InputText()],
            [sg.Text("Password"), sg.InputText(key='password', password_char='*')],
            [sg.Button('Login'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Login', layout)

# Event Loop to keep reading until login info matches
while True:
    login = False
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user clicks cancel or close, window will close, no successful login
        break
    if event == 'Login': # if user clicks login and info matches, window will close, login successful
        if values[1] and values[2]:
            login = True
            break

window.close()
