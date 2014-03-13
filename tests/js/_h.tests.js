describe('helper function', function(){

    it('should check if string', function() {
        expect(_h.isString('val')).toEqual(true);
        expect(_h.isString(NaN)).toEqual(false);
        expect(_h.isString(1)).toEqual(false);
        expect(_h.isString(null)).toEqual(false);
        expect(_h.isString(false)).toEqual(false);
        expect(_h.isString(undefined)).toEqual(false);
        expect(_h.isString({})).toEqual(false);
    });

    it('should check if array', function() {
        expect(_h.isArray([1])).toEqual(false);
        expect(_h.isArray([,])).toEqual(true);
        expect(_h.isArray([])).toEqual(true);
        expect(_h.isArray({})).toEqual(false);
        expect(_h.isArray(undefined)).toEqual(false);
        expect(_h.isArray(1)).toEqual(false);
        expect(_h.isArray(NaN)).toEqual(false);
        expect(_h.isArray(false)).toEqual(false);
    });

    it('should check if int', function() {
        expect(_h.isInt(1)).toEqual(true);
        expect(_h.isInt(Number.MAX_VALUE)).toEqual(false);  // Believe it or not
        expect(_h.isInt(Number.MIN_VALUE)).toEqual(false);  // Believe it or not
        expect(_h.isInt(Infinity)).toEqual(false);          // Believe it or not
        expect(_h.isInt([])).toEqual(false);
        expect(_h.isInt({})).toEqual(false);
        expect(_h.isInt(undefined)).toEqual(false);
        expect(_h.isInt(NaN)).toEqual(false);
        expect(_h.isInt(false)).toEqual(false);
    });

    it('should check if variable is set', function() {
        var value = '';
        expect(_h.isSet(1)).toEqual(true);                  // R-value
        expect(_h.isSet(value)).toEqual(false);              // L-value
        expect(_h.isSet(null)).toEqual(false);
        expect(_h.isSet(undefined)).toEqual(false);
    });

    it('should convert convert string to int', function() {
        expect(_h.int('1')).toEqual(1);
        expect(_h.int('1.9')).toEqual(1);
        expect(_h.int('-1')).toEqual(-1);
        expect(_h.int('Not a number')).toBeNaN();
        expect(_h.int('a')).toBeNaN();
        expect(_h.int(NaN)).toBeNaN();
        expect(_h.int(null)).toBeNaN();
        expect(_h.int([])).toBeNaN();
        expect(_h.int({})).toBeNaN();
        expect(_h.int(undefined)).toBeNaN();
        expect(_h.int(true)).toBeNaN();
    });

    it('should get the current time', function() {
        var timestamp = 1391677820622;
        spyOn(Date.prototype, 'getTime').and.returnValue(timestamp);
        expect(_h.time()).toEqual(timestamp);
    });

    it('should get the text Sunday', function() {
        var actual = _h.getNextSunday(new Date('2014', '11', '01'));
        var expected = new Date('2014', '11', '07');
        expect(actual.toUTCString()).toEqual(expected.toUTCString());

        actual = _h.getNextSunday(new Date('2014', '01', '06'));
        expected = new Date('2014', '01', '09');
        expect(actual.toUTCString()).toEqual(expected.toUTCString());
    });

    it('should convert json to object', function() {
        var json = {};
        expect(_h.jsonParse(json)).toEqual({});
        expect(_h.jsonParse(1)).toEqual(1);
    });

});
