from conans import ConanFile


class ScmtestConan(ConanFile):
    name = "scm_test"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }
    version = "0.0.1"

    def source(self):
        pass

    def build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        pass

