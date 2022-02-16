import pytest
import brownie
from brownie import config, Contract, accounts, interface, chain, ZERO_ADDRESS
from brownie import network


def test_token(chain, gov, user, user2, accounts, token):
    print("Governance balance on token contract creation:",token.balanceOf(gov)/10**token.decimals())
    print("Token name:", token.name())
    print("Token symbol:", token.symbol())
    token.transfer(user, 100e18, {"from":gov})

def test_mint(chain, gov, user, user2, accounts, token):
    amount_to_mint = 1_000e18
    before_balance = token.balanceOf(user2)
    token.mint(user2, amount_to_mint, {"from":gov})
    assert token.balanceOf(user2) == before_balance + amount_to_mint

def test_burn(chain, gov, user, user2, accounts, token):
    amount_to_burn = 1_000e18
    before_balance = token.balanceOf(gov)
    token.burn(gov, amount_to_burn, {"from":gov})
    assert token.balanceOf(gov) == before_balance - amount_to_burn

def transfer_governance_to_user(chain, gov, user, user2, accounts, token):
    amount_to_mint = 1_000e18
    token.transferGovernance(user, {"from":gov})
    before_balance = token.balanceOf(user2)
    token.mint(user2, amount_to_mint, {"from":user})
    with brownie.reverts():
        token.mint(user2, amount_to_mint, {"from":gov})
    with brownie.reverts():
        token.burn(user2, amount_to_mint, {"from":gov})
    assert token.balanceOf(user2) == before_balance + amount_to_mint

def burn_keys(chain, gov, user, user2, accounts, token):
    token.transferGovernance(ZERO_ADDRESS, {"from":gov})
    with brownie.reverts():
        token.mint(user2, 1_000e18, {"from":gov})