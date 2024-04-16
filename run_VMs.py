import pyautogui
import time
import os

def run_vm_py(n):
    # Step 1: Press start button
    pyautogui.press('win')
    time.sleep(1)
    
    # Step 2: Type 'terminal' and press enter
    pyautogui.write('anaconda prompt')
    time.sleep(1)
    pyautogui.press('enter')
    
    # Delay to allow time for terminal to open
    time.sleep(1)
    
    # Step 3: Type 'cd idea' and press enter
    pyautogui.write('cd idea')
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    # Step 4: Type 'cd VMs' and press enter
    pyautogui.write('cd VMs')
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    # Step 5: Type 'VM_1' and press enter
    #pyautogui.write(f'cd VM_{number}')
    pyautogui.write(f'cd VM_{n}')
    pyautogui.press('enter')
    
    # Step 6: Type 'python'
    pyautogui.write('python g')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    
def test_vm_py(n):
    # Step 1: Press start button
    pyautogui.press('win')
    time.sleep(1)
    
    # Step 2: Type 'terminal' and press enter
    pyautogui.write('anaconda prompt')
    time.sleep(1)
    pyautogui.press('enter')
    
    # Delay to allow time for terminal to open
    time.sleep(1)
    
    # Step 3: Type 'cd idea' and press enter
    pyautogui.write('cd document')
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    pyautogui.write('cd ideatrade_tradingView')
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    # Step 4: Type 'cd VMs' and press enter
    pyautogui.write('cd VMs')
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    # Step 5: Type 'VM_1' and press enter
    #pyautogui.write(f'cd VM_{number}')
    pyautogui.write(f'cd VM_{n}')
    pyautogui.press('enter')
    
    # Step 6: Type 'python'
    pyautogui.write('python g')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    
    # Step 7: Wait for 10 seconds
    time.sleep(5)

time.sleep(1)
start_VMs = 10
end_VMs = 16
for i in range(start_VMs,1+end_VMs):
    print(i)
    test_vm_py(i)
    time.sleep(1)

 
