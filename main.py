import pyautogui, pyperclip
import webbrowser
import time


# Time sleeping durations
dt = 2
dt1 = 1
dt2 = 0.5
dt3 = 4

draggingDuration = 0.5
# entering the new password
passWord = input("enter the new password =>")
passWord1 = input("re enter your password =>")
while passWord != passWord1:
    print("ERROR: the passwords don't match...")
    passWord = input("enter the new password =>")
    passWord1 = input("re enter your password =>")

# opening the website
webbrowser.open("http://192.168.1.1/login_security.html")

# getting back to the browser
webX = 217
webY = 755

pyautogui.moveTo(webX, webY, draggingDuration)


pyautogui.click()

adminX = 677
adminY = 301
pyautogui.moveTo(adminX, adminY, draggingDuration)
time.sleep(dt * 3)
# entering the password and the stuffs
pyautogui.click()
pyautogui.typewrite("admin")
pyautogui.typewrite("\t")
pyautogui.typewrite("admin")
pyautogui.press("enter")   # this is a hot key
# moving to interface setup
interfaceX = 566
interfaceY = 160
pyautogui.moveTo(interfaceX, interfaceY, draggingDuration)
time.sleep(dt3)
pyautogui.click()
# moving to wireless
wirelessX = 684
wirelessY = 209
pyautogui.moveTo(wirelessX, wirelessY, draggingDuration)
pyautogui.click()
time.sleep(dt1)
# move to another place before scrolling down
pyautogui.moveTo(1286, 345)
pyautogui.vscroll(-10000)
# move to the field of the password coordinates
passX = 671
passY = 251
pyautogui.moveTo(passX, passY, draggingDuration)
pyautogui.click()
pyautogui.hotkey("ctrl", "a")
pyautogui.typewrite(passWord)
time.sleep(1)
# go to the save button
saveX = 645
saveY = 746
pyautogui.moveTo(saveX, saveY, draggingDuration)
pyautogui.click()
time.sleep(dt3 * 2)
# THE second part of entering the password in my laptop & creating a bot that i can run from windows running
wifiX = 1206
wifiY = 767
pyautogui.moveTo(wifiX, wifiY, draggingDuration)
time.sleep(dt)
pyautogui.click()
networkX = 1088
networkY = 639

pyautogui.moveTo(networkX, networkY, draggingDuration)

time.sleep(dt*3)
pyautogui.click()
manageX = 468
manageY = 304
pyautogui.moveTo(manageX, manageY, draggingDuration)
time.sleep(dt * 2)
pyautogui.click()
forgetX = 134
forgetY = 203
pyautogui.moveTo(forgetX, forgetY, draggingDuration)
time.sleep(dt)
pyautogui.click()
# Type in forget button
forgetButtonX = 406
forgetButtonY = 253
pyautogui.moveTo(forgetButtonX, forgetButtonY, draggingDuration)
pyautogui.click()
# go back to the wifi
pyautogui.moveTo(wifiX, wifiY, draggingDuration)
pyautogui.click()
time.sleep(dt * 2)

# connecting to tp link
tpX = 1154
tpY = 197
pyautogui.moveTo(tpX, tpY, draggingDuration)
pyautogui.click()
# the connect button
connectX = 1257
connectY = 282
pyautogui.moveTo(connectX, connectY, draggingDuration)
pyautogui.click()
time.sleep(1)

pyautogui.typewrite(passWord)
time.sleep(1)
# next button
nextX = 1104
nextY = 351
pyautogui.moveTo(nextX, nextY, draggingDuration)
pyautogui.click()














