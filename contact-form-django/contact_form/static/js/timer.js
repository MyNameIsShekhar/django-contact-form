// ---------------timer----------------------

$(document).ready(function() {
  var timerInterval;
  var timer = 20;

  // start timer countdown
  function startTimer() {
    timerInterval = setInterval(function() {
      timer--;
      $('#timer').text(timer);
      if (timer == 0) {
        clearInterval(timerInterval);
        window.location.href = '/contactus/';
      }
    }, 1000);
  }

  // reset timer and start over
  function resetTimer() {
    clearInterval(timerInterval);
    timer = 20;
    $('#timer').text(timer);
    startTimer();
  }

  // start timer on page load
  $(document).ready(function() {
    startTimer();
  });

  // restart timer on button click
  $('#main-btn').click(function() {
    clearInterval(timerInterval);
    window.location.href = '/contactus/';
  });
  
});