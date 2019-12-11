function Result(){
  var investors = $('#investors').val();
  var investors_amt = $('#investors_amt').val();
  var season = $('#season').val();
  var episode = $('#episode').val();
  var gender = $('#gender').val();
  localStorage.setItem("investors", investors)
  localStorage.setItem("investors_amt", investors_amt)
  localStorage.setItem("season", season)
  localStorage.setItem("episode", episode)
  localStorage.setItem("gender", gender)
}
