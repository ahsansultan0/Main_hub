import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print("URL =", repr(url))
print("KEY =", "exists" if key else "MISSING")

spabase = create_client(url, key)

print("CLIENT CREATED")

print(spabase.auth)