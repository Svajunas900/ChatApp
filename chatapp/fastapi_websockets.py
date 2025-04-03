from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
import sqlite3


app = FastAPI()
con = sqlite3.connect("db.sqlite3")


class ConnectionManager:
  def __init__(self):
    self.active_connections: list[WebSocket] = []
  
  async def connect(self, websocket: WebSocket):
    await websocket.accept()
    self.active_connections.append(websocket)

  def disconnect(self, websocket: WebSocket):
    self.active_connections.remove(websocket)

  async def send_personal_message(self, message: str, websocket: WebSocket):
    await websocket.send_text(message)

  async def broadcast(self, message: str):
    for connection in self.active_connections:
      await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{client_id}/{conversation_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int, conversation_id: int):
  await manager.connect(websocket)
  try:
    while True:
      data = await websocket.receive_text()

      res = con.execute(f"SELECT username FROM auth_user WHERE id={client_id}")
      username = res.fetchone()[0]
      con.execute(f"INSERT INTO app1_messages (conversation_id, user_id_id, user_name, text, created_at) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)", (conversation_id, client_id, username, data))
      con.commit()
      await manager.broadcast(data)
  except WebSocketDisconnect:
    manager.disconnect(websocket)
    await manager.broadcast(f"Client #{client_id} left the chat")
  
if __name__ == "__main__":
  uvicorn.run("fastapi_websockets:app", port=5000, log_level="info")