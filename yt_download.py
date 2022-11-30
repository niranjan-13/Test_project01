import pyautogui,time
time.sleep(7)
for i in range(1):
    #pyautogui.moveTo(630,589,duration=1.0) #Active Window
    pyautogui.moveTo(565,631,duration=1.0) #Active Window
    pyautogui.click() #Active Window
    time.sleep(2)
    #pyautogui.moveTo(476,625,duration=0.75)#Share
    pyautogui.moveTo(480,665,duration=0.75)#Share
    pyautogui.click()
    time.sleep(2)
    #pyautogui.moveTo(466,430,duration=0.75)#Copy
    pyautogui.moveTo(475,433,duration=0.75)#Copy
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(762,438,duration=0.75)#Active another window
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1190,327,duration=0.75)#Clear
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('ctrl','v')#Paste the lInk
    time.sleep(9)
    pyautogui.moveTo(925,527,duration=0.75)#Download Right Click
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.moveTo(943,207,duration=0.75)#Open in new window
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(854,463,duration=0.5)#Drag the Title
    pyautogui.click()
    pyautogui.drag(300,0,duration=2.5)
    time.sleep(2)
    pyautogui.hotkey('ctrl','c')#Copy the Title
    time.sleep(2)
    pyautogui.moveTo(1003,24,duration=0.75)#Go to Download Window
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1053,378,duration=0.5)#Right Click on Video
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.write('v')
    time.sleep(2)
    pyautogui.hotkey('ctrl','v')#Paste the Title
    time.sleep(1)
    pyautogui.moveTo(1202,448,duration=0.5)#Save the Video
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('ctrl','w')#Close the Window
    time.sleep(3)
    pyautogui.moveTo(403,20,duration=0.75)#Previous Window Active
    pyautogui.click()
    pyautogui.moveTo(564,631,duration=1.0) #Active Window
    pyautogui.click() #Active Window
    time.sleep(2)
    #pyautogui.moveTo(85,486,duration=1.5) #Skip Next 
    pyautogui.moveTo(85,486,duration=1.5) #Skip Next 
    pyautogui.click() 
    time.sleep(10)
    pyautogui.moveTo(340,309,duration=1.5) #Pause Video
    pyautogui.click() 
    time.sleep(5)
