from fastapi import FastAPI
import uvicorn
import service

#from schemas import #스키마 만드실때 추가


app = FastAPI()

#################



@app.get("/")
def test():
  return "Hi"










#################
if __name__ == '__main__':
  uvicorn.run(app)
