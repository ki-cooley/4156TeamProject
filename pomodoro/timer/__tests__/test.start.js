jest
  .dontMock('fs')
  .dontMock('jquery');

var $ = require('jquery');
var html = require('fs').readFileSync('./templates/timer/start.html').toString();

describe('validateInitial', function() {

  it('initial', function() {
    document.documentElement.innerHTML = html;
   // initial state
    expect($('#reset_timer').hasClass('reset')).toBeFalsy();
    $('#reset_timer').val('reset');
    expect($('#err').hasClass('hidden')).toBeFalsy();
  });
});

test('Check reset button', () => {
  document.body.innerHTML = html;

  const demo = document.getElementById('demo');
  const reset = document.getElementById('pomodoro-reset');
//  const todolist = document.getElementById('todoList');

  reset.value = 'reset';
//  reset.click();

  expect(demo.innerHTML).toBe('Starting Timer');
});

test('Check break button', () => {
  document.body.innerHTML = html;

  const demo = document.getElementById('demo');
  const break_button = document.getElementById('pomodoro-break');

  break_button.value = 'skip_to_break';

  expect(demo.innerHTML).toBe('Starting Timer');
});