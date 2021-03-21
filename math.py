#!/usr/bin/env/python
# encoding: utf-8
'''
@Author:Lin HaoXian
@MakeData:February 17, 2021 22:56:30
@works:aut.py
@Studio:Guangzhou Game Language Production Co., Ltd.,
@Introduce:

introduce
================

This module is for mathematical operations.
The main function is four operation, formula operation, advanced number operation and so on.
I recommend the Math library if you want to work with trigonometric functions.
For other mathematical operations, I recommend this module.
This module uses a lot of math knowledge and inherits some of the functionality of the Math library.
The Math library is arguably the granddaddy of this module.And this module is also one of the cores of the whole module.
Well, I want to say how much, here is the code introduction:

see https://github.com/user123as/math

Code introduce
==============
'''

from AUT.typing import second_num
from AUT.typing import third_num

class Math:
    def __init__(self):
        self.res = 0

    def math(self,num_list:second_num,symbol:str):
        '''
        Four operations for two digits
        :param num_list:Two factors, which cannot be less than and equal to 0 (fill in the tuple) (required)
        :param symbol:Operation Symbol (required)
        :return:The result of the operation
        '''

        self.num_list = num_list
        self.symbol = symbol

        if self.num_list[0] <= 0 or self.num_list[1] <= 0:
            raise ValueError('The factor cannot be less than or equal to 0')
        else:
            if self.symbol == '+':
                self.res = self.num_list[0] + self.num_list[1]
            if self.symbol == '-':
                if self.num_list[0] - self.num_list[1] <= 0:
                    raise ValueError('The result cannot be less than or equal to 0')
                else:
                    self.res = self.num_list[0] - self.num_list[1]
            if self.symbol == '*':
                self.res = self.num_list[0] * self.num_list[1]
            if self.symbol == '/':
                if self.num_list[0] / self.num_list[1] <= 0:
                    raise ValueError('The result cannot be less than or equal to 0')
                else:
                    self.res = self.num_list[0] / self.num_list[1]

        return self.res

    def third_math(self,num_list:third_num,symbol:str):
        '''
        Four operations in three digits
        :param num_list:Three factors that cannot be 0 or less than 0 (required) (fill in tuples)
        :param symbol:Operation Symbol (required)
        :return:The result of the operation
        '''

        self.num_list = num_list
        self.symbol = symbol

        if self.num_list[0] <= 0 or self.num_list[1] <= 0 or self.num_list[2] <= 0:
            raise ValueError('The factor cannot be less than or equal to 0')
        else:
            if self.symbol == '+':
                self.res = self.num_list[0] + self.num_list[1] + self.num_list[2]
            if self.symbol == '-':
                if self.num_list[0] - self.num_list[1] - self.num_list[2] <= 0:
                    raise ValueError('The result cannot be less than or equal to 0')
                else:
                    self.res = self.num_list[0] - self.num_list[1] - self.num_list[2]
            if self.symbol == '*':
                self.res = self.num_list[0] * self.num_list[1] * self.num_list[2]
            if self.symbol == '/':
                if self.num_list[0] / self.num_list[1] / self.num_list[2] <= 0:
                    raise ValueError('The result cannot be less than or equal to 0')
                else:
                    self.res = self.num_list[0] / self.num_list[1] / self.num_list[2]

        return self.res

    def second_float_math(self,float_num_list:second_num,symbol:str):
        '''
        A two-digit four-digit operation that can be less than but not equal to 0
        :param float_num_list:Two factors that cannot be 0 (required) (fill in tuples)
        :param symbol:Operation Symbol (required)
        :return:The result of the operation
        '''

        self.float_num_list = float_num_list
        self.symbol = symbol

        if self.float_num_list[0] == 0 or self.float_num_list[1] == 0:
            raise ValueError('The factor cannot be less than or equal to 0')
        else:
            if self.symbol == '+':
                self.res = self.float_num_list[0] + self.float_num_list[1]
            if self.symbol == '-':
                if self.float_num_list[0] - self.float_num_list[1] == 0:
                    raise ValueError('The result cannot be less than or equal to 0')
                else:
                    self.res = self.float_num_list[0] - self.float_num_list[1]
            if self.symbol == '*':
                self.res = self.float_num_list[0] * self.float_num_list[1]
            if self.symbol == '/':
                if self.float_num_list[0] / self.float_num_list[1] == 0:
                    raise ValueError('The result cannot be less than or equal to 0')
                else:
                    self.res = self.float_num_list[0] / self.float_num_list[1]

        return self.res

    def third_float_math(self,float_num_list:third_num,symbol:str):
        '''
        A third-digit four-digit operation that can be less than but not equal to 0
        :param float_num_list:Third factors that cannot be 0 (required) (fill in tuples)
        :param symbol:Operation Symbol (required)
        :return:The result of the operation
        '''

        self.float_num_list = float_num_list
        self.symbol = symbol

        if self.float_num_list[0] == 0 or self.float_num_list[1] == 0 or self.float_num_list[2] == 0:
            raise ValueError('The factor cannot be less than or equal to 0')
        else:
            if self.symbol == '+':
                self.res = self.float_num_list[0] + self.float_num_list[1] + self.float_num_list[2]
            if self.symbol == '-':
                if self.float_num_list[0] - self.float_num_list[1] - self.float_num_list[2] == 0:
                    raise ValueError('The result cannot be less than or equal to 0')
                else:
                    self.res = self.float_num_list[0] - self.float_num_list[1] - self.float_num_list[2]
            if self.symbol == '*':
                self.res = self.float_num_list[0] * self.float_num_list[1] * self.float_num_list[1]
            if self.symbol == '/':
                if self.float_num_list[0] / self.float_num_list[1] / self.float_num_list[2] == 0:
                    raise ValueError('The result cannot be less than or equal to 0')
                else:
                    self.res = self.float_num_list[0] / self.float_num_list[1] / self.float_num_list[2]

        return self.res

    def float_num(self,set_num:float,get_num:int):
        '''
        The decimal place of an exact decimal
        :param set_num:Numbers requiring exact decimal places (required)
        :param get_num:Accurate decimal places required (required)
        :return:Accurate results
        '''

        self.set_num = set_num
        self.get_num = get_num

        self.res = round(self.set_num,self.get_num)

        return self.res


