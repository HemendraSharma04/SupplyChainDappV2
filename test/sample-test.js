const { expect } = require("chai");
const { ethers } = require("hardhat");

// eslint-disable-next-line no-undef
describe("SupplyChain", () => {
  // eslint-disable-next-line no-undef
  it("Should work properly", async () => {
    const Supply = await ethers.getContractFactory("Supplychain");
    const supply = await Supply.deploy();
    await supply.deployed();

  
  });
});
