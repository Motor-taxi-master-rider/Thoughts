

"""
覆盖型描述符:

    >>> obj = Model()
    >>> obj.__dict__['over'] = 'obj instance property over'
    >>> obj.over  # doctest: +ELLIPSIS
    Overriding.__get__() invoked with args:
        self     = <descriptorkinds.Overriding object at 0x...>
        instance = <descriptorkinds.Model object at 0x...>
        owner    = <class 'descriptorkinds.Model'>
    >>> Model.over  # doctest: +ELLIPSIS
    Overriding.__get__() invoked with args:
        self     = <descriptorkinds.Overriding object at 0x...>
        instance = None
        owner    = <class 'descriptorkinds.Model'>
    >>> sub_obj = SubClass()
    >>> sub_obj.__dict__['over'] = 'sub_obj instance property over'
    >>> sub_obj.over  # doctest: +ELLIPSIS
    Overriding.__get__() invoked with args:
        self     = <descriptorkinds.Overriding object at 0x...>
        instance = <descriptorkinds.SubClass object at 0x...>
        owner    = <class 'descriptorkinds.SubClass'>
    >>> SubClass.over  # doctest: +ELLIPSIS
    Overriding.__get__() invoked with args:
        self     = <descriptorkinds.Overriding object at 0x...>
        instance = None
        owner    = <class 'descriptorkinds.SubClass'>

#行为完全符合策略2。额外的，这里测试了获取类属性时传入参数的值。

没有 __get__ 方法的覆盖型描述符:

    >>> obj.__dict__['over_no_get'] = 'obj instance property over_no_get'
    >>> obj.over_no_get  # doctest: +ELLIPSIS
    'obj instance property over_no_get'
    >>> sub_obj.over_no_get  # doctest: +ELLIPSIS
    <descriptorkinds.OverridingNoGet object at 0x...>
    >>> sub_obj.__dict__['over_no_get'] = 'sub_obj instance property over_no_get'
    >>> sub_obj.over_no_get  # doctest: +ELLIPSIS
    'sub_obj instance property over_no_get'

#行为符合策略4。其行为更像非覆盖型描述符。但无法直接使用obj.over_no_get的方式给实例属性赋值。

非覆盖型描述符：
    >>> obj.non_over  # doctest: +ELLIPSIS
    NonOverriding.__get__() invoked with args:
        self     = <descriptorkinds.NonOverriding object at 0x...>
        instance = <descriptorkinds.Model object at 0x...>
        owner    = <class 'descriptorkinds.Model'>
    >>> obj.non_over = 'obj instance property non_over'
    >>> obj.non_over  # doctest: +ELLIPSIS
    'obj instance property non_over'
    >>> sub_obj.non_over  # doctest: +ELLIPSIS
    NonOverriding.__get__() invoked with args:
        self     = <descriptorkinds.NonOverriding object at 0x...>
        instance = <descriptorkinds.SubClass object at 0x...>
        owner    = <class 'descriptorkinds.SubClass'>
    >>> sub_obj.__dict__['non_over'] = 'sub_obj instance property non_over'
    >>> sub_obj.non_over  # doctest: +ELLIPSIS
    'sub_obj instance property non_over'

#行为符合策略4。
"""

# BEGIN DESCRIPTORKINDS
def print_args(name, *args):  # <1>
    cls_name = args[0].__class__.__name__
    arg_names = ['self', 'instance', 'owner']
    if name == 'set':
        arg_names[-1] = 'value'
    print('{}.__{}__() invoked with args:'.format(cls_name, name))
    for arg_name, value in zip(arg_names, args):
        print('    {:8} = {}'.format(arg_name, value))


class Overriding:  # <2>
    """a.k.a. data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)  # <3>

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:  # <4>
    """an overriding descriptor without ``__get__``"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:  # <5>
    """a.k.a. non-data or shadowable descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Model:  # <6>
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):  # <7>
        print('Model.spam() invoked with arg:')
        print('    self =', self)

class SubClass(Model):
    def spam(self):
        print('SubClass.spam() invoked with arg:')
        print('    self =', self)

#END DESCRIPTORKINDS
