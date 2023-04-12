#version 3.11

#Calcula el salario de un empleado
_getInputUser=""
_salario=""
_pagasExtras=""
_complementos=""
_otrosConceptosRetribuidos=""
_irpf=""
_seguridadSocial=""


def _startProgram():
    _salario=input("Introduce tu salario")
    _pagasExtras=input("Introduce tus pagas extras")
    _complementos=input("")
    _otrosConceptosRetribuidos=input("")
    _irpf=input("")
    _seguridadSocial=input("")
