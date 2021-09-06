import ipaddress
from exceptions import NotUniqueInterfaceNameError, RouteNotExistsError, InterfaceNotExistsError


class Router:
    def __init__(self):
        self._ip_interfaces = {}
        self._ip_routes = {}

    def add_ip_interface(self, interface_name: str, address: str):
        """
        Adds interfaces to the router.
        Raises NotUniqueInterfaceNameError exception if an interface with that name exists.
        :param interface_name: Interface name, any string.
        :param address: Interface address (for example: 192.168.0.1/24).
        """
        if interface_name in self._ip_interfaces:
            raise NotUniqueInterfaceNameError(f'Interface {interface_name} already exists')

        interface = ipaddress.ip_interface(address)
        self._ip_interfaces[interface_name] = interface
        self._ip_routes[interface.network] = interface.ip

    def delete_ip_interface(self, interface_name: str):
        """
        Removes an interface by its name.
        Raises InterfaceNotExistsError exception if no interface with the same name exists.
        :param interface_name: Interface name, any string.
        """
        if interface_name in self._ip_interfaces:
            del self._ip_interfaces[interface_name]
        else:
            raise InterfaceNotExistsError(f'Interface {interface_name} not exists')

    def print_ip_interfaces(self):
        """
        Prints to the console a list of all initialized interfaces.
        """
        for interface_name, address in self._ip_interfaces.items():
            print(f'Interface {interface_name} has {address} ip address')

    def add_ip_route(self, network_addr: str, gateway_ip: str):
        """
        Adds a route to the network through a gateway.
        Raises RouteNotExistsError exception if the route to the gateway is not found.
        :param network_addr: Destination network address (for example: 172.16.0.0/16).
        :param gateway_ip: IP address of the gateway (for example: 192.168.2.1).
        """
        network = ipaddress.ip_network(network_addr)
        gateway = ipaddress.ip_address(gateway_ip)

        for route_network in self._ip_routes:
            if gateway in route_network:
                break
        else:
            raise RouteNotExistsError(f'Route to {gateway} not exists')

        self._ip_routes[network] = gateway

    def delete_ip_route(self, network_addr: str):
        """
        Removes the route to the network by the network address.
        Raises RouteNotExistsError exception if the network with the given address is not found.
        :param network_addr: Destination network address (for example: 172.16.0.0/16).
        """
        network = ipaddress.ip_network(network_addr)

        if network in self._ip_routes:
            del self._ip_routes[network]
        else:
            raise RouteNotExistsError(f'Interface {network_addr} not exists')

    def print_ip_routes(self):
        """
        Prints to the console a list of all initialized routes.
        """
        for network_addr, gateway_ip in self._ip_routes.items():
            print(f'The destination network {network_addr} via gateway {gateway_ip}')
