#!/usr/bin/python3
#coding:utf-8
import Card
class BabyCard(Card):
    def __init__(self , title :str,Description:str , value:int ):
        super.__init__(self,title,Description)
        self._value = value
    def __str__(self):
        return "title : {}  \n Descriptoin : {}  \n value : {}".format(self ._title ,self._Description ,self._value)
    @property
    def get_value(self ):
        return self._value
    pass
