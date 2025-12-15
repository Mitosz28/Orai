def maganhangzot_torol(szoveg):
    maganhangzok="aeiouAEIOU"
    eredmeny=""

    for karakter in szoveg:
        if karakter not in maganhangzok:
            eredmeny+=karakter

    return eredmeny