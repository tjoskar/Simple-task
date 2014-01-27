describe('StorageTest', function(){

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
        expect(_h.isArray([1])).toEqual(true);
        expect(_h.isArray([,])).toEqual(true);
        expect(_h.isArray([])).toEqual(true);
        expect(_h.isArray({})).toEqual(false);
        expect(_h.isArray(undefined)).toEqual(false);
        expect(_h.isArray(1)).toEqual(false);
        expect(_h.isArray(NaN)).toEqual(false);
        expect(_h.isArray(false)).toEqual(false);
    });

    it('should check if int', function() {
        expect(_h.isInt(1)).toEqual(true);                  // Believe it ot not
        expect(_h.isInt(Number.MAX_VALUE)).toEqual(false);  // Believe it ot not
        expect(_h.isInt(Number.MIN_VALUE)).toEqual(false);  // Believe it ot not
        expect(_h.isInt(Infinity)).toEqual(false);
        expect(_h.isInt([])).toEqual(false);
        expect(_h.isInt({})).toEqual(false);
        expect(_h.isInt(undefined)).toEqual(false);
        expect(_h.isInt(NaN)).toEqual(false);
        expect(_h.isInt(false)).toEqual(false);
    });

});
