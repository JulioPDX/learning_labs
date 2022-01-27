#!/usr/bin/env python

"""Script used to configure the network"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from tools import nornir_set_creds
from rich import inspect, print


norn = InitNornir(config_file="nornir_settings/config.yaml")
nornir_set_creds(norn)

interface_results = norn.run(
    name=f"Gathering interfaces!",
    task=napalm_get,
    getters=["get_interfaces"],
)

for host in norn.inventory.hosts.keys():
    interfaces = interface_results[host].result
    for int in interfaces["get_interfaces"]:
        if interfaces["get_interfaces"][int]["mtu"] < 1500:
            print(
                f":triangular_flag_on_post: MTU checks did not pass for {int} on {host} :triangular_flag_on_post:"
            )
        else:
            print(
                f":white_heavy_check_mark: All interface checks passed for {int} on {host} :white_heavy_check_mark:"
            )
    # for interface in interfaces["get_interfaces"]:
    #     inspect(interface)
    # list_of_interface_values = [
    #     value for elem in interfaces for value in elem.values()]


# def get_network(task):
#     """Configures network with NAPALM"""
#     interface_results = task.run(
#         name=f"Gathering OSPF neighbors for {task.host.name}!",
#         task=napalm_get,
#         getters=["get_interfaces"],
#     )
# print(interface_results[0].result["get_interfaces"])
# for host in norn.inventory.hosts.keys():

# print(
#     f":white_heavy_check_mark: MTU checks did not pass for {interface} :white_heavy_check_mark:"
# )


# def main():
#     """Used to run all the things"""
#     norn = InitNornir(config_file="nornir_settings/config.yaml")
#     nornir_set_creds(norn)
#     result = norn.run(task=get_network)
# print_result(result)


# if __name__ == "__main__":
#     main()
