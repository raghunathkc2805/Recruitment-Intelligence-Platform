from pathlib import Path

p = Path("api/app.py")

text = p.read_text(encoding="utf-8")

if "custom_docs" in text:
    print("Swagger patch already exists")
    exit()

text = text.replace(
    "from fastapi import FastAPI",
    "from fastapi import FastAPI\nfrom fastapi.responses import HTMLResponse\nfrom fastapi.staticfiles import StaticFiles"
)

text = text.replace(
    'docs_url="/docs"',
    'docs_url=None'
)

swagger_code = '''

app.mount("/static", StaticFiles(directory="api/static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_docs():

    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Recruitment Intelligence Platform</title>
        <link rel="stylesheet" href="/static/swagger-ui.css">
    </head>
    <body>

    <div id="swagger-ui"></div>

    <script src="/static/swagger-ui-bundle.js"></script>

    <script>
    SwaggerUIBundle({
        url: "/openapi.json",
        dom_id: "#swagger-ui"
    })
    </script>

    </body>
    </html>
    """)

'''

text = text.replace(
    "app.add_middleware(SecurityHeadersMiddleware)",
    swagger_code + "\napp.add_middleware(SecurityHeadersMiddleware)"
)

p.write_text(text, encoding="utf-8")

print("Local Swagger UI patch applied")
