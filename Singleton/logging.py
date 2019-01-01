class logging:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(logging, cls).__new__(cls)

        return cls.__instance

    def log(self, message):
        print(message)