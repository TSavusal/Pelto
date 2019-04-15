ELAIMET = {
    "a": "aasi",
    "k": "koira",
    "@": "kissa",
    "h": "hemuli",
    "l": "lammas"
}

def tutki_ruutu(merkki, x, y):
    if merkki == " ":
        pass
    else:
        print("Ruudusta", (x, y), "löytyy", ELAIMET[merkki])
    
def tutki_kentta(pelto):
    list1 = list(enumerate(pelto[0:]))
    for i, k in list1:
        print(list(enumerate(k, start=1)))
    for y in list1:
        for x in y:
            tutki_ruutu(x, xindex, yindex)
    #for i, k in list1:
        #list2.append(list(enumerate(k, start=1)))
            #[[(1, ' '), (2, 'a'), (3, ' '), (4, ' '), (5, 'l')],
            #[(1, ' '), (2, 'k'), (3, '@'), (4, 'k'), (5, ' ')],
            #[(1, 'h'), (2, ' '), (3, 'a'), (4, 'k'), (5, ' ')]]