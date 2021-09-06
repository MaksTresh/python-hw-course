class RouterError(Exception):
    pass


class NotUniqueInterfaceNameError(RouterError):
    pass


class InterfaceNotExistsError(RouterError):
    pass


class RouteNotExistsError(RouterError):
    pass
