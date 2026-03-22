import pytest
from employee_functions import Employee

# Sem @pytest.fixture o código fica:

def test_give_default_raise():
    emp = Employee("João", "Silva", 30000)
    emp.dar_aumento()
    assert emp.salario == 35000


def test_give_custom_raise():
    emp = Employee("João", "Silva", 30000)
    emp.dar_aumento(2000)
    assert emp.salario == 32000

# Com @pytest.fixture o código fica:

@pytest.fixture
def employee():
    return Employee("João", "Silva", 30000)

def test_give_default_raise(employee):
    employee.dar_aumento()
    assert employee.salario == 35000


def test_give_custom_raise(employee):
    employee.dar_aumento(2000)
    assert employee.salario == 32000