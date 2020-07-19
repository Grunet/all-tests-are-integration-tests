function customIncludes(searchElement) {
  if (this.indexOf(searchElement) >= 0) {
    return true;
  } else {
    return false;
  }
}

Array.prototype.customIncludes = customIncludes;

//The actual test portion is below
const { mock_indexOf } = require("../derivedMock.js");

const assert = require("assert");
const sinon = require("sinon");

describe("Array", function () {
  describe("#customIncludes()", function () {
    before(function () {
      //Using the generated mock
      sinon.stub(Array.prototype, "indexOf").callsFake(mock_indexOf);
    });

    it("should return False when the value is not present", function () {
      assert.equal([3, 2, 1].customIncludes(4), false);
    });

    it("should return True when the value is present", function () {
      assert.equal([3, 2, 1].customIncludes(1), true);
    });
  });
});
