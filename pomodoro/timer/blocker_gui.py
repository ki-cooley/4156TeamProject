#!/usr/bin/env Python3
import PySimpleGUI as sg
from blocker import blocker
import sys
import os


if os.geteuid() == 0:
    sg.ChangeLookAndFeel('GreenTan')

  #  layout = [Personalized_block_list(x) for x in range(1, 6)] + [[sg.Button('Save'), sg.Button('Exit')]]

    # ------ Menu Definition ------ #
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'], ]

    # ------ Column Definition ------ #
    column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

 #   layout = [Personalized_block_list(x) for x in range(1, 6)]
    layout = [
        [sg.Menu(menu_def, tearoff=True)],
        # 0
        [sg.Text('Website Blocker', size=(40, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Frame(layout=[
            # social m = 1, entertainment = 2, shopping = 3
        [sg.Text('social media eg: twitter, facebook, whatsapp ...')],
        [sg.Text('entertainment eg: youtube, hulu, steam, tiktok ...')],
        [sg.Text('shopping eg: amazon, saphora, instagram ...')],
        [sg.Checkbox('social media'),  sg.Checkbox('entertainment'),  sg.Checkbox('shopping')]
             ], title='TYPES',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
        # 4,5,6,7,8
        [sg.Frame(layout=[
            [sg.Text("Please enter a valid domain name")],
            [sg.InputText()],
            [sg.InputText()],
            [sg.InputText()],
            [sg.InputText()],
            [sg.InputText()],
        ], title='Personalized Block List', title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
        # 9, 10, 11, 12, 13
        [sg.Frame(layout=[
            [sg.Text('Need a white list of some websites? No Problem!')],
            [sg.InputText()],
            [sg.InputText()],
            [sg.InputText()],
            [sg.InputText()],
            [sg.InputText()],
        ], title='White List', title_color='red', relief=sg.RELIEF_SUNKEN,
            tooltip='Use these to set flags')],
        # 14, 15, 16, 17
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
    while True:
        if values[14]:
            block_time = 30
            break
        if values[15]:
            block_time = 60
            break
        if values[16]:
            block_time = 120
            break
        if values[17]:
            block_time = 240
            break

    window.close()
    #print(event)
    blocker(values, 2)
    print(values)


    if event != 'Cancel':
        sg.popup('Congratulation!',
                'You stayed focused for ' + str(block_time) + ' minute(s)')

else:
    print("not root. please enter admin password")
    os.execvp('sudo', ['sudo', 'python3'] + sys.argv)