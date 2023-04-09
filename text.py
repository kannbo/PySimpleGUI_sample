import PySimpleGUI as sg
import sys
texts=sys.argv
if not len(sys.argv)==1:
    texts=sys.argv[1:]
layout=[[sg.Text("",key="text")],
        [sg.Button("→",key="Button")]]
text=sg.Window("hello",layout,size=(300, 100))
a=0
while True:
    event,values=text.read()
    if event==sg.WINDOW_CLOSED:
        break
    elif event=="Button":
        a=a+1
        text["text"].update(texts[a%len(texts)])
