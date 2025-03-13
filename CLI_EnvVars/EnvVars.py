# To set an environment variable in Windows, use  $env:API_TOKEN = "your_token_value" in terminal
# To set an environment variable in Linux, use  export API_TOKEN = "your_token_value" in terminal
import os
print(os.getenv("API_TOKEN"))
