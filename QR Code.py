import qrcode
import os
print("-------QR CODE GENERATOR-------")
data=input("Enter the text or URL:")
img=qrcode.make(data)
file_name=input("enter the filename(without.png):")

print(f"\n QR Code Generated Successfully!")
print(f"Saved as:{file_name}.png")


save_path = os.path.join(os.getcwd(), file_name + ".png")
img.save(save_path)

print("Saved at:", save_path)
