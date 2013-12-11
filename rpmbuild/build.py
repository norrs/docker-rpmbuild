#!/usr/bin/env python

"""Docker rpmbuild.

Usage:
    docker-packager --spec=<file> --source=<tarball> [--output=<path>] <image>

Options:
    -h --help           Show this screen.
    --output=<path>     Output directory for RPMs [default: .].
    --source=<tarball>  Tarball containing package sources.
    --spec=<file>       RPM Spec file to build.

"""

import sys

from docopt import docopt
from rpmbuild import Packager, PackagerContext, PackagerException

def main():
    args = docopt(__doc__, version='Docker Packager 0.0.1')

    context = PackagerContext(args['<image>'], args['--source'], args['--spec'], args['--output'])
    try:
        with Packager(context) as p:
            p.build()

    except PackagerException:
        print >> sys.stderr, 'Container build failed!'
        sys.exit(1)

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
