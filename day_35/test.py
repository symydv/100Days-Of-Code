import os
from dotenv import load_dotenv
load_dotenv()
a= 1
b = int(os.environ.get("number")
)
print(a+b)