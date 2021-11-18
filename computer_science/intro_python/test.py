alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]

mot = input("donner le message a coder : ")
n = int(input("Incrémentation: "))

mot_liste = list(mot)

crypt_list = []
# in=0
# print(mot_liste)
for i in range(len(mot_liste)):


    if mot_liste[i] != ' ':

        ind = alphabet.index(mot_liste[i])
        yo = alphabet[ind + n]
        crypt_list.append(yo)

    else :
        crypt_list.append(' ')

print(''.join(crypt_list))