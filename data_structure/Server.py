class Server:
    def __init__(self, serverId : str) -> None:
        self.serverId = serverId
        self.members = []
        self.timedRoleOfServer = {}