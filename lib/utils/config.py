import gconf

class GConf(object):
    """Gconf Wrapper"""

    def __new__(cls, *args, **kwargs):
        if '_inst' not in vars(cls):
            cls._inst = super(GConf, cls).__new__(cls, *args, **kwargs)
        return cls._inst

    def __init__(self):
        self.dir = "/apps/gphotoframe/"
        self.gconf = gconf.client_get_default()
        self.gconf.add_dir(self.dir[:-1], gconf.CLIENT_PRELOAD_NONE)

    def set_notify_add(self, key, cb):
        self.gconf.notify_add (self.dir + key, cb)

    def set_int(self, key, val):
        return self.gconf.set_int(self.dir + key, int(val))

    def get_int(self, key, default=None):
        if self.gconf.get(self.dir + key) is None:
            val = default
        else:
            val = self.gconf.get_int(self.dir + key)
        return val

    def set_float(self, key, val):
        return self.gconf.set_float(self.dir + key, float(val))

    def get_float(self, key, default=0.0):
        val = self.gconf.get_float(self.dir + key)
        return val if val != 0.0 else default

    def set_string(self, key, val):
        return self.gconf.set_string(self.dir + key, val)

    def get_string(self, key):
        val = self.gconf.get_string(self.dir + key)
        return val

    def set_bool(self, key, val):
        return self.gconf.set_bool(self.dir + key, val)

    def get_bool(self, key, default=None):
        path = self.dir + key
        val = default if self.gconf.get(path) is None \
            else self.gconf.get_bool(path)
        return val

    def recursive_unset(self, key):
        self.gconf.recursive_unset(self.dir + key, 
                                   gconf.UNSET_INCLUDING_SCHEMA_NAMES)

    def all_entries(self, key):
        return self.gconf.all_entries(key)

    def all_dirs(self, key):
        return self.gconf.all_dirs(self.dir + key)

    def set_value(self, key, value):
        if isinstance(value, int):
            self.set_int(key, value)
        elif isinstance(value, bool):
            self.set_bool(key, value)
        else:
            self.set_string(key, value)

    def get_value(self, entry):
        if entry.get_value() is None:
            value = None
        elif entry.get_value().type == gconf.VALUE_INT:
            value = entry.get_value().get_int()
        elif entry.get_value().type == gconf.VALUE_BOOL:
            value = entry.get_value().get_bool()
        else:
            value = entry.get_value().get_string()

        return value
