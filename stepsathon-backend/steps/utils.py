"""Module Containing helper functions for the app."""
from io import BytesIO
from django.utils import timezone
from cryptography.fernet import Fernet


def encrypt_user_event(user, event):
    user_email = user.email
    encryption_key = event.encryption_key
    event_uuid = event.uuid
    msg = event_uuid + user_email
    encrypted_msg = encryption_key.encrypt(msg)

    return encrypted_msg




"""

#someway to import the database, i forgot how to work in sql lol. imma assume db = database

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


def login_valid(user):
    # Check if the user is already logged in
    if user.is_authenticated:
        return False, "You are already logged in"
    if user.username not in db.username:
        return False, "No such user exists"
    #check if password matches, if not:
        return False, "Incorrect Password"
    #check if IMEI matches, if not:
        return False, "Login from original device please"

    # Check if the user is registered for the event
    # if not event.users.filter(pk=user.pk).exists():
    #     return False, "You are not registered for this event"

    # # Check if the user is registered for the event
    # if event.users.filter(pk=user.pk).first().attended:
    #     return False, "You have already attended this event"

    return True, "Login Successful!!"

def register_user(name, password, IMEI):
    user = CustomUser(name=name, password=password, IMEI=IMEI)
    if user.name in db.username:
        return False, "username already exists"
    #push this information in the database
    #also find a way to extract IMEI lmao, not sure if backend can extract IMEI or frontend
    return True, "Created a new user"



    
"""