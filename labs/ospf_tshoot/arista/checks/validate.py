#!/usr/bin/env python

"""Script used to configure the network"""

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from rich import print


norn = InitNornir(config_file="nornir_settings/config.yaml")

interface_results = norn.run(
    name="Gathering interfaces!",
    task=send_command,
    command="show interfaces",
)

ospf_results = norn.run(
    name="Gathering neighbors!",
    task=send_command,
    command="show ip ospf neighbor",
)

route_results = norn.run(
    name="Gathering routes!",
    task=send_command,
    command="show ip route",
)

for host in norn.inventory.hosts.keys():
    # Checking Interfaces
    int_result = interface_results[host][0]
    int_parsed = int_result.scrapli_response.textfsm_parse_output()
    for interface in int_parsed:
        if interface["link_status"] != "up" or int(interface["mtu"]) < 1500:
            print(
                f":red_circle: Interface checks did not pass for {interface['interface']} on {host} :red_circle:"
            )
        else:
            print(
                f":leafy_green: Interface checks passed for {interface['interface']} on {host} :leafy_green:"
            )

    # Simple neighbor check
    data = ospf_results[host]
    ospf_parsed = data.scrapli_response.textfsm_parse_output()
    for neigh in ospf_parsed:
        if neigh["state"] != "FULL":
            print(
                f":red_circle: Neighbor checks did not pass for {neigh['neighbor_id']} on {host} :red_circle:"
            )
        else:
            print(
                f":leafy_green: Neighbor checks passed for {neigh['neighbor_id']} on {host} :leafy_green:"
            )

    # Checking Routes
    if host == "R8" or host == "R9" or host == "R14":
        route_result = route_results[host][0]
        route_parsed = route_result.scrapli_response.textfsm_parse_output()
        route = "13.13.13.0"
        routes = [
            value for elem in route_parsed for value in elem.values()]
        if route in routes:
            print(
                f":leafy_green: Route: {route} exists in routing table for {host} :leafy_green:")
        else:
            print(
                f":red_circle: Route: {route} does not exists in routing table for {host} :red_circle:")
