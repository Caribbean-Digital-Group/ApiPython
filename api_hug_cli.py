#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tercer método: acceso cli"""
import datetime
import hug

@hug.cli()
@hug.get(examples="name=Edgar Lopez&age=35")
@hug.local()
def say_hello(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Decimos hola al usuario y calculamos su año de nacimiento"""
    year_of_birth = datetime.datetime.now().year - age
    return {
        'message': "Hola {0}, naciste el año {1}".format(name, year_of_birth),
        'took': float(hug_timer)
    }


if __name__ == '__main__':
    print(say_hello("Gabriel", 23))