import pytest, web3
from brownie import config, Contract, accounts, interface
from brownie import network


# @pytest.fixture(autouse=True)
# def isolation(fn_isolation):
#     pass

@pytest.fixture
def gov(accounts):
    yield accounts[0]

@pytest.fixture
def user(accounts):
    yield accounts[1]

@pytest.fixture
def user2(accounts):
    yield accounts[1]

@pytest.fixture
def token(gov, ERC20):
    token = gov.deploy(ERC20, "BurgerDAO token", "BRGR", 10_000_000e18)
    yield token