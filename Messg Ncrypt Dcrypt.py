import random
import sys

#Mixed List of list & symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?',' ']
user_choice = input("Type 'n' to 'encrypt' ,Type 'd' to 'decrypt' :\n")
messg = input('Type Your Messege:\n')
shift_no = int(input('Shift No:\n'))
empty_list = []

def user_direc(dco_nco):
    if dco_nco == 'n':
        for i in messg:
            indx= letters.index(i)
            sh_indx = indx + shift_no

            if sh_indx > len(letters):
                sh_indx -=len(letters)
                print(sh_indx)

            empty_list.append(letters[sh_indx])
            enco_messg = empty_list

        print(f"Here's your Encoded msgg: {''.join(enco_messg)}.")
        enco_messg.clear()

    if dco_nco == 'd':
        deco_messg = []
        for i in messg:
            indx= letters.index(i)
            re_sh_indx = indx - shift_no


            deco_messg += letters[re_sh_indx]   #edit with decoded string

        print(f"Here's your Decoded msgg: {''.join(deco_messg)}.")
        deco_messg.clear()
#        sys.exit(0)   #if no further acess to func.
    
#Nco_Dco Func in action:
user_direc(user_choice)        
#Nxt_stps
nxt_step = input("Are you done with it OR You want to continue? [y/n]\n ")     
    
nxt_step_TF = False
if nxt_step == 'y':
    nxt_step_TF = True

while nxt_step_TF == True:
    if nxt_step == 'y' :
        user_choice = input("Type 'n' to 'encrypt' ,Type 'd' to 'decrypt' :\n")
        messg = input('Type Your Messege:\n')
        shift_no = int(input('Shift No:\n'))
        user_direc(user_choice)
        nxt_step = input("Are you done with it OR You want to continue? [y/n]\n ")     
        if nxt_step == 'n':
            nxt_step_TF = False
