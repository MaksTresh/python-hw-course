from router import Router
from exceptions import RouteNotExistsError

if __name__ == '__main__':
    router = Router()
    router.add_ip_interface('eth0', '192.168.5.14/24')
    router.add_ip_route('172.16.0.0/16', '192.168.5.1')

    try:
        router.add_ip_route('172.24.0.0/16', '192.168.8.1')
    except RouteNotExistsError:
        print('Cannot add ip route to 172.24.0.0/16 via 192.168.8.1')

    router.add_ip_route('172.24.0.0/16', '172.16.8.1')

    router.print_ip_interfaces()
    router.print_ip_routes()
