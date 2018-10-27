from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class Test(BotPlugin):
    """
    testing inputs
    """
    migration_ground = ['test1', 'test2', 'test3']
    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does

    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"

    @botcmd(split_args_with=None)
    @arg_botcmd('name', type=str)
    @arg_botcmd('--favorite-number', type=int, unpack_args=False)
    def hello(self, message, args):
        """
        A command which says hello to someone.

        If you include --favorite-number, it will also tell you their
        favorite number.
        """
        if args.favorite_number is None:
            return "Hello {name}".format(name=args.name)
        else:
            return "Hello {name}, I hear your favorite number is {number}".format(
                name=args.name,
                number=args.favorite_number,
            )

    @botcmd(split_args_with=None)
    @arg_botcmd('name', type=str)
    def migration_add(self, mess, name=None):
        self.migration_ground.append(name)
        return f"Added {name}, to the migration group"

    @botcmd(split_args_with=None)
    @arg_botcmd('name', type=str)
    def migration_remove(self, mess, name=None):
        self.migration_ground.remove(name)
        return f"Removed {name}, to the migration group"

    @botcmd
    def migration_list(self, mess, args):
        return f"Migration list {self.migration_ground} args {args}"
