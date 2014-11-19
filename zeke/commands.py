from __future__ import print_function

import sys

from . import zookeeper, dns


def discover():
    for result in dns.discover_zk_via_dns():
        print(result)


def print_value(key, host):
    try:
        zk = zookeeper.Zookeeper(get_zk_hosts(host))
        result = zk.get_value(key)
        print(result.decode('utf-8'))
    except zookeeper.NoNodeError as e:
        print('Node not found:', key, file=sys.stderr)
        raise CommandError(e)


def get_zk_hosts(host):
    if host:
        return [host]
    else:
        return dns.discover_zk_via_dns()


class CommandError(Exception):
    pass