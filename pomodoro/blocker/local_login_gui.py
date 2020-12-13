import PySimpleGUI as sg
from timer.api_local import login
import blocker_gui

def login_gui():
    
    """
    creates a local login window
    :return: no return value
    """
    
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Please login here')],
                [sg.Text("User id"), sg.InputText()],
                [sg.Text("Password"), sg.InputText(key='password', password_char='*')],
                [sg.Button('Login'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Login', layout)

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        window.close()

    if event == 'Login':
        token = api_local.login(values[1], values[2])
        if token is None:
            sg.popup("Login unsuccessful, please enter correct user id and password")
            login_gui()
        else:
            window.close()
            blocker_gui.blocker_gui(values[1])

