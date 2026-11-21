from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Users CRUD API",
    description="API для управления пользователями с хранением данных в памяти",
    version="1.0.0",
)


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class User(BaseModel):
    id: int
    name: str
    email: EmailStr


users_db: list[User] = []
next_id: int = 1


def find_user(user_id: int) -> User:
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с id={user_id} не найден",
    )


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> User:
    global next_id
    if any(u.email == payload.email for u in users_db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким email уже существует",
        )
    user = User(id=next_id, name=payload.name, email=payload.email)
    next_id += 1
    users_db.append(user)
    return user


@app.get("/users", response_model=list[User])
def get_users() -> list[User]:
    return users_db


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    return find_user(user_id)


@app.put("/users/{user_id}", response_model=User)
def replace_user(user_id: int, payload: UserCreate) -> User:
    user = find_user(user_id)
    if any(u.email == payload.email and u.id != user_id for u in users_db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким email уже существует",
        )
    user.name = payload.name
    user.email = payload.email
    return user


@app.patch("/users/{user_id}", response_model=User)
def update_user(user_id: int, payload: UserUpdate) -> User:
    user = find_user(user_id)
    if payload.email is not None:
        if any(u.email == payload.email and u.id != user_id for u in users_db):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Пользователь с таким email уже существует",
            )
        user.email = payload.email
    if payload.name is not None:
        user.name = payload.name
    return user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int) -> None:
    user = find_user(user_id)
    users_db.remove(user)
