from fastapi import FastAPI, Form
import pyshorteners

app = FastAPI()
@app.get("/")
async def index():
    return """
    <form action="/shorten_url/" method="post">
        Original URL: <input type="text" name="url"><br>
        <input type="submit" value="Shorten">
    </form>
    """

@app.post("/shorten_url/")
async def shorten_url(url: str = Form(...)):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return f'<a href="{shortened_url}">{shortened_url}</a>'


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(__name__ + ":app", host="0.0.0.0", port=8888, log_level="info", reload=True)




