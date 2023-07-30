#!/sur/bin/python3
'''
    module 7-base_geometry
'''


class BaseGeometry:
    ''' class BaseGeometry '''
    def area(self):
        ''' method area without implementation '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            method that raise errors depending the case
            Args:
                name: name of the object to evaluate
                value: value of name
        '''
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(self.name))
