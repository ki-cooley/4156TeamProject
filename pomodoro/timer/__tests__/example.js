jest
  .dontMock('fs')
  .dontMock('jquery');

var $ = require('jquery');
var html = require('fs').readFileSync('./templates/timer/start.html').toString();

describe('validateSubmits', function() {

  it('shows/hides error banner', function() {
    document.documentElement.innerHTML = html;
  });

});