# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# import requests
# import os

# app = FastAPI()

# LANGFLOW_WEBHOOK = "https://agent-builder.nhtech.link/api/v1/webhook/fcf98cc6-6a0d-4ea4-b18d-7bcf6a100dd1"
# WEBHOOK_KEY = os.getenv("WEBHOOK_KEY", "sk-DUAimQsir-R-99iRuOJ_Qo3yk1Qa7xhbX47wyIWpg-E")

# APPROVE_WEBHOOK_URL = "https://agent-builder.nhtech.link/api/v1/webhook/a2085853-72dd-410e-bc12-f8580040f114"


# @app.get("/")
# def home():
#     return {
#         "status": "running",
#         "message": "DreamHomes API Working"
#     }


# @app.get("/payment-done", response_class=HTMLResponse)
# def payment_done(installment_id: str):
#     requests.post(
#         LANGFLOW_WEBHOOK,
#         headers={"Content-Type": "application/json", "x-api-key": WEBHOOK_KEY},
#         json={"installment_id": installment_id},
#         timeout=30
#     )
#     return f"""
#     <html>
#     <body style="font-family:Arial;background:#f0fdf4;display:flex;align-items:center;
#                  justify-content:center;min-height:100vh;margin:0;">
#       <div style="background:white;border-radius:16px;box-shadow:0 10px 40px rgba(0,0,0,0.1);
#                   max-width:480px;width:100%;overflow:hidden;">
#         <div style="background:#16a34a;padding:28px;text-align:center;">
#           <h1 style="color:white;margin:0;">🏠 DreamHomes</h1>
#           <p style="color:#bbf7d0;margin:5px 0 0;">Real Estate Payment Portal</p>
#         </div>
#         <div style="padding:40px;text-align:center;">
#           <h2 style="color:#16a34a;">✅ Payment Confirmed!</h2>
#           <p style="color:#6b7280;margin:16px 0;">Your payment has been successfully recorded.</p>
#           <div style="background:#f9fafb;border:1px solid #e5e7eb;border-radius:10px;padding:16px;text-align:left;margin:20px 0;">
#             <p style="font-size:14px;">Installment ID: <strong>{installment_id}</strong></p>
#             <p style="font-size:14px;margin-top:8px;">Status:
#               <span style="background:#dcfce7;color:#16a34a;padding:4px 16px;border-radius:20px;font-weight:700;">✅ PAID</span>
#             </p>
#           </div>
#           <p style="color:#6b7280;font-size:14px;">📧 Invoice sent to your registered email.</p>
#         </div>
#         <div style="border-top:1px solid #f3f4f6;padding:16px;text-align:center;font-size:12px;color:#9ca3af;">
#           DreamHomes Real Estate | payments@dreamhomes.in
#         </div>
#       </div>
#     </body>
#     </html>
#     """


# @app.get("/approve-booking", response_class=HTMLResponse)
# def approve_booking(
#     client_name: str = "N/A",
#     client_email: str = "N/A",
#     submission_id: str = "",
#     stage: str = "manager"
# ):
#     cr_approval_url = (
#         f"https://dreamhomes-payment-api.onrender.com/approve-booking"
#         f"?client_name={client_name}"
#         f"&client_email={client_email}"
#         f"&submission_id={submission_id}"
#         f"&stage=cr"
#     )

#     requests.post(
#         APPROVE_WEBHOOK_URL,
#         headers={"Content-Type": "application/json", "x-api-key": WEBHOOK_KEY},
#         json={
#             "client_name": client_name,
#             "client_email": client_email,
#             "submission_id": submission_id,
#             "stage": stage,
#             "cr_approval_url": cr_approval_url
#         },
#         timeout=30
#     )

#     if stage == "manager":
#         title = "✅ Sales Manager Approval Completed"
#         message = "This booking has been approved and forwarded to the Client Relations team for final validation."
#     else:
#         title = "✅ Final Approval Completed"
#         message = "All documents are being prepared and the client will receive a confirmation email shortly."

#     return f"""
#     <html>
#     <body style="font-family:Arial;background:#f0fdf4;display:flex;justify-content:center;
#                  align-items:center;min-height:100vh;margin:0;">
#       <div style="background:white;border-radius:16px;padding:40px;max-width:520px;width:100%;
#                   text-align:center;box-shadow:0 10px 40px rgba(0,0,0,0.1);">

#         <h1 style="color:#16a34a;margin-bottom:4px;">🏠 DreamHomes</h1>
#         <p style="color:#9ca3af;font-size:13px;margin-top:0;">Approval Portal</p>
#         <hr style="border:none;border-top:1px solid #e5e7eb;margin:20px 0;">

#         <h2 style="color:#16a34a;">{title}</h2>

