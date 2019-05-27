# -*- coding:utf-8 -*-

"""Brain calc game functions."""
import random

GAME_DESCRIPTION = 'What is the result of the expression?'

operations = {
    '+': lambda num1, num2: num1 + num2,
    '-': lambda num1, num2: num1 - num2,
    '*': lambda num1, num2: num1 * num2,
}


def generate_question():
    """Create game question."""
    num1 = _generate_number()
    num2 = _generate_number()
    operator = _generate_operator()

    question = '{num1} {operator} {num2}'.format(
        num1=num1, num2=num2, operator=operator,
    )
    expected_answer = _get_expected_answer(operator, num1, num2)
    return question, expected_answer


def _generate_number():
    """Create random number."""
    return random.randrange(1, 100)


def _generate_operator():
    """Get operator."""
    operation_list = list(operations.keys())
    return random.choice(operation_list)


def _get_expected_answer(operator, num1, num2):
    return str(operations[operator](num1, num2))
