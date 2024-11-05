class CreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__}{args}")
        super().__init__(*args, **kwargs)