#         <div style="background:#f9fafb;border:1px solid #e5e7eb;border-radius:10px;
#                     padding:16px;text-align:left;margin:20px 0;font-size:14px;">
#           <p style="margin:0 0 8px;">👤 Client: <strong>{client_name}</strong></p>
#           <p style="margin:0 0 8px;">📧 Email: <strong>{client_email}</strong></p>
#           <p style="margin:0 0 8px;">🆔 Submission ID: <strong>{submission_id if submission_id else "N/A"}</strong></p>
#           <p style="margin:0;">📌 Stage:
#             <span style="background:#dcfce7;color:#16a34a;padding:3px 12px;border-radius:20px;font-weight:700;">
#               {"Sales Manager" if stage == "manager" else "Client Relations (CR)"}
#             </span>
#           </p>
#         </div>

#         <p style="color:#374151;margin:16px 0;">{message}</p>

#       </div>
#     </body>
#     </html>
#     """



from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import os

app = FastAPI()

LANGFLOW_WEBHOOK = "https://agent-builder.nhtech.link/api/v1/webhook/fcf98cc6-6a0d-4ea4-b18d-7bcf6a100dd1"
WEBHOOK_KEY = os.getenv("WEBHOOK_KEY", "sk-DUAimQsir-R-99iRuOJ_Qo3yk1Qa7xhbX47wyIWpg-E")

# Webhook 1 — Sales Manager approve kare → CR ko mail
MANAGER_APPROVE_WEBHOOK = "https://agent-builder.nhtech.link/api/v1/webhook/a2085853-72dd-410e-bc12-f8580040f114"

# Webhook 2 — CR approve kare → Client ko mail (APNA NAYA WEBHOOK URL YAHAN DAALO)
CR_APPROVE_WEBHOOK = "https://agent-builder.nhtech.link/api/v1/webhook/f2eac84c-9e28-4907-89c6-51c83e8672a7"


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
def approve_booking(
    client_name: str = "N/A",
    client_email: str = "N/A",
    submission_id: str = "",
    stage: str = "manager"
):
    if stage == "manager":
        # ✅ Sales Manager ne approve kiya → Webhook 1 trigger → CR ko mail jayegi
        requests.post(
            MANAGER_APPROVE_WEBHOOK,
            headers={"Content-Type": "application/json", "x-api-key": WEBHOOK_KEY},
            json={
                "client_name": client_name,
                "client_email": client_email,
                "submission_id": submission_id,
                "stage": "manager"
            },
            timeout=30
        )
        title = "✅ Sales Manager Approval Completed"
        message = "This booking has been approved and forwarded to the Client Relations team for final validation."

    else:
        # ✅ CR Team ne approve kiya → Webhook 2 trigger → Client ko mail jayegi
        requests.post(
            CR_APPROVE_WEBHOOK,
            headers={"Content-Type": "application/json", "x-api-key": WEBHOOK_KEY},
            json={
                "client_name": client_name,
                "client_email": client_email,
                "submission_id": submission_id,
                "stage": "cr"
            },
            timeout=30
        )
        title = "✅ Final Approval Completed"
        message = "All documents are being prepared and the client will receive a confirmation email shortly."

    return f"""
    <html>
    <body style="font-family:Arial;background:#f0fdf4;display:flex;justify-content:center;
                 align-items:center;min-height:100vh;margin:0;">
      <div style="background:white;border-radius:16px;padding:40px;max-width:520px;width:100%;
                  text-align:center;box-shadow:0 10px 40px rgba(0,0,0,0.1);">

        <h1 style="color:#16a34a;margin-bottom:4px;">🏠 DreamHomes</h1>
        <p style="color:#9ca3af;font-size:13px;margin-top:0;">Approval Portal</p>
        <hr style="border:none;border-top:1px solid #e5e7eb;margin:20px 0;">

        <h2 style="color:#16a34a;">{title}</h2>

        <div style="background:#f9fafb;border:1px solid #e5e7eb;border-radius:10px;
                    padding:16px;text-align:left;margin:20px 0;font-size:14px;">
          <p style="margin:0 0 8px;">👤 Client: <strong>{client_name}</strong></p>
          <p style="margin:0 0 8px;">📧 Email: <strong>{client_email}</strong></p>
          <p style="margin:0 0 8px;">🆔 Submission ID: <strong>{submission_id if submission_id else "N/A"}</strong></p>
          <p style="margin:0;">📌 Stage:
            <span style="background:#dcfce7;color:#16a34a;padding:3px 12px;border-radius:20px;font-weight:700;">
              {"Sales Manager" if stage == "manager" else "Client Relations (CR)"}
            </span>
          </p>
        </div>

        <p style="color:#374151;margin:16px 0;">{message}</p>

      </div>
    </body>
    </html>
    """