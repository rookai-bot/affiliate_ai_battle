import requests

def trigger_deploy():
    url = "https://api.netlify.com/build_hooks/686bc19907d2f35a66882f94"
    resp = requests.post(url)
    if resp.status_code == 200:
        print("[deployer] 🚀 Netlify redeploy triggered successfully.")
    else:
        print(f"[deployer] ❌ Failed to trigger deploy: {resp.status_code}")
