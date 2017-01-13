"""Run code in a jail."""

# configure is a reexport for backwards compatibility
from .jail import configure  # pylint: disable=unused-import
from .jail import get_codejail
    # The number of processes and threads to allow.
    "NPROC": 15,
        * `"NPROC"`: the maximum number of process or threads creatable by the
            jailed code.  The default is 15.



def jail_code(command, code=None, files=None, extra_files=None, argv=None,
              stdin=None, slug=None):
    """
    Run code in a jailed subprocess.

    This function calls through to the `jail_code()` method on the `Jail`
    object.

    `command` is an abstract command ("python", "node", ...) that must have
    been configured using `configure`.

    All other arguments, return values, and behavior are documented at
    `codejail.jail.Jail.jail_code`

    This function exists primarily for backwards compatibility.  For new code,
    consider using `codejail.jail.Jail.jail_code` instead.

    >>> import codejail.jail
    >>> jail = codejail.jail.get_codejail("python")
    >>> jail.jail_code(...)
    """
    jail = get_codejail(command)
    result = jail.jail_code(
        code=code,
        files=files,
        extra_files=extra_files,
        argv=argv,
        stdin=stdin,
        slug=slug
    )
    return result

    # Allow a small number of subprocess and threads.  One limit controls both,
    # and at least OpenBLAS (imported by numpy) requires threads.
    nproc = LIMITS["NPROC"]
    if nproc:
        rlimits.append((resource.RLIMIT_NPROC, (nproc, nproc)))