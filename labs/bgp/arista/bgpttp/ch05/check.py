from scrapli import Scrapli

device = {
   "host": "internet",
   "auth_username": "admin",
   "auth_password": "admin",
   "auth_strict_key": False,
   "platform": "arista_eos"
}

conn = Scrapli(**device)
conn.open()
routes = conn.send_command('show ip route')

if '100.1.1.0/24' not in routes.result:
    print('Route was not found')
    exit(1)
else:
    print('Route was found!')

conn.close()
