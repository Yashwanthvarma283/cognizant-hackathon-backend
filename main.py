from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(title="Supply Chain Digital Twin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Data Models
class User(BaseModel):
    id: str
    name: str
    email: str
    role: str
    status: str # pending, approved, suspended
    last_login: str

# In-memory store
mock_users = [
    {"id": "1", "name": "Sarah Jenkins", "email": "sarah@admin.com", "role": "admin", "status": "approved", "last_login": "2 mins ago"},
    {"id": "2", "name": "Michael Chen", "email": "michael@supplier.com", "role": "supplier", "status": "approved", "last_login": "1 hour ago"},
    {"id": "3", "name": "Elena Rostova", "email": "elena@consumer.com", "role": "consumer", "status": "pending", "last_login": "3 hours ago"},
    {"id": "4", "name": "John Doe", "email": "john@supplier.com", "role": "supplier", "status": "pending", "last_login": "Never"},
    {"id": "5", "name": "Jane Smith", "email": "jane@consumer.com", "role": "consumer", "status": "approved", "last_login": "5 hours ago"},
]

@app.get("/")
def read_root():
    return {"message": "Supply Chain Digital Twin API is running"}

@app.get("/admin/users", response_model=List[User])
def get_users():
    return mock_users

@app.patch("/admin/users/{user_id}")
def update_user(user_id: str, updated_data: dict):
    for user in mock_users:
        if user["id"] == user_id:
            user.update(updated_data)
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/admin/users/{user_id}")
def delete_user(user_id: str):
    global mock_users
    mock_users = [u for u in mock_users if u["id"] != user_id]
    return {"message": "User deleted successfully"}

@app.get("/admin/stats")
def get_admin_stats():
    return {
        "total_users": len(mock_users),
        "pending_approvals": len([u for u in mock_users if u["status"] == "pending"]),
        "active_suppliers": len([u for u in mock_users if u["role"] == "supplier" and u["status"] == "approved"]),
        "active_consumers": len([u for u in mock_users if u["role"] == "consumer" and u["status"] == "approved"]),
    }
