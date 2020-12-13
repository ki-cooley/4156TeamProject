#!/usr/bin/env Python3
import PySimpleGUI as sg
import blocker
import sys
import os

def blocker_gui(token):
    
    """   
    :param id: get user id from local login window
    :return: no return value
    """

    if os.geteuid() == 0:
        sg.ChangeLookAndFeel('GreenTan')

        # ------ Menu Definition ------ #
        menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
                    ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                    ['Help', 'About...'], ]

        #   layout = [Personalized_block_list(x) for x in range(1, 6)]
        layout = [
            [sg.Menu(menu_def, tearoff=True)],
            # values[0]
            [sg.Text('Website Blocker', size=(40, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Frame(layout=[
            # social m = values[1], entertainment = 2, shopping = 3
            [sg.Text('social media eg: twitter, facebook, whatsapp ...')],
            [sg.Text('entertainment eg: youtube, hulu, steam, tiktok ...')],
            [sg.Text('shopping eg: amazon, sephora, instagram ...')],
            [sg.Checkbox('social media'),  sg.Checkbox('entertainment'),  sg.Checkbox('shopping')]
            ], title='TYPES',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
            # 4,5,6,7,8
            [sg.Frame(layout=[
                [sg.Text("Please enter a valid domain name, e.g., facebook")],
                [sg.InputText()],
                [sg.InputText()],
                [sg.InputText()],
                [sg.InputText()],
                [sg.InputText()],
            ], title='Personalized block list', title_color='red', relief=sg.RELIEF_SUNKEN,
                tooltip='Use these to set flags')],
            # values[9], 10, 11, 12, 13
            [sg.Frame(layout=[
                [sg.Text('Need a white list of some websites? No Problem!')],
                [sg.InputText()],
                [sg.InputText()],
                [sg.InputText()],
                [sg.InputText()],
                [sg.InputText()],
            ], title='White List', title_color='red', relief=sg.RELIEF_SUNKEN,
                tooltip='Use these to set flags')],
            # values[14], 15, 16, 17
            [sg.Frame(layout=[
                [sg.Text('Please select how long the website blocker should work in minutes :')],
                [sg.Radio('30 mins ', "RADIO1", default=True),
                 sg.Radio('1 hr', "RADIO1"), sg.Radio('2 hr', "RADIO1"), sg.Radio('4 hr', "RADIO1")],
                ],title='REQURIED',title_color='red',relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],

            [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]
        ]


        window = sg.Window('Turn Off Distractions : Stay Focus', layout, default_element_size=(40, 1), grab_anywhere=False)

        event, values = window.read()
        block_time = 0

        window.close()
        #print(event)
        if event == "Submit":
            if values[14]:
                block_time = 30
            if values[15]:
                block_time = 60
            if values[16]:
                block_time = 120
            if values[17]:
                block_time = 240
            blocker.blocker(values, block_time, token)

        if event == 'Submit':
            sg.popup('Congratulation!',
                    'You stayed focused for ' + str(block_time) + ' minute(s)')

    else:
        print("not root. please enter admin password")
        os.execvp('sudo', ['sudo', 'python3'] + sys.argv)
