from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import HTMLResponse, FileResponse
import requests
import os

app = FastAPI()

LANGFLOW_WEBHOOK = "https://agent-builder.nhtech.link/api/v1/webhook/fcf98cc6-6a0d-4ea4-b18d-7bcf6a100dd1"
WEBHOOK_KEY = os.getenv("WEBHOOK_KEY", "sk-cQzPJUpymdgI4FDsoiGPkboMUoIE3K3pryUt5xa7zyc")

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "DreamHomes API Working"
    }

@app.get("/payment-done", response_class=HTMLResponse)
def payment_done(installment_id: str):
    requests.post(
        LANGFLOW_WEBHOOK,
        headers={"Content-Type": "application/json", "x-api-key": WEBHOOK_KEY},
        json={"installment_id": installment_id},
        timeout=30
    )
    return f"""
    <html>
    <body style="font-family:Arial;background:#f0fdf4;display:flex;align-items:center;
                 justify-content:center;min-height:100vh;margin:0;">
      <div style="background:white;border-radius:16px;box-shadow:0 10px 40px rgba(0,0,0,0.1);
                  max-width:480px;width:100%;overflow:hidden;">
        <div style="background:#16a34a;padding:28px;text-align:center;">
          <h1 style="color:white;margin:0;">🏠 DreamHomes</h1>
          <p style="color:#bbf7d0;margin:5px 0 0;">Real Estate Payment Portal</p>
        </div>
        <div style="padding:40px;text-align:center;">
          <h2 style="color:#16a34a;">✅ Payment Confirmed!</h2>
          <p style="color:#6b7280;margin:16px 0;">Your payment has been successfully recorded.</p>
          <div style="background:#f9fafb;border:1px solid #e5e7eb;border-radius:10px;padding:16px;text-align:left;margin:20px 0;">
            <p style="font-size:14px;">Installment ID: <strong>{installment_id}</strong></p>
            <p style="font-size:14px;margin-top:8px;">Status: 
              <span style="background:#dcfce7;color:#16a34a;padding:4px 16px;border-radius:20px;font-weight:700;">✅ PAID</span>
            </p>
          </div>
          <p style="color:#6b7280;font-size:14px;">📧 Invoice sent to your registered email.</p>
        </div>
        <div style="border-top:1px solid #f3f4f6;padding:16px;text-align:center;font-size:12px;color:#9ca3af;">
          DreamHomes Real Estate | payments@dreamhomes.in
        </div>
      </div>
    </body>
    </html>
    """

@app.get("/approve-booking", response_class=HTMLResponse)
def approve_booking(client_name: str, client_email: str, submission_id: str = ""):
    
    # ← YAHAN Agent 2 ka webhook URL daalo
    APPROVAL_WEBHOOK = "https://agent-builder.nhtech.link/api/v1/webhook/78b52af3-f506-49cd-9d5e-cfb34742a7e7"
    WEBHOOK_KEY = os.getenv("WEBHOOK_KEY", "sk-cQzPJUpymdgI4FDsoiGPkboMUoIE3K3pryUt5xa7zyc")

    requests.post(
        APPROVAL_WEBHOOK,
        headers={
            "Content-Type": "application/json",
            "x-api-key": WEBHOOK_KEY
        },
        # ← YAHAN client_name, email, id bhejo
        json={
            "client_name": client_name,
            "client_email": client_email,
            "submission_id": submission_id
        },
        timeout=30
    )

    return f"""
    <html><body style="font-family:Arial;text-align:center;padding:50px;background:#f0fdf4;">
      <div style="background:white;border-radius:16px;padding:40px;max-width:400px;
                  margin:auto;box-shadow:0 10px 40px rgba(0,0,0,0.1);">
        <h2 style="color:#16a34a;">✅ Booking Approved!</h2>
        <p>Documents being sent to <b>{client_name}</b></p>
        <p style="color:#6b7280;font-size:14px;">{client_email}</p>
        <p style="color:#9ca3af;font-size:12px;margin-top:16px;">
          Agent will send documents to client shortly.
        </p>
      </div>
    </body></html>
    """


@app.get("/booking-form.html")
def booking():
    return FileResponse("booking-form.html")

@app.get("/welcome-docs.html")
def welcome():
    return FileResponse("welcome-docs.html")

@app.get("/agreement-to-sell.html")
def agreement():
    return FileResponse("agreement-to-sell.html")