from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import PySimpleGUI as sg
import os
import sys

direct = "insert path google account "
pathconfigC = "insert path file config1" //backup
pathconfigT = "insert path file config2" //backup
pathconfigP = "insert pat file config3"	//backup

def restart():
        os.execv(sys.executable, [sys.executable, "insert path folder autom2" ]+sys.argv)

def getfilePrince():
    cont=0
    with open(pathconfigP,"r") as infile:
        for x in infile:
            x=x.rstrip()
            cont+=1
            window.FindElement(f'-IN3-{cont}-').Update(x)


def getfileType():
    cont=0
    with open(pathconfigT,"r") as infile:
        for x in infile:
            x=int(x)
            cont+=1
            window.FindElement(f'-IN2-{cont}-').Update(x)


def getfileCategory():
    cont=0
    with open(pathconfigC,"r") as infile:
        for x in infile:
            x=int(x)
            cont+=1
            window.FindElement(f'-IN1-{cont}-').Update(x)

def writefilePrince(var):
    text_file=open(pathconfigP,"w")
    for x in range(1,var+1):
        text_file.write(value[f'-IN3-{x}-']+'\n')
    text_file.close()

def writefileType(var):
    text_file=open(pathconfigT,"w")
    for x in range(1,var+1):
        text_file.write(value[f'-IN2-{x}-']+'\n')
    text_file.close()

def writefileCategory(var):
    text_file=open(pathconfigC,"w")
    for x in range(1,var+1):
        text_file.write(value[f'-IN1-{x}-']+'\n')
    text_file.close()


def sendlink(urlpath, dirpath):
    options=Options()
    options.add_argument(dirpath)
    options.add_argument("profile-directory=Profile 2")
    web = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    web.get(urlpath)
    web.maximize_window()
    return web




def addrange(var, web):
    '''time.sleep(3)'''

    connect=WebDriverWait(web, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/form/div[3]/div[2]/button'))).click()
    print("questa è connect",connect)
    ventes=WebDriverWait(web,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/section[2]/div/form/div[1]/div/div/div/div[1]/div/div/div/div[4]/div/div[2]/div/div/label")))
    web.execute_script("arguments[0].scrollIntoView();", ventes)
    select = WebDriverWait(web, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section[2]/div/form/div[1]/div/div/div/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div/span[2]/a")))
    web.execute_script("arguments[0].click();", select)
    var = var-1
    for x in range(var):
        time.sleep(1)
        select = WebDriverWait(web, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section[2]/div/form/div[1]/div/div/div/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div/span[2]/a")))
        web.execute_script("arguments[0].click();", select)


    time.sleep(3)


def addCategory(selectbotton, category, div, web):
    WebDriverWait(web, 2).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/section[2]/div/form/div[1]/div/div/div/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div/span[1]/table/tbody/tr[{selectbotton}]/td[3]/div/a/span[1]"))).click()
    WebDriverWait(web, 2).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[{div}]/ul/li/ul/li[{category}]/div"))).click()

def addType(selectbotton, types, div, web):
    WebDriverWait(web, 2).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[1]/div/section[2]/div/form/div[1]/div/div/div/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div/span[1]/table/tbody/tr[{selectbotton}]/td[4]/div/a/span[1]"))).click()
    WebDriverWait(web, 2).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[{div}]/ul/li/ul/li[{types}]/div"))).click()

def addPrix(selectBotton, prix, web):
    text=WebDriverWait(web, 2).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[1]/div/section[2]/div/form/div[1]/div/div/div/div[1]/div/div/div/div[4]/div/div[2]/div/div/div/div/span[1]/table/tbody/tr[{selectBotton}]/td[7]/input")))
    text.send_keys(f"{prix}")

sg.theme('DarkAmber')

if __name__ == '__main__':
  layout = [
           [sg.Text("Autom v2.0")],
           [sg.Text('Paste url')],
           [sg.InputText()],
           [sg.Text('Paste directory')],
           [sg.InputText(f'{direct}')],
           [sg.Text('Ajouter Ventes', justification='center')],
           [sg.InputText(size=(4, 4), justification='center'), sg.Button('Confirmation')],
           [sg.Frame('Lista Categorie', [[sg.Text('Categorie', pad=(130, 0)), sg.Text('Tipo', pad=(160, 0)), sg.Text('Prezzo', pad=(135, 0))]], key='keyframe')],
           [sg.Button('Invia',size=(10,0),disabled=True), sg.Exit(),sg.Button('Restart'),sg.Button("Emergenza",button_color="blue",disabled=True)]]

  window = sg.Window('Autom',resizable=True,size=(1045,600),finalize=True).Layout([[sg.Column(layout=layout, scrollable=True,size=(1045,600))]])

  num_buttons = 0
  check = False
  check1 = False
  while True:                             # The Event Loop

        event,value = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
                break
        if event == 'Confirmation' and value[2]=='':
            sg.popup('Cretino devi mettere un numero ok??')
        if event == 'Confirmation' and value[2]!='':
                 window['Confirmation'].update(disabled=True)
                 num_buttons += int(value[2])
                 for x in range(1, num_buttons+1):
                    window.extend_layout(window['keyframe'], [[sg.Text(f'{x}', key=f'-IN0-{x}-'), sg.InputText(justification='center', key=f'-IN1-{x}-'), sg.InputText(justification='center', key=f'-IN2-{x}-'), sg.InputText(justification='center', key=f'-IN3-{x}-')]])
                 window.set_min_size(size=(1045,601))
                 window['Emergenza'].update(disabled=False, button_color='red')
                 window['Invia'].update(disabled=False)

        if event == 'Emergenza' :
            getfileCategory()
            getfileType()
            getfilePrince()

        if event == 'Restart':
            restart()


        if event == 'Invia' and value[0]!= '' and value[1]!= '':
                   var=int(value[2])
                   cont=4

                   writefileCategory(var)
                   writefileType(var)
                   writefilePrince(var)

                   web = sendlink(value[0], value[1])
                   addrange(int(value[2]), web)
                   for x in range(1, var+1):
                       addCategory(x, int(value[f'-IN1-{x}-']), cont, web)
                       cont += 1
                       addType(x, int(value[f'-IN2-{x}-']), cont, web)
                       cont += 1

                   check=True

                   for x in range(1,var+1):
                       addPrix(x,value[f'-IN3-{x}-'],web)

                   check1=True


        if(check== True and check1== True):
                    sg.popup('Tutto fatto!')
  window.close()


