from fixture.wd import WD


class Application:

    def __init__(self):
        self.wd_init = WD()
        self.wd = self.wd_init.wd
