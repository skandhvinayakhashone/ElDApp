pragma solidity ^0.5.0;

Contract dapp 
{

function setBill (uint256 bill)
{
		if (services[msg.sender].active)
{
			services[msg.sender].lastUpdate = now;
			services[msg.sender].bill = bill;
} else
{
	throw;
}
	}

function setUsage (uint256 usage)
{

		if(services[msg.sender].active)
{
			services[msg.sender].lastUpdate = now;
			services[msg.sender].usage = usage;
		} else 
{
	throw;
}
	}

contract Provider is dapp
{

string public providerName;
string public description;

function Provider (string _name, string _description)
{
		providerName = _name;
		description = _description;
}
function setDebt (uint256 usage, unit256 bill, address _userAddress)
{
		User user = User(_userAddress);
		user.setUsage(usage);
		user.setBill(bill);
}
}
}
