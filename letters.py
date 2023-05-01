letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?',' ']

empty_list =[]
i=input()
indx= letters.index(i)
sh_indx = indx + 3
if sh_indx > len(letters):
    sh_indx =-len(letters)
   # print((letters)[52])
print(letters[sh_indx])