class Equation:
    def __init__(self):
        self.res = 0
        self.width = 0
        self.height = 0
        self.long = 0
        self.n = 3.14

    def rectangle_area(self,long:int,width:int):
        '''
        Used to calculate the area of a rectangle
        :param long:Length of a square (required)
        :param width:The width of a square (required)
        :return:The result of the operation
        '''

        self.long = long
        self.width = width

        if self.long == 0 or self.width == 0:
            raise ValueError('The length and width of a rectangle cannot be 0')
        else:
            self.res = self.long * self.width

        return self.res

    def rectangle_circumference(self,long:int,width:int):
        '''
        Used to calculate the circumference of a rectangle
        :param long:Length of a rectangle (required)
        :param width:The width of a rectangle (required)
        :return:The result of the rectangle
        '''

        self.long = long
        self.width = width

        if self.long == 0 or self.width == 0:
            raise ValueError('The length and width of a rectangle cannot be 0')
        else:
            self.res = (self.long+self.width) * 2

        return self.res

    def cuboid_volume(self,long:int,width:int,height:int):
        '''
        Used to calculate the volume of a cuboid
        :param long:Length of a cuboid (required)
        :param width:The width of a cuboid (required)
        :param height:The height of a cuboid (required)
        :return:The result of the operation
        '''

        self.long = long
        self.width = width
        self.height = height

        if self.long == 0 or self.width == 0 or self.height == 0:
            raise ValueError('The height and width and long of a cuboid cannot be 0')
        else:
            self.res = self.long*self.width*self.height

        return self.res

    def cuboid_Surface_area(self,long:int,width:int,height:int):
        '''
        Used to calculate the Surface area of a cuboid
        :param long:Length of a cuboid (required)
        :param width:The width of a cuboid (required)
        :param height:The height of a cuboid (required)
        :return:The result of the operation
        '''

        self.long = long
        self.width = width
        self.height = height

        if self.long == 0 or self.width == 0 or self.height == 0:
            raise ValueError('The height and width and long of a cuboid cannot be 0')
        else:
            self.res = 2*(self.long*self.width+self.width*self.height+self.height*self.long)

        return self.res

    def square_area(self,side:int):
        '''
        Used to calculate the area of a square
        :param side:The length of the side of the square (required)
        :return:The result of the operation
        '''

        self.side = side

        if self.side == 0:
            raise ValueError('The sides cannot be equal to 0')
        else:
            self.res = self.side * self.side

        return self.res

    def square_circumference(self,side:int):
        '''
        Used to calculate the circumference of a square
        :param side:The length of the side of the square (required)
        :return:The result of the operation
        '''

        self.side = side

        if self.side == 0:
            raise ValueError('The sides cannot be equal to 0')
        else:
            self.res = self.side * 6

        return self.res

    def cube_area(self,side:int):
        '''
        Used to calculate the area of a cube
        :param side:The length of the side of the cube (required)
        :return:The result of the operation
        '''

        self.side = side

        if self.side == 0:
            raise ValueError('The sides cannot be equal to 0')
        else:
            self.res = self.side * self.side * self.side

        return self.res

    def cube_Surface_area(self,side:int):
        '''
        Used to calculate the surface area of a cube
        :param side:The length of the side of the cube (required)
        :return:The result of the operation
        '''

        self.side = side

        if self.side == 0:
            raise ValueError('The sides cannot be equal to 0')
        else:
            self.res = self.side * self.side * 6

        return self.res

    def circular_area(self,radius:int):
        '''
        Used to compute the area of a circle
        :param radius:The radius of the circle (required)
        :return:The result of the operation
        '''

        self.radius = radius

        if self.radius == 0:
            raise ValueError('The radius cannot be equal to 0')
        else:
            self.res = (self.radius*self.radius)*self.n

        return self.res

    def circumference(self,radius:int):
        '''
        Used to compute the circumference of a circle
        :param radius:The radius of the circle (required)
        :return:The result of the operation
        '''

        self.radius = radius

        if self.radius == 0:
            raise ValueError('The radius cannot be equal to 0')
        else:
            self.res = 2 * self.radius * self.n

        return self.res

    def cylindrical_surface_area(self,radius:int,height:int):
        '''
        Used to calculate the surface area of a cylinder
        :param radius:The radius of the cylindrical (required)
        :param height:The height of the cylindrical (required)
        :return:The result of the operation
        '''

        self.radius = radius
        self.height = height

        if self.radius == 0 or self.height == 0:
            raise ValueError('The radius and height cannot be equal to 0')
        else:
            self.res = (self.n * self.radius * 2 * self.height) + 2*(self.radius*self.radius*self.n)

        return self.res

    def Cylindrical_side_area(self,radius:int,height:int):
        '''
        Used to calculate the side area of a cylinder
        :param radius:The radius of the cylindrical (required)
        :param height:The height of the cylindrical (required)
        :return:The result of the operation
        '''

        self.radius = radius
        self.height = height

        if self.radius == 0 or self.height == 0:
            raise ValueError('The radius and height cannot be equal to 0')
        else:
            self.res = self.n * self.radius * 2 * self.height

        return self.res

    def Cylindrical_bottom_area(self,radius:int):
        '''
        Used to calculate the bottom area of a cylinder
        :param radius:The radius of the cylindrical (required)
        :return:The result of the operation
        '''

        self.radius = radius

        if self.radius == 0:
            raise ValueError('The radius cannot be equal to 0')
        else:
            self.res = self.radius*self.radius*self.n

        return self.res

    def Cylindrical_volume(self,radius:int,height:int):
        '''
        Used to calculate the volume of a cylinder
        :param radius:The radius of the cylindrical (required)
        :param height:The height of the cylindrical (required)
        :return:The result of the operation
        '''

        self.radius = radius
        self.height = height

        if self.radius == 0 or self.height == 0:
            raise ValueError('The radius and height cannot be equal to 0')
        else:
            self.res = (self.n * self.radius * 2 * self.height) * self.height

        return self.res

    def Conical_bulk(self,radius:int,height:int):
        '''
        Used to calculate the volume of a cone
        :param radius:The radius of the conical (required)
        :param height:The height of the conical (required)
        :return:The result of the operation
        '''

        self.radius = radius
        self.height = height

        if self.radius == 0 or self.height == 0:
            raise ValueError('The radius and height cannot be equal to 0')
        else:
            self.res = (self.n * self.radius * 2 * self.height) * self.height / 3

        return self.res

    def interest(self,principal:int,profits:int,period:int):
        '''
        Used to calculate interest
        :param principal:The principal (required)
        :param profits:profits (required)
        :param period:For a period (required)
        :return:The result of the operation
        '''

        self.principal = principal
        self.profits = profits
        self.period = period

        if self.principal == 0 or self.profits == 0 or self.period == 0:
            raise ValueError('The principal and profits and period cannot be equal to 0')
        else:
            self.res = self.principal * self.profits * self.period

        return self.res

math = Math()
equation = Equation()
