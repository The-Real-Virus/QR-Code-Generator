import qrcode
import sys
import os
from PIL import Image

# Function to display banner
def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  QR-Code-Generator
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

# Show banner at script startup
show_banner()

# Ask user for input
choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()

if choice == 'n':
    print("\nExiting the script. Goodbye!")
    exit()
elif choice == 'y':
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen on Linux/Mac ('clear') or Windows ('cls')
else:
    print("\nInvalid choice. Exiting the script.")
    exit()

def logo():
    logo = r"""

 ██████╗ ██████╗        ██████╗ ██████╗ ██████╗ ███████╗
██╔═══██╗██╔══██╗      ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║   ██║██████╔╝█████╗██║     ██║   ██║██║  ██║█████╗  
██║▄▄ ██║██╔══██╗╚════╝██║     ██║   ██║██║  ██║██╔══╝  
╚██████╔╝██║  ██║      ╚██████╗╚██████╔╝██████╔╝███████╗
 ╚══▀▀═╝ ╚═╝  ╚═╝       ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                                                                                 
"""
    print(logo)

# Function to generate QR code
def generate_qr():
    url = input("Enter the URL to generate a QR code: ")
    if not url.startswith("http"):
        print("Invalid URL! Please enter a valid URL (starting with http/https).")
        sys.exit(1)
    
    # Customization options
    fill_color = input("Enter the QR code color (e.g., black, blue, red): ") or "black"
    back_color = input("Enter the background color (e.g., white, yellow): ") or "white"
    
    qr = qrcode.QRCode(
        version=2,  # Slightly larger QR code for better scanning
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (30%)
        box_size=15,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img_path = "custom_qr_code.png"
    img.save(img_path)
    
    print(f"QR Code successfully generated and saved as {img_path}!")
    
    # Show the QR code after generation
    img.show()

if __name__ == "__main__":
    logo()
    generate_qr()
