from rich import print
import requests

print("[bold italic green]Merhaba Python![/bold italic green]")

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
