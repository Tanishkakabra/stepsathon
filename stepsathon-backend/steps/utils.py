import qrcode
from io import BytesIO
from django.utils import timezone

def generate_qr_code(event, user):
    # Combine event information, user details, and a timestamp
    qr_data = f"Event: {event.name}\nUser: {user.username}\nTime: {timezone.now()}"

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create a QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to bytes
    buffer = BytesIO()
    qr_img.save(buffer, format="PNG")
    qr_image_data = buffer.getvalue()
    buffer.close()

    return qr_image_data
