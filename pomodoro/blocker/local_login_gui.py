import PySimpleGUI as sg
import os
import sys
from api_local import login
import blocker_gui
import platform

def login_gui():
    
    """
    creates a local login window
    :return: no return value
    """

    if os.geteuid() == 0:
        sg.theme('DarkAmber')   # Add a touch of color
        # All the stuff inside your window.
        layout = [  [sg.Text('Please login here')],
                    [sg.Text("User Name"), sg.InputText()],
                    [sg.Text("Password"), sg.InputText(key='password', password_char='*')],
                    [sg.Button('Login'), sg.Button('Cancel')] ]

        # Create the Window
        window = sg.Window('Login', layout)

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()

        if event == 'Login':
            if values[0] != '' and values['password'] != '':
                token = login(values[0], values['password'])
                if token is None:
                    sg.popup("Login unsuccessful, please enter correct user name and password")
                    login_gui()
                else:
                    window.close()
                    blocker_gui.blocker_gui(token)
            else:
                sg.popup("Login unsuccessful, please enter correct user name and password")
                login_gui()

    else:
        print("not root. please enter admin password")
        if platform.system() == "Linux" or platform.system() == "Darwin":
            os.execvp('sudo', ['sudo', 'python3'] + sys.argv)

login_gui()
