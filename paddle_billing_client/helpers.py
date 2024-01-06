import hashlib
import hmac


def validate_webhook_signature(
    signature_header: str, raw_body: bytes, secret_key: str
) -> bool:
    """
    Validate a Paddle webhook signature.
    More info: https://developer.paddle.com/webhooks/signature-verification

    :param signature_header: The Paddle-Signature header value.
    In Django for example, this is request.META['HTTP_PADDLE_SIGNATURE'].
    :param raw_body: The raw body of the request.
    :param secret_key: The secret key used to generate the signature.
    """
    ts_part, h1_part = signature_header.split(";")
    var, timestamp = ts_part.split("=")
    var, signature = h1_part.split("=")

    signed_payload = ":".join([timestamp, raw_body.decode("utf-8")])

    # Paddle generates signatures using a keyed-hash message authentication code (HMAC) with SHA256 and a secret key.
    computed_signature = hmac.new(
        key=secret_key.encode("utf-8"),
        msg=signed_payload.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()

    # Compare the computed signature with the signature extracted from the Paddle-Signature header.
    return hmac.compare_digest(computed_signature, signature)
