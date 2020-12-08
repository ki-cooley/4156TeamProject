jest
  .dontMock('fs')
  .dontMock('jquery');

var $ = require('jquery');
var html = require('fs').readFileSync('./templates/timer/home.html').toString();

describe('validateInitial', function() {

  it('initial', function() {
    document.documentElement.innerHTML = html;
   // initial state
    expect($('#reset_timer').hasClass('reset')).toBeFalsy();
    $('#reset_timer').val('reset');
    expect($('#err').hasClass('hidden')).toBeFalsy();
  });
});
