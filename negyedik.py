def elmozdulas(utvonal):
    vizszintes = 0
    fuggoleges = 0

    for lepes in utvonal:
        if lepes == "F":
            fuggoleges += 1
        elif lepes == "L":
            fuggoleges -= 1
        elif lepes == "J":
            vizszintes += 1
        elif lepes == "B":
            vizszintes -= 1

    if vizszintes == 0 and fuggoleges == 0:
        return "Nem mentunk sehova"

    return f"Vízszintes elmozdulás: {vizszintes}, Függőleges elmozdulás: {fuggoleges}"

