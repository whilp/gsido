from distutils.core import setup

meta = dict(
    name          = "gsido",
    version       = "0.1",
    license       = "MIT",
    description   = "Run commands using glexec",
    author        = "Will Maier",
    author_email  = "wcmaier@hep.wisc.edu",
    url           = "http://hg.hep.wisc.edu/cmsops/gsido",
    scripts       = ["gsido"],
)

setup(**meta)
