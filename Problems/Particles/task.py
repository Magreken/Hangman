var1 = input()
var2 = input()

if var1 == "0" and var2 == "0":
    print("Higgs boson Boson")
elif var1 == "1" and var2 == "0":
    print("Photon Boson")
elif var1 == "1/2":
    if var2 == "0":
        print("Muon Lepton")
    elif var2 == "-1":
        print("Electron Lepton")
    elif var2 == "2/3":
        print("Charm Quark")
    elif var2 == "-1/3":
        print("Strange Quark")
