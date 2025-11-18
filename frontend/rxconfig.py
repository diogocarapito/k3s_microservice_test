import reflex as rx

config = rx.Config(
    app_name="app",
    backend_url="http://backend-svc:8001",  # Backend service URL in k3s
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
