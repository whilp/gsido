# gsido

Switch to a grid user with glexec.

## Usage

    $ gsido -h
    Usage: gsido [options] [command]

    Execute a <command> as a grid user. If <command> is not specified, run the
    user's $SHELL. By default, the certificate or proxy specified in the environment
    variables GLEXEC_CLIENT_CERT or X509_USER_PROXY will be used. If they are not
    specified and /tmp/x509up_u<uid> is available, it will be used instead. A
    certificate specified with the '-c' option will always take precedence.


    Options:
      -v VERBOSE, --verbose=VERBOSE
                            set logging level to VERBOSE
      -c CERTIFICATE, --certificate=CERTIFICATE
                            use grid certificate or proxy CERTIFICATE
      -p PHASE, --phase=PHASE
                            glexec phase; internal
      -h, --help            show this help message and exit

## Notes

In glexec versions >= 0.8, the 'create_target_proxy' configuration value in
/etc/glexec.conf should be set to 'yes' (the default). When set to 'no',
commands run under gsido will not be able to read the original proxy, and so
$X509_USER_PROXY won't have a sensible value.
