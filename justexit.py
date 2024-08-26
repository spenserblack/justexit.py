class _JustExit:
    """
    Hacky class to allow exiting from a REPL without parentheses.
    """

    def __call__(self, *args, **kwargs):
        import sys

        return sys.exit(*args, **kwargs)

    def __repr__(self):
        """
        Allows exiting without parentheses.
        """
        return self(0)


exit = _JustExit()
