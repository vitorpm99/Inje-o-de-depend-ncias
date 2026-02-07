from fastapi import FastAPI, Depends, HTTPException, status, Request

app = FastAPI()

def get_credentials(request: Request):
    username = request.query_params.get("username") or request.headers.get("username")
    password = request.query_params.get("password") or request.headers.get("password")

    return {
        "username": username,
        "password": password
    }


def check_user(credentials: dict = Depends(get_credentials)):
    username = credentials.get("username")
    password = credentials.get("password")


    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    return username

@app.get("/me")
def me(current_user: str = Depends(check_user)):
    return {"message": f"Olá, {current_user}"}


@app.get(
    "/status",
    dependencies=[Depends(check_user)]
)
def status_route():
    return {"status": "ok"}
