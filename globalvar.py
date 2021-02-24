class GlobalVar:

    def _init(self):
        global _global_dict
        _global_dict = {}

    def set_value(self, name, value):
        _global_dict[name] = value

    def get_value(self, name, defvalue=None):
        try:
            return _global_dict[name]
        except KeyError:
            return defvalue
