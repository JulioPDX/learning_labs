"""Tools script that holds a variety of functions"""

import os


def nornir_set_creds(norn, username="admin", password="admin", platform="eos"):
    """
    Handler for settings credentials and platform
    """
    if not username:
        username = os.environ.get("NORNIR_USER")
    if not password:
        password = os.environ.get("MY_SECRET")

    for host_obj in norn.inventory.hosts.values():
        host_obj.username = username
        host_obj.password = password
        host_obj.platform = platform
