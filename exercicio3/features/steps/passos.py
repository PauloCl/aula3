#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Passos para a verificação."""

from behave import given, when, then

class Retangulo:
    def verifica_fora_dentro(self, pontos):
        """Verifica se os pontos estão dentro."""
        x, y = pontos
        if x < self.x or x > (self.x + self.largura):
            return False
        elif y < self.y or y > (self.y + self.altura):
            return False
        return True

    def __init__(self, x, y, largura, altura):
        """Insere os valores de x,y largura e altura"""
        self.largura = largura
        self.altura = altura
        self.x = x
        self.y = y


@given(u'um ponto com as coordenadas ({x:d}, {y:d})')
def given_two_cordenadas(context, x, y):
    """Temos o ponto com as cordenadas X e Y."""
    context.pontos = (x, y)


@given(u'um retângulo nas coordenadas ({x:d},{y:d}) e dimensão ({largura:d},{altura:d})')
def given_retangle(context, x, y, largura, altura):
    """Temos o retângulo com as cordenadas X e Y, e de dimensão, largura, altura."""
    context.retangulo = Retangulo(x, y, largura, altura)


@when(u'quero saber se o ponto está dentro do retangulo')
def when_retangle(context):
    """Verifica se o ponto está dentro ou fora do retangulo."""
    pontos = context.pontos
    context.resposta = context.retangulo.verifica_fora_dentro(pontos)


@then(u'o resultado é "{esperado}".')
def then_verification(context, esperado):
    booleano = True if bool(esperado) == True else False
    assert context.resposta == booleano
