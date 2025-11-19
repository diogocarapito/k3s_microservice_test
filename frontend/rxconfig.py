import reflex as rx

config = rx.Config(
    app_name="app",
    api_url="ws://backend-svc:8001",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
