import time

def afficher_horloge():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print("\r" + current_time, end="")
        time.sleep(1)

afficher_horloge()





