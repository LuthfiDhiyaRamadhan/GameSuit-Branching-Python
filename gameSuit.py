import random
komputer = random.choice (['G','K','B'])
#print(f"Komputer memilih{komputer}")
print("Komputer telah memilih. Sekarang giliran anda")
player = input(" Pilihan Anda {G,K,B}").upper()
#draw=0, komputer menang=1,player menang=2
if (komputer=="G") and (player=="G"):
    print("Komputer memilih gunting.draw!")
elif(komputer == "G") and (player == "k"):
    print("Komputer memilih gunting. anda kalah!")
elif(komputer=="G") and (player=="B"):
    print("Komputer memilih gunting.anda menang!")
elif komputer =="K":
    print("Komputer memilih kertas.", end="")
    if player == "G":
        print("anda menang!")
    elif player == "K":
        print("Draw!")
    elif player == "B":
        print("anda Kalah!")
elif komputer =="B":
    print("Komputer memilih batu.",end="")
    if player=="G":
        print("anda kalah!")
    elif player=="K":
        print("anda menang!")
    elif player=="B":
        print("Draw!")