import oGUI

oGUI.init()

checkbox = oGUI.Checkbox(oGUI.gray, oGUI.orange, 125, 150, 20, 20)
rect = oGUI.Rect(oGUI.darkgray, 100, 100, 300, 500)
button = oGUI.Button(oGUI.gray, oGUI.orange, 120, 200, 30, 30)
button2 = oGUI.Button(oGUI.darkgray, oGUI.lightgray, 368, 103, 30, 35)
myText = oGUI.Text(oGUI.orange, 195, 110, 30, "oGUI Demo")
while True:
    oGUI.startLoop() #Start of Draw Loop
    rect.draw() #Drawing Rectangle, Box, Checkbox, and Button
    checkbox.draw()
    button.draw()
    button2.draw()
    myText.draw() #Drawing Text
    oGUI.endLoop() #End of Draw Loop
    myText.font('Roboto')
    myText.dropShadow(oGUI.black, 2) #Setting Text Object's DropShadow
    
    if button.is_enabled(): #Do something if the button is enabled/pressed
        print('Button was pressed')