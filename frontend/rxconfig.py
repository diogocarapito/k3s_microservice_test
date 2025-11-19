import reflex as rx

config = rx.Config(
    app_name="app",
    api_url="http://backend-svc:8001",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
