# from fastapi import FastAPI, Form
# import pyshorteners
# import hashlib

# app = FastAPI()
# # def func():
# def shorten_url(long_url: str) -> str:
#     # Use the md5 hash function to create a unique hash for the long URL
#     hash_object = hashlib.md5(long_url.encode())
#     short_url = hash_object.hexdigest()[:6]
#     # Return the first 6 characters of the hash as the shortened URL
#     return short_url

# # print(shorten_url("https://www.example.com/very/long/path"))



# @app.get("/")
# async def index():
#     return """
#     <form action="/shorten_url/" method="post">
#         Original URL: <input type="text" name="url"><br>
#         <input type="submit" value="Shorten">
#     </form>
#     """
 

# @app.post("/shorten_url/")
# async def shorten_url_endpoint(url: str = Form(...)):
#     short_url = shorten_url(url)
#     return {"original_url": url, "short_url": short_url}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(__name__ + ":app", host="127.0.0.1", port=8888, log_level="info", reload=True)
# # from fastapi import FastAPI, Form
# # import requests

# # app = FastAPI()

# # BITLY_ACCESS_TOKEN = "61d14d43ea1dfc73efffe2916598869e96ae33e6"
# # BITLY_API_URL = "https://api-ssl.bitly.com/v4/shorten"

# # @app.get("/")
# # async def index():
# #     return """
# #         <form action="/shorten_url/" method="post">
# #             Original URL: <input type="text" name="url"><br>
# #             <input type="submit" value="Shorten">
# #         </form>
# #     """

# # @app.post("/shorten_url/")
# # async def shorten_url(url: str = Form(...)):
# #     headers = {
# #         "Authorization": f"Bearer 61d14d43ea1dfc73efffe2916598869e96ae33e6",
# #         "Content-Type": "application/json",
# #     }
# #     data = {"long_url": url}
# #     response = requests.post(BITLY_API_URL, headers=headers, json=data)
# #     response.raise_for_status()
# #     json_response = response.json()
# #     return json_response["link"]
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
    uvicorn.run(__name__ + ":app", host="127.0.0.1", port=8888, log_level="info", reload=True)




