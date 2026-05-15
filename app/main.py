from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import razorpay
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = razorpay.Client(
    auth=(
        "rzp_test_Sp8cEV0iWpweoq",
        "K7tbHHEY348sSmDNMMiMUxCq"
    )
)

@app.get("/")
def home():
    return {"message":"Backend Running"}

@app.post("/create-order")
def create_order(data: dict):

    amount = int(data["amount"])

    order = client.order.create({
        "amount": amount * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    return order
import hmac
import hashlib
from fastapi import Request

@app.post("/verify-payment")
async def verify_payment(request: Request):

    data = await request.json()

    razorpay_payment_id = data["razorpay_payment_id"]
    razorpay_order_id = data["razorpay_order_id"]
    razorpay_signature = data["razorpay_signature"]

    body = razorpay_order_id + "|" + razorpay_payment_id

    expected_signature = hmac.new(
        bytes(os.getenv("RAZORPAY_KEY_SECRET"), 'utf-8'),
        bytes(body, 'utf-8'),
        hashlib.sha256
    ).hexdigest()

    if expected_signature == razorpay_signature:
        return {"success": True}
    else:
        return {"success": False}