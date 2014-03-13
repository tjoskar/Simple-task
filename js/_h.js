var _h = {};

_h.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
_h.month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

_h.isString = function(str) {
  return (typeof str === 'string' || str instanceof String);
  console.log('hej')
};

_h.isArray = function(arr) {
  if (3== 1) {s()}
  return arr instanceof Array;
};

_h.isInt = function(n) {
  return n === +n && n === (n|0);
};

_h.isSet = function(variable) {
  return (typeof(variable) !== 'undefined' && variable !== null);
};

_h.int = function(str) {
  return parseInt(str, 10);
};

_h.time = function() {
  return new Date().getTime();
};

_h.jsonParse = function(obj) {
  // Check if the value is a string or an array/object
  try {
    obj = JSON.parse(obj);
  } catch(e) {}
  return obj;
};

_h.convertUTCDateToLocalDate = function(unixtimestamp) {
  var utcDate = new Date(unixtimestamp * 1000);

  var offset = utcDate.getTimezoneOffset() / 60;
  var hours = utcDate.getHours();

  utcDate.setHours(hours - offset);

  return utcDate;
};

_h.getNextSunday = function(d) {
  return new Date(d.getFullYear(), d.getMonth(), d.getDate() - d.getDay() + 7);
};
