import os

# === Customize your QR code here ===
DATA_TO_ENCODE = "https://ForgeXdigital.site"       # The URL or text you want to encode
OUTPUT_FOLDER = "qr_codes"                   # Folder where QR code image will be saved
OUTPUT_FILENAME = "T3STER.png"            # Filename of QR code image (png or svg)

# Optional QR code settings
VERSION = 2             # QR version (1 to 40)
ERROR_CORRECTION = 'M'  # Error correction level: L, M, Q, H
BOX_SIZE = 10           # Size of each box in pixels
BORDER = 4              # Border thickness (boxes)
FILL_COLOR = "black"    # Color of the QR code dots
BACK_COLOR = "white"    # Background color

def generate_qr():
    import qrcode as qr_lib
    import qrcode.image.svg
    import os

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created folder '{OUTPUT_FOLDER}'")

    output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILENAME)

    error_correction_map = {
        'L': qr_lib.constants.ERROR_CORRECT_L,
        'M': qr_lib.constants.ERROR_CORRECT_M,
        'Q': qr_lib.constants.ERROR_CORRECT_Q,
        'H': qr_lib.constants.ERROR_CORRECT_H,
    }

    if ERROR_CORRECTION not in error_correction_map:
        raise ValueError("Invalid error correction level. Choose from L, M, Q, H.")

    qr = qr_lib.QRCode(
        version=VERSION,
        error_correction=error_correction_map[ERROR_CORRECTION],
        box_size=BOX_SIZE,
        border=BORDER,
    )
    qr.add_data(DATA_TO_ENCODE)
    qr.make(fit=True)

    ext = os.path.splitext(OUTPUT_FILENAME)[1].lower()
    if ext == '.svg':
        factory = qr_lib.image.svg.SvgImage
        img = qr.make_image(image_factory=factory)
        img.save(output_path)
    else:
        img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)
        img.save(output_path)

    print(f"QR code saved at '{output_path}'")

if __name__ == "__main__":
    generate_qr()
