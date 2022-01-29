#!/bin/bash
if python validate.py; then
    echo success
else
    rm /usr/local/lib/python3.9/site-packages/ntc_templates/templates/arista_eos_show_ip_ospf_neighbor.textfsm
    cp arista_eos_show_ip_ospf_neighbor.textfsm /usr/local/lib/python3.9/site-packages/ntc_templates/templates/
    python validate.py
fi