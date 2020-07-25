import pyqrcode as qr

#print("Welcome to Appu's QR code generator!", end="\n\n")
#
#print("Type below the info you want into your qr code:")
#data = input("> ")
#
#print("\nDo you want it to be saved into a file?\n(Type the name of the file below or leave empty for no file)")
#filename = input("> ")
#save = len(filename) > 0
#
#qrcode = pyqrcode.create(data)
#if save:
#    qrcode.png(filename + ".png")
#print(qrcode.terminal(quiet_zone=2))

print("""\
Type of info to save to the QR code?
[1] - Plain text
[2] - Wi-Fi network
[3] - Image
[4] - None
[5] - None
""")

option = int(input("> "))

print("\nDo you want it to be saved into a png?\n(Type the name of the file below or leave empty to print it out to the terminal)")
filename = input("> ")
save = len(filename) > 0

if option == 1:
    data = input("\nType the text to be saved into the QR:\n> ")
    qrcode = qr.create(data)
    if save:
        qrcode.png(filename + ".png")
    print(qrcode.terminal(quiet_zone=2))
elif option == 2:
    wifi_name = input("Wifi name:\n> ")
    wifi_encryption = input("Wifi encryption type:\n> ")
    wifi_password = input("Wifi password:\n> ")
    qrcode = qr.create("WIFI:S:" + wifi_name + ";T:" + wifi_encryption + ";P:" + wifi_password + ";;")
    if save:
        qrcode.png(filename + ".png")
    print(qrcode.terminal(quiet_zone=2))
elif option == 3:
    print("Option 3")
elif option == 4:
    print("Option 4")
elif option == 5:
    print("Option 5")
else:
    print("Patata")