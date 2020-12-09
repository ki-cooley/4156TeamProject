jest
  .dontMock('fs')
  .dontMock('jquery');

var $ = require('jquery');
var html = require('fs').readFileSync('./templates/timer/break.html').toString();

describe('validateInitial', function() {

  it('initial', function() {
    document.documentElement.innerHTML = html;
   // initial state
    expect($('#reset_timer').hasClass('reset')).toBeFalsy();
    $('#reset_timer').val('reset');
    expect($('#err').hasClass('hidden')).toBeFalsy();
  });
});

//test('Check reset button', () => {
//  document.body.innerHTML = html;
//
//  const demo = document.getElementById('demo');
//  const reset = document.getElementById('pomodoro-reset');
//
//  reset.value = 'reset';
//
//  expect(demo.innerHTML).toBe('Starting Timer');
//});

test('Check reset button', () => {
  document.body.innerHTML = html;

  const demo = document.getElementById('demo');
  const break_button = document.getElementById('pomodoro-reset');

  break_button.value = 'new_session';

  expect(demo.innerHTML).toBe('Break Time');
});

test('Check reset button with invalid input', () => {
  document.body.innerHTML = html;

  const demo = document.getElementById('demo');
  const break_button = document.getElementById('pomodoro-reset');

  break_button.value = 'skip_to_breakbad';

  expect.not.stringMatching(demo.innerHTML, 'Break Time');
});
