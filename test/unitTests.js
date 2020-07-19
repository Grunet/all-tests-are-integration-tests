const assert = require("assert");
const sinon = require("sinon");

describe("Array", function () {
  describe("#indexOf()", function () {
    let callIndex = 0;

    before(function () {
      sinon.spy(Array.prototype, "indexOf");
    });

    it("should return -1 when the value is not present", function () {
      assert.equal([3, 2, 1].indexOf(4), -1);
    });

    it("should return 2 when the value is the 3rd element", function () {
      assert.equal([3, 2, 1].indexOf(1), 2);
    });

    afterEach(function () {
      const spyCall = Array.prototype.indexOf.getCall(callIndex);
      callIndex++;

      console.log(spyCall.thisValue);
      console.log(spyCall.args);
      console.log(spyCall.returnValue);
    });
  });
});
