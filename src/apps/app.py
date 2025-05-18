from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import uvicorn
import asyncio
import requests
import os

from utils.main import RAG
app = FastAPI()
chat_history = []
# Mount static directories
app.mount("/static", StaticFiles(directory="C:/vishwa/LLM_law_bot2/src/apps/static"), name="static")
app.mount("/images", StaticFiles(directory="C:/vishwa/LLM_law_bot2/src/apps/static/images"), name="images")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="C:/vishwa/LLM_law_bot2/src/apps/templates")



# Home and Role Selection
@app.get("/", response_class=HTMLResponse)
async def role_selection(request: Request):
    return templates.TemplateResponse("roleselection.html", {"request": request})

@app.get("/role", response_class=HTMLResponse)
async def roleselection_page(request: Request):
    return templates.TemplateResponse("roleselection.html", {"request": request})

@app.get("/login")
async def catch_login():
    return RedirectResponse(url="/role") 

# Chatbot Pages
@app.get("/judgechatbot.html", response_class=HTMLResponse)
async def judge_chatbot(request: Request):
    return templates.TemplateResponse("judgechatbot.html", {"request": request})

@app.get("/judgedashboard.html", response_class=HTMLResponse)
async def judge_dashboard(request: Request):
    return templates.TemplateResponse("judgedashboard.html", {"request": request})

@app.get("/viewall.html", response_class=HTMLResponse)
async def view_all(request: Request):
    return templates.TemplateResponse("viewall.html", {"request": request})

@app.get("/judgecalender.html", response_class=HTMLResponse)
async def judge_calender(request: Request):
    return templates.TemplateResponse("judgecalender.html", {"request": request})

@app.get("/advocatedashboard.html", response_class=HTMLResponse)
async def advocate_dashboard(request: Request):
    return templates.TemplateResponse("advocatedashboard.html", {"request": request})

@app.get("/advocateresources.html", response_class=HTMLResponse)
async def advocate_resources(request: Request):
    return templates.TemplateResponse("advocateresources.html", {"request": request})

# ========== Other Role Pages ==========
@app.get("/woman.html", response_class=HTMLResponse)
async def woman_page(request: Request):
    return templates.TemplateResponse("woman.html", {"request": request})

@app.get("/citizen.html", response_class=HTMLResponse)
async def citizen_page(request: Request):
    return templates.TemplateResponse("citizen.html", {"request": request})

@app.get("/minor.html", response_class=HTMLResponse)
async def minor_page(request: Request):
    return templates.TemplateResponse("minor.html", {"request": request})

# ========== Chatbot Pages ==========
@app.get("/studentchatbot.html", response_class=HTMLResponse)
async def student_page(request: Request):
    return templates.TemplateResponse("studentchatbot.html", {"request": request})

@app.get("/advocatechatbot.html", response_class=HTMLResponse)
async def advocatechatbot_page(request: Request):
    return templates.TemplateResponse("advocatechatbot.html", {"request": request})

@app.get("/womanchatbot.html", response_class=HTMLResponse)
async def womanchatbot_page(request: Request):
    return templates.TemplateResponse("womanchatbot.html", {"request": request})

@app.get("/safetytips.html", response_class=HTMLResponse)
async def safetytips_page(request: Request):
    return templates.TemplateResponse("safetytips.html", {"request": request})

@app.get("/resources.html", response_class=HTMLResponse)
async def resources_page(request: Request):
    return templates.TemplateResponse("resources.html", {"request": request})

@app.get("/legalrights.html", response_class=HTMLResponse)
async def legalrights_page(request: Request):
    return templates.TemplateResponse("legalrights.html", {"request": request})

@app.get("/FIR.html", response_class=HTMLResponse)
async def fir_page(request: Request):
    return templates.TemplateResponse("FIR.html", {"request": request})

@app.get("/studentdashboard.html", response_class=HTMLResponse)
async def student_page(request: Request):
    return templates.TemplateResponse("studentdashboard.html", {"request": request})

# WebSocket for Chatbot

@app.get("/judgechatbot.html", response_class=HTMLResponse)
def conversation():
    with open(r"C:\vishwa\LLM_law_bot2\src\apps\templates\judgechatbot.html", "r") as file:
        converstional_html = file.read()
    return HTMLResponse(converstional_html)


async def stream_text_conversational(websocket: WebSocket, query: str):
    chat_limit = 10
    temp_chat = {"user": "" ,"system":""}
    temp_chat["user"] = query
    model_response = ""
    temp_text = ""
    completion = RAG(query, chat_history)
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            await websocket.send_text(chunk.choices[0].delta.content)
            await asyncio.sleep(0.01)
            model_response += chunk.choices[0].delta.content
    # print(model_response)
    temp_chat['system']=model_response
    chat_history.append(temp_chat)
    if len(chat_history)>chat_limit:
        chat_history.pop(0)
    print(chat_history)
  
@app.websocket("/conversational_chat")
async def conversational_chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            query = await websocket.receive_text()
            print(query)
            await stream_text_conversational(websocket, query)
        except WebSocketDisconnect:
            chat_history.clear()
            print("chat history:", chat_history)
            break


# Run the application
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
