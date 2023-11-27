"""Module Containing helper functions for the app."""
from io import BytesIO
from django.utils import timezone
from cryptography.fernet import Fernet


def encrypt_user_event(user, event):
    """Encrypts the user and event information to be stored in the QR code."""
    user_email = user.email
    encryption_key = event.encryption_key
    user_imei = user.imei
    event_uuid = event.uuid
    msg = event_uuid + user_email + user_imei
    encrypted_msg = encryption_key.encrypt(msg)

    return encrypted_msg

