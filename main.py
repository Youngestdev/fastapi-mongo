import uvicorn

app_module = 'app:app'
host="0.0.0.0"
port=8080
reload=True
if __name__ == '__main__':
    uvicorn.run(app=app_module, host=host, port=port, log_level="info", reload=reload)