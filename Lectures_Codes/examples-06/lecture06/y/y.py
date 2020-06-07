#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import yaml


def print_client(client):
    print(f'Client {client["id"]} with speed {client["speed"]} in path {client["path"]}')


def print_node(node):
    print(f'Node {node["id"]} at position ({node["location"][0]}, {node["location"][1]})')


# Reading a yaml file
with open('example.yaml') as s:
    config = yaml.safe_load(s)
    for client in config['clients']:
        print_client(client)
    for node in config['nodes']:
        print_node(node)


# Writing a yaml file
structure = {
    "clients":  [
        {
            "id": "00000001",
            "speed": 1,
            "path": [[1, 1], [20, 1], [1, 200]]
        }, {
            "id": "00000002",
            "speed": 2,
            "path": [[1, 1], [20, 1], [1, 200]]
        }
    ],
    "nodes": [
        {
            "id": "NODE001",
            "location": [0, 0]
        }, {
            "id": "NODE002",
            "location": [30, 40]
        }, {
            "id": "NODE003",
            "location": [100, 100]
        }
    ]
}


with open('output.yaml', 'w') as s:
    yaml.safe_dump(structure, s)
