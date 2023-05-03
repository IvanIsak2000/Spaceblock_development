#!/usr/bin/env python3

from fastapi import FastAPI, Body, status, Request
import tomllib

app = FastAPI()


@app.get('/log_in/{user_name}/{user_token}') 
async def log_in(user_name: str, user_token: str) -> bool:
    with open('database.toml', 'rb') as file:
        db = tomllib.load(file)
    print(db)

    if db[user_name]['user_token'] == user_token:
        return True
    
    else:
        return False