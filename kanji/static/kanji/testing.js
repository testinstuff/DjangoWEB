
    function Test(word)
    {
      var correct = "Yahooo Correct";
      var wrong = "Buuuuu Wrong";
      var input = document.getElementById("amm");
      // var input_lower = input.toLowerCase();
      var lower_word = word.toLowerCase();
      var lower_input = input.value.toLowerCase();

      if (lower_input==lower_word)
      {
        document.getElementById("score").innerHTML=correct;
        return true;
      }
      else{
        document.getElementById("score2").innerHTML=wrong;
        return false;
      }
    }
