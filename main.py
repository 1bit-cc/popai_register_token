import requests

def getCode(email:str):
    r = requests.post("https://api.popai.pro/api/v1/auth/toLoginByEmailValidationCode",
                      headers={
                          "authority": "api.popai.pro",
                          "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                          "app-name": "popai-web",
                          "gtoken": "",
                          "language": "en",
                          "origin": "https://www.popai.pro",
                          "pop-url": "https://www.popai.pro/",
                          "referer": "https://www.popai.pro/",
                      },json={
                          "email":email,
                          "token":""
                      })
    print("[INFO][getCode]"+r.text)

    if r.status_code == 200:
        # {"code":200,"message":"success","data":"Success","showToUser":false}
        return True if r.json()["data"] == "Success" else False
    else:
        print("[ERROR][getCode] " + r.text)
        return False

def login_EmailCode(email:str,code:str):
    r =  requests.post("https://api.popai.pro/api/v1/auth/loginByEmailValidationCode",
                       headers={
                           "authority": "api.popai.pro",
                          "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                          "app-name": "popai-web",
                          "gtoken": "",
                          "language": "en",
                          "origin": "https://www.popai.pro",
                          "pop-url": "https://www.popai.pro/",
                          "referer": "https://www.popai.pro/",
                       },json={
                           "email":email,
                           "code":code
                       })
    
    print("[INFO][login_EmailCode]"+r.text)
    if r.status_code == 200:
        # {"code":200,"message":"success","data":"Success","showToUser":false}
        return r.json()["data"] if r.json()["code"] == 200 else ""
    else:
        print("[ERROR][login_EmailCode] " + r.text)
        return False

# Send
# https://api.popai.pro/api/v1/chat/send

if __name__== "__main__":
    em = input("Email: ")
    print("GET Code Status: {}".format(getCode(em)))
    code = input("Code: ")
    print("\nJWT Token: {}".format(login_EmailCode(em,code)))
