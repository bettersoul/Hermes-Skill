import requests
import sys

def write_record(base_id, table_id, fields, app_id, app_secret):
    # Step 1: Get fresh token
    auth_url = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/'
    auth_payload = {'app_id': app_id, 'app_secret': app_secret}
    auth_headers = {'Content-Type': 'application/json'}
    
    try:
        auth_resp = requests.post(auth_url, json=auth_payload, headers=auth_headers, timeout=10)
        auth_resp.raise_for_status()
        token = auth_resp.json().get('app_access_token')
        if not token:
            raise ValueError('No app_access_token in response')
    except Exception as e:
        print(f'❌ Failed to get token: {e}')
        return None

    # Step 2: Write record
    write_url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{base_id}/tables/{table_id}/records'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    data = {'fields': fields}
    
    try:
        resp = requests.post(write_url, headers=headers, json=data, timeout=10)
        if resp.status_code == 200:
            result = resp.json()
            if result.get('code') == 0 and 'record' in result.get('data', {}):
                return result['data']['record'].get('record_id')
            else:
                print(f'⚠️  API error: {result.get("msg", "Unknown")}')
        else:
            print(f'⚠️  HTTP {resp.status_code}: {resp.text[:100]}')
    except Exception as e:
        print(f'❌ Exception: {e}')
    
    return None

if __name__ == '__main__':
    if len(sys.argv) < 6:
        print('Usage: python write.py <base_id> <table_id> <field1> <value1> ... <app_id> <app_secret>')
        sys.exit(1)
    
    base_id = sys.argv[1]
    table_id = sys.argv[2]
    app_id = sys.argv[-2]
    app_secret = sys.argv[-1]
    
    # Parse fields: key1 value1 key2 value2 ...
    fields = {}
    for i in range(3, len(sys.argv)-2, 2):
        if i+1 < len(sys.argv)-2:
            key = sys.argv[i]
            value = sys.argv[i+1]
            fields[key] = value
    
    rid = write_record(base_id, table_id, fields, app_id, app_secret)
    if rid:
        print(f'✅ Written: {rid}')
    else:
        print('❌ Write failed')