document.addEventListener('DOMContentLoaded', function() {
   var timer_01 = document.getElementById("timer-01")
   var timer_02 = document.getElementById("timer-02")
   var timer_03 = document.getElementById("timer-03")

   var timer_01_val = timer_01.innerHTML

   var date = new Date(timer_01_val * 1000)
   var date_02 = new Date()

    timer_01.innerHTML = date
    timer_02.innerHTML = date_02
    var millis = date_02.getTime() - date.getTime()

    function millisToMinutesAndSeconds(millis) {
      var minutes = Math.floor(millis / 60000);
      var seconds = ((millis % 60000) / 1000).toFixed(0);
      return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
    }
    var start_time = millisToMinutesAndSeconds(millis)
    timer_03.innerHTML = start_time
    setInterval(
        function () {
//            start_time --
            millis -= 10
            timer_03.innerHTML = millisToMinutesAndSeconds(millis)
        }, 1
    )




}, false);
